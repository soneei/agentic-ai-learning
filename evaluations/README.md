# Evaluation / Error Analysis

## 核心思想

不靠“答案看起来对不对”评估，而是：

```text
把错误定位到具体某一步 → 统计频次 → 决定优先改哪个组件
```

> 错误频次 × 有没有明确改法 = 优先级

没有 trace 就无法做错误分析——只能说“结果不好”，不能说“第几步出了问题”。
Tool Use Loop 的 `trace` 和 `status/reason` 就是这里的原料。

## 第一个工具：`error_analyzer.py`

输入一批 case，每个 case 写清：

- `name`：样本名
- `data`：输入数据
- `should_succeed`：是否期望成功（区分“真失败”和“本来就该拦下”）

处理流程：

```text
跑 run_loop → 压缩成 outcome_label
→ 只挑“本该成功却失败”的样本
→ 用 CATALOG 归因到具体 step
→ 按频次排序 → 输出 top_priority（该先改的组件）
```

### 错误分类表 CATALOG

| 结果标签 | 归因组件 | 含义 | 改法方向 |
|---|---|---|---|
| `stopped:upstream_error` | read_dataset | 原始数据缺字段，第一步拦下 | 补数据源，别改下游 |
| `stopped:max_steps_reached` | orchestrator | 步数超限，疑似死循环 | 检查注册表/next_step 是否成环 |
| `stopped:no_tool_for_next_step` | check_data_quality | 异常数据停在人工核查 | 设计内拦截；要自动化就加核查工具 |

### 关键设计

- `should_succeed=False` 的样本停下不算错误——防止把“正确拦截”误判成 bug
- 归因到 step 而不是笼统说“错了”，才能定位到具体工人
- `top_priority` 给出频次最高的组件和改法，直接指导下一步

## 测试

`test_error_analyzer.py`，5 个用例：标签压缩、全好样本零失败、失败正确归因、预期失败不计入、top_priority 选频次最高。

```bash
cd .. && PYTHONPATH="labs/03-tool-use-loop:evaluations" python3 -m unittest evaluations/test_error_analyzer.py
```

5 个测试全部通过。

## 现在的完整链路

```text
Lab01 Reflection → Lab02 JSON Planning → Lab03 Tool Use Loop → Evaluation
错误分析用 trace 反查前面每个工具，找出最高频的失败点。
```

下一步：把 error analysis 用到一组真实构造的失败样本上，形成一份错误分析报告。
