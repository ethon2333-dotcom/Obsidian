# 知识拓展 Loop 状态

- 锚点：手机AI智能体 / AI Agent框架 / PM / 效率工具
- 策略：BREADTH > DEPTH，每轮 3-4 篇「广度种子笔记」，从锚点向外辐射一到两跳，深度留白给 Ethon
- 只写 `01-笔记/`，不动 `10-知识飞轮/`

## 已覆盖（日期｜主题｜落点）

### 2026-08-09（第 1 轮）
- Agent 评测与基准体系（GAIA/τ-bench/OSWorld/AndroidWorld/SWE-bench + 轨迹评测转向）｜`01-笔记/AI Agent 框架/Agent 评测与基准 学习笔记.md`
- 移动端 NPU 硬件与推理编译栈（Hexagon/APU/ANE/Tensor + QAIRT/NeuroPilot/LiteRT/ExecuTorch，NNAPI 弃用）｜`01-笔记/AI模型基础/移动端 NPU 与推理编译栈 学习笔记.md`
- PKM 方法论与 Obsidian 生态（Zettelkasten/PARA/LYT + 工具横向 + AI×PKM 张力）｜`01-笔记/知识管理与效率工具/PKM 方法论与 Obsidian 生态 学习笔记.md`【新建子文件夹 + MOC】
- Agentic UX 交互设计模式（六侧模式 + HAX/PAIR/Apple HIG + 自主性光谱 L0–L5）｜`01-笔记/PM决策层/Agentic UX 交互设计模式 学习笔记.md`

### 2026-08-10（第 2 轮）
- 端侧小语言模型 SLM 生态（Phi/Gemma/Qwen/Llama/MiniCPM/SmolLM 横向选型图谱，刻意避开量化与架构分类）｜`01-笔记/AI模型基础/端侧小语言模型 SLM 生态 学习笔记.md`
- 语音交互与端侧 ASR/TTS（KWS→VAD→ASR→意图→TTS 全链路端云切分 + 级联 vs 端到端语音大模型范式转变）｜`01-笔记/手机AI智能体/语音交互与端侧 ASR TTS 学习笔记.md`
- 隐私计算与端云协同（信任光谱：纯端侧→TEE→Apple PCC/Google TIE→普通云 + 差分隐私/联邦学习 + 法规时间表）｜`01-笔记/安全/隐私计算与端云协同 学习笔记.md`
- AI 眼镜与可穿戴意图入口【热点】（形态谱系 + 玩家横向 + 功耗约束 + 交互范式 + Android XR/visionOS 阵营）｜`01-笔记/发散图谱/AI 眼镜与可穿戴意图入口 学习笔记.md`
- **顺带补洞**：新建 `01-笔记/AI模型基础/AI模型基础 MOC.md`——该文件夹此前是全库唯一无索引的子文件夹（6 篇裸放），按「认知→选型→落地」三层组织

### 2026-08-15（第 3 轮）
- 数据飞轮与 AI 产品度量（数据飞轮闭环 + AI 功能专属度量体系：北极星/采纳率/幻觉率/信任衰减/打扰率盲区，与增长模型·用户研究互补）｜`01-笔记/PM决策层/数据飞轮与 AI 产品度量 学习笔记.md`
- AI 编程助手与 Agentic Coding 工具生态（Copilot/Cursor/Claude Code/Codex/Windsurf/Devin/通义灵码 等谱系 + 从补全到自主 SWE Agent 演进）｜`01-笔记/知识管理与效率工具/AI 编程助手与 Agentic Coding 工具生态 学习笔记.md`
- 智能座舱与车机 HMI 意图入口（车机意图入口形态谱系 + 玩家横向：鸿蒙座舱/小米/蔚小理/百度/高通/英伟达/AAOS + 与手机端侧意图框架同源技术）｜`01-笔记/发散图谱/智能座舱与车机 HMI 意图入口 学习笔记.md`
- 合成数据与模型后训练（合成数据范式 + SFT/DPO/RLHF/RLAIF 后训练，端侧小模型训练侧，刻意区别于端侧量化/推理）｜`01-笔记/AI模型基础/合成数据与模型后训练 学习笔记.md`

### 2026-08-15（第 4 轮 · 当日第二次运行）
- 模型蒸馏与师生训练（数据/特征/关系/自蒸馏；大→小迁移；端侧小模型供给源；DeepSeek 蒸馏/Phi 哲学/distillation scaling）｜`01-笔记/AI模型基础/模型蒸馏与师生训练 学习笔记.md`
- 多模态 GUI 理解与 UI Grounding（screen understanding；OCR+布局/UI 元素检测/set-of-mark/VLM grounding；与 GUI Agent 架构区分算法侧 vs 架构侧）｜`01-笔记/手机AI智能体/多模态 GUI 理解与 UI Grounding 学习笔记.md`
- 无障碍 Accessibility 与 GUI Agent 同源技术栈（a11y tree / AT-SPI / TalkBack / VoiceOver；GUI Agent 看懂界面的同源底座）｜`01-笔记/发散图谱/无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记.md`
- 时序/事件驱动与 Agent 主动服务（event-driven / 情境感知；触发源 / 打扰预算 / 信任衰减；与端侧意图框架同源）｜`01-笔记/PM决策层/时序事件驱动与 Agent 主动服务 学习笔记.md`

### 2026-08-16（第 5 轮）
- 端侧多模态 VLM（on-device VLM/SMM 模型能力；区别于 [[多模态 GUI 理解与 UI Grounding]] 算法侧与端侧 SLM 语言侧）｜`01-笔记/手机AI智能体/端侧多模态 VLM 学习笔记.md`
- 端云协同推理与混合部署（hybrid inference / 端云分流路由；区别于端侧推理落地与隐私计算信任技术）｜`01-笔记/AI模型基础/端云协同推理与混合部署 学习笔记.md`
- 意图框架开发者生态与平台经济（平台激励经济；区别于平台治理与商业生态博弈）｜`01-笔记/PM决策层/意图框架开发者生态与平台经济 学习笔记.md`
- 多智能体协作与编排（Multi-Agent Orchestration 模式与框架；区别于单 agent 循环与 Agent 协议）｜`01-笔记/AI Agent 框架/多智能体协作与编排 学习笔记.md`

### 2026-08-17（第 6 轮）
- 端侧 AI 功耗与散热约束（Power/Thermal Budget；功耗预算/TDP/DVFS/thermal throttle/TOPS-W/Always-on 预算；区别于 NPU 编译栈与端侧推理落地）｜`01-笔记/手机AI智能体/端侧 AI 功耗与散热约束 学习笔记.md`
- Agent 可观测性 / LLM Observability（tracing/eval/cost&latency/feedback 回路 + LangSmith/Langfuse/Phoenix/Datadog/Traceloop + OpenTelemetry/OpenInference；区别于 Agent 评测基准与工具调用安全）｜`01-笔记/AI Agent 框架/Agent 可观测性 LLM Observability 学习笔记.md`
- 低代码/无代码 Agent 搭建平台（Coze/Dify/n8n/元器 等四类 + 2025-2026 平台爆发；区别于 AI 编程助手与 Agentic Coding）｜`01-笔记/知识管理与效率工具/低代码无代码 Agent 搭建平台 学习笔记.md`
- 端侧模型安全与越狱（on-device prompt injection/jailbreak/extraction/poisoning + on-device guardrail + EU AI Act；区别于工具调用安全与隐私计算）｜`01-笔记/安全/端侧模型安全与越狱 学习笔记.md`

### 2026-09-01（第 7 轮）
- 端侧 AI 芯片架构谱系（NPU/GPU/ASIC/DSP 微架构对比 + 主流 SoC NPU 布局；区别于 NPU 编译栈与功耗约束）｜`01-笔记/手机AI智能体/端侧 AI 芯片架构谱系 学习笔记.md`【新增】
- 世界模型与仿真合成环境（JEPA/Genie/GameNGen/Dreamer + 仿真平台 Isaac/Omniverse 等；合成数据上游技术）｜`01-笔记/AI模型基础/世界模型与仿真合成环境 学习笔记.md`【新增】
- AI 搜索与 RAG 问答产品生态（Perplexity/秘塔/Genspark + 知识库 AI 化工具；区别于 RAG 技术原理）｜`01-笔记/知识管理与效率工具/AI 搜索与 RAG 问答产品生态 学习笔记.md`【新增】
- Agent 记忆系统（Mem0/Letta/分层记忆；区别于个性化建模）｜`01-笔记/AI Agent 框架/Agent 记忆系统 学习笔记.md`【新增】
- Embodied AI 与机器人 Agent（VLA/机器人基础模型/玩家格局）｜`01-笔记/发散图谱/Embodied AI 与机器人 Agent 学习笔记.md`【合并升级既有 08-19 旧版】
- Agent 推理成本优化（prompt caching/batching/prefix sharing/模型路由）｜`01-笔记/AI Agent 框架/Agent 推理成本优化 学习笔记.md`【合并升级既有 08-19 旧版】

### 2026-09-02（第 8 轮）
- 端侧推理框架生态（TF Lite/LiteRT·MNN·NCNN·ONNX Runtime Mobile·ExecuTorch 跨平台推理运行时对比；区别于 NPU 编译栈与端侧量化）｜`01-笔记/手机AI智能体/端侧推理框架生态 学习笔记.md`【新增】
- GraphRAG 与知识图谱增强 Agent（MS GraphRAG/LightRAG/HippoRAG/私有KG+RAG；区别于向量 RAG 与 Agent 记忆）｜`01-笔记/AI Agent 框架/GraphRAG 与知识图谱增强 Agent 学习笔记.md`【新增】
- AI 原生浏览器与 Agent 浏览器（Comet/Dia/Perplexity/Arc；浏览器作为 Agent 代操作入口；区别于 AI 搜索产品）｜`01-笔记/知识管理与效率工具/AI 原生浏览器与 Agent 浏览器 学习笔记.md`【新增】
- AI 视频与多模态生成（Sora2/Kling/Veo3/Runway/MJ/Flux/Suno；扩散+时空一致性/自回归/世界模型范式；热点新知）｜`01-笔记/发散图谱/AI 视频与多模态生成 学习笔记.md`【新增】

### 2026-09-04（第 9 轮）
- 端侧扩散模型与端侧图像生成（on-device diffusion / SnapFusion·LCM·一致性模型 / 骁龙·天玑·Apple NPU 跑扩散 / 端侧文生图产品；区别于 [[端侧多模态 VLM 学习笔记]] 视觉理解）｜`01-笔记/手机AI智能体/端侧扩散模型与端侧图像生成 学习笔记.md`【新增】
- 多模态评测基准（MMMU/MMBench/SEED-Bench/MMWorld/AI2D/MMMU-Pro/OCRBench；按能力维度分类；区别于 [[Agent 评测与基准 学习笔记]] 轨迹评测）｜`01-笔记/AI模型基础/多模态评测基准 学习笔记.md`【新增】
- AI 监管与合规落地（EU AI Act 分阶段生效 / 中国生成式AI办法·算法备案·大模型备案 / 美国州法态势 / 产品合规要点；区别于 [[隐私计算与端云协同 学习笔记]] 信任技术）｜`01-笔记/PM决策层/AI 监管与合规落地 学习笔记.md`【新增】
- 模型服务化与 LLM 网关（LiteLLM/Portkey/Cloudflare AI Gateway/OpenRouter/云厂网关；统一API·路由·限流·守护；区别于 [[Agent 推理成本优化 学习笔记]] 成本技巧）｜`01-笔记/AI Agent 框架/模型服务化与 LLM 网关 学习笔记.md`【新增】

> ⚠️ 本轮重大发现：状态文件此前止于 08-17，但库内 08-18~08-19 已批量新增大量笔记（Context Engineering、个性化与端侧用户记忆、Agent 协议生态、RAG 详细、端侧大模型推理、Apple Intelligence 端侧架构、HarmonyOS 元服务、安卓厂商意图识别等），导致本轮初选 2 主题撞车（已改为合并升级）。下方黑名单已据真实库容全面刷新。

### 2026-09-12（第 10 轮）
- 端侧语音大模型（端到端语音 LLM：GPT-4o realtime/Moshi/Mini-Omni/Qwen-Audio/GLM-4-Voice + 全双工/副语言 + 端侧蒸馏量化；区别于 [[语音交互与端侧 ASR TTS 学习笔记]] 级联链路）｜`01-笔记/手机AI智能体/端侧语音大模型 学习笔记.md`【新增】
- ANN 索引算法专题（HNSW/IVF-PQ/IVF-HNSW/DiskANN/ScaNN/LSH + PQ·SQ 量化 + 选型指南；聚焦索引算法本身，区别于 [[向量数据库 学习笔记]] 产品概览）｜`01-笔记/AI Agent 框架/ANN 索引算法专题 学习笔记.md`【新增】
- 提示词工程→上下文工程演进史与 Prompt Ops（演进时间线 + 提示词版本管理/评测/观测工具链 LangSmith/PromptLayer/Humanloop；区别于 [[Context Engineering 学习笔记]] 概念层）｜`01-笔记/AI 工程/提示词工程到上下文工程演进与 Prompt Ops 学习笔记.md`【新增】
- 数字人与虚拟人（技术栈 TTS/语音克隆/口型驱动/化身渲染 + 代表 HeyGen/D-ID/百度曦灵/商汤如影 等 + 产品形态；热点新知，区别于 [[AI 视频与多模态生成 学习笔记]]）｜`01-笔记/发散图谱/数字人与虚拟人 学习笔记.md`【新增】

### 2026-09-13（第 11 轮）
- 模型水印与内容溯源（数字水印类型 + C2PA/CAI provenance 链 + 生成式AI标识监管 EU/中国办法/NIST + SynthID/Truepic/Azure/Reality Defender；区别于 [[端侧模型安全与越狱 学习笔记]] 模型被攻击）｜`01-笔记/安全/模型水印与内容溯源 学习笔记.md`【新增】
- 智能体身份与信任（AgentCard/A2A·Entra Agent ID·OAuth for Agents 授权委托 + 人类可识别 AI 标识 + 硬件级审批；区别于 [[AI 监管与合规落地 学习笔记]] 监管框架与 [[Confirmation UI 分级与产品责任边界]] 确认 UX）｜`01-笔记/PM决策层/智能体身份与信任 学习笔记.md`【新增】
- 语音 Agent 架构（voice-first 全双工 Agent 循环 + 级联 vs 端到端 + 语音意图→App Intents 映射 + Realtime API/Gemini Live/VAPI/Retell/Pipecat；区别于 [[端侧语音大模型 学习笔记]] 模型与 [[语音交互与端侧 ASR TTS 学习笔记]] 级联链路）｜`01-笔记/手机AI智能体/语音 Agent 架构 学习笔记.md`【新增】
- 数据 Agent 与 Text-to-SQL（NL2SQL 演进 + agentic 数据分析 + SQLCoder/PandasAI/Copilot/Cortex Analyst/Genie + 与 RAG 结构化vs非结构化对照）｜`01-笔记/AI Agent 框架/数据 Agent 与 Text-to-SQL 学习笔记.md`【新增】

## 下轮候选（避免重复，可直接取用）

- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ 注意：`向量数据库 学习笔记` 第四节已覆盖概览，需做**深度差异化**否则重复
- 多模态 GUI 理解（screen understanding、set-of-mark、UI 元素 grounding）——⚠️ 与 `工业级 GUI Agent 架构` 有重叠风险，需聚焦「视觉 grounding 算法侧」差异化
- Agent 记忆系统（Mem0/Letta/记忆分层，⚠️ `Agent 记忆与个性化意图理解` 已部分覆盖）
- 数据飞轮与 AI 产品度量（AI 功能的北极星指标、留存归因）——PM 锚点，第 2 轮未覆盖 PM，**优先**
- 开发者生态与平台经济（意图框架的开发者激励设计）
- 无障碍（Accessibility）与 GUI Agent 的同源技术栈
- 提示词工程 → 上下文工程的演进史与 Prompt 管理工程化（⚠️ 查 `Context Engineering 学习笔记` 重叠度）
- 合成数据与模型后训练（SFT/DPO/RLHF 对端侧小模型的意义）
- 智能座舱 / 车机 HMI 的意图入口（跨端锚点外辐射）
- AI 编程助手与 Agentic Coding 工具生态（效率工具锚点外辐射）
- 时序/事件驱动架构与 Agent 主动服务（主动预推的技术底）
- 模型蒸馏与师生训练（distillation scaling law，Phi 合成数据哲学的延伸）——本轮「合成数据」可深潜
- 世界模型（World Model）与仿真合成环境（合成数据上游技术）
- 合成数据质量·污染与 Model Collapse（Nature 2024）——本轮「合成数据」可深潜
- AI 编程助手「自主 SWE Agent 的代码安全责任」（与工具调用安全同源）——本轮「Agentic Coding」可深潜
- 车机/座舱 Agent 安全与责任边界（与 Confirmation UI 同源，跨端延伸）——本轮「智能座舱」可深潜
- 多模态 GUI 理解（screen understanding / set-of-mark / UI grounding）——⚠️ 与「工业级 GUI Agent 架构」重叠，需聚焦视觉 grounding 算法侧差异化
- 开发者生态与平台经济（意图框架开发者激励设计）——PM 锚点外辐射
- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，需深度差异化
- 提示词工程→上下文工程演进史与 Prompt 管理工程化——⚠️ 查 `Context Engineering` 重叠度
- 无障碍 Accessibility 与 GUI Agent 同源技术栈
- 端侧多模态 VLM（on-device vision-language 视觉理解，区别于 SLM 语言模型与 GUI 理解/grounding 算法）
- 端侧 AI 功耗与散热约束（Power/Thermal budget，区别于 NPU 编译栈）
- 模型服务化与端云协同推理（hybrid inference routing / 端云分流）
- Agent 记忆系统深潜（Mem0/Letta，⚠️ `Agent 记忆与个性化意图理解` 已部分覆盖，需做差异化）
- 开发者生态与平台经济（意图框架开发者激励 / 双边市场，⚠️ 与 `OS-PM-Agent平台治理与开发者生态` 区分治理 vs 经济激励）

### 2026-08-16 补充候选（刷新，移除已覆盖项）
- 端侧 AI 功耗与散热约束（Power/Thermal budget，区别于 NPU 编译栈与端侧推理落地）
- AI 芯片架构谱系（NPU vs GPU vs ASIC vs DSP，区别于 NPU 编译栈）
- Agent 可观测性 / LLM Observability（tracing / eval / LangSmith / Arize，区别于 Agent 评测基准）
- 世界模型 World Model 与仿真合成环境（合成数据上游技术）
- 合成数据质量·污染与 Model Collapse（Nature 2024，本轮「合成数据」可深潜）
- AI 搜索与 RAG 问答工具（个人知识库 AI 化，区别于 PKM 方法论与 Obsidian 生态）
- Embodied AI / 机器人 Agent（与端侧智能同源，发散图谱外辐射）
- 端侧模型安全与越狱（on-device model safety / red-teaming，与安全文件夹互补）
- 个性化与端侧用户记忆（on-device personalization，⚠️ 与 `Agent 记忆与个性化意图理解` 区分个性化 vs 记忆系统）
- Agent 推理成本优化（caching / batching / 投机，区别于已覆盖的投机采样）
- 低代码/无代码 Agent 搭建平台（效率工具锚点外辐射）
- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，需深度差异化
- 提示词工程→上下文工程演进史（⚠️ 查 `Context Engineering` 重叠度）

## 已覆盖主题黑名单（据真实库容 2026-09-01 全面刷新，勿重复立题）

RAG(详细) / 向量数据库 / Context Engineering / 端侧大模型推理 / 端侧模型量化 / 端侧 SLM 模型家族 / 移动端 NPU 与推理编译栈 / 端云协同推理与混合部署 / 模型蒸馏与师生训练 / 合成数据与模型后训练 / 世界模型与仿真合成环境 / 多模态 GUI 理解与 UI Grounding / 端侧多模态 VLM / 端侧 AI 功耗与散热约束 / 端侧 AI 芯片架构谱系 / 语音交互与端侧 ASR TTS / 隐私计算与端云协同 / 端侧模型安全与越狱 / 工具调用安全 / Apple Intelligence 端侧架构 / HarmonyOS 元服务 / 端侧意图框架 / 个性化与端侧用户记忆 / 安卓厂商意图识别破局策略 / Agent 协议生态 / Agent 评测与基准 / Agent 可观测性 LLM Observability / Agent 推理成本优化 / 多智能体协作与编排 / Agent 记忆系统 / MCP 与设备侧 MCP / LangChain / LangGraph / Loop Engineering / Graph Engineering / 投机采样 / PagedAttention·KV Cache / AI Runtime 调度 / App Intents / Confirmation UI / GUI Agent 架构 / AI 眼镜与可穿戴意图入口 / 智能座舱与车机 HMI 意图入口 / Embodied AI 与机器人 Agent / 无障碍 Accessibility 与 GUI Agent 同源技术栈 / Agentic UX 交互设计模式 / 用户研究方法 / 增长模型 / 数据飞轮与 AI 产品度量 / 意图框架开发者生态与平台经济 / 时序事件驱动与 Agent 主动服务 / PKM 方法论与 Obsidian 生态 / AI 编程助手与 Agentic Coding / 低代码无代码 Agent 搭建平台 / AI 搜索与 RAG 问答产品生态 / Figma / Go / Rust / 端侧推理框架生态 / GraphRAG 与知识图谱增强 Agent / AI 原生浏览器与 Agent 浏览器 / AI 视频与多模态生成 / 端侧扩散模型与端侧图像生成 / 多模态评测基准 / AI 监管与合规落地 / 模型服务化与 LLM 网关 / 端侧语音大模型 / ANN 索引算法 / 提示词工程到上下文工程演进 / 数字人与虚拟人 / 模型水印与内容溯源 / 智能体身份与信任 / 语音 Agent 架构 / 数据 Agent 与 Text-to-SQL

## 下轮候选（刷新·库内未覆盖，可直接取用）

- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，需做深度差异化（聚焦索引算法本身）
- 提示词工程→上下文工程演进史与 Prompt Ops（⚠️ `Context Engineering` 已覆盖概念，本文可聚焦"工程化演进史 + prompt 管理工具链"差异化）
- 端侧推理框架生态（TF Lite / MNN / NCNN / ONNX Runtime Mobile，区别于厂商 NPU 编译栈与端侧推理概念）
- AI 原生浏览器 / Agent 浏览器（Comet / Perplexity 浏览器 / Dia，效率工具锚点外辐射）
- AI 视频与多模态生成（Sora / Kling / 可灵 / Veo，发散图谱外辐射）
- 数字人 / 虚拟人（发散图谱外辐射，与端侧智能/可穿戴同源）
- AI 监管与合规落地（EU AI Act 实施、中国生成式 AI 办法、AI 备案，区别于隐私计算信任技术）
- 多模态评测基准（MMMU / SEED-Bench / MMWorld，区别于 Agent 评测基准）
- 端侧扩散模型 / 端侧图像生成（区别于端侧 VLM 视觉理解）
- GraphRAG / 知识图谱增强 Agent（区别于 Graph Engineering、RAG 详细）
- 模型服务化与 LLM 网关（区别于已覆盖的 Agent 推理成本优化）
- 推理服务可观测与成本护栏产品（区别于 Agent 可观测性）

### 2026-09-02 补充候选（本轮未取，下轮可直取）
- 端侧扩散模型 / 端侧图像生成（与本轮「AI 视频与多模态生成」呼应，但聚焦端侧落地，区别于端侧 VLM 视觉理解）
- 多模态评测基准（MMMU / SEED-Bench / MMWorld，区别于 Agent 评测基准）
- AI 监管与合规落地（EU AI Act 实施、中国生成式 AI 办法、AI 备案，区别于隐私计算信任技术）
- 模型服务化与 LLM 网关（区别于已覆盖的 Agent 推理成本优化）
- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，需做深度差异化（聚焦索引算法本身）
- 提示词工程→上下文工程演进史与 Prompt Ops（⚠️ `Context Engineering` 已覆盖概念，本文聚焦工程化演进史 + prompt 管理工具链差异化）
- 端侧推理框架生态已覆盖，相关纵深（如 ONNX 生态、TFLite 历史）留待 Ethon 补充，勿重复立题

### 2026-09-04 补充候选（本轮未取，下轮可直取）
- 数字人 / 虚拟人（发散图谱外辐射，与端侧智能/可穿戴同源）
- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，聚焦索引算法本身差异化
- 提示词工程→上下文工程演进史与 Prompt Ops（⚠️ `Context Engineering` 已覆盖概念，本文聚焦工程化演进史 + prompt 管理工具链差异化）
- 端侧语音大模型（端到端语音 LLM：GPT-4o audio / Mini-Omni / Moshi；区别于已覆盖的级联 ASR/TTS）
- 模型水印与内容溯源（C2PA / 生成标识国标；与 AI 监管合规同源，技术侧纵深）
- 智能体身份与信任（Agent identity / 授权委托 / 人类可识别 AI 标识；跨 PM 与端侧安全）

### 2026-09-12 补充候选（本轮未取，下轮可直取）
- 端侧语音大模型落地工程（流式全双工工程化 / 端侧语音 LLM 蒸馏量化深潜；区别于本轮概念广度）
- 索引算法工程实践（FAISS/ScaNN 调参 / Recall@k vs 延迟折中曲线 / GPU 索引 RAFT；区别于本轮算法概览）
- 提示词评测基准（PromptBench / 提示词鲁棒性 / 对抗样本；区别于本轮 Prompt Ops 工具链）
- 数字人实时驱动与端侧化（wav2lip 口型驱动深潜 / 3D Gaussian 化身渲染 / 端侧数字人商用方案；区别于本轮技术栈广度）
- 语音 Agent 架构（语音作为 Agent 入口 / 语音意图理解跨端侧意图框架；新外辐射）
- 模型水印与内容溯源（C2PA / 生成标识国标；技术侧纵深，与 AI 监管合规同源）
- 智能体身份与信任（Agent identity / 授权委托 / 人类可识别 AI 标识；跨 PM 与端侧安全）

### 2026-09-13 补充候选（本轮未取，下轮可直取）
- 模型水印与内容溯源落地工程（SynthID on-device 性能 / C2PA 链上隐私折中 / 水印对抗抹除鲁棒性；区别于本轮技术广度）
- 智能体身份互认与授权吊销（跨厂商 AgentCard 互认 / delegated authority 吊销机制 / 端侧 TEE 硬件锚定成本；区别于本轮概念广度）
- 语音 Agent 落地工程（全双工打断检测 barge-in / 语音意图→App Intents 映射可靠性 / 端侧流式语音 Agent 功耗；区别于本轮架构范式）
- 数据 Agent 准确率与治理（复杂多表 join 准确率 / semantic layer 接入 / 私有库 schema 泄露风险 / Agent 改数权限边界；区别于本轮方案广度）
- AI 评测红队与对齐（red-teaming / alignment，与 [[端侧模型安全与越狱 学习笔记]] 端侧面呼应，可新立题）
- 多模态评测基准（MMMU / SEED-Bench / MMWorld；⚠️ 第 9 轮已覆盖，勿重复）
- 端侧扩散模型（⚠️ 第 9 轮已覆盖，勿重复）
