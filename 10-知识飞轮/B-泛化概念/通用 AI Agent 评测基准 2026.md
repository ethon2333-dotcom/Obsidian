---
type: concept
status: draft
derived_from: "[[AI Agent 半月情报简报 2026-07-31]]"
tags:
  - AIAgent
  - 评测
  - Benchmark
  - 通用智能体
---

# 通用 AI Agent 评测基准（2026）

> 全新主题（2026-07 检索新增）。聚焦**通用/云端智能体**的评测基准体系。端侧专用基准见 [[Local Agent Bench 端侧智能体基准]]；单点路由评测见 [[Function Calling 端侧工具调用]]。本篇与二者互补、不重复。

## 一句话定义

2026 年通用智能体评测从「单点刷分」走向「**可复现、跨基准可比、能力解耦**」：用统一框架把「模型能力 / 脚手架 / 环境」效应分开，才能公平衡量 Agent 真实水平。

## 为什么重要

- **解决评测乱象**：过去各基准用不同环境/打分，结果无法横比（AgentCompass 把模型/工具/环境三要素解耦）。
- **暴露能力边界**：OmniaBench 显示即便前沿模型 Overall Pass@1 仅 ~58%，规划/约束保持/自适应纠正是共性短板。
- **与端侧互补**：端侧看「能不能在手机上跑通路由」（[[Local Agent Bench 端侧智能体基准]]），通用看「复杂任务端到端完成度」，二者都应进评估 SOP。

## 适用边界

- 多数基准偏云端/通用场景；端侧资源约束下的评测仍靠 Local Agent Bench 类。
- 基准迭代快，引用需标注版本/日期。

## 证据与例子（2026-07 窗口）

- **AgentCompass**（上海AI实验室，arXiv 2607.13705）：开源智能体能力评测基础设施，解耦模型/工具/环境三要素，可复现可扩展。
- **OmniaBench**（arXiv 2607.14989）：通用智能体基准，90 L1 / 354 L2 域、1431 任务；Claude-Sonnet-5 **58.54** / GPT-5.6-Sol **57.14** Pass@1。
- **AgenticDataBench**（清华+蚂蚁，arXiv 2607.01647）：数据科学智能体评测，433 技能标签；放宽步数/超时仅 0.6% 改善→瓶颈在推理决策。
- **EdgeBench**（7-22）：边缘/端侧 Agent 的 benchmark 与排行榜方法论。
- **A Unified Framework**（arXiv 2605.27898）：统一 7 基准/24 域/15 模型/400K rollouts，分离「模型 vs 脚手架/环境」效应（方法论背景）。

## 可复用启发

- Agent 评估应**双轨 + 分层**：通用基准（AgentCompass/OmniaBench）+ 端侧基准（[[Local Agent Bench 端侧智能体基准]]）+ 单点路由（[[Function Calling 端侧工具调用]]）。
- 选型别只看总分，要看**在你目标场景子域**的具体表现（AgenticDataBench 启示：最强未必最省、最便宜未必最差）。

## 关联

- 来源：[[AI Agent 半月情报简报 2026-07-31]]
- 端侧基准：[[Local Agent Bench 端侧智能体基准]]
- 单点路由：[[Function Calling 端侧工具调用]]
- 方法：[[系统级 Intent 路由评估 SOP]]

#标签/AIAgent #标签/评测 #标签/Benchmark
