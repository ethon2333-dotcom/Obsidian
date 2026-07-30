---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, FunctionCalling, 端侧Planner, 评测, 概念]
---

# Function Calling 端侧工具调用

> 含「端侧 Planner 模型横向评测表」（2026-07-30 实测）。未实测模型标注「待补」，不臆造数据。

## 一句话定义

**端侧 Function Calling** 是在设备本地用小模型 Planner 完成「Tool Choice（选哪个工具）+ 参数抽取（填槽）」的能力，让意图路由零单查询成本、毫秒级响应。

## 为什么重要

- 实测证明「小模型 + 单应用 Schema 微调」即可在端侧达到可用路由准确率，是压低延迟/成本的关键。
- 与云端大模型形成「本地优先 + 低置信升级」的混合架构。

## 适用边界

- 端侧模型适合窄域 / 单应用 Schema；跨域、多轮、低置信需升级云端。
- 设备算力约束（NPU/内存）决定可跑模型规模（见 [[OS-PM-3B模型内存预算推演]] 相关思路）。

## 证据与例子：端侧 Planner 模型横向评测（2026-07-30）

| 模型 | 规模 | 策略 | 关键指标（实测） | 定位 |
|------|------|------|-----------------|------|
| **FunctionGemma 270M** | 270M | 单应用 Tool Schema 微调 + LiteRT-LM | Mobile Actions 微调 **base 58% → 85%**；BFCL Simple 61.6 / Parallel 39（详见下方 2026-07 增补） | 端侧 Planner（主路由） |
| **qwen3-0.6b-tool-router** | 0.6B | 禁 CoT + 严格 JSON，确定性 edge router | BFCL Multi-Turn Base **90.42%**；Relevance **90.89%** | 确定性边缘路由 |
| **Qwen3-Embedding-0.6B** | 0.6B | 语义缓存学习环 | 降低云端依赖（高频意图留端侧） | 语义缓存 |
| Gemma 4 | 待补 | — | 待实测 | 待跟踪 |
| Qwen3-Coder-Next | 待补 | — | 待实测 | 待跟踪 |

> 说明：Gemma 4 / Qwen3-Coder-Next 为待跟踪项，数据回填后更新本表（回流 [[OS PM 近一月情报简报 2026-07-31]]）。

### 2026-07 增补（官方实测，来源 [[OS PM 近一月情报简报 2026-07-31]]）

- **FunctionGemma 官方 BFCL（零样本）**：Simple 61.6 / Multiple 63.5 / Parallel 39 / Parallel-Multiple 29.5 / Live-Simple 36.2 / Live-Multiple 25.7 / Live-Parallel 22.9 / Live-Parallel-Multiple 20.8 / Relevance 61.1 / Irrelevance 73.7。并行/多函数组合场景显著下滑 → 官方强调"必须微调"。
- **S25 Ultra 实测（dynamic_int8, CPU LiteRT XNNPACK 4 线程, ctx 1024）**：Mobile Actions 微调 prefill **1718 tok/s**、decode **125.9 tok/s**、TTFT **0.3s**、模型 **288MB**、峰值 RSS **551MB**。
- **Local Agent Bench Round 3**：qwen3:1.7b **#1（0.960）**、functiongemma **0.640（435ms）** → 详见 [[Local Agent Bench 端侧智能体基准]]。
- **口径说明**：早期简报记 FunctionGemma "46%→90%"（基准未注明），与 Google 官方 "base 58% → Mobile Actions 微调 85%" 口径不同；以 **官方 58%→85%** 为准。

## 可复用启发

- 选型顺序：先小模型本地路由（FunctionGemma 类）→ 低置信升级云端 → 语义缓存吸收高频。
- 评估必须上 BFCL / 内部 benchmark，记录准确率、参数抽取 F1、延迟、tok/s（见 [[系统级 Intent 路由评估 SOP]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 路由：[[Intent Router 语义路由]] ｜ 方法：[[系统级 Intent 路由评估 SOP]]
- 算力：[[OS-PM-3B模型内存预算推演]]（跨库参考）

#标签/FunctionCalling #标签/端侧Planner #标签/评测
