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
