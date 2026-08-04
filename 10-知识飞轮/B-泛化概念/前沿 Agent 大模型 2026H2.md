---
type: concept
status: draft
derived_from: "[[AI Agent 半月情报简报 2026-07-31]]"
tags:
  - AIAgent
  - 前沿模型
  - Agent底座
  - 2026H2
---

# 前沿 Agent 大模型（2026 H2）

> 全新主题（2026-07 检索新增）。聚焦 2026 下半年把「Agent 能力」作为核心卖点的前沿大模型。端侧小模型见 [[Function Calling 端侧工具调用]]；端到端基准见 [[Local Agent Bench 端侧智能体基准]]；本篇是「云端/前沿」对照层。

## 一句话定义

2026 H2 的大模型竞争从「通用能力」转向「**每任务成本 + Agent 专项基准（编码/计算机使用）**」：厂商用更低价格、更大上下文、更高 Agent 基准分来争夺「Agent 执行底座」位置。

## 为什么重要

- **定价成为主战场**：Claude Opus 5 以半价逼近 frontier；Gemini 用 Flash 家族碎片化疗程（3.6/3.5-Lite/3.5-Cyber）。对 OS PM，「选哪个模型做 Agent 大脑」变成成本-能力权衡。
- **Agent 专项基准取代通用刷分**：Frontier-Bench（终端编码）、OSWorld-Verified（计算机使用）成为新标尺，比 MMLU 类更能反映「能不能把事办成」。

## 适用边界

- 这些是**云端/前沿**模型，非端侧；端侧路由仍看 [[Function Calling 端侧工具调用]] 的小模型。
- 模型迭代极快，本笔记为 **2026-07-31 快照**，需定期回流更新。

## 证据与例子（2026-07 窗口）

- **Claude Opus 5**（7-24）：近 frontier、半价，$5/$25 per M token、1M 上下文；Frontier-Bench v0.1（终端编码 Agent）**43.3%**（Opus 4.8 18.7%、Fable 5 33.7%）。
- **Gemini 3.6 Flash**（7-21）：每任务约少 17% token；OSWorld-Verified 计算机使用 **83.0%**，计算机使用工具内置于 Gemini API；3.5 Flash-Lite 350 tok/s、$0.3/$2.5 per M；3.5 Flash Cyber（安全微调，仅政府/受信试点）。Gemini 4 预训练已启动。
- **GPT-5.6 家族 + ChatGPT Work**（7-9，窗口前缘）：Sol/Terra/Luna 三档，Enterprise 150 万上下文；ChatGPT Work 为跨应用执行型 Agent。
- **Cursor Router**（7-22）：请求级模型路由，frontier 质量下成本降 30~60%。

## 可复用启发

- OS PM 评估「Agent 大脑」应同时看：**Agent 专项基准分 + 每任务成本 + 上下文窗口 + 工具调用/计算机使用内建能力**，而非仅通用榜。
- 与端侧分层：云端前沿模型做复杂规划/低置信升级，端侧小模型做本地路由（见 [[Function Calling 端侧工具调用]]）。

## 深化补充

- **数字口径提醒**：本笔记的 OSWorld-Verified 83.0%（Gemini 3.6 Flash）、Frontier-Bench 43.3%（Claude Opus 5）等为**厂商自述 / 2026-07 窗口快照**，非独立复核榜；据 web 复核，OSWorld 官方榜（361 项任务）头部条目与部分中文媒体「实在 Agent 90.2%」口径不一致——该 90.2% 仅见于媒体，**官方榜快照未见**，需以 os-world.github.io 为准（待核实，见 [[OSWorld 计算机操作基准]]）。
- **与端侧分层**：云端前沿模型做复杂规划/低置信升级，端侧小模型（如 [[Simple Attention Network 无FFN端侧路由]]、[[Function Calling 端侧工具调用]]）做本地路由，二者经 [[Intent Router 语义路由]] 衔接。
- **Agent 专项基准**：除 Frontier-Bench / OSWorld-Verified，还应纳入 [[通用 AI Agent 评测基准 2026]] 与 [[Local Agent Bench 端侧智能体基准]] 做端云对照。

- [ ] Claude Opus 5 的 Frontier-Bench 43.3% 与 Gemini OSWorld-Verified 83.0% 是否同测试集、同后处理？横向对比需对齐口径。
- [ ] GPT-5.6 / ChatGPT Work 在 Agent 专项基准上的公开分数缺失，待补。
- [ ] 模型迭代极快，本笔记需设定回流周期（如月度）更新快照，避免数字过时。

## 关联

- 来源：[[AI Agent 半月情报简报 2026-07-31]]
- 端侧对照：[[Function Calling 端侧工具调用]] ｜ [[Local Agent Bench 端侧智能体基准]]
- 平台落地：[[企业级 Agent 平台与 Agent-as-Asset 2026]]

#标签/AIAgent #标签/前沿模型 #标签/Agent底座
