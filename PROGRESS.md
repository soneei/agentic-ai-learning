# Learning progress

## Overall

- Current stage: Lab 03 Tool Use Loop 进行中
- Modules done: 3 / 7（Agent vs hardcoded tool、Agentic workflow、Reflection）
- Course progress: 课程共 8 节，目前只有前 3 节材料，其余 5 节尚未学习
- Current focus: 完成 Tool Use Loop
- Learning goal: 成为能够独立做产品、解决真实问题并获得收入的超级个体
- Current coding gap: 还不懂如何写代码，需要从最小可运行实验开始
- Last updated: 2026-11-24

## Modules

| Module | Status | Evidence |
|---|---|---|
| Agent vs hardcoded tool | Done | `notes/00-two-day-learning-summary.md` |
| Agentic workflow | Done | `notes/00-two-day-learning-summary.md` |
| Reflection | Done | 已完成 Direct Generation vs Reflection 闭环：`labs/01-direct-generation-vs-reflection/COMPARISON.md` |
| Planning | In progress | 已完成基础 JSON Plan、三类分支和最小执行器：`labs/02-json-planning/executor.py` |
| Tool use | Done | Lab 03 完成：四个工具 + 调度器 `orchestrator.py`，15 个测试通过；能自动执行、读结果、更新状态、继续或安全停止：`labs/03-tool-use-loop/` |
| Evaluation / error analysis | Done | 错误分析器 + 失败样本报告完成：`evaluations/FAILURE-REPORT.txt`，7 样本注入 5 错全抓到、2 正常无误判、归因正确；10 个测试通过 |
| Research agent | In progress | 已设计任务边界：`labs/04-research-agent/README.md`（四模式整合、IN/OUT 硬边界、criteria 复用）；尚未写代码 |

## What I understand

- Agent 不只是多调用几次模型，关键是由谁决定下一步行动。
- Agentic workflow 的核心是把复杂任务拆成多个可观察、可迭代的步骤。
- Reflection 需要明确的 criteria，不能只要求模型“检查一下”。
- Tool use 中，LLM 输出工具调用请求，真正执行函数的是开发者侧代码。
- Evaluation 应先看失败样本和 trace，再决定改哪个组件。
- 已能逐行解释最小 JSON Planning 执行器，并总结其链路：结构化输入 → 按优先级判断 → 选择路径 → 结构化输出。
- 已区分确定性规则执行器与完整 Agent，识别出自然语言理解、运行时规划、工具执行、观察—行动循环、失败恢复、记忆和质量评估等缺口。
- Tool Use Loop 闭环：调度器用注册表把 next_step 字符串映射成真实函数，循环执行；四种停止条件保证遇到错误、异常、死循环或未注册步骤时安全停下，不瞎猜。
- 错误归因思想：只统计“本该成功却失败”的样本，归因到具体 step 再排序；“本来就该拦下”的不能算 bug。

## Current questions

- Reflection 在什么任务上能稳定提升质量？
- 如何用统一标准比较 direct generation 与 reflection？
- 如何记录一次实验中的中间结果和失败原因？

## Next actions

1. ~~串起工具执行循环~~ 已完成：`orchestrator.py`，15 个测试通过。
2. ~~测试停止条件、失败恢复和最终输出~~ 已完成：5 个调度器测试覆盖正常完工、早停、待核查、步数上限。
3. ~~完成 Evaluation / Error Analysis 实验~~ 已完成：失败样本报告，10 个测试通过。
4. 再进入 Research Agent 实验。（任务边界已设计，下一步：跑通调度器基线产出小结）
