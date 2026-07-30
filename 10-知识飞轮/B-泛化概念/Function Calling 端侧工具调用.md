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
| **FunctionGemma 270M** | 270M | 单应用 Tool Schema 微调 + LiteRT-LM | Tool Choice / 参数抽取 **46% → 90%**；Pixel 7 ~**2000 tok/s** prefill | 端侧 Planner（主路由） |
| **qwen3-0.6b-tool-router** | 0.6B | 禁 CoT + 严格 JSON，确定性 edge router | BFCL Multi-Turn Base **90.42%**；Relevance **90.89%** | 确定性边缘路由 |
| **Qwen3-Embedding-0.6B** | 0.6B | 语义缓存学习环 | 降低云端依赖（高频意图留端侧） | 语义缓存 |
| Gemma 4 | 待补 | — | 待实测 | 待跟踪 |
| Qwen3-Coder-Next | 待补 | — | 待实测 | 待跟踪 |

> 说明：Gemma 4 / Qwen3-Coder-Next 为待跟踪项，数据回填后更新本表（回流 [[AppIntent 跨平台情报简报 2026-07-30]]）。

## 可复用启发

- 选型顺序：先小模型本地路由（FunctionGemma 类）→ 低置信升级云端 → 语义缓存吸收高频。
- 评估必须上 BFCL / 内部 benchmark，记录准确率、参数抽取 F1、延迟、tok/s（见 [[系统级 Intent 路由评估 SOP]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 路由：[[Intent Router 语义路由]] ｜ 方法：[[系统级 Intent 路由评估 SOP]]
- 算力：[[OS-PM-3B模型内存预算推演]]（跨库参考）

#标签/FunctionCalling #标签/端侧Planner #标签/评测
