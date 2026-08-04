---
tags: [product, pm, os, 端侧AI, llm, 知识库, 学习笔记]
aliases: ["OS PM 知识库", "操作系统产品经理", "端侧AI知识库"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 🗺️ OS 产品经理知识库 · MOC

> [!abstract] 这是什么
> 围绕 **OS 产品经理（AI-Native OS / 端侧大模型方向）** 的技术知识库，源自一次 Gemini 深度对话的导出整理。主线议题：**端侧 LLM 如何在有限的 RAM / NPU 算力 / 功耗下运行**，以及 **OS 如何用「页表管理 + 剪枝 + 异构调度」压制资源占用、PM 该关注哪些指标与权衡**。

## 🧭 主题地图（原子笔记）

### A. 基础与全局视角
- [[OS-PM-概览与四大核心领域]] —— PM 要深化的 4 大领域：架构/交互/生态/工程
- [[OS-PM-系统架构与底层技术]] —— 5 层架构、能力解耦、资源调度与功耗、AI-Native OS 三件套

### B. 指标与诊断
- [[OS-PM-性能与稳定性指标体系]] —— FPS/Jank/ANR/Crash/PSS/Thermal 指标 + 埋点逻辑 + 诊断三步法

### C. 端侧大模型的系统级挑战（核心）
- [[OS-PM-端侧大模型系统级挑战]] —— PSS 双重挤压、NPU 抢占、内存墙功耗、传统 LMK/ZRAM 失效
- [[OS-PM-PagedAttention与KV Cache剪枝]] —— 虚拟内存哲学：分页存储 + 量化 + Token 驱逐
- [[OS-PM-3B模型内存预算推演]] —— 2k/8k/32k 上下文下 Weight+KV+激活+Overhead 的 PSS 推演表
- [[OS-PM-投机采样原理与能效优化]] —— 小模型猜、大模型验，把 Memory-Bound 变 Compute-Bound
- [[OS-PM-AI Runtime动态调度与降级策略]] —— 温控/电量/内存三维下的 SpecDec 动态降级矩阵
- [[OS-PM-系统AI Runtime vs 应用引擎]] —— 为什么 OS 要自研 AI Runtime（4 大护城河）

### D. 方法论 / 跨学科发散
- [[PM 需求定义 跨学科发散]] —— 把"定义需求"辐射到需求工程/JTBD/情境调查/经济学/设计思维/敏捷/博弈论/合规/逻辑/FMEA/OKR，收敛给 PM 的 5 条启示，并落到 OS/Android PM 实战（系统级 App Intent 开放能力需求定义）

## 🔗 关联
- 与 [[PRD MOC]] 互补：本库偏「技术原理与指标」，PRD 库偏「需求文档怎么写」
- 关键贯穿概念：`PagedAttention`、`KV Cache`、`Chunked Prefill`、`INT4 量化`、`Speculative Decoding`、`NPU QoS`

## ✅ 推荐学习顺序
MOC → 概览 → 系统架构 → 性能指标体系 → 端侧挑战 → PagedAttention → 内存预算 → 投机采样 → AI Runtime 调度 → 系统 AI Runtime 边界

## 💡 一句话记忆锚点
> 端侧 LLM 的瓶颈不是「NPU 算力不够」，而是「**内存带宽不够（Memory-Bound）**」——所有优化都围绕「少搬权重、少占 RAM、按需分页」。
