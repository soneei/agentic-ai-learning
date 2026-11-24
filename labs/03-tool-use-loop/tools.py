"""Tool Use Loop 的第一个本地工具：read_dataset。"""

from typing import Dict, List


def read_dataset(dataset: Dict[str, object]) -> Dict[str, object]:
    """读取并整理数据，不负责计算或解释。"""
    required_fields: List[str] = ["company", "unit", "years", "metrics"]

    missing_fields = [
        field for field in required_fields
        if field not in dataset
    ]

    if missing_fields:
        return {
            "status": "error",
            "data": None,
            "missing_fields": missing_fields,
            "next_step": "fetch_from_source",
        }

    return {
        "status": "success",
        "data": dataset,
        "missing_fields": [],
        "next_step": "calculate_changes",
    }


def calculate_changes(tool_result: Dict[str, object]) -> Dict[str, object]:
    """基于已读取的数据计算逐年变化，只输出表内可核验的事实。"""
    if tool_result["status"] != "success":
        return {
            "status": "error",
            "data": None,
            "next_step": tool_result["next_step"],
        }

    dataset = tool_result["data"]
    years = dataset["years"]
    metrics = dataset["metrics"]

    changes = {}
    for name, values in metrics.items():
        yearly = []
        for i in range(1, len(values)):
            previous = values[i - 1]
            current = values[i]
            change = {
                "year": years[i],
                "absolute": round(current - previous, 4),
                "growth_rate": round((current - previous) / previous, 4)
                if previous != 0 else None,
            }
            yearly.append(change)
        changes[name] = yearly

    return {
        "status": "success",
        "data": {
            "company": dataset["company"],
            "unit": dataset["unit"],
            "changes": changes,
        },
        "next_step": "check_data_quality",
    }


def check_data_quality(tool_result: Dict[str, object]) -> Dict[str, object]:
    """检查上游计算结果的质量，标记异常但不自行解释原因。"""
    if tool_result["status"] != "success":
        return {
            "status": "error",
            "data": None,
            "flags": [],
            "next_step": tool_result["next_step"],
        }

    data = tool_result["data"]
    changes = data["changes"]

    flags = []
    for metric, yearly in changes.items():
        for item in yearly:
            rate = item["growth_rate"]
            if rate is None:
                flags.append({
                    "metric": metric,
                    "year": item["year"],
                    "issue": "zero_base_growth_rate_undefined",
                })
            elif rate > 1.0:
                flags.append({
                    "metric": metric,
                    "year": item["year"],
                    "issue": "abnormal_growth_rate_over_100pct",
                })
            elif rate < -0.5:
                flags.append({
                    "metric": metric,
                    "year": item["year"],
                    "issue": "abnormal_drop_over_50pct",
                })

    if flags:
        return {
            "status": "warning",
            "data": data,
            "flags": flags,
            "next_step": "verify_source_and_calculation",
        }

    return {
        "status": "success",
        "data": data,
        "flags": [],
        "next_step": "generate_summary",
    }
