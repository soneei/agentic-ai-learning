"""用一组故意构造的失败样本，跑错误分析器，产出可复现的分析报告。"""

from typing import Dict, List

from error_analyzer import analyze


def good_data():
    return {
        "company": "星河数据工具",
        "unit": "百万元",
        "years": [2023, 2024, 2025],
        "metrics": {"revenue": [100, 140, 196], "net_profit": [12, 15, 17]},
    }


def build_cases() -> List[Dict[str, object]]:
    """故意构造：2 个正常 + 3 个缺字段 + 2 个异常数据。"""
    cases = [
        {"name": "正常样本 A", "data": good_data(), "should_succeed": True,
         "fault": "无（基线）"},
        {"name": "正常样本 B", "data": good_data(), "should_succeed": True,
         "fault": "无（基线）"},
        {"name": "缺 metrics ①", "data": {"company": "星河", "unit": "百万元", "years": [2023]},
         "should_succeed": True, "fault": "故意删掉 metrics 字段"},
        {"name": "缺 metrics ②", "data": {"company": "星河", "unit": "百万元", "years": [2023]},
         "should_succeed": True, "fault": "故意删掉 metrics 字段"},
        {"name": "缺 unit", "data": {"company": "星河", "years": [2023, 2024],
                                     "metrics": {"revenue": [1, 2]}},
         "should_succeed": True, "fault": "故意删掉 unit 字段"},
        {"name": "暴涨暴跌 ①", "data": {**good_data(), "metrics": {"revenue": [100, 300, 50]}},
         "should_succeed": True, "fault": "故意造 +200% 涨幅和 -83% 跌幅"},
        {"name": "暴涨暴跌 ②", "data": {**good_data(), "metrics": {"net_profit": [10, 40, 5]}},
         "should_succeed": True, "fault": "故意造 +300% 涨幅和 -87% 跌幅"},
    ]
    return cases


def generate_report() -> str:
    cases = build_cases()
    # analyze 只认 name/data/should_succeed，fault 是我们报告用的标注
    clean_cases = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
    result = analyze(clean_cases)
    fault_map = {c["name"]: c["fault"] for c in cases}

    lines = []
    lines.append("总样本：%d" % result["total_cases"])
    lines.append("识别出失败：%d" % result["failure_count"])
    lines.append("")
    lines.append("=== 失败归因明细 ===")
    for f in result["failures"]:
        lines.append("- %s ｜ 归因组件=%s ｜ 注入的错误=%s ｜ 改法=%s" % (
            f["name"], f["step"], fault_map[f["name"]], f["fix_hint"]))
    lines.append("")
    lines.append("=== 频次统计 ===")
    for step, count in result["freq_by_step"].items():
        lines.append("- %s：%d 次" % (step, count))
    lines.append("")
    top = result["top_priority"]
    lines.append("=== 优先修 ===")
    lines.append("%s（%d 次）— %s" % (top["step"], top["count"], top["fix_hint"]))
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_report())
