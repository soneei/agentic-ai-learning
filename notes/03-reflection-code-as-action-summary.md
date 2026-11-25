# Reflection 与 Code as Action：本课总结

## 1. Reflection 的主线

Reflection 不是简单重写，而是根据明确 criteria 检查输出并提出改进动作。

```text
identify the output object
→ understand its purpose
→ select matching criteria
→ check readability, clarity, completeness
→ identify a specific problem
→ propose an improvement action
→ rerun the checklist
```

关键原则：

> **Reflection criteria must be selected according to the object being reviewed.**

不同输出对象不能机械使用同一套细则：数据图表关注单位、时间范围、图例和数据来源；日程卡关注日期、时间、任务、上下文和完成标准；研究报告关注证据、事实与推测、边界和待核查项。

## 2. Two different LLMs

一个模型负责 initial generation，另一个模型负责 reflection。不同模型可能有互补的 strengths and weaknesses，但“两模型更好”只是待验证的假设。

> **Two models are not always better than one. We need evaluation to verify the improvement.**

## 3. Tool accumulation problem

固定工具方案面对更多问题时，往往需要不断增加工具来处理 edge cases，工具列表会膨胀，系统变得 brittle and inefficient。

## 4. Code as Action

```text
user question
→ LLM writes Python code
→ code expresses a multi-step plan
→ interpreter executes the code
→ answer
```

> **The code itself is the plan.**

代码可以组合多个函数，直接表达和执行多步计划，相比固定工具列表更灵活。但灵活性增加也意味着预先控制减少，执行安全要求提高。

## 5. Safe execution

生成代码不能直接无约束执行。最小实验验证了四种情况：正常多步计算可以执行；缺少标签时拒绝；文件访问被拒绝；运行时错误以结构化结果返回。

> **Code as Action expands planning flexibility, but execution must be constrained and evaluated.**

本实验不是生产级 sandbox。真实系统还需要进程隔离、资源限制、超时、网络和文件权限控制。

## 6. Multi-agent

Multi-agent system 使用多个 Agent 按角色分工协作完成复杂任务。它不是天然优于单 Agent，仍需要明确指标、基线、成本和错误率来 Evaluation。
