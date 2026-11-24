"""Tool Use Loop 调度器：按 next_step 自动派活，直到完成或停止。"""

from typing import Callable, Dict, List

from tools import (
    read_dataset,
    calculate_changes,
    check_data_quality,
    generate_summary,
)

# 工具注册表：把 next_step 的字符串映射到真正的函数
# 这是“字符串 → 行动”的关键一步
TOOL_REGISTRY: Dict[str, Callable[[Dict[str, object]], Dict[str, object]]] = {
    "calculate_changes": calculate_changes,
    "check_data_quality": check_data_quality,
    "generate_summary": generate_summary,
}

MAX_STEPS = 10  # 防止死循环的保险丝


def run_loop(dataset: Dict[str, object], max_steps: int = MAX_STEPS) -> Dict[str, object]:
    """从原始数据出发，自动调用工具，直到完成或安全停止。"""
    trace: List[Dict[str, object]] = []

    # 起点：先把原始数据交给 read_dataset
    result = read_dataset(dataset)
    trace.append({
        "tool": "read_dataset",
        "status": result["status"],
        "next_step": result["next_step"],
    })

    steps = 0
    while True:
        # 停止条件 1：步数超过上限，防止死循环
        if steps >= max_steps:
            return {
                "status": "stopped",
                "reason": "max_steps_reached",
                "result": result,
                "trace": trace,
            }

        next_step = result["next_step"]

        # 停止条件 2：next_step = done，正常完工
        if next_step == "done":
            return {
                "status": "completed",
                "reason": "done",
                "result": result,
                "trace": trace,
            }

        # 停止条件 3：上游报错，不继续派活
        if result["status"] == "error":
            return {
                "status": "stopped",
                "reason": "upstream_error",
                "result": result,
                "trace": trace,
            }

        # 查注册表，把字符串变成真正的函数
        tool = TOOL_REGISTRY.get(next_step)
        if tool is None:
            # 停止条件 4：遇到不认识的下一步（如需要人工核查），停下不乱调
            return {
                "status": "stopped",
                "reason": "no_tool_for_next_step",
                "result": result,
                "trace": trace,
            }

        # 执行工具 → 拿到结果 → 更新状态 → 进入下一轮
        result = tool(result)
        steps += 1
        trace.append({
            "tool": next_step,
            "status": result["status"],
            "next_step": result["next_step"],
        })
