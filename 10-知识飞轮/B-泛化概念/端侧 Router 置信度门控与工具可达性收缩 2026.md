---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-16]]"
tags: [AppIntent, 端侧Planner, Needle2, 置信度门控, 工具可达性, 概念]
aliases: [Needle2, 端侧Router门控, 工具可达性收缩]
---

# 端侧 Router 置信度门控与工具可达性收缩（2026）

## 一句话定义

**Needle 2（Cactus Compute，2026-08 中旬发布）** 把端侧函数调用模型的两个**执行安全机制**产品化：**① 置信度门控**——每个响应带置信分，低于阈值返回空调用 `[]` 而非硬猜；**② 工具可达性收缩**——声明工具超过 5 个时用对比检索头只放行 top-5，未选中工具在当轮**不可达（unreachable）而非 merely unlikely**。两者共同把「端侧→云端升级」从启发式变成显式阈值。

## 为什么重要

- **它把「低置信升级云端」这门 OS Agent 架构的核心取舍，从文案变成了可配置参数。** 此前本库记录的 Hybrid Router（[[Function Calling 端侧工具调用]] 08-01 增补）只说「5× 成本节省、<120ms」，没说触发条件；Needle 2 给出工程闭环：置信分 = min(校准头, 解码概率)，阈值由产品定，低于则 re-ask 或 escalate。
- **工具可达性收缩是 ADI（[[Agent Data Injection 数据注入攻击]]）的低成本预防**：未选中工具不仅概率低，而是**结构性不可达**——prompt injection 无法借「误召回」把写动作塞进读上下文，因为该工具的 schema 根本没进当轮 KV。这与 Chrome Origin Sets「unselected tools unreachable」同源（[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]）。
- 与 [[Simple Attention Network 无FFN端侧路由]]（Needle 26M）是同一家族：**Needle 26M 论证「无 FFN 能路由」，Needle 2 论证「路由还能自带安全闸」**。

## 适用边界

- 适用：窄域 / 单应用 schema 的**单次（single-shot）工具调用 + 结构化抽取**；设备无 GPU/NPU（树莓派 5、<$200 手机、ESP32-S3 微控制器、可穿戴）。
- 不适用：多轮 / 多工具串行依赖推理仍由云端大模型承担（Cactus 自承「No small model is perfect, and Needle says so instead of guessing」）。
- ⚠️ **厂商自述数字，非 Berkeley 官方榜**：BFCL v4 = 42.6（Cactus 归因于语料偏向消费设备动作而非通用/企业 API）；Mobile Actions 63.7 / DroidCall 17.0 / Seal-Tools in-domain 32.6 / OOD 28.7 / 函数名准确率 98.3% / BFCL 3,641 行格式良好率 93.4%。

## 证据与例子（Cactus Compute 官方页 + 多源交叉，2026-08 中旬）

**规模与部署**
- 45M 参数，单一 **14MB 二进制**，整轮会话 **~28MB RAM**；CQ2-bit（**从预训练起就做 2-bit 量化**，非事后量化，部署的 2-bit 模型即训练模型）；密封进自研 C++ 引擎，推理时**无运行时安装、无模型下载**。
- 速度（厂商自述）：树莓派 5 **500 tok/s decode**、Meta Quest 3S / Apple Vision Pro **400–1,500**、<$200 手机（三星 A 系列等）**300–700**。
- 跨平台预编译二进制/静态库：macOS / Linux（x86-64 / ARM64 / ARMv7 / RISC-V / MIPS32el）/ Windows / Android / iOS·watchOS·tvOS / WebAssembly；MIT 许可上架 HuggingFace。
- 已落地：Pebble Index 01 智能戒指本地跑 Needle 做离线语音动作（提醒/笔记/闹钟/计时器），动作以 **MCP tools** 暴露，云处理保留作高质量兜底。

**架构（Simple Attention Network 升级版）**
- 27 层 / 512 宽；**Hadamard MLP 替代 FFN**（延续无 FFN 路线，见 [[Simple Attention Network 无FFN端侧路由]]）、保留 GQA 注意力、加 **hashed n-gram engram 记忆**、multi-lane hyper-connections。
- **70 MFLOPs/token**（35M/45M 参数 matmul-active）；对比 LFM2.5-230M 460、FunctionGemma 270M 540、Apple FM ~6000——量级再降一阶。
- 权重**不解出到 RAM**：2-bit 码在向量寄存器内展开、融合成 int8 点积；字节级 grammar（从 JSON schema 编译）约束每个 token，结构 token 可跳过 **98%** 词表投影；256-token 滑动窗口 + system turn/工具声明 pin 为 KV sink，**内存不随对话增长**。

**① 置信度门控（confidence gating）**
- 每个响应带一个置信值 = **min(校准后处理头 calibrated head, 调用 token 的解码概率)**。
- **离线请求返回空调用 `[]`**（empty call），而非编造一个最接近的工具。
- 产品契约是**阈值**：高于阈值→直接执行；低于→re-ask 或 escalate 到云端。把「端侧→云端升级」变成显式旋钮。

**② 工具可达性收缩（top-5 retrieval gating）**
- 声明 ≤5 个工具 → 直接渲染；**>5 个 → 对比检索头（contrastive retrieval head）对每个 schema 嵌入一次，按 turn 打分，只放行 top-5**。
- **未选中工具在该 turn 不可达（unreachable），不只概率低**——其 schema 不进当轮 KV，prompt injection 无法借误召回把它塞进来。

## 可复用启发

- **端侧 router 的「安全」不应只靠准确率，要靠「结构性不可达」**：把危险工具的 schema 物理上挡在上下文外，比训练模型「别调它」可靠一个数量级（与 [[带外防御与确定性门控]] 同构）。
- **置信度门控 = 端云协同的结算点**：OS PM 设计端侧 Planner 时，应把「置信阈值」当作一等产品参数，而非留给模型自决（呼应 [[Confirmation UI 安全机制]] 的「触发器应由系统确定性判定」）。
- **规模阶梯更新（体积维度，手机可塞下限）**：Needle 26M（INT4 14MB）→ **Needle 2（CQ2-bit 14MB / 28MB RAM / 45M）** → Bonsai-1.7B（1-bit 0.25GB）→ FunctionGemma 270M（288MB）→ Bonsai-8B（1-bit 1.15GB）。Needle 2 在「同等 14MB 体积」下把参数从 26M 升到 45M 并加安全闸，是体积约束下「加闸不增体积」的样本。

## 与其他概念的关系

- **上游/同族**：[[Simple Attention Network 无FFN端侧路由]]（Needle 26M，论证无 FFN 能路由）；本文是同一架构的**机制升级**（CQ2-bit + 置信门控 + 可达性收缩）。
- **互补**：[[Function Calling 端侧工具调用]]（规模阶梯 + BFCL 表，Needle 2 入表）｜ [[Agent Data Injection 数据注入攻击]]（可达性收缩是 ADI 的低成本预防）｜ [[Chrome Agent Origin Sets 与用户对齐评判器 2026]]（unselected tools unreachable 同源）｜ [[Confirmation UI 安全机制]]（置信阈值 = 系统确定性触发器）｜ [[带外防御与确定性门控]]（结构性不可达同构）。
- **索引**：[[意图框架·跨体系索引 MOC]]

## 2026-08-16 增补背景

> 来源：[[AppIntent 每日情报 2026-08-16]]。Needle 2 为本窗口（2026-08-10→08-16）**唯一新增的端侧 router 模型发布**，填补了本库「端侧 Planner 已有架构（无 FFN）但缺安全闸样本」的缺口。其与 Needle 26M 的区别不在于「更大」，而在于**首次把置信门控与工具可达性收缩做成产品化闭环**。

## 2026-08-17 增补：Needle 2 发布日期锚定 + Pebble 量产落地 + SAN 论文（来源 [[AppIntent 每日情报 2026-08-17]]）

> 接续本笔记 08-16 创建。本期补发布日期与生产落地实证（Cactus 官方页 + 多家媒体 2026-08-11 起报道）。

- **发布日期锚定**：Cactus Compute 于 **2026-08-11** 发布 Needle 2（此前记「2026-08 中旬」，现可精确）。
- **首个真实产品落地——Pebble Index 01 智能戒指**：$75 屏幕less 可穿戴，录音传手机 App，App 本地跑 Needle 做离线语音动作（提醒/笔记/闹钟/计时器），动作以 **MCP tools** 暴露，云处理保留作高质量兜底。这是「小 action 模型坐在消费产品本地语音识别与确定性应用代码之间」的首个量产证明点（非浏览器 demo）。
- **架构论文锚定**：Simple Attention Network 升级版对应 arXiv **2607.18363**（Hadamard MLP 替代 FFN + engram 记忆），与 [[Simple Attention Network 无FFN端侧路由]] 同源。
- ⚠️ 厂商自述数字（500 tok/s 等）仍**无独立复现**；Pebble 落地为厂商披露，以产品固件实测为准。

## 2026-09-01 增补：Needle 2 升级契约第三方确认（来源 [[AppIntent 每日情报 2026-09-01]]）

> 接续 08-16/08-17。本期补 aibacon 对 Needle 2 的**独立第三方确认**与「升级契约」的明确表述。

- **BFCL v4 = 42.6% 获独立确认**（aibacon，第三方）：与 Cactus 自报一致；并明确给出设计契约——**置信分趋零时返回空调用 `[]`，而非编造最接近的工具**，把「端侧→云端升级」做成确定性旋钮（呼应本笔记 08-16 的「阈值 = 产品参数」主张）。
- **许可与落地广度**：MIT 代码 + Apache-2.0 权重；可编译到 RISC-V / MIPS32el；实测落 ESP32（28MB RAM）、树莓派 5（500+ tok/s）、Meta Quest 3S / Apple Vision Pro（400–1,500 tok/s）、<$200 安卓手机（300–700）。是「小 action 模型坐在本地 ASR 与确定性应用代码之间」的量产级样本之一。
- **与 ADI 防护的关系再强化**：「未选中工具物理不可达（unreachable）+ 低置信返回空而非硬猜」共同构成 ADI 的两道低成本闸门——前者防误召回写动作，后者防硬编不存在的调用；二者都不依赖模型「变乖」，而是结构/协议层强制（与 [[带外防御与确定性门控]] 同构）。详见 [[Agent Data Injection 数据注入攻击]]。

⚠️ aibacon 为第三方技术媒体，数字为 Cactus 模型卡 + Berkeley 榜引述；无独立复现，以产品固件实测为准。

#标签/Needle2 #标签/端侧Planner #标签/置信度门控 #标签/工具可达性 #标签/FunctionCalling