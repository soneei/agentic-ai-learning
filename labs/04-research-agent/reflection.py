"""规则版 Reflection：按 Lab01 的 5 条 criteria 检查基线报告。

诚实说明：这是确定性规则检查，不是 LLM 自审。
数字、越界词、边界声明能查；微妙的语义越界查不了。
"""

from typing import Dict, List

from orchestrator import read_dataset, calculate_changes

# 越界词：出现这些就是给了买卖建议
BANNED_TERMS = ["买入", "卖出", "推荐", "建议买", "目标价", "加仓", "减仓", "值得投资"]
# 推测词：小结里不该出现（只报告事实）
SPECULATIVE_TERMS = ["预计", "将会", "大概率", "很可能", "必然会"]


def check_report(run_result: Dict[str, object], dataset: Dict[str, object]) -> Dict[str, object]:
    """对基线报告跑 5 条 criteria，返回逐条结果和总体判定。

    必须传入原始 dataset 作为对照基准——
    只拿报告本身无法核对“数字有没有抄错”。
    """
    summary = run_result["result"]["summary"]
    confirmed = summary["confirmed_changes"]

    # 从原始证据重新算一遍期望值，作为核对基准
    read = read_dataset(dataset)
    calc = calculate_changes(read)
    raw_changes = calc["data"]["changes"]

    checks: List[Dict[str, object]] = []

    # Criterion 1：数字有没有抄错——逐条对照原文数字
    expected = {}
    for metric, yearly in raw_changes.items():
        for item in yearly:
            rate = item["growth_rate"]
            rate_text = "无法计算（基数为0）" if rate is None else f"{round(rate * 100, 1)}%"
            expected[metric, item["year"]] = (str(item["absolute"]), rate_text)

    number_errors = []
    for line in confirmed:
        for (metric, year), (abs_txt, rate_txt) in expected.items():
            if line.startswith(f"{metric} {year}"):
                if abs_txt not in line or rate_txt not in line:
                    number_errors.append(line)
    checks.append({
        "criterion": "数字正确",
        "pass": not number_errors,
        "detail": number_errors or "全部数字与原始 changes 一致",
    })

    # Criterion 2：每条结论能回到表内（带 metric + year）
    untraceable = [line for line in confirmed if not any(
        line.startswith(f"{m} {y}") for m, y in expected
    )]
    checks.append({
        "criterion": "结论可追溯",
        "pass": not untraceable,
        "detail": untraceable or "每条都带指标名和年份",
    })

    # Criterion 3：事实和推测分开（小结里不该有推测词）
    speculation_hits = [t for t in SPECULATIVE_TERMS if any(t in line for line in confirmed)]
    checks.append({
        "criterion": "事实推测分开",
        "pass": not speculation_hits,
        "detail": speculation_hits or "未发现推测性措辞",
    })

    # Criterion 4：有没有买卖建议（越界）
    boundary_text = " ".join(confirmed) + " " + " ".join(summary["data_limitations"])
    banned_hits = [t for t in BANNED_TERMS if t in boundary_text]
    checks.append({
        "criterion": "无越界建议",
        "pass": not banned_hits,
        "detail": banned_hits or "未发现买卖建议",
    })

    # Criterion 5：有没有数据边界声明
    limits = summary["data_limitations"]
    has_limits = bool(limits) and any("不给买卖建议" in x for x in limits)
    checks.append({
        "criterion": "有数据边界",
        "pass": has_limits,
        "detail": limits or "缺少边界声明",
    })

    all_pass = all(c["pass"] for c in checks)
    return {
        "all_pass": all_pass,
        "checks": checks,
        "verdict": "报告合格，无需修订" if all_pass else "发现问题，需人工复核",
    }
