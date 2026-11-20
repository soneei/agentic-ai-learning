# Learning progress

## Overall

- Current stage: 完成 Day 1–2 学习记录
- Completion: 2 / 8 modules
- Current focus: JSON Planning
- Learning goal: 成为能够独立做产品、解决真实问题并获得收入的超级个体
- Current coding gap: 还不懂如何写代码，需要从最小可运行实验开始
- Last updated: 2026-11-20

## Modules

| Module | Status | Evidence |
|---|---|---|
| Agent vs hardcoded tool | Done | `notes/00-two-day-learning-summary.md` |
| Agentic workflow | Done | `notes/00-two-day-learning-summary.md` |
| Reflection | Done | 已完成 Direct Generation vs Reflection 闭环：`labs/01-direct-generation-vs-reflection/COMPARISON.md` |
| Planning | Not started | - |
| Tool use | Not started | - |
| Evaluation / error analysis | Not started | - |
| Research agent | Not started | - |

## What I understand

- Agent 不只是多调用几次模型，关键是由谁决定下一步行动。
- Agentic workflow 的核心是把复杂任务拆成多个可观察、可迭代的步骤。
- Reflection 需要明确的 criteria，不能只要求模型“检查一下”。
- Tool use 中，LLM 输出工具调用请求，真正执行函数的是开发者侧代码。
- Evaluation 应先看失败样本和 trace，再决定改哪个组件。

## Current questions

- Reflection 在什么任务上能稳定提升质量？
- 如何用统一标准比较 direct generation 与 reflection？
- 如何记录一次实验中的中间结果和失败原因？

## Next actions

1. 选择一个适合反思的简单任务。
2. 固定同一份输入，分别运行 direct generation 和 reflection。
3. 用明确 criteria 比较两份结果。
4. 记录改善、退化和无法判断的地方。
5. 把实验过程整理到 `labs/01-direct-generation-vs-reflection/`。
6. 比较 Direct Generation 与 Reflection 的收益、代价和适用场景。
