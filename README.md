# Agentic AI Learning

我的 Agentic AI 学习、实验与作业记录。

这个项目以 Andrew Ng 的 Agentic AI 课程为起点，但目标不只是保存课程笔记，而是记录一条可验证的工程成长路径：

> 学习概念 → 形成理解 → 编写最小实验 → 观察结果 → 分析错误 → 迭代改进

## 当前进度

- [x] 完成 Day 1：Agent 与硬编码工具的区别
- [x] 完成 Day 2：Agentic AI workflow 基础概念
- [ ] 完成 Direct Generation vs Reflection 实验
- [ ] 完成 JSON Planning 实验
- [ ] 完成 Tool Use Loop
- [ ] 建立 Trace / Span 记录
- [ ] 完成 Error Analysis
- [ ] 完成 Research Agent

详细进度见 [`PROGRESS.md`](./PROGRESS.md)。

## 仓库结构

- `notes/`：课程概念与个人学习笔记
- `labs/`：最小可运行实验
- `assignments/`：课程作业与完成记录
- `evaluations/`：实验评估、trace、span 与错误分析
- `PROGRESS.md`：学习进度看板
- `CHANGELOG.md`：项目更新记录
- `HANDWRITING-REVIEW.md`：手写记录与反复回顾协议
- `QUESTION-GUIDE.md`：每个学习步骤如何提问

## 对话方式

学习过程中默认采用短输出：一次只讲一个重点，先给结论，再给一个动作；手写内容直接给可抄的短句。需要展开时再展开。

## 学习原则

1. 先拆任务，再写代码
2. 不把“多调用几次模型”误认为 Agent
3. 用 JSON 等机器可解析格式表达计划
4. 通过 trace 找到真正出错的步骤
5. 先统计错误，再决定优化优先级
6. 一次只改一个组件，再做回归验证

## 说明

本仓库主要记录个人理解、实验代码和作业过程。课程内容仅作学习参考，版权归原作者及课程平台所有。公开发布前会对课程原文、翻译、实验数据和个人信息进行检查。
