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

## 2026-11-24

- 项目状态核对：校正 PROGRESS.md 与代码不一致处——Next actions 删除已完成的 calculate_changes、Completion 表述改为 Modules done 3/7、Last updated 更新为 11-24；实测 4 个测试仍全部通过。
- 实现 `check_data_quality` 工具：异常标记（除零、涨幅>100%、跌幅>50%）+ 正常/核查分流，8 个测试全部通过。写测试时发现"跌幅下限 -100%，abs 阈值抓不到暴跌"的缺陷并修正为涨跌分开判断。
- 实现 `generate_summary` 工具：把质检通过的数据整理为结构化小结（确认变化/待核实/数据边界），上游报错则透传；10 个测试全部通过，四个工具齐备。
- 提交根目录 README 的 14 天总计划说明（`2c36b24`）。
