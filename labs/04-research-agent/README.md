# Lab 04：Research Agent（综合实验）

## 一句话定位

把前面四个模式装成一台机器：给一个研究问题，Agent 自己规划 → 调用工具 → 反思 → 评估，产出带边界的研究报告。

```text
Reflection + Planning + Tool Use + Evaluation → Research Agent
```

## 任务边界（本阶段只定这个，先不写代码）

### 做什么（IN）

- 输入：一组虚拟公司经营数据（沿用星河数据工具，不用真实数据）
- 输出：一份结构化研究小结 + 一个反思检查记录 + 一个错误归因
- 只回答：“这家公司发生了哪些可核验的变化？”

### 不做什么（OUT）——硬边界

- 不接真实金融 API、不碰真实股票行情
- 不给买卖建议、不预测股价、不推断估值
- 不解释“为什么变化”（只报告“发生了什么”）
- 数字必须来自表内，不编造、不引入外部信息
- 数据缺失或异常 → 停下等人工核查，绝不猜一个答案

> 边界的作用：把“能力”和“责任”框住。宁可少做，不可越界。

## 四块零件怎么装进这台机器

| 模式 | 来自 | 在 Research Agent 里负责 |
|---|---|---|
| Planning | Lab 02 | 把研究问题拆成步骤，处理缺失/澄清/异常分支 |
| Tool Use | Lab 03 | 真正执行 read → calculate → check → summary，调度器串循环 |
| Reflection | Lab 01 | 报告出来后，按 criteria 自检：数字对不对、有没有越界 |
| Evaluation | Eval 模块 | 注入失败样本，归因到组件，统计该先修哪个 |

## 完整链路（目标形态）

```text
研究问题
  → Planning：拆步骤 + 分支判断
  → Tool Use：调度器执行四工具，产出小结
  → Reflection：按 criteria 检查小结，必要时修订
  → Output：带边界的最终报告
  （旁线）Evaluation：拿失败样本归因，反馈该改哪个组件
```

## Reflection criteria（复用 Lab 01，不重新发明）

小结出来后，逐条检查：

1. 数字有没有抄错？
2. 每条结论能不能回到表内找到依据？
3. 事实和推测有没有分开？
4. 有没有给出买卖建议？（有就是越界）
5. 有没有承认“表内无法判断”的事情？

## 关键认识

- Research Agent 不是新技术，是把已验证的零件编排起来
- 边界比能力重要：能做什么决定上限，不做什么决定可信度
- Reflection 和 Evaluation 的区别：前者查“这份报告对不对”，后者查“哪个组件总出错”

## 下一步

按顺序，一次一个动作：

1. 让调度器跑通基线，产出第一份小结（复用现有代码）
2. 加 Reflection：让 Agent 按 criteria 自检报告
3. 加 Evaluation：注入失败样本，产出归因
4. 形成完整报告

## 第一步：跑通基线（已完成）

`baseline.py` 复用 Lab03 的调度器 + 四工具，不写任何新工具，第一次把机器开起来。

- 自动找到 Lab03 工具目录，一键可跑
- 输入 3 个指标（营收/净利润/经营现金流）× 3 年
- 走完 read → calculate → check → summary，产出小结
- `BASELINE-SUMMARY.txt` 是真实运行输出
- 5 个测试通过

修过的真实 bug：`run_loop` 返回的最外层是调度器结果，真正的工具输出嵌在 `result["result"]` 里。`format_summary` 一开始少拆了一层导致 `KeyError: 'summary'`，已修正。

> 这又一次印证：跑起来才会暴露问题，光看代码看不出来。

## 第二步：加 Reflection 自检（已完成）

`reflection.py` 把 Lab01 的 5 条 criteria 变成确定性检查代码。

**诚实定位**：这是规则版 Reflection，不是 LLM 自审。
数字、越界词、边界声明能查；微妙的语义越界查不了。

**一个关键设计**：检查时必须传入原始 dataset 做对照基准。
只拿报告本身无法核对“数字有没有抄错”——Reflection = 报告 + 原始证据 → 核对。

5 条 criteria：

- 数字正确（逐条对照原始 changes）
- 结论可追溯（带指标名和年份）
- 事实推测分开（禁推测词）
- 无越界建议（禁买卖词）
- 有数据边界声明

像 Lab01 一样，用故意造错验证：`test_reflection.py` 注入 4 种错（数字错、买卖建议、推测措辞、无依据结论），全部被抓到；干净报告全 PASS。5 个测试通过。

## 第三步：加 Evaluation，形成综合报告（已完成 · 四块零件齐）

`research_agent.py` 把三块结果拼成一条流水线：

```text
Tool Use（基线产出小结）
  → Reflection（按 5 条 criteria 自检，传原始证据对照）
  → Evaluation（复用 7 失败样本集，归因到组件）
  → 综合报告 COMPREHENSIVE-REPORT.txt
```

Planning 已体现在调度器的分支逻辑里。至此四块零件全部在同一个 Research Agent 里跑通。

综合报告三部分：

1. 基线小结：4 工具执行链 + 6 条可核验变化
2. Reflection：5 条 criteria 全 PASS
3. Evaluation：7 样本识别 5 失败，归因 read_dataset 3 次 / check_data_quality 2 次，优先修 read_dataset

6 个测试通过。全仓库四个模块（Lab02/03/04 + evaluations）测试全部 OK。

## 状态

Research Agent 全链路完成。四块零件齐备，课程前 3 节的核心模式已全部转成可运行代码 + 测试 + 报告。
下一步：可选——补第 4～8 节课程内容，或把本仓库整理后推送 GitHub。
