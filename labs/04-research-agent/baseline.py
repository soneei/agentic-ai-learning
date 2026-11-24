"""Research Agent 基线：复用 Lab03 的调度器 + 四工具，产出第一份小结。

不写任何新工具——这一步只是把已验证的零件第一次装起来跑通。
"""

import sys
from pathlib import Path

# 自动找到 Lab03 的工具目录，不管从哪个目录启动都能跑
LAB03 = Path(__file__).resolve().parent.parent / "03-tool-use-loop"
sys.path.insert(0, str(LAB03))

from orchestrator import run_loop  # noqa: E402


# 虚拟公司数据（沿用星河数据工具，不碰真实数据）
RESEARCH_DATASET = {
    "company": "星河数据工具",
    "unit": "百万元",
    "years": [2023, 2024, 2025],
    "metrics": {
        "revenue": [100, 140, 196],
        "net_profit": [12, 15, 17],
        "operating_cash_flow": [18, 22, 35],
    },
}


def run_baseline(dataset=None):
    """跑一次完整流程，返回结果（含 trace 和小结）。"""
    return run_loop(dataset or RESEARCH_DATASET)


def format_summary(result) -> str:
    """把结构化小结转成可读文本。

    注意：run_loop 返回的最外层是调度器结果，
    真正的工具输出嵌在 result["result"] 里。
    """
    s = result["result"]["summary"]
    lines = [
        "# Research Agent 基线小结",
        "",
        "公司：%s（单位：%s）" % (s["company"], s["unit"]),
        "",
        "## 确认的变化",
    ]
    for item in s["confirmed_changes"]:
        lines.append("- " + item)
    lines.append("")
    lines.append("## 待核实事项")
    if s["items_to_verify"]:
        for item in s["items_to_verify"]:
            lines.append("- " + item)
    else:
        lines.append("- 无")
    lines.append("")
    lines.append("## 数据边界")
    for item in s["data_limitations"]:
        lines.append("- " + item)
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    result = run_baseline()
    print("运行状态：%s（%s）" % (result["status"], result["reason"]))
    print("走过的工具：" + " → ".join(step["tool"] for step in result["trace"]))
    print()
    print(format_summary(result))
