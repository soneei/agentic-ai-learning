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
