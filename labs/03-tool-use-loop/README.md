# Lab 03：Tool Use Loop

## 实验目标

把 JSON Planning 中的“选择下一步”变成真实的工具调用循环：

```text
任务 → 选择工具 → 执行工具 → 获得结果 → 更新状态 → 决定下一步
```

## 业务任务

仍使用虚拟公司经营数据，完成一份可核验的基础研究小结。

## 第一版工具范围

为了先理解 Agent 机制，第一版只使用本地、确定性的工具：

- `read_dataset`：读取虚拟公司数据
- `calculate_changes`：计算指标变化
- `check_data_quality`：检查缺失字段和异常结果
- `generate_summary`：生成结构化小结

不接真实金融 API，不生成投资建议。先验证 Tool Use Loop 的控制流。

## 观察重点

- Agent 如何选择工具
- 工具如何返回结果
- 返回结果如何更新下一步状态
- 什么时候继续，什么时候停止
- 工具失败时如何处理

## 第一个工具：`read_dataset`

代码位于 `tools.py`，它只负责检查必要字段并返回结构化结果：

```text
输入 dataset
→ 检查 company / unit / years / metrics
→ 缺失字段：返回 error 和 fetch_from_source
→ 字段齐全：返回 success 和 calculate_changes
```

它不计算增长率、不判断异常，也不生成投资结论，保持单一职责。

运行测试（注意设置 PYTHONPATH）：

```bash
PYTHONPATH=. python3 -m unittest test_tools.py
```

## 第二个工具：`calculate_changes`

接收 `read_dataset` 的返回结果，计算逐年变化：

```text
若上游 status 不是 success → 直接透传错误，不计算
若上游 success → 对每个指标算 absolute 和 growth_rate
→ 输出 changes，并把 next_step 指向 check_data_quality
```

关键点：

- 只输出表内可核验的数字，不解释原因、不下结论
- 上一步的错误会原样传递，不会带着坏数据继续算
- 除零时 growth_rate 返回 None，避免崩溃

## 第三个工具：`check_data_quality`

接收 `calculate_changes` 的输出，检查数据质量，只标记异常、不解释原因：

```text
上游报错 → 透传，不检查
发现异常 → status=warning，flags 列出问题，next_step=verify_source_and_calculation
数据正常 → status=success，next_step=generate_summary
```

检查三类异常：

- `zero_base_growth_rate_undefined`：基数为 0，增长率无定义
- `abnormal_growth_rate_over_100pct`：涨幅超过 100%
- `abnormal_drop_over_50pct`：跌幅超过 50%

一个设计要点：跌幅下限是 -100%，所以用 `abs(rate) > 1` 永远抓不到暴跌，涨停和跌停必须分开设阈值。这是写测试时发现并修正的真实缺陷。

## 第四个工具：`generate_summary`

接收质检通过的数据，整理成结构化小结：

```text
上游报错 → 透传，不生成
正常 → 输出 confirmed_changes / items_to_verify / data_limitations
→ next_step = done
```

小结只写表内事实：绝对变化、同比增长率、数据边界。不解释原因、不预测趋势、不给买卖建议。

至此四个工具齐了：

```text
read_dataset → calculate_changes → check_data_quality → generate_summary
```

## 调度器：`orchestrator.py`

把四个工具串成真正的 Tool Use Loop。核心是**注册表 + 循环 + 停止条件**：

```text
工具注册表：next_step 字符串 → 真正的函数
循环：执行工具 → 读结果 → 更新状态 → 再决定
停止：done / 上游报错 / 步数超限 / 遇到不认识的下一步
```

关键设计：

- 注册表把字符串变成函数调用，这是“选工具”的本质
- 停止条件 3：上游报错就停，不让坏数据继续流
- 停止条件 4：`check_data_quality` 发现异常后，`next_step=verify_source_and_calculation` 注册表里没有对应函数 → 安全停下，等人工核查，绝不瞎调
- `trace` 记录每一步走了哪个工具、什么状态，方便复盘
- `max_steps` 是防死循环的保险丝

测试：`test_orchestrator.py`，5 个用例覆盖正常完工、trace 顺序、缺字段早停、异常数据停下待核查、步数上限。

全部测试（工具 10 + 调度器 5 = 15）通过。

```bash
PYTHONPATH=. python3 -m unittest test_tools.py test_orchestrator.py
```

至此 Tool Use Loop 完整闭环：四个工具 + 一个调度器，能自动执行、读结果、更新状态、继续或安全停止。

下一步：Evaluation / Error Analysis。
