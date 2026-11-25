# Learning progress

## Overall

- Current stage: 第 3 节课上半部分已完成，Code as Action 实验已跑通，等待继续学习下半部分
- Modules done: 基础设计模式 7 / 7 已跑通；当前课程新增 Reflection 图表工作流与 Planning with Code Execution，概念测试通过、实验复盘中
- Course progress: 课程共 8 节，当前完成第 3 节课上半部分；概念小测试和 Code as Action 最小实验完成，下半部分待继续
- Small-test rule: 每个课程小节完成一个小测试；8 节全部完成后进入综合大工具项目
- Final project direction: 业务研究与决策证据助手（暂定，使用虚拟数据）
- Learning upgrade: 从结果检查、固定工具和 JSON 计划，升级到对象感知 Reflection、Code as Action、安全执行边界和 multi-agent 评估；每节一个小测试，并使用纠错表复盘
- GitHub practice: 研究优秀开源工程中的 prompt、工具注册、测试和错误处理结构，不复制课程原文或私有数据
- Current focus: 继续第 3 节课下半部分；暂不推进生产级 Sandbox，先保持学习版原型边界
- Project goal: learn by building reliable, reusable agentic systems through small, testable experiments
- Project promise: every lesson should leave a runnable artifact, a test boundary, and a reusable learning path
- Learning scope: agent design patterns, planning, tool use, reflection, evaluation, controlled execution, and multi-agent systems
- Last updated: 2026-11-25

## Modules

| Module | Status | Evidence |
|---|---|---|
| Agent vs hardcoded tool | Done | `notes/00-two-day-learning-summary.md` |
| Agentic workflow | Done | `notes/00-two-day-learning-summary.md` |
| Reflection | Done | 已完成 Direct Generation vs Reflection 闭环：`labs/01-direct-generation-vs-reflection/COMPARISON.md` |
| Planning | In progress | 已完成基础 JSON Plan、三类分支和最小执行器：`labs/02-json-planning/executor.py` |
| Tool use | Done | Lab 03 完成：四个工具 + 调度器 `orchestrator.py`，15 个测试通过；能自动执行、读结果、更新状态、继续或安全停止：`labs/03-tool-use-loop/` |
| Evaluation / error analysis | Done | 错误分析器 + 失败样本报告完成：`evaluations/FAILURE-REPORT.txt`，7 样本注入 5 错全抓到、2 正常无误判、归因正确；10 个测试通过 |
| Research agent | Done | 四块零件全链路跑通：`research_agent.py` 产出综合报告 `COMPREHENSIVE-REPORT.txt`（基线+Reflection+Evaluation），6 测试通过；全仓库测试 OK |

## What I understand

- Agent 不只是多调用几次模型，关键是由谁决定下一步行动。
- Agentic workflow 的核心是把复杂任务拆成多个可观察、可迭代的步骤。
- Reflection 需要明确的 criteria，不能只要求模型“检查一下”。
- Tool use 中，LLM 输出工具调用请求，真正执行函数的是开发者侧代码。
- Evaluation 应先看失败样本和 trace，再决定改哪个组件。
- 已能逐行解释最小 JSON Planning 执行器，并总结其链路：结构化输入 → 按优先级判断 → 选择路径 → 结构化输出。
- 已区分确定性规则执行器与完整 Agent，识别出自然语言理解、运行时规划、工具执行、观察—行动循环、失败恢复、记忆和质量评估等缺口。
- Code as Action：代码本身可以承载多步计划；相比固定工具列表更灵活，但必须在受限环境中执行，并用测试验证安全拒绝与运行错误。
- Multi-agent system：多个 Agent 按角色分工协作解决复杂任务，但是否优于单 Agent 仍需通过指标、基线和 Evaluation 验证。
- Tool Use Loop 闭环：调度器用注册表把 next_step 字符串映射成真实函数，循环执行；四种停止条件保证遇到错误、异常、死循环或未注册步骤时安全停下，不瞎猜。
- 错误归因思想：只统计“本该成功却失败”的样本，归因到具体 step 再排序；“本来就该拦下”的不能算 bug。

## Current questions

- 如何把 Reflection 的对象识别和 criteria 选择，变成可重复的评估步骤？
- RestrictedExecutor 怎样逐步升级为真正隔离、可超时、可限资源的执行环境？
- Code as Action 与 Tool Use Loop 在什么任务边界下各自更合适？
- Multi-agent 相比单 Agent 的收益，应该用什么 baseline 和指标验证？

## Next actions

1. 在后续学习时继续第 3 节课下半部分，不把上半部分误记为整节完成。
2. 继续沿用学习版 RestrictedExecutor 做受控实验，不扩展成生产级 Sandbox。
3. 后续课程继续沿用“概念 → 小测试 → 实验 → 纠错 → 工程同步”的闭环。
4. 每节新课先读取材料，确定主线，再设计对应小测试和可见产出。
5. 8 节全部完成后，启动“业务研究与决策证据助手”综合大工具项目，并用课程中验证过的边界、评估和反馈闭环逐步实现。
