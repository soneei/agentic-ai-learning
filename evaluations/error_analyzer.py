"""错误分析器：把一批运行结果归因到具体组件，统计频次，指出优先改哪里。

核心思想（来自课程 Evaluation / Error Analysis）：
不要只看“这次对不对”，而要看“错在哪一步、错了几次、值不值得先修”。
"""

from typing import Dict, List

from orchestrator import run_loop


def outcome_label(run: Dict[str, object]) -> str:
    """把一次运行结果压缩成一个可比较、可统计的标签。"""
    if run["status"] == "completed":
        return "completed"
    return f"stopped:{run['reason']}"


# 错误分类表：每种结果归因到哪个组件、什么意思、改法方向
CATALOG: Dict[str, Dict[str, str]] = {
    "stopped:upstream_error": {
        "step": "read_dataset",
        "meaning": "原始数据缺字段，第一步就拦下了",
        "fix_hint": "优先补数据源字段，不要改下游逻辑",
    },
    "stopped:max_steps_reached": {
        "step": "orchestrator",
        "meaning": "步数超限，疑似死循环",
        "fix_hint": "检查注册表和 next_step 是否形成环",
    },
    "stopped:no_tool_for_next_step": {
        "step": "check_data_quality",
        "meaning": "数据异常，停在人工核查（这是设计好的安全停止）",
        "fix_hint": "若要自动化，需新增核查工具；否则属正常拦截",
    },
}


def analyze(cases: List[Dict[str, object]]) -> Dict[str, object]:
    """跑一批 case，把没达到预期的失败归因到组件并统计频次。"""
    failures = []

    for case in cases:
        run = run_loop(case["data"])
        label = outcome_label(run)
        expected_ok = case["should_succeed"]
        actual_ok = run["status"] == "completed"

        # 只看“本该成功却失败”的样本——这才是要修的错误
        if expected_ok and not actual_ok:
            info = CATALOG.get(label, {"step": "unknown", "meaning": label, "fix_hint": "待分析"})
            failures.append({
                "name": case["name"],
                "label": label,
                "step": info["step"],
                "fix_hint": info["fix_hint"],
            })

    # 按频次统计，多的排前面
    by_step: Dict[str, int] = {}
    for f in failures:
        by_step[f["step"]] = by_step.get(f["step"], 0) + 1

    ranked = sorted(by_step.items(), key=lambda kv: -kv[1])

    top = None
    if ranked:
        top_step, top_count = ranked[0]
        top = {
            "step": top_step,
            "count": top_count,
            "fix_hint": next(f["fix_hint"] for f in failures if f["step"] == top_step),
        }

    return {
        "total_cases": len(cases),
        "failure_count": len(failures),
        "failures": failures,
        "freq_by_step": dict(ranked),
        "top_priority": top,  # 错误最多、该先改的组件
    }
