# Agentic AI Learning

A hands-on engineering project for studying agent design patterns and building reusable, reliable agentic systems.

This repository is more than a learning log. Each lesson aims to produce a small artifact that can be run, inspected, reused, or extended by other learners and builders. It contains original notes, experiments, tests, failure analysis, reusable components, and design decisions. It does not publish private data or full course transcripts.

## What this project is about

The project follows a learn-by-building loop. Every lesson connects a concept to a runnable experiment, a testable boundary, and a reusable artifact.

The learning path moves from individual design patterns to a verifiable research workflow:

```text
Understand a pattern
→ build the smallest experiment
→ test normal and failure cases
→ inspect the evidence
→ record the root cause
→ improve the design
```

The project is updated as new lessons, experiments, reusable components, and test results are completed. The public repository contains the engineering artifacts and their boundaries, not private study conversations or personal routines.

The central question is not “Can the model generate an answer?” but:

> **Can the system plan, act, verify, fail safely, and improve?**

## Current status

The first three course sections have produced these engineering artifacts:

- Direct Generation vs. Reflection
- JSON Planning with branching decisions
- Tool Use Loop with trace records
- Evaluation and error analysis
- Research Agent pipeline
- Reflection for chart generation
- Planning with Code Execution
- Code as Action with a restricted local executor

The current lesson is partially complete. The first half is finished; the second half will continue in the next study session.

## Current lesson: Code as Action

The current experiment tests this principle:

> **The code itself is the plan.**

Instead of expanding a fixed tool list for every new question, the model can generate a multi-step program for a controlled interpreter.

The prototype supports:

- extracting code from `<execute_python>...</execute_python>` tags
- basic AST validation
- a restricted execution namespace
- structured success and error results
- refusal of selected unsafe operations

This is a **learning prototype**, not a production sandbox. Production execution would require process or container isolation, timeouts, resource limits, network and file permissions, data isolation, monitoring, audit logs, cleanup, and security testing.

See [Lab 05: Code as Action](./labs/05-code-as-action/).

## Engineering principles

1. **Identify the output before selecting evaluation criteria.**
2. **Define what “better” means before running Reflection or Evaluation.**
3. **Use the planning format that matches the task.** JSON is useful for fixed workflows; executable code can express richer dynamic plans.
4. **Treat tool growth as a design trade-off.** More tools can create brittle routing and more edge cases.
5. **Design capability and safety together.** A prototype executor must not be described as a production sandbox.
6. **Treat multi-agent collaboration as a hypothesis.** Compare it with a baseline using explicit metrics.
7. **Use traces, tests, and failure samples to locate root causes.**
8. **Change one variable at a time and run regression tests.**
9. **Turn each error into a test, rule, or boundary for the next iteration.**

## Built for reuse

The repository is designed for two audiences:

- **Builders** can run the small tools, inspect the implementation, and extend the tests.
- **Learners** can follow the concept → experiment → test → correction path and reproduce the reasoning process.

Each artifact should make four things clear:

1. What problem it solves
2. How to run or inspect it
3. What the tests prove
4. What the artifact does not guarantee

## Learning workflow

Each lesson follows the same engineering loop:

```text
Course concept
→ understand the concept
→ small knowledge check
→ visible artifact
→ normal-case test
→ failure-case test
→ error record
→ project update
```

The difficulty increases gradually:

```text
single tool
→ multiple tools
→ branching
→ missing or abnormal data
→ tool failure
→ controlled code execution
→ quality evaluation
```

## Course artifacts

| Area | Evidence |
|---|---|
| Reflection | [Direct Generation vs. Reflection](./labs/01-direct-generation-vs-reflection/) |
| Planning | [JSON Planning](./labs/02-json-planning/) |
| Tool use | [Tool Use Loop](./labs/03-tool-use-loop/) |
| Research | [Research Agent](./labs/04-research-agent/) |
| Code execution | [Code as Action](./labs/05-code-as-action/) |
| Evaluation | [Error Analysis](./evaluations/) |
| Lesson notes | [Reflection and Code as Action](./notes/03-reflection-code-as-action-summary.md) |

## Final project direction

After the course sections are complete, the validated patterns will be combined into a **Business Research and Decision Evidence Assistant** using synthetic data only.

The target workflow is:

```text
User question
→ clarify the goal and definitions
→ plan the work
→ call tools or controlled code
→ check data quality
→ reflect against task-specific criteria
→ evaluate failures
→ produce an evidence-based report
```

The system is intended to support analysis, not make unreviewed decisions. It should preserve evidence, boundaries, unresolved questions, and failure causes.

## Repository guide

- [Progress](./PROGRESS.md)
- [Changelog](./CHANGELOG.md)
- [Handwriting and review protocol](./HANDWRITING-REVIEW.md)
- [Question guide](./QUESTION-GUIDE.md)
- [Course notes](./notes/)
- [Labs](./labs/)
- [Evaluations](./evaluations/)

## Scope and safety

All experiments use synthetic inputs. This repository must not contain private company information, personal data, internal screenshots, credentials, tokens, databases, or sensitive local paths.

The course source remains the property of its original authors and platforms. This repository records personal understanding and original experiments rather than full course materials.
