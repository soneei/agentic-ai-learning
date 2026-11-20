"""最小 JSON Planning 分支执行器。

本脚本不调用大语言模型，只验证：
1. 数据缺失时是否回到原始数据源
2. 口径模糊时是否先澄清并暂停
3. 结果异常时是否进入核查
4. 原始数据也缺失时是否停止猜测
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Scenario:
    name: str
    missing_fields: List[str]
    source_has_missing_fields: bool
    ambiguous_definition: bool
    abnormal_result: bool


def choose_path(scenario: Scenario) -> Dict[str, object]:
    """根据数据状态选择下一步路径。"""
    if scenario.missing_fields:
        if scenario.source_has_missing_fields:
            return {
                "status": "补充数据",
                "next_step": "fetch_from_source",
                "message": f"从原始数据源补充字段：{', '.join(scenario.missing_fields)}",
            }
        return {
            "status": "无法判断",
            "next_step": "stop_without_guessing",
            "message": "原始数据源也缺少关键字段，停止分析，不编造数据",
        }

    if scenario.ambiguous_definition:
        return {
            "status": "等待澄清",
            "next_step": "ask_for_clarification",
            "message": "时间范围、单位或比较口径不明确，先向用户澄清",
        }

    if scenario.abnormal_result:
        return {
            "status": "进入核查",
            "next_step": "verify_source_and_calculation",
            "message": "结果异常，复核原始数据、计算公式和输入口径",
        }

    return {
        "status": "继续分析",
        "next_step": "generate_hypotheses",
        "message": "数据状态正常，可以继续提出带边界的可能解释",
    }


def run_demo() -> None:
    scenarios = [
        Scenario("数据缺失但原始源可补充", ["operating_cash_flow"], True, False, False),
        Scenario("口径模糊", [], False, True, False),
        Scenario("结果异常", [], False, False, True),
        Scenario("原始数据也缺失", ["debt_maturity"], False, False, False),
        Scenario("数据正常", [], False, False, False),
    ]

    for scenario in scenarios:
        result = choose_path(scenario)
        print(f"[{scenario.name}] -> {result['status']} / {result['next_step']}")
        print(f"  {result['message']}")


if __name__ == "__main__":
    run_demo()
