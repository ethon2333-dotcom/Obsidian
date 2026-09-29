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

### 2026-09-14（第 12 轮）
- AI 评测红队与对齐（red-teaming 方法学 + 对齐 RLHF/RLAIF/DPO/Constitutional + 安全基准 HarmBench/AdvBench + 前沿实验室红队实践；区别于 [[端侧模型安全与越狱 学习笔记]] 端侧被攻击 / [[AI 监管与合规落地 学习笔记]] 监管 / [[Agent 评测与基准 学习笔记]] 能力评测）｜`01-笔记/安全/AI 评测红队与对齐 学习笔记.md`【新增】
- 端侧模型微调与个性化训练（LoRA/QLoRA/DoRA/adapter + Apple 端侧个性化 Adaptable Models + federated fine-tuning + personal LoRA；区别于 [[模型蒸馏与师生训练 学习笔记]] 蒸馏 / [[合成数据与模型后训练 学习笔记]] 通用后训练 / [[个性化与端侧用户记忆 学习笔记]] 记忆 / [[端侧大模型推理 学习笔记]] 推理）｜`01-笔记/手机AI智能体/端侧模型微调与个性化训练 学习笔记.md`【新增】
- AI 用户研究与产品洞察工具链（Dovetail/Looppanel/Maze/UserTesting AI/Zoom AI/synthetic users；AI 提效研究环节；区别于 [[用户研究方法 学习笔记]] 方法论 / [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[增长模型 学习笔记]] 增长）｜`01-笔记/PM决策层/AI 用户研究与产品洞察工具链 学习笔记.md`【新增】
- AI 设计工具与生成式 UI（Figma AI/v0/Galileo/Uizard/Motiff/Canva Magic/design-to-code；热点新知·贴合 Ethon Figma 兴趣；区别于 [[Figma 学习笔记]] 方法 / [[Agentic UX 交互设计模式 学习笔记]] 范式 / [[低代码无代码 Agent 搭建平台 学习笔记]] 低代码平台）｜`01-笔记/原型与Figma/AI 设计工具与生成式 UI 学习笔记.md`【新增】

### 2026-09-15（第 13 轮执行）
- AI 会议转录与纪要 Agent（实时/异步转录 + 纪要生成 + 行动项提取；Fireflies/Otter/Recap/通义听悟/飞书妙记/Notion AI/Zoom AI/Tact/Fathom；2025-2026 多说话人分离 + 日历·CRM 打通 + 端侧隐私转录；区别于 [[AI 用户研究与产品洞察工具链 学习笔记]] 访谈分析）｜`01-笔记/知识管理与效率工具/AI 会议转录与纪要 Agent 学习笔记.md`【新增】
- OS 级系统 Agent 与跨应用自动化（Siri/Gemini Live/Astra/Windows Copilot/Claude Computer Use/Operator + 跨 app 编排 + computer-use；区别于 [[GUI Agent 架构 学习笔记]] 技术架构侧 / [[端侧意图框架 学习笔记]] 语义路由 / [[语音 Agent 架构 学习笔记]] 语音入口）｜`01-笔记/手机AI智能体/OS 级系统 Agent 与跨应用自动化 学习笔记.md`【新增】
- 知识图谱与本体工程（本体建模 Ontology/RDF/OWL + 抽取→对齐→存储/查询 SPARQL·Cypher + Neo4j/Jena/Protégé/RDFox/Stardog；区别于 [[GraphRAG 与知识图谱增强 Agent 学习笔记]] 应用侧，聚焦"如何造出 KG"；区别于 [[向量数据库 学习笔记]] 向量检索）｜`01-笔记/AI Agent 框架/知识图谱与本体工程 学习笔记.md`【新增】
- AI 陪伴与情感陪伴 Agent（companion agents 产品形态 + 伦理边界；Character.AI/Replika/Pi/豆包/星野/猫箱/Grok Companion/Talkie；热点新知；区别于 [[数字人与虚拟人 学习笔记]] 技术栈）｜`01-笔记/发散图谱/AI 陪伴与情感陪伴 Agent 学习笔记.md`【新增】

### 2026-09-16（第 14 轮执行）
- 知识库问答与 Enterprise Search（企业级 RAG / 权限感知检索 / ACL 文档级租户隔离 + 混合检索 + Glean/Hebbia/Coveo/Elastic AI/365 Copilot 检索层/Vertex RAG Engine；区别于 [[AI 搜索与 RAG 问答产品生态 学习笔记]] 消费级与 [[RAG 详细 学习笔记]] 原理 / [[向量数据库 学习笔记]] 向量检索）｜`01-笔记/AI Agent 框架/知识库问答与 Enterprise Search 学习笔记.md`【新增】
- 端侧大模型安全芯片级防护（TEE/TrustZone/Secure Enclave/iSE/SE 硬件信任根 + 权重加密存储与运行时解密 + NPU 安全域 + 侧信道；区别于 [[端侧模型安全与越狱 学习笔记]] 软件层与 [[隐私计算与端云协同 学习笔记]] 端云联邦）｜`01-笔记/安全/端侧大模型安全芯片级防护 学习笔记.md`【新增】
- AI 辅助竞品情报与行业扫描（AI 辅助竞品情报收集/行业监测/情报结构化与预警；Crayon/AlphaSense/Kompyte/Similarweb AI/秘塔 等；公开渠道红线/NDA；区别于 [[AI 用户研究与产品洞察工具链 学习笔记]] 与 [[数据飞轮与 AI 产品度量 学习笔记]]）｜`01-笔记/竞品情报/AI 辅助竞品情报与行业扫描 学习笔记.md`【新增】
- 本地优先 AI 与个人 LLM 桌面应用生态（LM Studio/Ollama/Jan/PrivateGPT/AnythingLLM/Open WebUI + GGUF 量化模型 + 本地知识库；2025-2026 个人本地推理爆发；热点新知；区别于 [[端侧大模型推理 学习笔记]] 技术原理 / [[端侧 SLM 模型家族 学习笔记]] 模型 / [[端侧推理框架生态 学习笔记]] 移动端运行时 / [[AI 搜索与 RAG 问答产品生态 学习笔记]] 云端）｜`01-笔记/知识管理与效率工具/本地优先 AI 与个人 LLM 桌面应用生态 学习笔记.md`【新增】

### 2026-09-16 补充候选（本轮未取，下轮可直取）
- 企业搜索落地工程（权限感知检索准确率 / 租户隔离实现 / 接入既有数据湖成本；区别于本轮方案广度）
- 端侧安全芯片级防护工程（TEE 内 NPU 推理延迟开销 / 权重加密解密功耗 / 侧信道实测防护强度；区别于本轮概念广度）
- 竞品情报自动化工作流（周报自动生成 pipeline / 多源去重 / 情报可信度评分；区别于本轮工具广度）
- 本地优先 AI 与 Obsidian/PKM 打通（本地 LLM 跑个人知识库 RAG / 离线隐私 / 与云端 AI 搜索协同；区别于本轮应用生态广度）
- AI Agent 评测的红队专项（针对 Agent 链路注入的 red-teaming；区别于 [[AI 评测红队与对齐 学习笔记]] 模型层）

### 2026-09-17（第 15 轮执行）
- 服务端 LLM 推理引擎生态（vLLM/SGLang/TensorRT-LLM/TGI/Ollama/LMDeploy/llama.cpp + continuous batching/PagedAttention/speculative decoding/prefix caching；服务端/云端视角，区别于 [[端侧推理框架生态 学习笔记]] 移动端 / [[模型服务化与 LLM 网关 学习笔记]] 路由抽象 / [[端侧大模型推理 学习笔记]] 端侧）｜`01-笔记/AI 工程/服务端 LLM 推理引擎生态 学习笔记.md`【新增】
- AI Agent 沙箱与安全执行环境（E2B/Modal/Daytona/microVM/gVisor/远程浏览器沙箱 + 隔离粒度/资源限制/网络出口控制；区别于 [[工具调用安全 学习笔记]] 鉴权 / [[端侧模型安全与越狱 学习笔记]] 模型层 / [[AI 评测红队与对齐 学习笔记]] 模型 red-teaming）｜`01-笔记/安全/AI Agent 沙箱与安全执行环境 学习笔记.md`【新增】
- AI 产品商业模式与定价策略（API 按量/订阅/分层/混合/按结果/outcome-based/AI 加成溢价 + unit economics 与护城河；PM 变现视角，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[增长模型 学习笔记]] 增长 / [[意图框架开发者生态与平台经济 学习笔记]] 平台激励）｜`01-笔记/PM决策层/AI 产品商业模式与定价策略 学习笔记.md`【新增】
- AI 在即时通讯与办公协作入口（微信/钉钉/飞书/Slack/Teams/Zoom AI 作为 Agent 高频常驻入口；热点外辐射，区别于 [[OS 级系统 Agent 与跨应用自动化 学习笔记]] OS 编排 / [[AI 原生浏览器与 Agent 浏览器 学习笔记]] 浏览器 / [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]] 本地桌面）｜`01-笔记/发散图谱/AI 在即时通讯与办公协作入口 学习笔记.md`【新增】

### 2026-09-17 补充候选（本轮未取，下轮可直取）
- 服务端推理引擎性能评测基准（MLPerf Inference / 各引擎吞吐延迟对比 / 长上下文 serving；区别于本轮广度）
- AI Agent 沙箱的取证与审计日志（执行痕迹留证 / 合规审计 / 不可抵赖；区别于本轮隔离技术广度）
- AI 产品定价心理账户与价格歧视实操（分层定价实验 / 企业谈判折扣；区别于本轮模式广度）
- IM 内 Agent 的企业权限与数据合规（群聊 Agent 租户隔离 / 敏感词 / 审计；区别于本轮形态广度）
- 推理引擎的量化与稀疏化集成（AWQ/GPTQ 在 serving 侧集成 / W4A16 / 稀疏化加速；区别于 [[端侧模型量化 学习笔记]] 端侧）
- AI 原生长文本与文档协作（Notion AI/文档智能体/Gemini in Docs；区别于 [[AI 在即时通讯与办公协作入口 学习笔记]] 聊天入口）
- 智能体经济学与 AI 成本归因（token 成本分摊到功能/用户/会话；区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量）
- 语音 Agent 落地工程（全双工打断检测 barge-in / 语音意图→App Intents 映射可靠性；区别于 [[语音 Agent 架构 学习笔记]] 范式）

### 2026-09-18（第 16 轮执行）
- 语音 Agent 落地工程（barge-in 打断检测 / 回声消除·去混响 / VAD 尾点 / turn-taking / 语音意图→App Intents 映射可靠性 / 端侧流式功耗延迟；主流框架 Realtime API·Gemini Live·VAPI·Retell·LiveKit·Pipecat 取舍对比；区别于 [[语音 Agent 架构 学习笔记]] 范式，聚焦落地工程难点）｜`01-笔记/手机AI智能体/语音 Agent 落地工程 学习笔记.md`【新增】
- 智能体经济学与 AI 成本归因（cost-per-task / 多步调用链路成本追踪 / unit economics / 归因工具 LangSmith·Langfuse·Helicone·OpenLIT·Portkey；区别于 [[AI 产品商业模式与定价策略 学习笔记]] 定价/变现 与 [[数据飞轮与 AI 产品度量 学习笔记]] 度量）｜`01-笔记/PM决策层/智能体经济学与 AI 成本归因 学习笔记.md`【新增】
- AI 原生长文本与文档协作【热点新知】（Notion AI·Gemini in Docs·365 Copilot·飞书豆包工作伙伴·腾讯文档·WPS 灵犀 / doc agent / Agentic RAG；区别于 [[AI 在即时通讯与办公协作入口 学习笔记]] 聊天入口 与 [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]] 本地桌面）｜`01-笔记/知识管理与效率工具/AI 原生长文本与文档协作 学习笔记.md`【新增】
- 推理引擎的量化与稀疏化集成（AWQ/GPTQ/FP8/NVFP4·KV cache 量化·2:4 结构化稀疏 在 vLLM·SGLang·TensorRT-LLM·LMDeploy 的集成对比；云端 serving 视角，区别于 [[端侧模型量化 学习笔记]] 端侧）｜`01-笔记/AI 工程/推理引擎的量化与稀疏化集成 学习笔记.md`【新增】

### 2026-09-19（第 17 轮执行）
- AI 工作流自动化与编排（触发-动作/DAG/Agentic workflow 范式 + Zapier AI·Zapier Agents·Make·n8n·Relay.app·飞书/钉钉自动化·Coze/Dify workflow；区别于 [[低代码无代码 Agent 搭建平台 学习笔记]] 搭建平台）｜`01-笔记/知识管理与效率工具/AI 工作流自动化与编排 学习笔记.md`【新增】
- 个人知识库 AI 化与本地 RAG（Obsidian Copilot·Smart Connections·Obsidian Bases·privateGPT·NotebookLM 等个人库 RAG；区别于 [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]] 桌面推理应用 / [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论）｜`01-笔记/知识管理与效率工具/个人知识库 AI 化与本地 RAG 学习笔记.md`【新增】
- 操作系统原生 AI 功能图谱（Android Circle to Search·Gemini·iOS/Apple Intelligence·HarmonyOS 小艺 内建 AI 功能产品层；区别于 [[Apple Intelligence 端侧架构 学习笔记]] 架构 / [[OS 级系统 Agent 与跨应用自动化 学习笔记]] 系统 Agent）｜`01-笔记/手机AI智能体/操作系统原生 AI 功能图谱 学习笔记.md`【新增】
- AI 产品需求定义与 Agent 设计规范（eval 前置/HITL/降级/权限可撤销/成功标准模糊/spec-driven；区别于 [[Agentic UX 交互设计模式 学习笔记]] 交互 / [[数据飞轮与 AI 产品度量 学习笔记]] 度量）｜`01-笔记/PM决策层/AI 产品需求定义与 Agent 设计规范 学习笔记.md`【新增】

### 2026-09-20（第 18 轮执行）
- AI 评测红队 Agent 链路注入（Agent 多步链路间接注入/工具投毒/多 Agent 传播 + AgentDojo/InjecAgent/ToolEmu/OfficeBench + 防御隔离·沙箱·护栏；区别于 [[AI 评测红队与对齐 学习笔记]] 模型层 / [[工具调用安全 学习笔记]] 鉴权 / [[Agent 沙箱与安全执行环境 学习笔记]] 隔离）｜`01-笔记/安全/AI 评测红队 Agent 链路注入 学习笔记.md`【新增】
- 提示词与上下文鲁棒性评测基准（PromptBench/PromptAttack/AdvGLUE/FLAMES/RobustBench/CheckList + ART/Counterfit/Garak + 与上下文工程结合；区别于 [[提示词工程到上下文工程演进与 Prompt Ops 学习笔记]] 工具链 / [[Context Engineering 学习笔记]] 概念）｜`01-笔记/AI 工程/提示词与上下文鲁棒性评测基准 学习笔记.md`【新增】
- AI 营销与增长 Agent 生态（AI SDR/广告投放/内容矩阵/CRM 预测 + Clay·11x·Gong·HubSpot·Adobe GenStudio·Mutiny·Intercom；区别于 [[增长模型 学习笔记]] / [[AI 产品商业模式与定价策略 学习笔记]] / [[智能体经济学与 AI 成本归因 学习笔记]]）｜`01-笔记/PM决策层/AI 营销与增长 Agent 生态 学习笔记.md`【新增】
- AI 音乐与音频生成【热点新知】（文生音乐/音频扩散/音源分离/拟声 + Suno·Udio·Stable Audio·MusicGen·Riffusion·Demucs·TinyMusician 端侧；版权争议/实时化/端侧轻量化；区别于 [[AI 视频与多模态生成 学习笔记]] 视觉 / [[数字人与虚拟人 学习笔记]] TTS / [[端侧语音大模型 学习笔记]]）｜`01-笔记/发散图谱/AI 音乐与音频生成 学习笔记.md`【新增】

### 2026-09-20 补充候选（本轮未取，下轮可直取）
- AI 营销增长 Agent 实测（Clay/11x 真实 pipeline 转化率 / GTM Agent 与 CRM 打通成本 / 品牌安全护栏实测；区别于本轮广度）
- AI 音乐音频端侧化与可穿戴（TinyMusician 端侧时延实测 / 耳戴设备实时生成 / 与 [[AI 眼镜与可穿戴意图入口 学习笔记]] 声音层结合；区别于本轮产品广度）
- Agent 链路注入红队实操（InjecAgent 真实失守率 / 工具投毒检测方案 / 多 Agent 传播阻断；区别于本轮攻防概念广度）
- 鲁棒性评测落地（PromptBench 接入 CI / 长上下文鲁棒性基准 / 中文对抗样本；区别于本轮基准概览）
- 垂直行业 Agent 纵深入（AI 法律合同审查 / AI 医疗健康 Agent / AI 教育自适应学习；区别于已覆盖通用 Agent）

### 2026-09-21（第 19 轮执行）
- 垂直行业 Agent 纵深入（法律 Harvey/CoCounsel/Leya·医疗 Hippocratic/Dragon Copilot/AMIE/OpenEvidence·教育 Khanmigo/Coursera Coach/Ivy.ai；按"行业 × 部署形态 × 监管责任门槛"；区别于 [[多智能体协作与编排 学习笔记]]/[[Agent 评测与基准 学习笔记]]/[[数据 Agent 与 Text-to-SQL 学习笔记]]/[[知识库问答与 Enterprise Search 学习笔记]]）｜`01-笔记/AI Agent 框架/垂直行业 Agent 纵深入 学习笔记.md`【新增】
- AI 音乐音频端侧化与可穿戴（TinyMusician/端侧 TTS 轻量化/Kokoro/Bark·耳戴 NPU/SoC/Anker Thus CIM·AI 眼镜声学层·功耗延迟预算；区别于 [[AI 音乐与音频生成 学习笔记]] 云端广度 / [[AI 眼镜与可穿戴意图入口 学习笔记]] 视觉交互）｜`01-笔记/手机AI智能体/AI 音乐音频端侧化与可穿戴 学习笔记.md`【新增】
- Agent 链路注入红队实操（AgentDojo/InjecAgent/ToolEmu 实测失守率 + MCP 工具投毒扫描 + 多 Agent 传播阻断 + 4 层护栏 playbook；区别于 [[AI 评测红队 Agent 链路注入 学习笔记]] 概念框架 / [[AI Agent 沙箱与安全执行环境 学习笔记]] 隔离技术 / [[AI 评测红队与对齐 学习笔记]] 模型层）｜`01-笔记/安全/Agent 链路注入红队实操 学习笔记.md`【新增】
- AI 工作流自动化实测（Zapier Agents GA 完成率与计费·n8n 自托管 TCO·Make/Relay.app 人机协同·Coze/Dify 私有化+RAG·长链路错误复利衰减与企业 ROI；区别于 [[AI 工作流自动化与编排 学习笔记]] 平台范式 / [[低代码无代码 Agent 搭建平台 学习笔记]] 搭建）｜`01-笔记/知识管理与效率工具/AI 工作流自动化实测 学习笔记.md`【新增】

### 2026-09-22（第 20 轮执行）
- AI 辅助阅读与信息摄取工具生态（消费/摄取外部内容：网页/视频/播客/论文/书籍经 AI 摘要·简报·综述·知识萃取；Recall/Readwise/NotebookLM/Plaud 类；区别于 [[AI 原生长文本与文档协作 学习笔记]] 写作侧 / [[AI 会议转录与纪要 Agent 学习笔记]] 会议 / [[AI 搜索与 RAG 问答产品生态 学习笔记]] 搜索）｜`01-笔记/知识管理与效率工具/AI 辅助阅读与信息摄取工具生态 学习笔记.md`【新增】
- 负责任 AI 与 AI 产品伦理落地（RAI 产品化：MS RAI Toolbox/Dashboard·Google PAIR·NIST AI RMF·Model Cards/Datasheets·公平性偏差测试·可解释性 UX·Responsible Launch·红队发布闸门；PM 视角，区别于 [[AI 监管与合规落地 学习笔记]] 法规 / [[AI 评测红队与对齐 学习笔记]] 技术）｜`01-笔记/PM决策层/负责任 AI 与 AI 产品伦理落地 学习笔记.md`【新增】
- 端侧 AI 模型格式与部署互操作标准（模型产物打包与互通：ONNX/GGUF/.pte/.tflite/.mnn/Core ML + 互转工具链；区别于 [[端侧推理框架生态 学习笔记]] 运行时 / [[端侧模型量化 学习笔记]] 量化）｜`01-笔记/手机AI智能体/端侧 AI 模型格式与部署互操作标准 学习笔记.md`【新增】
- AI 消费硬件与 Ambient Computing（脱离手机的 standalone AI 终端 + 环境计算入口：AI Pin·Rabbit R1·AI 玩具·AI 录音笔·AI 吊坠·Humane·Brilliant Labs；热点新知；区别于 [[AI 眼镜与可穿戴意图入口 学习笔记]] 视觉 / [[智能座舱与车机 HMI 意图入口 学习笔记]] 车机 / [[AI 音乐音频端侧化与可穿戴 学习笔记]] 耳戴）｜`01-笔记/发散图谱/AI 消费硬件与 Ambient Computing 学习笔记.md`【新增】

### 2026-09-25（第 21 轮执行）
- 智能体商店与 Agent 分发平台生态（GPT Store/Claude Skills/Coze/豆包/元器/文心/百宝箱/Gemini Gems 等；按分发模式四分：平台内嵌/独立开放/企业私有/协议化能力 MCP·A2A·Skills；区别于 [[低代码无代码 Agent 搭建平台 学习笔记]] 搭建 / [[多智能体协作与编排 学习笔记]] / [[Agent 协议生态 学习笔记]]）｜`01-笔记/AI Agent 框架/智能体商店与 Agent 分发平台生态 学习笔记.md`【新增】
- 笔记软件横向对比（Logseq/Notion/Roam/Capacities vs Obsidian；按范式四分：文档优先双链/大纲块编辑/云端块数据库/对象型；区别于 [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论 / [[个人知识库 AI 化与本地 RAG 学习笔记]]）｜`01-笔记/知识管理与效率工具/笔记软件横向对比 学习笔记.md`【新增】
- AI 手机与 AI OS 产品竞争格局（AI Phone/AI OS 品类；各厂商战略定位：端侧优先 vs 云优先、自研 vs 借力；区别于 [[操作系统原生 AI 功能图谱 学习笔记]] 功能清单 / [[端侧意图框架 学习笔记]] 架构）｜`01-笔记/手机AI智能体/AI 手机与 AI OS 产品竞争格局 学习笔记.md`【新增】
- AI 写作与内容创作助手生态（Jasper/Copy.ai/Sudowrite/文心一言/豆包/Kimi/通义/元宝/秘塔写作猫 等；按场景四分：营销/长文小说/学术/社媒/多模态；区别于 [[AI 原生长文本与文档协作 学习笔记]] 文档内原生）｜`01-笔记/知识管理与效率工具/AI 写作与内容创作助手生态 学习笔记.md`【新增】

### 2026-09-22 补充候选（本轮未取，下轮可直取）
- AI 辅助阅读工具实测（Recall 摘要准确率 / NotebookLM 跨源综述幻觉率 / 端侧离线阅读助手；区别于本轮广度）
- RAI 产品落地实操（公平性测试 dashboard / 偏差缓解上线流程 / 可解释性 UX 在手机 AI 的落地；区别于本轮方法工具广度）
- 端侧模型格式工程实践（ONNX→TFLite 量化精度损失曲线 / GGUF 与 .pte 在同源模型的端侧延迟对比；区别于本轮格式概览）
- AI 消费硬件成败深潜（Humane 关停复盘 / Rabbit 欠薪与 OS 虚标 / 录音笔赛道为何跑通；区别于本轮形态广度）
- 笔记软件横向（Logseq/Notion/Roam vs Obsidian 产品定位；效率工具纵深）
- AI 写作与内容创作助手生态（Jasper/Copy.ai/文心一言写作；区别于 [[AI 原生长文本与文档协作 学习笔记]]）

### 2026-09-21 补充候选（本轮未取，下轮可直取）
- 垂直行业 Agent 监管与责任归属深潜（各行业 liability 框架 / 医疗 FDA SaMD / 法律 unauthorized practice 边界；区别于本轮行业产品广度）
- AI 音乐音频端侧化实测（TinyMusician 端侧时延实测 / 耳戴 SoC 实时生成功耗 / 与 AI 眼镜声音层联动工程；区别于本轮产品广度）
- Agent 链路注入红队专项 benchmark（AGENTVIGIL/ASB 等新一代基准 / 多 Agent 传播阻断实测 / 企业 red-team 常态化流程；区别于本轮攻防实操广度）
- 工作流自动化企业落地 ROI 与可靠性长测（真实企业 pipeline 完成率 / 长链路错误复合衰减曲线 / 私有部署 TCO 实测；区别于本轮实测广度）

### 2026-09-19 补充候选（本轮未取，下轮可直取）
- AI 工作流自动化实测（Zapier Agents 真实任务完成率 / 本地 n8n 私有部署成本 / 工作流 Agent 长链路可靠性；区别于本轮广度）
- 个人知识库 RAG 工程（本地 embedding 模型选型 / vault 万篇索引性能 / Obsidian Bases 与 RAG 协同；区别于本轮形态广度）
- 操作系统 AI 功能采纳与端侧占比（各功能端侧运行比例 / 国内安卓厂商对齐 / 功能使用率；区别于本轮功能清单广度）
- AI 产品需求评审实操（eval 与 PRD 绑定流程 / 非确定性需求评审会 / Agent 任务 SLA 模板；区别于本轮规范广度）
- AI 评测红队针对 Agent 链路注入（区别于 [[AI 评测红队与对齐 学习笔记]] 模型层）
- 提示词评测基准（PromptBench / 鲁棒性；区别于 [[提示词工程到上下文工程演进与 Prompt Ops 学习笔记]] 工具链）

### 2026-09-18 补充候选（本轮未取，下轮可直取）
- 语音 Agent 落地工程实测（barge-in 误唤醒率 / 端侧语音 Agent 功耗基线 / 长程 function-calling 失准率；区别于本轮广度）
- 智能体经济学实操（成本归因 dashboard / outcome-based 计费谈判 / 成本透明化对 PM 决策影响；区别于本轮概念）
- AI 原生长文本与文档协作实操（doc agent 多人协作权限模型 / 与 Obsidian 本地知识库 RAG 打通；区别于本轮形态广度）
- 推理引擎量化集成实测（W4A16 精度回退 / 稀疏化硬件门槛 Ampere+ / NVFP4 Blackwell 专属；区别于本轮广度）
- AI 工作流自动化与编排（Zapier AI / Make / 工作流 Agent；区别于低代码 Agent 搭建平台）
- 个人知识库 AI 化本地 RAG（Obsidian + 本地 LLM RAG / 离线隐私；区别于本地优先 AI 应用生态）

### 2026-09-15 补充候选（本轮未取，下轮可直取）
- AI 会议转录与纪要 Agent 落地工程（本地端侧 ASR 准确率 / 与 Obsidian 双向同步 / 企业数据合规；区别于本轮广度）
- OS 级系统 Agent 权限与安全边界（跨 app 权限模型 / computer-use 安全护栏 / OS Agent 与第三方 app 生态博弈；区别于本轮平台能力广度）
- 知识图谱抽取准确率评测与增量更新（LLM 抽取误差 / 本体版本治理 / KG+向量混合检索；区别于本轮构建广度）
- AI 陪伴 Agent 长期记忆架构与依赖度度量（memory architecture / 未成年人护栏设计 / 情感替代风险；区别于本轮产品形态广度）
- 知识库问答与 Enterprise Search（企业级 RAG 检索 / 权限感知检索；区别于 [[AI 搜索与 RAG 问答产品生态 学习笔记]]）
- AI 辅助竞品情报与行业扫描（竞品情报 folder；AI 提效情报收集/监测；PM+效率 辐射）
- 端侧大模型安全芯片级防护（TEE/SE 端侧推理保护；区别于 [[端侧模型安全与越狱 学习笔记]] 软件侧）

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

RAG(详细) / 向量数据库 / Context Engineering / 端侧大模型推理 / 端侧模型量化 / 端侧 SLM 模型家族 / 移动端 NPU 与推理编译栈 / 端云协同推理与混合部署 / 模型蒸馏与师生训练 / 合成数据与模型后训练 / 世界模型与仿真合成环境 / 多模态 GUI 理解与 UI Grounding / 端侧多模态 VLM / 端侧 AI 功耗与散热约束 / 端侧 AI 芯片架构谱系 / 语音交互与端侧 ASR TTS / 隐私计算与端云协同 / 端侧模型安全与越狱 / 工具调用安全 / Apple Intelligence 端侧架构 / HarmonyOS 元服务 / 端侧意图框架 / 个性化与端侧用户记忆 / 安卓厂商意图识别破局策略 / Agent 协议生态 / Agent 评测与基准 / Agent 可观测性 LLM Observability / Agent 推理成本优化 / 多智能体协作与编排 / Agent 记忆系统 / MCP 与设备侧 MCP / LangChain / LangGraph / Loop Engineering / Graph Engineering / 投机采样 / PagedAttention·KV Cache / AI Runtime 调度 / App Intents / Confirmation UI / GUI Agent 架构 / AI 眼镜与可穿戴意图入口 / 智能座舱与车机 HMI 意图入口 / Embodied AI 与机器人 Agent / 无障碍 Accessibility 与 GUI Agent 同源技术栈 / Agentic UX 交互设计模式 / 用户研究方法 / 增长模型 / 数据飞轮与 AI 产品度量 / 意图框架开发者生态与平台经济 / 时序事件驱动与 Agent 主动服务 / PKM 方法论与 Obsidian 生态 / AI 编程助手与 Agentic Coding / 低代码无代码 Agent 搭建平台 / AI 搜索与 RAG 问答产品生态 / Figma / Go / Rust / 端侧推理框架生态 / GraphRAG 与知识图谱增强 Agent / AI 原生浏览器与 Agent 浏览器 / AI 视频与多模态生成 / 端侧扩散模型与端侧图像生成 / 多模态评测基准 / AI 监管与合规落地 / 模型服务化与 LLM 网关 / 端侧语音大模型 / ANN 索引算法 / 提示词工程到上下文工程演进 / 数字人与虚拟人 / 模型水印与内容溯源 / 智能体身份与信任 / 语音 Agent 架构 / 数据 Agent 与 Text-to-SQL / AI 评测红队与对齐 / 端侧模型微调与个性化训练 / AI 用户研究与产品洞察工具链 / AI 设计工具与生成式 UI / AI 会议转录与纪要 Agent / OS 级系统 Agent 与跨应用自动化 / 知识图谱与本体工程 / AI 陪伴与情感陪伴 Agent / 知识库问答与 Enterprise Search / 端侧大模型安全芯片级防护 / AI 辅助竞品情报与行业扫描 / 本地优先 AI 与个人 LLM 桌面应用生态 / 服务端 LLM 推理引擎生态 / AI Agent 沙箱与安全执行环境 / AI 产品商业模式与定价策略 / AI 在即时通讯与办公协作入口 / 语音 Agent 落地工程 / 智能体经济学与 AI 成本归因 / AI 原生长文本与文档协作 / 推理引擎的量化与稀疏化集成 / AI 工作流自动化与编排 / 个人知识库 AI 化与本地 RAG / 操作系统原生 AI 功能图谱 / AI 产品需求定义与 Agent 设计规范 / AI 评测红队 Agent 链路注入 / 提示词与上下文鲁棒性评测基准 / AI 营销与增长 Agent 生态 / AI 音乐与音频生成 / 垂直行业 Agent 纵深入 / AI 音乐音频端侧化与可穿戴 / Agent 链路注入红队实操 / AI 工作流自动化实测 / AI 辅助阅读与信息摄取工具生态 / 负责任 AI 与 AI 产品伦理落地 / 端侧 AI 模型格式与部署互操作标准 / AI 消费硬件与 Ambient Computing / 智能体商店与 Agent 分发平台生态 / 笔记软件横向对比 / AI 手机与 AI OS 产品竞争格局 / AI 写作与内容创作助手生态

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

### 2026-09-14 补充候选（本轮未取，下轮可直取）
- AI 会议转录与纪要 Agent（Fireflies/Otter/Recap/通义听悟/飞书妙记；效率+PM 辐射，区别于 [[AI 用户研究与产品洞察工具链 学习笔记]]）
- 数字人实时驱动与端侧化（wav2lip 口型驱动深潜 / 3D Gaussian 化身渲染 / 端侧数字人商用方案；区别于 [[数字人与虚拟人 学习笔记]] 技术栈广度）
- OS 级系统 Agent 与跨应用自动化（Siri / Gemini Live on Android / Windows Copilot / Claude Computer Use 平台视角；区别于 [[GUI Agent 架构 学习笔记]] 技术架构侧 与 [[端侧意图框架 学习笔记]]）
- AI 辅助竞品情报与行业扫描（竞品情报 folder；AI 提效情报收集/监测；PM+效率 辐射）
- 知识图谱与本体工程（KG ontology / Neo4j / 本体建模；区别于 [[GraphRAG 与知识图谱增强 Agent 学习笔记]] 应用侧）
- AI 陪伴/情感陪伴 Agent（companion agents 产品形态与伦理边界；发散图谱/PMA 辐射）

### 2026-09-25 补充候选（本轮未取，下轮可直取）
- AI 翻译与跨语言知识工具生态（沉浸式翻译/DeepL/AI 字幕/跨语言 RAG；效率工具锚点外辐射，区别于 [[AI 辅助阅读与信息摄取工具生态 学习笔记]] 摄取）
- Agent 评测自动化与 LLM-as-judge 工程（Ragas/DeepEval/Giskard/PromptFoo eval harness；区别于 [[Agent 评测与基准 学习笔记]] 基准本身）
- AI 产品的隐私设计模式（Privacy by Design UX for AI；区别于 [[隐私计算与端云协同 学习笔记]] 技术 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] 伦理）
- 端侧推理的动态路由与模型选择（runtime model routing on-device / 端侧模型动态选型；区别于 [[端云协同推理与混合部署 学习笔记]] 端云分流）
- AI 原生长图与演示文稿生成（AI PPT / 文生 PPT；效率工具锚点外辐射，区别于 [[AI 设计工具与生成式 UI 学习笔记]] 设计侧）
- 智能体间经济结算与 micropayment（agent economy / agent payment；AI Agent框架 + PM 双锚点外辐射）
