# Lab 05：Code as Action

## 学习目标

验证一个核心想法：

> **The code itself is the plan.**

模型不先输出 JSON 步骤，再由固定执行器逐步解释；它可以返回一段被明确标签包住的 Python 代码，由受控解释器检查后执行。

## 实验流程

```text
model output
→ extract <execute_python>...</execute_python>
→ validate code
→ execute in a restricted environment
→ return result or safe refusal
```

## 安全边界

本实验只演示一个受限执行器，不是完整 sandbox。它会：

- 只接受完整的 `execute_python` 标签
- 拒绝 `import`、文件访问、网络访问和危险 dunder 名称
- 只暴露少量安全内置函数
- 代码执行失败时返回结构化错误
- 不接触真实文件、数据库、网络或公司数据

生产系统仍需要真正的隔离沙箱、资源限制、超时和权限控制。

## 小测试

```bash
PYTHONPATH=labs/05-code-as-action python3 -m unittest test_executor.py -v
```

## 可迁移原则

> **Code as Action expands planning flexibility, but execution must be constrained and evaluated.**
>
> Code as Action 扩大了计划表达能力，但执行必须受限并经过评估。
