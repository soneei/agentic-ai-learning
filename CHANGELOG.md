# Changelog

## 2026-11-20

- 创建 Agentic AI 学习项目本地仓库骨架。
- 建立 README、PROGRESS 和 CHANGELOG。
- 规划 notes、labs、assignments、evaluations 四类内容目录。
- 确定下一步实验为 Direct Generation vs Reflection。
- 新增手写学习与回顾协议，明确手写本、实验和 GitHub 的分工。
- 新增对话输出压缩协议：一次一个重点，先结论后动作，默认短输出。
- 记录学习动机、工程师成长目标，并新增 Agentic AI 学习提问指南。
- 将第一个实验收敛为“表内可核验变化”，创建 Direct Generation prompt 初稿和合格判定清单。
- 完成首轮 Reflection：按同一检查清单复核 Direct Generation，发现一处措辞可更精确，但不需要大幅重写。
- 构造故意含计算错误和越界判断的输出，验证 Reflection 能识别错误、表外推断和投资结论。
- 比较 Direct Generation 与 Reflection 的收益、代价和适用场景，完成首个实验闭环。
- 将 Reflection 模块标记为完成，开始 Lab 02：JSON Planning。
- 根据用户提出的四步任务，修正为“口径确认 → 描述变化 → 异常检测 → 带边界解释 → 验证 → 输出”的七步计划。
- 纳入 Module 1 PDF 学习材料，补充 Planning 的运行时工具选择、澄清、分支、兜底和 trace 观察要点。
- 将用户提出的三个分支转换为 JSON Planning：缺失数据回原始数据补充、口径模糊先澄清、结果异常进入核查；新增“原始数据也缺失时不得猜测”的边界。
- 编写 `executor.py` 和 `test_executor.py`，用五个场景验证 JSON 分支选择；5 个单元测试全部通过。
- 记录关键认识：Agent 设计模式是业务能力的放大器，不是金融等领域专业判断的替代品；直觉负责发现问题，专业语言负责转化为可验证任务。
- 明确自检质量的前置条件：标准明确、数据可验证、结果可交叉验证；这些条件依赖业务实践，Agent 不能凭空创造可靠标准。
- 完成最小 JSON Planning 执行器逐行学习，整理从 Scenario 输入到 choose_path 分支判断、结构化输出和演示运行的完整链路。
- 分析执行器距离完整 Agent 的差距：自然语言理解、动态规划、真实工具调用、观察—行动循环、失败恢复、停止条件、记忆和质量评估。
- 启动 Lab 03：Tool Use Loop，沿用虚拟金融数据分析，先用本地确定性工具验证“选择工具 → 执行 → 观察 → 更新状态 → 继续或停止”。
- 今日学习收尾：暂停在 `read_dataset` 完成后的检查点；下次继续 `calculate_changes`、其余工具、完整循环，再进入 Evaluation / Error Analysis，最后进入 Research Agent。

## 2026-11-23

- 明确项目定位：按长期"工程学习档案"方式持续复盘并更新到 GitHub。
- 澄清课程进度：Andrew Ng Agentic AI 课程共 8 节，目前手上只有前 3 节材料，后 5 节尚未学习。
- 提交此前遗留的 3 个 Reflection 实验文件，工作区清空；完成全仓公开安全检查（无公司信息、PII、密钥、本地路径）。
- 实现 `calculate_changes` 工具：错误透传、逐年增长率计算、除零保护，4 个单元测试全部通过。
- 手写协议新增"代码要不要手记"判断标准：能查到的语法不记，能迁移的判断原则要记。

## 2026-11-25

- 校正课程工程进度同步：README、PROGRESS、CHANGELOG 必须与当天实际学习内容一致，不能提前把未来课程写成“明天开始”。
- 当前学习内容更新为 Reflection 图表工作流与 Planning with Code Execution；本课下半部分下午继续，目标是在 1–2 小时内完成并留下作品产出。
- 明确课程推进规则：每个小节完成一个小测试，但整体进度优先；讲解需照顾零计算机基础，同时避免把单个概念拆得过碎。
- 完成本课概念小测试：fixed-tool approach、Code as Action、safe sandbox、flexibility/control trade-off、multi-agent system。
- 新增 `labs/05-code-as-action/`：使用 `<execute_python>...</execute_python>` 标签提取代码，做 AST 安全检查，在受限命名空间执行多步计划；覆盖正常执行、缺少标签、文件访问拒绝和运行时错误 4 个测试，全部通过。
- 产出 `DEMO-RESULT.txt`，记录 Code as Action 的成功结果与安全拒绝结果。当前课程概念与最小实验已完成，17:00–18:30 继续复盘并补充最终学习记录。
- 根据课程深入程度全面更新项目档案：README 从“第 1–3 节/明天开始”改为当前课程收尾状态；补充对象感知 Reflection、Code as Action、安全边界、multi-agent 验证和反馈闭环五条升级线；更新学习原则、课程路线、Lab 05 入口和下一步。同步修正 PROGRESS 的当前阶段、课程状态与下一课交接规则；将 Evaluation 文档从“待做失败样本”改为“已完成并迁移到安全边界测试”。
- 用户确认当前只完成第 3 节课上半部分：生产级 Sandbox 暂不开发，RestrictedExecutor 仅作为学习版原型，用于验证“代码本身即计划、危险代码拒绝、错误结构化返回”；已将 README 和 PROGRESS 改回准确的“下半部分待继续”，避免把整节课提前标记完成。

## 2026-11-24

- 项目状态核对：校正 PROGRESS.md 与代码不一致处——Next actions 删除已完成的 calculate_changes、Completion 表述改为 Modules done 3/7、Last updated 更新为 11-24；实测 4 个测试仍全部通过。
- 实现 `check_data_quality` 工具：异常标记（除零、涨幅>100%、跌幅>50%）+ 正常/核查分流，8 个测试全部通过。写测试时发现"跌幅下限 -100%，abs 阈值抓不到暴跌"的缺陷并修正为涨跌分开判断。
- 实现 `generate_summary` 工具：把质检通过的数据整理为结构化小结（确认变化/待核实/数据边界），上游报错则透传；10 个测试全部通过，四个工具齐备。
- 提交根目录 README 的 14 天总计划说明（`2c36b24`）。
- 回顾 check_data_quality：正式/白话双语讲解、4 个测试用例复盘、涨跌阈值分开判断的 bug 来源。
- 实现调度器 `orchestrator.py`：注册表把 next_step 字符串映射为真实函数，while 循环自动执行；四种停止条件（done / 上游报错 / 步数超限 / 未注册步骤）安全停下，`trace` 记录每步。
- 新增 `test_orchestrator.py` 5 个用例；全部 15 个测试通过，Tool Use Loop 完整闭环。
- 启动 Evaluation / Error Analysis：建 `evaluations/error_analyzer.py`，按 outcome_label 归因到组件、统计频次、输出 top_priority；区分“真失败”与“预期拦截”（should_succeed）；5 个测试通过。
- 完成失败样本分析报告：`failure_report.py` 构造 7 样本（注入 5 错），`FAILURE-REPORT.txt` 真实输出显示 5 错全抓到、2 正常无误判、归因分布 read_dataset 3 / check_data_quality 2；新增 5 个测试，共 10 个通过。
- 启动 Lab 04 Research Agent：设计任务边界 `labs/04-research-agent/README.md`——四模式整合定位、IN/OUT 硬边界、Reflection criteria 复用 Lab01、完整链路与目标形态。
- 跑通 Research Agent 基线：`baseline.py` 复用 Lab03 调度器+四工具，产出 `BASELINE-SUMMARY.txt`（3 指标 6 条变化，带数据边界）；修复 `format_summary` 少拆一层 result 的 KeyError；5 个测试通过。
- Research Agent 加 Reflection：`reflection.py` 把 Lab01 五条 criteria 变成规则版检查（需传原始 dataset 做对照基准）；注入 4 种错全抓到，5 个测试通过。明确规则版 ≠ LLM 自审的能力边界。
- Research Agent 全链路完成：`research_agent.py` 把 Tool Use 基线 + Reflection + Evaluation 拼成一条流水线，产出综合报告 `COMPREHENSIVE-REPORT.txt`（三部分：基线小结/Reflection 全 PASS/Evaluation 优先修 read_dataset）；6 个测试通过，全仓库 Lab02/03/04+evaluations 测试全部 OK。四块零件齐备。
