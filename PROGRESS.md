# Learning progress

## Overall

- Current stage: 完成 Day 1–2 学习记录
- Completion: 2 / 8 modules
- Course progress: 课程共 8 节，目前只有前 3 节材料，其余 5 节尚未学习
- Current focus: 完成 Tool Use Loop
- Learning goal: 成为能够独立做产品、解决真实问题并获得收入的超级个体
- Current coding gap: 还不懂如何写代码，需要从最小可运行实验开始
- Last updated: 2026-11-20

## Modules

| Module | Status | Evidence |
|---|---|---|
| Agent vs hardcoded tool | Done | `notes/00-two-day-learning-summary.md` |
| Agentic workflow | Done | `notes/00-two-day-learning-summary.md` |
| Reflection | Done | 已完成 Direct Generation vs Reflection 闭环：`labs/01-direct-generation-vs-reflection/COMPARISON.md` |
| Planning | In progress | 已完成基础 JSON Plan、三类分支和最小执行器：`labs/02-json-planning/executor.py` |
| Tool use | In progress | 已启动 Lab 03：`labs/03-tool-use-loop/README.md`，第一版使用本地虚拟数据工具 |
| Evaluation / error analysis | Not started | - |
| Research agent | Not started | - |

## What I understand

- Agent 不只是多调用几次模型，关键是由谁决定下一步行动。
- Agentic workflow 的核心是把复杂任务拆成多个可观察、可迭代的步骤。
- Reflection 需要明确的 criteria，不能只要求模型“检查一下”。
- Tool use 中，LLM 输出工具调用请求，真正执行函数的是开发者侧代码。
- Evaluation 应先看失败样本和 trace，再决定改哪个组件。
- 已能逐行解释最小 JSON Planning 执行器，并总结其链路：结构化输入 → 按优先级判断 → 选择路径 → 结构化输出。
- 已区分确定性规则执行器与完整 Agent，识别出自然语言理解、运行时规划、工具执行、观察—行动循环、失败恢复、记忆和质量评估等缺口。

## Current questions

- Reflection 在什么任务上能稳定提升质量？
- 如何用统一标准比较 direct generation 与 reflection？
- 如何记录一次实验中的中间结果和失败原因？

## Next actions

1. 完成 Tool Use Loop 的 `calculate_changes` 工具。
2. 完成 `check_data_quality` 和 `generate_summary` 工具。
3. 串起真正的工具执行、结果读取、状态更新和自动选下一步。
4. 测试停止条件、失败恢复和最终输出。
5. 完成 Evaluation / Error Analysis 实验。
6. 再进入 Research Agent 实验。
