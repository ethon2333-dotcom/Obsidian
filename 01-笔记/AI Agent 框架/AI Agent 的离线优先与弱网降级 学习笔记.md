---
title: AI Agent 的离线优先与弱网降级 学习笔记
tags: [AI Agent, 离线优先, 弱网降级, 可靠性, local-first, 韧性, 边缘AI]
created: 2026-11-05
source: "WebSearch 核实（2026-11-05）+ 公开技术资料 / 厂商博客 / 社区文章"
---

# AI Agent 的离线优先与弱网降级 学习笔记

> [!quote] 心智模型
> **把"网络可用"当成一种临时特权而非默认前提：Agent 先靠本地推理/规则把活干完，联网只是"可叠加的增强"，断网时要能 store-and-forward、优雅降级，恢复后要能智能对账与同步。**

> [!info] 定位
> 🌱 广度种子：从「AI Agent 框架」锚点向外辐射，落在**可靠性/韧性**视角——与 [[AI Agent 的流式与实时交互架构 学习笔记]]（聚焦实时流式）相反维度，本篇专讲"无网/弱网下的运行能力与优雅降级"。点到为止，深度留给 Ethon 后续补。

---

## 一、广度覆盖表（点到为止）

| 维度（定义 / 分类） | 主流方案与代表（框架 / 开源 / 模式） | 2025-2026 进展 | 代表产品或研究 |
|---|---|---|---|
| **离线策略类型（分类）**：local-first / offline-capable / degraded-mode 三档 | ① Local-first（本地库为真相源，网络仅用于同步）② Remote-when-available（本地先解，不足再上云）③ Graceful degradation（LLM→规则/模板） | 2026 local-first 工具链成熟：Yjs / Automerge 2.0 / Loro / ElectricSQL / Zero / PowerSync 等形成完整生态（masturbyte, 2026） | Ink & Switch 2019 七原则；Notion 2025 末 offline-first 重构；Linear 用 CRDT 重写 sync 层 |
| **本地推理 / 规则兜底**：断网期间用端侧小模型或确定性规则维持核心能力 | 端侧 LLM（Ollama / llama.cpp / MLX / TF Lite / ONNX）、规则引擎、决策表、clinical decision rules | 端侧 NPU 普及：Apple Foundation Models（~3B，2-bit QAT）、Qualcomm Snapdragon 8 Elite、Google Gemini Nano、Samsung Galaxy AI（2025-2026 大量出货） | Strands Agents SDK + Ollama（AWS DEV301，边缘离线 Agent）；Google Scam Detection（Gemini Nano 实时本地） |
| **离线任务队列（store-and-forward）**：动作先落本地 durable store，恢复后批量执行 | Durable execution（Temporal / Inngest / Restate / DBOS）、本地消息队列、意图日志（intent log） | "把远程依赖当 best-effort" 成主流实践；CRM/工单/库存类写操作普遍改为本地排队 + 延后对账（GlobalNodes, 2026） | 见 [[AI Agent 的持久化与状态管理 学习笔记]]；现场服务平板、工厂 MES 离线工单 |
| **冲突解决与同步**：网络恢复后本地 vs 远端状态对账 | CRDT（自动合并）/ OT / LWW / 领域特定 resolver / 用户协助解决；向量时钟、逻辑时钟 | CRDT 性能：Automerge 2.0（Rust→Wasm，~100x）、Loro（合并快 2-5x）；增量 delta sync + 压缩（gzip/CBOR/MessagePack） | CouchDB/PouchDB 复制；RxDB（21.4k★）、ElectricSQL、PowerSync |
| **优雅降级策略（LLM→规则/模板）**：能力阶梯式收缩 | 4 级降级（Full→Degraded→Fallback→Offline）、circuit breaker + rule-based fallback、模板/缓存兜底 | "Silicon Protocol" 模式：熔断器开后立刻切规则引擎，恢复后自动探测关断（Towards AI, 2026，多行业部署） | Dipankar「4 Degradation Levels」；医疗分诊规则引擎、金融技术分析信号 |
| **重试退避与熔断**：弱网下避免雪崩、重复执行 | 指数退避 + jitter、circuit breaker、幂等键（idempotency key）、Saga 补偿 | "queue-and-retry 对时间敏感流程是灾难"被明确警示——需定义 fallback 而非只重试（Towards AI, 2026） | 见 [[多智能体编排的容错与错误传播隔离 学习笔记]]、[[AI Agent 工具调用的幂等性与副作用管理 学习笔记]] |
| **离线状态 UI**：让用户知道"现在能/不能做什么" | 离线徽标、能力降级提示、"AI Offline — Manual Mode"、pending 队列可见、乐观更新 | 离线优先 UX 标配：无 spinner、本地即时读写；清晰告知哪些能力受限（Dipankar Level 2/3/4 预设文案） | 移动端离线 Agent；PocketPal AI / OfflineChatbot 等本地助手 |

---

## 二、几个关键点的延伸指针（不展开）

- **Local-first 七原则**（Ink & Switch 2019）：No spinners / 数据跨设备 / 网络可选 / 无缝协作 / Long Now 等，区别于"离线缓存"或"乐观更新"。
- **"local-first, remote-when-available" 循环**：Agent 先用 on-device 资源解题，仅在不足且联网时升级到云端模型或外部服务（GlobalNodes 2026）。
- **恢复序列不只是刷队列**：需对排队动作按当前状态重新校验（工单可能已被别人关掉）、先拉新鲜上下文再应用延迟决策、回放/摘要离线期、解决本地/远端冲突（GlobalNodes）。
- **端侧硬件天花板**：RAM（硬门槛）、内存带宽（decode 阶段瓶颈，移动 50-90 GB/s vs 数据中心 GPU 2-3 TB/s）、热预算（移动被动散热）三者决定可持续体验（andreinita.co, 2026）。
- **与网关层的关系**：模型路由 / fallback 常承载在 LLM 网关（见 [[模型服务化与 LLM 网关 学习笔记]]），但熔断/降级决策应在 Agent 编排层定义。

---

## 三、待解问题（深度盲区，留给 Ethon 补）

- [ ] **离线 Agent 的"规划质量"如何不劣化？** 端侧小模型做任务分解/工具选择的成功率边界在哪？与云端 planner 的差距如何量化（连接 [[AI Agent 的测试时计算与推理时缩放 学习笔记]]）？
- [ ] **弱网下的"部分成功"如何向用户与下游系统表达？** 哪些结果算 approximate / pending-enrichment，如何结构化标记并避免下游误用？
- [ ] **多 Agent 协作在断网分区时的一致性模型？** 分区两侧各自推进后如何 merge 计划与副作用（连接 [[多智能体编排的容错与错误传播隔离 学习笔记]]、[[AI Agent 工具调用的幂等性与副作用管理 学习笔记]]）？
- [ ] **离线降级的安全护栏是否要收紧？** 规则兜底路径是否跳过原有护栏，反而放大风险（连接 [[Agent 安全护栏模式库 学习笔记]]）？
- [ ] **Android 端侧 Agent 的离线能力现状**（作为 OS PM 视角）：片上 NPU、模型分发（AAB 内嵌 / 动态下发）、权限与后台限制对 store-and-forward 的影响，待结合厂商文档核实。

---

## 四、库内关联（防信息孤岛）

- [[AI Agent 的流式与实时交互架构 学习笔记]] —— 相反维度（实时流式 vs 离线降级）；断线重连/续传与之咬合。
- [[AI Agent 的持久化与状态管理 学习笔记]] —— durable store / checkpoint 是 store-and-forward 与 resume 的承载层。
- [[AI Agent 工具调用的幂等性与副作用管理 学习笔记]] —— 排队动作重放时靠幂等键防双执行。
- [[多智能体编排的容错与错误传播隔离 学习笔记]] —— 熔断/降级/补偿同源；本篇是"断网触发"那一端。
- [[Agent 安全护栏模式库 学习笔记]] —— 降级闸门、规则兜底的护栏编排。
- [[多模态 RAG 端侧化实测 学习笔记]] / [[AI Agent 的测试时计算与推理时缩放 学习笔记]] / [[模型服务化与 LLM 网关 学习笔记]] —— 端侧推理、本地思考预算、网关 fallback 路由。

---

## 附：来源清单

1. powerapp.pro — *Design Patterns for Offline-First Apps*（2026，桌面/Raspberry Pi 本地 AI、sync/冲突/设备安全模式）
2. masturbyte.com — *Local-First Software and CRDTs - The Post-Cloud App Stack*（CRDT 生态、2026 工具链成熟）
3. automations.pro — *Putting Privacy First: Offline-First Micro Apps with Local Browsers & Edge AI*（Puma / Pi 5 边缘 AI 架构模式）
4. Towards AI (pub.towardsai.net) — *The Silicon Protocol*（2026，circuit breaker + rule-based fallback，多行业部署案例）
5. dipankar.name — *Defence in Depth for AI Agents*（4 Degradation Levels、RTO、预设文案）
6. 腾讯云开发者社区 — *AI Agent 如何在低带宽或断网环境中工作*（2025-09，本地化/边缘/增量同步/异步队列）
7. globalnodes.com — *Resilience Patterns for Agents in Unreliable Network Environments*（local-first remote-when-available、eventual consistency、recovery 序列）
8. DEV Community (dev.to/aws) — *AI agents at the edge: Build for offline, scale in cloud (DEV301)*（Strands Agents SDK + Ollama 边缘离线 Agent）
9. zanexatech.com — *On-Device AI Agents in 2026*（手机端离线 Agent 能力、NPU 设备清单）
10. 百度百科 — *端侧智能体* / *本地化AI数字助手*（定义、路线、市场口径）
11. andreinita.co — *On-Device AI Comes of Age*（硬件 RAM/带宽/热预算天花板，2026）
12. softunis.com — *决胜边缘：端侧AI崛起下的移动应用开发新战略*（2025-12，移动端云协同战略口径）

## ⚠️ 待核实清单

- ⚠️ 百度百科称端侧智能体"用户规模 5.35 亿、实际任务成功率仅约两成、高敏感权限平均接近 40%"——第三方测评数字，口径与样本待核实。
- ⚠️ softunis「2025 年底超 60% 主流应用部署端云协同、约 35% 核心 AI 迁移端侧」——媒体预测性口径，非审计数据，待核实。
- ⚠️ Towards AI「Silicon Protocol 跨 7 家机构挽回损失 $56.54M、单机构部署成本 $200K-300K」——厂商/媒体案例，未独立审计，待核实。
- ⚠️ andreinita.co 引 Qualcomm「Snapdragon 8 Elite 上 Gemma/Llama 经 Matrix Extension 达 2.9x TTFT 提升」「移动内存带宽 50-90 GB/s vs 数据中心 2-3 TB/s」——厂商基准口径，具体数值待核实。
- ⚠️ 各厂商端侧模型参数规模（Apple ~3B、Qualcomm 测试 0.27B-8B 等）与出货节奏，以厂商官方为准，待逐条复核。
- ⚠️ 文中提及的腾讯 QClaw、Kimi Work、OpenClaw 等本地 Agent 产品（2026 上半年）为公开报道口径，功能细节与可用性待核实。

---

#标签/AI Agent #标签/离线优先 #标签/弱网降级 #标签/可靠性
