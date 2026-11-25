# Agentic AI Learning

我的 Agentic AI 学习、实验与作业记录。

这个项目以 Andrew Ng 的 Agentic AI 课程为起点，但目标不只是保存课程笔记，而是记录一条可验证的工程成长路径：

> 学习概念 → 形成理解 → 编写最小实验 → 观察结果 → 分析错误 → 迭代改进

## 当前14天总计划（2026-11-24至2026-12-07）

这个项目不是孤立的课程任务，而是雪宁14天生活与成长实验中的【主学习线】。

### 14天三条主线

1. 【生活底盘】认真吃饭、限制手机、每天步行与静坐，保证学习可持续。
2. 【Agent课程与工程作品】完成当前课程项目检查点，持续留下代码、测试、笔记和GitHub更新。
3. 【趋势判断作品集】只做轻量嵌入，不与Agent课程争夺主线时间；后续整理算力、美图等已有案例。

### 本项目在总计划中的职责

本项目只负责：课程学习、代码实验、测试验证、学习笔记、进度更新和工程作品沉淀。生活底盘与长期复盘规则见工作区的`长期复盘与执行系统.md`。

### 每次学习前必须知道

- 今天可能是学习新内容，也可能是收尾/复盘日；以总计划和项目文件状态为准，不擅自跳章节。
- 一次只推进一个小动作，先核对状态，再修改代码，再运行测试。
- 每个学习单元至少留下：概念解释、代码/实验变化、测试或观察结果、未解决问题。
- 若任务未完成，记录真实原因（目标过大、环境阻力、时间估计、身体能量、任务不清、外部阻塞、逃避或优先级冲突），不写人格化自责。
- 每次完成后更新`PROGRESS.md`和`CHANGELOG.md`，让其他任务能读取当前状态。

### 当前交接点

前 3 节课程材料对应的基础实验已经完成。今天已完成第 3 节课上半部分：Reflection 图表工作流、对象识别、Code as Action、safe sandbox、flexibility/control trade-off 与 multi-agent 概念测试；并留下了 Lab 05 最小实验。第 3 节课下半部分将在后续学习时继续，当前不提前标记整节课完成。课程学习不只记录“会不会”，还记录标准如何选择、边界如何定义、实验如何验证以及错误如何进入下一轮设计。8 节全部完成后，再把这些能力合并成一个综合大工具。

## 当前进度

- [x] 完成 Day 1：Agent 与硬编码工具的区别
- [x] 完成 Day 2：Agentic AI workflow 基础概念
- [x] 完成 Direct Generation vs Reflection 实验
- [x] 完成 JSON Planning 实验
- [x] 完成 Tool Use Loop
- [x] 建立 Trace / Span 记录
- [x] 完成 Error Analysis
- [x] 完成 Research Agent
- [x] 完成本课概念小测试：Reflection、Code as Action、safe sandbox、multi-agent
- [x] 完成 Lab 05：Code as Action 最小实验

> 说明：以上是已完成的实验能力和本课学习产出，不等同于课程 8 节全部完成。当前课程还要完成最终复盘与记录；后续每节继续保留一个小测试和一个可见产出，全部课程完成后进入综合大工具项目。

详细进度见 [`PROGRESS.md`](./PROGRESS.md)。

## 课程与测试路线

| 阶段 | 状态 | 交付物 |
|---|---|---|
| 第 1–3 节 | 基础实验已完成 | 概念笔记、Lab 01–04、测试与错误分析 |
| 当前课程 | 概念测试已完成，实验复盘中 | Reflection / Code as Action 总结、Lab 05、测试与安全边界记录 |
| 后续课程 | 待学习 | 每节一个小测试 + 一个可见产出 |
| 8 节全部完成后 | 规划中 | 综合大工具（期末项目） |

### 期末综合大工具：业务研究与决策证据助手（暂定）

把课程 8 节学到的能力，合并成一个面向虚拟业务数据的可验证研究工作台：用户提出一个业务问题，工具先澄清目标与口径，再规划步骤、读取数据、调用分析工具、检查异常、回到原始证据做 Reflection，最后输出带数据来源、边界声明、待核查项和错误归因的研究报告。全程使用虚拟数据，不接公司真实资料。

### 当前工程升级方式

随着课程深入，项目的验收标准已经从“代码能运行”升级为“系统是否可解释、可验证、可控、可迭代”。当前采用五条升级线：

1. **从结果检查到对象感知 Reflection**：先识别输出对象和用途，再选择匹配 criteria；避免 checklist 看起来完整却检查错对象。
2. **从固定工具到代码承载计划**：比较 JSON Planning、Tool Use Loop 与 Code as Action 的边界；代码可以表达更丰富的多步计划，但执行必须受控。
3. **从能执行到安全执行**：学习版先做 RestrictedExecutor；后续只记录生产级要求，不把本地 `exec` 原型误称为 Sandbox。
4. **从单 Agent 到协作假设**：理解 multi-agent 的角色分工，但必须用 baseline、指标、成本和错误率验证是否真的更好。
5. **从一次性修错到反馈闭环**：每个小实验都记录“预期、实际、错误类型、根因、修复、回归测试、可迁移原则”，并把根因转化为下一轮测试或设计约束。

复杂度按一个变量递增：

```text
单工具 → 多工具 → 多分支 → 缺失/异常数据 → 工具失败 → 受控执行 → 质量评估
```

每个小节仍保持一个小测试，但测试会逐渐回答更真实的问题：系统能否安全停止、解释为什么、保留证据，并在下一轮变得更好。

它不是“替人拍板”的聊天机器人，而是一个能留下过程证据的研究副驾：

- **输入**：业务问题、虚拟公司数据、分析目标与口径
- **过程**：Planning → Tool Use → Reflection → Evaluation → Research synthesis
- **输出**：结论、计算过程、证据引用、异常与待核查项、事实/推测分离、报告质量评估
- **验收**：正常样本、缺失数据、口径模糊、异常结果、工具失败、越界结论等场景都有测试

详细设计会随着第 4–8 节的小测试逐步收敛，现在先保留为方向，不提前假装已经完成。

## 快速入口

- [GitHub 仓库](https://github.com/soneei/agentic-ai-learning)
- [学习进度看板](./PROGRESS.md)
- [项目更新记录](./CHANGELOG.md)
- [手写复习协议](./HANDWRITING-REVIEW.md)
- [提问指南](./QUESTION-GUIDE.md)
- [课程与两日学习总结](./notes/00-two-day-learning-summary.md)
- [学习动机与提问能力](./notes/01-learning-motivation-and-questioning.md)
- [Module 1 设计模式笔记](./notes/02-module1-design-patterns.md)
- [本课总结：Reflection 与 Code as Action](./notes/03-reflection-code-as-action-summary.md)
- [Lab 01：Direct Generation vs Reflection](./labs/01-direct-generation-vs-reflection/)
- [Lab 02：JSON Planning](./labs/02-json-planning/)
- [Lab 03：Tool Use Loop](./labs/03-tool-use-loop/)
- [Lab 04：Research Agent](./labs/04-research-agent/)
- [Evaluation：错误分析](./evaluations/)
- [Lab 05：Code as Action](./labs/05-code-as-action/)

## 仓库结构

- [`notes/`](./notes/)：课程概念与个人学习笔记
- [`notes/02-module1-design-patterns.md`](./notes/02-module1-design-patterns.md)：Module 1 的 Planning / Tool Use / Reflection 对照与实验补充
- [`labs/`](./labs/)：最小可运行实验
- [`labs/01-direct-generation-vs-reflection/`](./labs/01-direct-generation-vs-reflection/)：Direct Generation 与 Reflection 实验
- [`labs/02-json-planning/`](./labs/02-json-planning/)：JSON Planning 实验
- [`labs/03-tool-use-loop/`](./labs/03-tool-use-loop/)：Tool Use Loop 实验
- [`labs/04-research-agent/`](./labs/04-research-agent/)：Research Agent 综合实验
- [`labs/05-code-as-action/`](./labs/05-code-as-action/)：Code as Action 受限执行实验
- [`evaluations/`](./evaluations/)：实验评估、trace、span 与错误分析
- [`PROGRESS.md`](./PROGRESS.md)：学习进度看板
- [`CHANGELOG.md`](./CHANGELOG.md)：项目更新记录
- [`HANDWRITING-REVIEW.md`](./HANDWRITING-REVIEW.md)：手写记录与反复回顾协议
- [`QUESTION-GUIDE.md`](./QUESTION-GUIDE.md)：每个学习步骤如何提问

## 对话方式

学习过程中默认采用短输出：一次只讲一个重点，先给结论，再给一个动作；手写内容直接给可抄的短句。需要展开时再展开。

## 当前学习原则

1. **先识别任务和输出对象，再决定流程**：先问要解决什么问题、正在检查什么产出。
2. **评价标准必须任务特定**：先定义“什么叫更好”，再做 Reflection 和 Evaluation。
3. **计划形式要匹配复杂度**：固定、可控的流程可用 JSON；需要动态组合多步操作时，Code as Action 更有表达力。
4. **工具不是越多越好**：工具增加前先判断是否造成 brittle、重复和边界爆炸。
5. **能力和安全一起设计**：生成代码必须受控执行，原型不能冒充生产 Sandbox。
6. **不把多 Agent 当作结论**：角色分工只是设计假设，必须和单 Agent baseline 比较。
7. **先观察证据，再归因和修改**：通过 trace、错误样本和测试定位根因，不凭感觉大改。
8. **一次只改一个变量，再做回归验证**：让每次复杂度升级都能解释、复现、回退。
9. **把错误沉淀为下一轮设计**：每次纠错都要产生新的测试、规则或边界。

## 说明

本仓库主要记录个人理解、实验代码和作业过程。课程内容仅作学习参考，版权归原作者及课程平台所有。公开发布前会对课程原文、翻译、实验数据和个人信息进行检查。
