"""Research Agent 全链路：基线 + Reflection + Evaluation → 综合报告。

四块零件第一次在同一条流水线里跑通：
  Tool Use（基线产出）→ Reflection（自检）→ Evaluation（失败归因）
  Planning 已在调度器的分支逻辑里体现。
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "labs" / "03-tool-use-loop"))
sys.path.insert(0, str(ROOT / "evaluations"))

from baseline import run_baseline, RESEARCH_DATASET, format_summary  # noqa: E402
from reflection import check_report  # noqa: E402
from error_analyzer import analyze  # noqa: E402
from failure_report import build_cases  # noqa: E402


def run_full_pipeline():
    """跑完整链路，返回三块结果。"""
    # 1. Tool Use：调度器产出基线小结
    baseline = run_baseline()

    # 2. Reflection：按 5 条 criteria 自检（传原始证据做对照）
    reflection = check_report(baseline, RESEARCH_DATASET)

    # 3. Evaluation：失败样本归因（复用已有 7 样本集）
    cases = build_cases()
    clean = [{k: v for k, v in c.items() if k != "fault"} for c in cases]
    evaluation = analyze(clean)

    return {
        "baseline": baseline,
        "reflection": reflection,
        "evaluation": evaluation,
    }


def format_full_report(pipeline) -> str:
    """把三块结果合成一份综合报告。"""
    baseline = pipeline["baseline"]
    reflection = pipeline["reflection"]
    evaluation = pipeline["evaluation"]

    lines = [
        "# Research Agent 综合报告",
        "",
        "虚拟数据研究 · 四模式全链路输出",
        "",
        "=" * 40,
        "",
        "## 第一部分：基线小结（Tool Use 产出）",
        "",
        "运行状态：%s" % baseline["status"],
        "执行链：" + " → ".join(s["tool"] for s in baseline["trace"]),
        "",
    ]
    summary = baseline["result"]["summary"]
    lines.append("公司：%s（单位：%s）" % (summary["company"], summary["unit"]))
    lines.append("")
    lines.append("确认的变化：")
    for item in summary["confirmed_changes"]:
        lines.append("  - " + item)
    lines.append("")

    lines += ["=" * 40, "", "## 第二部分：Reflection 自检", "",
              "结论：%s" % reflection["verdict"], ""]
    for c in reflection["checks"]:
        mark = "PASS" if c["pass"] else "FAIL"
        lines.append("  [%s] %s — %s" % (mark, c["criterion"], c["detail"]))
    lines.append("")

    top = evaluation["top_priority"]
    lines += ["=" * 40, "", "## 第三部分：Evaluation 失败归因", "",
              "样本总数：%d，识别失败：%d" % (
                  evaluation["total_cases"], evaluation["failure_count"]), ""]
    for step, count in evaluation["freq_by_step"].items():
        lines.append("  - %s：%d 次" % (step, count))
    lines.append("")
    if top:
        lines.append("优先修：%s（%d 次）— %s" % (top["step"], top["count"], top["fix_hint"]))
    lines.append("")

    lines += ["=" * 40, "", "## 总结", ""]
    all_pass = reflection["all_pass"]
    lines.append("- 报告自检：%s" % ("通过" if all_pass else "发现问题"))
    lines.append("- 系统改进优先级：%s" % (top["step"] if top else "无"))
    lines.append("- 说明：本报告基于虚拟数据，仅描述表内可核验变化，不含投资建议。")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    pipeline = run_full_pipeline()
    print(format_full_report(pipeline))
