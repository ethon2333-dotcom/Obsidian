---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-01]]"
tags: [AppIntent, 端侧Planner, SAN, FunctionCalling, 模型架构, 概念]
---

# Simple Attention Network 无 FFN 端侧路由

## 一句话定义

**Simple Attention Network（SAN）** 是一种**完全不含 MLP / FFN 层**的端侧函数调用模型架构：只有注意力与门控，靠「query ↔ 工具 schema」的匹配与参数抽取完成单次工具路由，论证「工具调用是检索-组装，不是推理」。代表实现是 Cactus Compute 的 **Needle（26M 参数、INT4 仅 14MB）**。

## 为什么重要

- 它从**架构层面反向验证**了本库长期主张的 [[意图模式规范]] 路线：**Schema 写得越规范、越自解释，Planner 就可以越小**——既然工具 schema 本来就写在 prompt 里，Planner 不需要世界知识，于是可以砍掉 FFN。
- 实测把端侧意图路由的**算力门槛往下拉了一个数量级**：26M / 14MB 能跑赢 270M~600M 的 FunctionGemma / Qwen-0.6B / Granite-350M / LFM2.5-350M（single-shot 场景），意味着**低端机也能上系统级 Agent 的结构化路由**（吃算力的反而是 GUI 路线）。
- 对 OS PM 的选型逻辑改写：**不要按「模型聪不聪明」选，要按「schema 匹配准不准」选**。

## 适用边界

- 适用：窄域 / 单应用 Schema 的**单次（single-shot）工具调用**（选工具 + 填槽 + 输出 JSON）。
- 不适用（团队明说「实验性单次调用」）：**多轮 / 多工具串行编排**所需的依赖推理不由 SAN 承担，需升级云端大模型。
- 可推广性（团队论断，待论文）：「无 FFN」可推广到任何**模型能访问外部结构化知识**的任务（RAG、检索增强生成），因为事实已在输入里。

## 证据与例子（Needle 架构与训练，来源 [[AppIntent 每日情报 2026-08-01]]）

- **规模与开源**：从 **Gemini 3.1 Flash Lite 蒸馏**，26M 参数，**MIT 全开源**（权重 + 数据生成脚本）；INT4 量化后 **14MB**，可放进桌面 CPU 的 L3 缓存。
- **SAN 结构**：编码器 **12 层（无 FFN）** + 解码器 **8 层**（masked self-attention + cross-attention）；`d=512`，**8 头 / 4 KV 头（GQA）**，BPE 词表 8192，RoPE，编码器与输出投影**共享嵌入权重**；门控残差 `x + sigmoid(gate)·Attn(Norm(x))`，gate 初始化 0；QK 头用 **ZCRMSNorm**；一个 **CLIP 式对比学习工具选择头**先从大工具集中筛出相关工具；**Muon 优化器** + 线性投影正交约束（防表征坍缩）；每 100 步注入 **INT4 量化感知训练**作正则噪声。去掉 MLP 砍掉约 **2/3 参数量**。
- **性能**：**6000 tok/s prefill、1200 tok/s decode**（Cactus 自家运行时）；单次函数调用优于 FunctionGemma-270M / Qwen-0.6B / Granite-350M / LFM2.5-350M。
- **训练成本**：预训练 **200B token / 16×TPU v6e / 27 小时**；后训练 **2B token 合成函数调用数据 / 45 分钟**；数据由 Gemini 跨 **15 个工具类别**（计时器、消息、导航、智能家居等）合成——典型「**把前沿模型当数据引擎，而非运行时依赖**」。
- **产品化上下文**：Cactus 同时提供 **Hybrid Router**——按复杂度在端侧/云端间路由函数调用，宣称 **5× 成本节省、端侧 <120ms 延迟**；跨 iOS/Android/macOS/可穿戴单一 SDK。与本库既有的「本地优先 + 低置信升级」架构完全同构。

> ⚠️ **口径纪律（延续本库规矩）**：上述对比为 **Cactus 自述、single-shot 场景，非官方 BFCL 榜单行**，不可与 BFCL 分数并列（具体测试集与数值待补）。团队自认更大模型在对话场景下 scope/capacity 更强，Needle 是窄域专才，「小模型会挑食（finicky）」，建议在自己的工具集上实测并微调。

## 可复用启发

- 「**工具调用是检索-组装，不是推理**」应成为端侧 Planner 选型的第一性原理：外部 schema 就在上下文里，模型无需用 FFN 记忆世界知识。
- 把「**云端逃逸率**」列为端侧路由一等指标（本地承接比例越高，成本/延迟优势才成立），与 [[Function Calling 端侧工具调用]] 同口径。
- 引用任何「XX 模型跑赢 YY」的横向对比前，先三问：官方榜还是自建同名基准？微调还是零样本？全量还是子集？

## 关联

- 来源：[[AppIntent 每日情报 2026-08-01]]
- 路由：[[Intent Router 语义路由]] ｜ 端侧模型：[[Function Calling 端侧工具调用]]
- Schema：[[Intent Schema Protocol 意图模式规范]] ｜ 方法：[[系统级 Intent 路由评估 SOP]]

#标签/SAN #标签/端侧Planner #标签/模型架构 #标签/FunctionCalling
