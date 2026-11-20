# 手写笔记｜Agentic AI 学习两日

> 记法说明：中文为主、术语保留英文原词；箭头表示因果，`✎` 是当下想法的标记，不是结论。
> 覆盖：Day 1 硬编码工具 vs Agent ｜ Day 2 Agentic AI Workflow 课程（Reflection / Planning / Tool Use / Evaluation / Research Agent）

---

## 目录（照这个顺序复习）

```
Day 1  ✎ 我那个工具到底算不算 agent
Day 2  ① agentic workflow 是什么   ② reflection   ③ planning
       ④ tool use 到底怎么发生的   ⑤ error analysis   ⑥ research agent
收尾   把六件事压成一张自测表
```

---

## Day 1｜硬编码工具 vs Agent

### ✎ 起因

我那个「上架前·广告文案合规预检」跑通了，页面看着像模像样——但它其实还是**规则引擎**：关键词命中，然后查法条表、目录表、处罚表，把结果拼出来。

**知识在表里，逻辑在代码里，两者分开存放。** 这就是「硬编码工具」的典型形态：判断在写代码那一刻就被冻结了。

### ✎ 一句话判据

> 如果不动代码，就改不了它的行为 —— 那它是 tool，不是 agent。

Agent 是把「查什么、调哪个工具、何时算做完」交给模型在**运行时**决定。行为不是一段固定序列。

### ✎ 六维对照（背这张表就够）

| 维度 | 硬编码工具 | Agent |
|---|---|---|
| 判断来源 | 关键词 / 正则 / 静态映射 | LLM 做 **semantic judgement** |
| 知识更新 | 改代码、重新发布 | 换 prompt / 拉最新目录 |
| 步骤顺序 | 固定流水线 | **Planning** 运行时编排 |
| 工具选择 | 调用点写死 | **Tool Use**：模型自己决定 |
| 出错处理 | 无自检 | **Reflection**：自审 + 修订 |
| 同义改写 / 隐晦表达 | 命中不到就漏判 | 语义泛化能兜住变体 |

### ✎ 我给自己排的三层

```
Layer 1  语义判断   关键词命中 → 模型判断（输出：违规点 / 法条 / 置信度 / 建议改写）
Layer 2  工具调用   证书查询 · 功能目录联网拉取 · 广告备案状态
Layer 3  规划+反思  拆成分 → 逐项查 → 自检漏判与误判 → 置信度 + 人工复核建议
```

**现在的位置：** L1、L2 骨架搭了，L3 是雏形——plan 还是**固定六项流水线**，模型只在「措辞」那一项被调用。它不决定查什么，也不决定什么时候停。

✅ 所以老实说：**它是「知识与逻辑分离」的中间态，不是完整 agent。** 距离 agent 差的就是「谁来决定」。

---

## Day 2｜课程六件事

### ① agentic workflow 是什么

关键词：**多步、迭代、可比一次性生成慢，但成果好得多**。

```
线性生成（一次成型、不许退格）
   ↓ 换成
大纲 → 检索 → 下载网页 → 初稿 → 读初稿看还缺什么 → 修订 → 循环
```

⚠️ 课程原话提醒：**agentic 工作流可以更慢，但 work product 好得多。** 别拿速度当唯一指标。

还有一句我记下来的话：**能不能把任务 decompose 成步骤、并让每一步执行好，决定了你能否做这件事。** 这不是技巧，是门槛。

`human-in-the-loop` 是可选项，但关键事实那一段值得留一个人。

---

### ② reflection｜为什么它有效

**Definition：** 让 agent 回头批自己的中间产物，找缺陷，改，再批。

**证据：** Wei et al. 那张图——浅柱 zero-shot、深柱同模型加 reflection，很多任务上深柱明显更高。

⚠️ 但 **your mileage may vary**。基础 HTML 收益有限；**嵌套结构**这种复杂输出才明显。

**什么时候特别值得开：**

- 结构化数据（HTML 表、嵌套 JSON）格式错了
- 步骤型指引（比如泡茶步骤）漏步、不连贯
- 生成域名 / 命名：可能有负面含义、难发音
- 邮件：语气对不对、事实与承诺有没有编

**提示词怎么写（就这两条）：**

1. 明确要求 **review / reflect on the first draft**（别说「改进一下」，它不知道改进什么）
2. 给一组明确的 **criteria**（易读吗？有负面含义吗？tone 对吗？事实准确吗？）

```text
Review the email first.
1) Check the tone.
2) Verify all facts, statements, and promises are accurate.
Based on the problems you find, write the next draft of the email.
```

⚠️ 成本：多绕几轮 = 更慢更贵；没有客观对错标准时，**过度反思会把自己绕进更差的答案**。

`✎` 我发现的坑：我的 reflection 是**规则巡检**，不是模型回审，而且没有「二次补查」闭环——发现问题却不回去重查，等于白反思。

---

### ③ planning｜计划要机器能读

**为什么 JSON：** 下游代码要 `parse`。英语写计划，人能读，代码读不稳。

**系统提示词骨架：**

```text
You have access to the following tools: {description of tools}
Create a step-by-step plan in JSON format.
Each step should have the following items:
step number, description, tool name, and args.
```

**输出长这样：**

```json
{
  "plan": [
    { "step": 1, "description": "Find round sunglasses",
      "tool": "get_item_descriptions", "args": { "query": "round sunglasses" } },
    { "step": 2, "description": "Check available stock",
      "tool": "check_inventory", "args": { "items": "results from step 1" } }
  ]
}
```

**格式排序（我的记忆锚）：**

```
JSON  >  XML  >  Markdown  >  plain text
稳        稳       有歧义      最不可靠
```

⚠️ 课程原话：Markdown「sometimes slightly more ambiguous」；plain text「the least reliable」。

**进阶：** 让模型 **写代码，让 code 表达计划**——极复杂流程要靠这个才稳定执行。

---

### ④ tool use｜函数调用到底怎么发生

这是我这两天花最多时间想清楚的一件事。

**关键认知：LLM 不直接调函数。** 它只是**输出一段特定格式的文本**，告诉你的代码「我要调这个」。真正执行的是你写的代码。

```
用户提问
  → LLM 扫工具集，决定要不要调
  → 输出标记（早期：FUNCTION CALL get_current_time）
  → 我的代码检测标记、抽出函数名和 args
  → 我调用函数，拿到结果（8 am）
  → 把结果塞回 conversational history
  → LLM 看着全部上下文，写最终回答
  → 有时它决定再调一个工具，循环继续
```

**早期写法（现在不用了，但懂了才知道原理）：**

```text
You have access to a tool called get_current_time.
To use it, output the following text exactly:
FUNCTION CALL get_current_time
```

带参数就是 `FUNCTION CALL get_current_time("Pacific/Auckland")`。

⚠️ 这套手写语法 **clunky**：要自己写提示词、自己字符串匹配、自己解析参数——**任何一处写错就静默失败**。

**现代 LLM：** 原生训练过，用特定语法请求工具调用，不用你手写标记。

**开发者的活到底是啥：** 想清楚这产品要干哪些事 → 每件事写成一个函数 → 摆给模型 → 模型自己选。

---

### ⑤ evaluation｜先别改，先数

**核心问题：** 工作流跑得不好，先改哪？多数人凭 gut 挑一个，然后埋头几个月，整体性能没动。

**方法：只分析失败样本 + 用 spreadsheet 计数。**

```
读 trace（每步的中间输出 = span）
  → 把「最终输出不满意」的样本单拎出来
  → 逐个判定：是哪一步差？差在哪？
  → 表格里数频次
```

**归因原则（这条最容易做错）：**

> 上游给的候选池本身就烂，下游「挑最佳来源」这一步**不该被判错**——它已经尽力了。

**排优先级不是看错误率，是看两件事的乘积：**

```
优先级 ≈ 错误频次 × 我有没有改进思路
```

错误多但我毫无办法的组件，先放着；错误多且我有明确改法的，立刻上。

⚠️ 术语：**trace** = 整次运行所有中间输出；**span** = 单步输出。来自 **observability** 领域。

`✎` 我的 ab 测试里 81.8%、误杀 10/21 —— 这就是典型的「某一个 span 偏严」，得回到 semantic 层去数，而不是改别的地方。

---

### ⑥ research agent｜课程那条主线的样子

```
研究主题（例：怎么造一家能跟 SpaceX 竞争的火箭公司）
→ planning 出调研步骤
→ web search + 下载网页
→ synthesize & rank findings
→ assess agent 检查连贯性
→ 生成完整 Markdown 报告
```

为什么值得跟：这套骨架能直接改成法务合规、医疗细分、产品调研的专用 research agent。

---

## 收尾｜把两天压成一张自测表

复习时只回答这六个问题，答不上就回去看对应节：

1. 我的系统里，**谁**决定下一步做什么？如果是代码里的固定顺序 → 它还不是 agent。
2. 我的 reflection 有**明确 criteria** 吗？还是只说「检查一下」？
3. 我的 plan 下游代码能**稳定 parse** 吗？是 JSON / XML 还是英语散文？
4. 我的工具调用是模型决定，还是调用点写死？
5. 我上一次读 **trace** 是什么时候？有没有数过哪个 span 最差？
6. 我改的那个组件，是「错误最多」的还是「我最会改」的？

---

## 易错点速记

⚠️ **把 agentic 等同于「多调几次模型」** —— 不是次数问题，是「谁决定步骤」。

⚠️ **反思没有 criteria** —— 等于让模型自由发挥，越思越飘。

⚠️ **计划用 Markdown / 纯文本** —— 人看得懂，代码解析不稳。

⚠️ **误判归因给下游** —— 上游输入烂的时候，下游不做替罪羊。

⚠️ **按直觉选组件改造** —— 课程原话：可能几个月，整体性能几乎没动。

⚠️ **以为 LLM 自己执行函数** —— 它只发信号，执行永远在你的代码里。

---

## 极简流程（贴在显示器边上）

```text
拆任务 → 每步配 model / tools / schema → 先搭个粗糙原型
→ 读 trace → 只挑失败样本 → 表格数错误 → 找 subpar 组件
→ 按「频次 × 改进思路」排序 → 单点改 → 回归 → 再迭代
```
