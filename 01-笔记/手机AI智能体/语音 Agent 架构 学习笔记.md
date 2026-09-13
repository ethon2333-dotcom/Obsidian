---
title: 语音 Agent 架构 学习笔记
tags: [手机AI, 语音Agent, AppIntent, 全双工, 广度种子]
created: 2026-09-13
source:
  - "WebSearch/WebFetch 2026-09-13: apiscout.dev 实时语音API对比(2026)"
  - "WebSearch/WebFetch 2026-09-13: Google Cloud Blog — Gemini Live API GA on Vertex AI (2025-12)"
  - "WebSearch/WebFetch 2026-09-13: Pipecat.ai / LiveKit Agents 官方文档"
  - "WebSearch/WebFetch 2026-09-13: Picovoice on-device voice agent cookbook"
  - "WebSearch/WebFetch 2026-09-13: EETTaiwan — 端侧语音AI / SLM 综述 (2026-08)"
---

# 语音 Agent 架构 学习笔记

> 心智模型一句话：**语音不是"又一种输入法"，而是把「听→想→做→说」串成一个全双工 Agent 循环、直接对接端侧意图框架（App Intents）的交互入口。**

本文是「手机 AI 智能体」知识树的🌱广度种子。它聚焦**"语音作为 Agent 交互入口的工程架构范式"**——如何把语音流变成一个能听、能想、能调工具、能说的持续循环，并与 [[端侧意图框架 学习笔记]] / [[App Intent 的核心作用]] 对接。刻意区别于：
- [[端侧语音大模型 学习笔记]]：讲**端到端语音 LLM 模型本身**（Speech LLM 的声学/语义范式）；
- [[语音交互与端侧 ASR TTS 学习笔记]]：讲**级联链路**（唤醒→ASR→意图→TTS）及端云切分。
本文不深钻声学模型，只铺架构广度。

---

## 1. 定义：什么是"语音 Agent"

语音 Agent = 一个以**语音为主要交互模态**的 Agent，运行在一个**持续存在的双向会话（session）**里，而不是"说一句、答一句"的请求-响应盒子。它的核心是把三类能力闭环：

- **听**：流式 ASR / 原生语音理解，实时把声波变成可推理的表征；
- **想**：LLM / SLM 推理 + 工具调用（function calling）→ 结构化意图；
- **做**：意图映射到 [[App Intent 的核心作用]] / 端侧意图框架，触发真实动作；
- **说**：流式 TTS / 原生语音生成，把结果说回给用户。

关键差异点是**全双工**：用户可以在 Agent「想」或「说」的中途插话（barge-in / 打断），系统要能检测到并让出话语权。这使得它更接近"对话"而非"命令"。

---

## 2. 分类对比

### 2.1 全双工 vs 半双工（按"话语权"）

| 维度 | 半双工（传统语音助手） | 全双工（语音 Agent） |
|---|---|---|
| 话语权 | 轮次严格交替：用户说完→Agent 答 | 可随时打断、插话、重叠 |
| 打断检测 | 无（常说完才响应） | barge-in：VAD 检测用户起音即停播 |
| 感知副语言 | 弱 | 可建模语气/情绪/节奏（affective） |
| 典型形态 | 智能音箱指令 | Realtime / Gemini Live / Moshi 类 |
| 工程难点 | 低 | 打断检测、回声消除、turn-taking |

### 2.2 级联（Cascade）vs 端到端语音 LLM（Speech LLM）

| 维度 | 级联 ASR→LLM→TTS | 端到端语音 LLM（Speech LLM） |
|---|---|---|
| 链路 | 三段独立模块拼接 | 单一模型原生处理音频 |
| 中间可读文本 | 有（便于调试/合规） | 无（黑盒音频流） |
| 延迟来源 | 每段叠加 | 单模型内部 |
| 副语言/情绪 | 易丢失 | 原生建模（语调、停顿、情绪） |
| 工具调用 | 在 LLM 段做 function calling | 需模型原生支持或外挂 |
| 生态成熟度 | 高（组件可换） | 快速演进中 |
| 代表 | Pipecat/LiveKit 级联管道、Picovoice | OpenAI Realtime、Gemini Live、Moshi |

> 现实里多数"语音 Agent 平台"是**级联 + 流式 + 全双工编排**：用流式 ASR、流式 LLM、流式 TTS 拼出低延迟体验，而非真·单一 Speech LLM。端到端语音 LLM 是模型侧的范式（见 [[端侧语音大模型 学习笔记]]），架构侧如何调度它则是本文主题。

---

## 3. 主流架构方案横向表

| 方案 | 类型 | 传输/连接 | 全双工 | 原生语音 | 工具调用 | 定位 |
|---|---|---|---|---|---|---|
| **OpenAI Realtime API** | 托管实时模型 API | WebRTC / WebSocket / SIP | ✅ | ✅ 端到端语音 | ✅ function calling（据称支持 MCP 服务器，待核实） | App 内语音助手 / copilot |
| **Gemini Live API** | 托管实时多模态 API | WebSocket（BidiGenerateContent） | ✅ | ✅ Native Audio（Gemini 2.5 Flash） | ✅ function calling + Search Grounding | 音视频多模态实验 / Google 生态 |
| **VAPI** | 托管语音 Agent 平台 | WebRTC / 电话(SIP) | ✅ | 级联（可换 STT/LLM/TTS） | ✅ | 快速上线电话/网页 Agent |
| **Retell AI** | 托管语音 Agent 平台 | 电话 / Web | ✅（barge-in 优化） | 级联 | ✅ | 可靠 AI 电话客服 |
| **LiveKit Agents** | 开源框架 | 自带 WebRTC 基础设施 | ✅ | 级联（STT→LLM→TTS） | ✅ | 高并发、易扩展 |
| **Pipecat** | 开源框架（Daily 维护） | WebRTC / Daily / WebSocket / SIP | ✅（含打断处理） | 级联，可接 Realtime/Live | ✅ | 灵活、多模态管道编排 |
| **Cartesia** | 低延迟 TTS 层 | 流式 API | —（TTS 侧） | 级联组件 | — | 让语音 Agent "说话"更自然 |
| **Hume** | 情感智能语音/TTS | API | — | 级联组件 | — | 情绪感知的表达层 |

> 上述"类型/传输/能力"为公开文档与 2026 年横向对比文章归纳；**具体延迟数字、价格、模型版本以厂商官方为准，部分二手数字见文末待核实清单。**

---

## 4. 语音意图理解 → 工具调用 / App Intents 映射

语音 Agent 的"做"这一步，本质是**把口语指令转成结构化意图**，再交给底层意图框架执行：

1. **口语 → 文本/语义表征**：流式 ASR 或原生语音理解产出转写或语义向量；
2. **语义 → 结构化意图**：LLM 把"帮我把客厅灯调暗一点"解析为 `{action: setBrightness, target: livingRoomLight, value: dim}` 形式的 function call / intent 参数；
3. **意图 → 系统执行**：映射到 [[端侧意图框架 学习笔记]] 中的 App Intents / 元服务，由 OS 或 App 实际执行；
4. **结果 → 语音回流**：执行结果回灌会话，流式 TTS 说出。

产业共识（据 Superteams.ai 课程等 2025-2026 资料）：**实时音频会话里的工具调用范式已收敛为同一形状**——API 只发"意图+参数"信号，业务执行由你的应用负责，再把结果回灌同一会话。这与 [[App Intent 的核心作用]] 中"App Intent 是 App 暴露给系统的标准门窗与对讲机"高度同构：语音 Agent 不过是把"对讲机"换成了一张会说的嘴。

跨端想象：
- **Apple App Intents**：语音 Agent 的 function call 直接落到 App Intents 域，由系统调度任意 App 的能力；
- **HarmonyOS 元服务**（见 [[HarmonyOS 元服务 学习笔记]]）：语音意图触发元服务卡片，免安装即调；
- **MCP / Context Engineering**（见 [[Context Engineering 学习笔记]]、[[MCP 与设备侧 MCP]]）：语音 Agent 的"工具箱"可用 MCP 标准化暴露，上下文工程决定它在该调哪个工具时该记住什么。

---

## 5. 端侧语音 Agent（on-device）

为什么要在手机本地跑语音 Agent：

- **隐私**：音频不出设备，避免敏感语音被上传/用作训练数据（GDPR/CCPA、医疗/会议场景强需求）；
- **延迟**：省去网络往返，配合 NPU/DSP 本地推理可达更低首字/首音延迟；
- **离线/可靠**：无网也能用，适合车载、穿戴、 Rural 等弱网场景；
- **成本**：免云端按分钟计费。

典型端侧栈（级联为主）：
- 唤醒词：Picovoice Porcupine（常驻、超低 CPU）；
- 流式 ASR：Picovoice Cheetah、Whisper / faster-whisper、NVIDIA Parakeet（ONNX 移植）；
- 端侧 LLM/SLM：picoLLM、MLC-LLM（Llama-3 / Phi-3.5 Mini，4/8-bit）、Gemma 3、Qwen2 等 1–7B 级 SLM；
- 流式 TTS：Picovoice Orca、Kokoro-82M（约 8200 万参数，端侧 NPU 可跑）、Piper；
- 硬件落点：现代 NPU/DSP 已能实时跑 0.5–30 亿参数 SLM（见 [[端侧 AI 芯片架构谱系 学习笔记]]、[[端侧推理框架生态 学习笔记]]）。

> 端侧语音 Agent 与 [[端侧语音大模型 学习笔记]] 的边界：本文关心"怎么把本地 ASR/SLM/TTS 编排成一个全双工 Agent 循环并接意图框架"，模型本身的能力与训练留给那篇。

---

## 6. 2025-2026 进展（广度速览，均待官方口径核实）

- **Gemini Live API 于 2025-12 在 Vertex AI 转为 GA**，基于 Gemini 2.5 Flash Native Audio，强调原生音频、多模态（音视频同会话）、affective dialogue、proactive audio（智能 barge-in）、continuous memory。
- **OpenAI Realtime API** 持续迭代（gpt-realtime），强化 function calling 与连接选项；有二手资料提及 MCP 服务器支持与 SIP 电话呼叫（待核实）。
- **开源框架成熟**：Pipecat（Daily）与 LiveKit Agents 成为自建语音 Agent 主流底座；Pipecat 主打灵活管道（可接任意模型），LiveKit 主打开箱即用线性管道与自动扩缩。
- **托管平台分化**：VAPI / Retell 主打"快速上线电话/网页 Agent"；Cartesia / ElevenLabs / Hume 主攻 TTS 与情感表达层。
- **端侧 SLM 上扬**：1–7B SLM + 端侧流式 ASR/TTS 使"本地全双工语音 Agent"在手机 NPU 上变得可行。
- ⚠️ 部分二手文章出现"GPT-Live / NVIDIA PersonaPlex-7B / GPT-5.5 绑定推理"等说法，**未见官方证实，统一标待核实，不采纳为事实**。

---

## 7. 代表产品 / 框架一览（便于后续深挖）

- 托管实时模型 API：OpenAI Realtime、Gemini Live
- 托管语音 Agent 平台：VAPI、Retell AI、Bland、ElevenLabs Conversational AI、Twilio ConversationRelay
- 开源框架：Pipecat、LiveKit Agents、SpeechBrain
- TTS / 表达层：Cartesia（Sonic）、Hume、ElevenLabs
- 端侧 SDK 栈：Picovoice（Porcupine/Cheetah/picoLLM/Orca）、Whisper、Kokoro-82M、MLC-LLM
- 评测/基准：FullDuplexBench、FDB 系列（打断/全双工能力，口径待核实）

---

## 8. 待解问题（BREADTH → 后续 DEPTH 入口）

- [ ] **全双工打断检测（barge-in）**：如何在噪声/重叠语音下可靠检测用户起音并即时停播？VAD vs 模型级 turn-taking 的取舍？
- [ ] **语音意图 → App Intents 映射可靠性**：口语的歧义、省略、指代，如何稳定落到结构化意图参数？失败回退策略？
- [ ] **端侧流式语音 Agent 的功耗**：常驻唤醒 + 本地 ASR/SLM/TTS 并发的续航与发热约束（关联 [[端侧 AI 功耗与散热约束 学习笔记]]）。
- [ ] **级联 vs 端到端语音 LLM 的架构抉择**：何时该用级联（可调试/可换件），何时该上原生 Speech LLM（副语言/延迟）？
- [ ] **跨端意图框架的语音接口标准化**：App Intents / 元服务 / MCP 如何统一承接语音 Agent 的工具调用？

---

## 附：来源清单

1. apiscout.dev — *Realtime Voice AI APIs Compared: OpenAI, Gemini, Vapi, Retell, Twilio* (2026) — 提供实时语音 API 七维对比与选型建议。
2. Google Cloud Blog / aibrew.news — *Gemini Live API GA on Vertex AI* (2025-12) — 原生音频、多模态、affective dialogue、proactive audio、tool use。
3. Pipecat.ai 官方文档 / GitHub — 开源语音多模态 Agent 框架，管道式编排，200+ 集成服务。
4. LiveKit Agents 文档 / Aize 对比文 (2025-12) — 线性 STT→LLM→TTS 管道，自带 WebRTC，自动扩缩。
5. Picovoice Cookbook — *On-device AI voice agent* — Porcupine/Cheetah/picoLLM/Orca 端侧级联栈与基准。
6. EETTaiwan (2026-08) — *端侧语音 AI：把说话变成新键盘* — SLM 1–7B、NPU/DSP 端侧推理综述。

## ⚠️ 待核实清单

- Gemini Live 在 Vertex AI 的"377ms 平均延迟"、OpenAI Realtime 的"$32/$64 每百万音频 token"等具体数字来自第三方测算，**以厂商官方定价/文档为准**。
- OpenAI Realtime 是否官方支持 **MCP 服务器 / SIP 电话呼叫**，仅见二手来源，待核实。
- "GPT-Live / NVIDIA PersonaPlex-7B / GPT-5.5 绑定边说边想"等说法**未见官方证实，不采纳为事实**。
- FullDuplexBench / FDB 系列基准的具体分数与排名口径不一，待核实。
- 各托管平台最新模型版本、资费、区域可用性变动频繁，**落地前以官网为准**。

#标签/手机AI #标签/语音Agent #标签/AppIntent #标签/全双工
