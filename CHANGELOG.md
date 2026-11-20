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
