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

RAG(详细) / 向量数据库 / Context Engineering / 端侧大模型推理 / 端侧模型量化 / 端侧 SLM 模型家族 / 移动端 NPU 与推理编译栈 / 端云协同推理与混合部署 / 模型蒸馏与师生训练 / 合成数据与模型后训练 / 世界模型与仿真合成环境 / 多模态 GUI 理解与 UI Grounding / 端侧多模态 VLM / 端侧 AI 功耗与散热约束 / 端侧 AI 芯片架构谱系 / 语音交互与端侧 ASR TTS / 隐私计算与端云协同 / 端侧模型安全与越狱 / 工具调用安全 / Apple Intelligence 端侧架构 / HarmonyOS 元服务 / 端侧意图框架 / 个性化与端侧用户记忆 / 安卓厂商意图识别破局策略 / Agent 协议生态 / Agent 评测与基准 / Agent 可观测性 LLM Observability / Agent 推理成本优化 / 多智能体协作与编排 / Agent 记忆系统 / MCP 与设备侧 MCP / LangChain / LangGraph / Loop Engineering / Graph Engineering / 投机采样 / PagedAttention·KV Cache / AI Runtime 调度 / App Intents / Confirmation UI / GUI Agent 架构 / AI 眼镜与可穿戴意图入口 / 智能座舱与车机 HMI 意图入口 / Embodied AI 与机器人 Agent / 无障碍 Accessibility 与 GUI Agent 同源技术栈 / Agentic UX 交互设计模式 / 用户研究方法 / 增长模型 / 数据飞轮与 AI 产品度量 / 意图框架开发者生态与平台经济 / 时序事件驱动与 Agent 主动服务 / PKM 方法论与 Obsidian 生态 / AI 编程助手与 Agentic Coding / 低代码无代码 Agent 搭建平台 / AI 搜索与 RAG 问答产品生态 / Figma / Go / Rust / 端侧推理框架生态 / GraphRAG 与知识图谱增强 Agent / AI 原生浏览器与 Agent 浏览器 / AI 视频与多模态生成 / 端侧扩散模型与端侧图像生成 / 多模态评测基准 / AI 监管与合规落地 / 模型服务化与 LLM 网关 / 端侧语音大模型 / ANN 索引算法 / 提示词工程到上下文工程演进 / 数字人与虚拟人 / 模型水印与内容溯源 / 智能体身份与信任 / 语音 Agent 架构 / 数据 Agent 与 Text-to-SQL / AI 评测红队与对齐 / 端侧模型微调与个性化训练 / AI 用户研究与产品洞察工具链 / AI 设计工具与生成式 UI / AI 会议转录与纪要 Agent / OS 级系统 Agent 与跨应用自动化 / 知识图谱与本体工程 / AI 陪伴与情感陪伴 Agent / 知识库问答与 Enterprise Search / 端侧大模型安全芯片级防护 / AI 辅助竞品情报与行业扫描 / 本地优先 AI 与个人 LLM 桌面应用生态 / 服务端 LLM 推理引擎生态 / AI Agent 沙箱与安全执行环境 / AI 产品商业模式与定价策略 / AI 在即时通讯与办公协作入口 / 语音 Agent 落地工程 / 智能体经济学与 AI 成本归因 / AI 原生长文本与文档协作 / 推理引擎的量化与稀疏化集成 / AI 工作流自动化与编排 / 个人知识库 AI 化与本地 RAG / 操作系统原生 AI 功能图谱 / AI 产品需求定义与 Agent 设计规范 / AI 评测红队 Agent 链路注入 / 提示词与上下文鲁棒性评测基准 / AI 营销与增长 Agent 生态 / AI 音乐与音频生成 / 垂直行业 Agent 纵深入 / AI 音乐音频端侧化与可穿戴 / Agent 链路注入红队实操 / AI 工作流自动化实测 / AI 辅助阅读与信息摄取工具生态 / 负责任 AI 与 AI 产品伦理落地 / 端侧 AI 模型格式与部署互操作标准 / AI 消费硬件与 Ambient Computing / 智能体商店与 Agent 分发平台生态 / 笔记软件横向对比 / AI 手机与 AI OS 产品竞争格局 / AI 写作与内容创作助手生态 / AI 原生长图与演示文稿生成 / Agent 评测自动化与 LLM-as-judge 工程 / AI 产品的隐私设计模式 / 智能体间经济结算与 micropayment / AI 翻译与跨语言知识工具生态 / 端侧推理的动态路由与模型选择

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

### 2026-10-03（第 22 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（效率工具×1 / AI Agent框架×2 / PM×1），含 1 热点新知（agent economy）。运行前 Glob 预检发现状态文件滞后——库内 09-29 已存在「AI 翻译与跨语言知识工具生态」「端侧推理的动态路由与模型选择」2 篇笔记（未入黑名单），故将这 2 个原候选主题剔除，改取其余 4 个 09-25 候选未取项。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `知识管理与效率工具/AI 原生长图与演示文稿生成 学习笔记.md`（文生PPT/文生长图/agentic deck generation；Gamma·Tome·Beautiful.ai·SlidesAI·Copilot·Canva·MindShow·讯飞智文·百度文库AI·WPS AI·豆包PPT·Skywork·Genspark；区别于 [[AI 设计工具与生成式 UI 学习笔记]] 设计侧/[[AI 写作与内容创作助手生态 学习笔记]] 产出侧/[[AI 辅助阅读与信息摄取工具生态 学习笔记]] 摄取侧；连 6 篇）
  2. `AI Agent 框架/Agent 评测自动化与 LLM-as-judge 工程 学习笔记.md`（eval harness 与 LLM-as-judge：Ragas/DeepEval/Giskard/PromptFoo/TruLens/Phoenix/Opik/LangSmith/Inspect/AgentEval + Zheng2023 偏差·JudgeBench；区别于 [[Agent 评测与基准 学习笔记]] 基准本身/[[Agent 可观测性 LLM Observability 学习笔记]] 线上 tracing；连 5 篇；待核实 6 项）
  3. `PM决策层/AI 产品的隐私设计模式 学习笔记.md`（Privacy-by-Design UX 模式：透明告知/同意控制/数据最小化/默认端侧/AI 披露/可携删除/隐私营养标签；区别于 [[隐私计算与端云协同 学习笔记]] 技术/[[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI/[[端侧大模型安全芯片级防护 学习笔记]] 硬件；连 6 篇；待核实 6 项）
  4. `AI Agent 框架/智能体间经济结算与 micropayment 学习笔记.md`【热点新知】（x402·AP2·Stripe MPP/ACP·Visa TAP·Mastercard Agent Pay·UCP·agent 钱包与授权额度；区别于 [[智能体商店与 Agent 分发平台生态 学习笔记]] 分发/[[模型服务化与 LLM 网关 学习笔记]] 计量/[[多智能体协作与编排 学习笔记]] 协同/[[Agent 协议生态 学习笔记]] 通信；连 4 篇；待核实 7 项）
- 待核实合计：4 篇共约 25 项（收购/交易额/抽成百分比/监管日期/厂商口径），均标「待核实」，无编造。
- ⚠️ 状态文件滞后修正：09-29 已存在但未入黑名单的 2 篇（AI 翻译、端侧推理动态路由）本轮已补入黑名单（见上方黑名单增量），避免后续撞车。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-03 下轮候选（库内未覆盖，可直接取用）
- 端侧模型 OTA 更新与生命周期管理（模型灰度/AB/回滚/端侧增量更新；手机AI智能体锚，区别于端侧推理框架生态）
- AI 产品的可解释性 UX 与归因展示（explainability UX / 为什么给这个结论；PM锚，区别于 [[负责任 AI 与 AI 产品伦理落地 学习笔记]] 伦理框架）
- 多模态文档智能 DocAI（文档解析/表格/版式理解；AI模型基础/AI Agent框架锚，区别于 [[多模态 GUI 理解与 UI Grounding 学习笔记]] 屏幕理解）
- 合成媒体检测与 deepfake 防御（检测/溯源/水印对抗；安全锚，区别于 [[模型水印与内容溯源 学习笔记]] 水印技术）
- AI 编程助手的代码安全责任（自主 SWE Agent 的代码安全责任边界；效率工具锚，区别于 [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]] 工具）
- AI 产品的可访问性（a11y）UX for AI（无障碍作为 AI 产品基线；PM/发散锚，区别于 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]] 技术栈）

### 2026-10-05（第 23 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体×1 / AI模型基础×1 / PM决策层×1 / 效率工具×1），广度均衡，无单独热点标记。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-03（第 22 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/端侧模型 OTA 更新与生命周期管理 学习笔记.md`（端侧模型灰度/AB/回滚/增量更新/注册表与版本治理/设备 fleet 管理；连 端侧推理框架生态/模型格式标准/端侧大模型推理/芯片谱系/原生 AI 功能图谱；待核实 6 项）
  2. `AI模型基础/多模态文档智能 DocAI 学习笔记.md`（文档解析/版式理解/表格抽取/OCR-free 文档 VLM；LayoutLM/Donut/Nougat/Marker/MinerU + Google Document AI/Azure Form Recognizer/AWS Textract/合合/达观；连 多模态GUI理解/端侧VLM/多模态评测/RAG；待核实 5 项）
  3. `PM决策层/AI 产品的可解释性 UX 与归因展示 学习笔记.md`（来源引用/置信度表达/归因高亮/依据可视化；连 负责任AI/AI产品伦理/Agentic UX/需求定义/数据飞轮/智能体身份；待核实 5 项）
  4. `知识管理与效率工具/AI 编程助手的代码安全责任 学习笔记.md`（自主 SWE Agent 责任归属/生成代码漏洞/侵权/护栏审查；连 AI编程助手生态/Agent沙箱/工具调用安全/Agent执行安全(PM视角)/红队对齐；待核实 6 项）
- 待核实合计：4 篇共 22 项（媒体口径流量节省百分比/厂商官方机制/市场数据/条款责任边界/落地案例），均标「待核实」，无编造。
- 状态文件：已追加第 23 轮记录、黑名单增量补入 4 主题（见下方黑名单增量）、增补下轮候选（deepfake 检测/a11y UX/OTA 工程/多模态RAG/可解释性评测/代码安全评测）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-05 黑名单增量（本轮新入，勿重复立题）
- 端侧模型 OTA 更新与生命周期管理
- 多模态文档智能 DocAI
- AI 产品的可解释性 UX 与归因展示
- AI 编程助手的代码安全责任

### 2026-10-05 下轮候选（库内未覆盖，可直接取用）
- 合成媒体检测与 deepfake 防御（检测/溯源/水印对抗；安全锚，区别于 [[模型水印与内容溯源 学习笔记]] 水印技术；第 22 轮遗留）
- AI 产品的可访问性（a11y）UX for AI（无障碍作为 AI 产品基线；PM/发散锚，区别于 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]] 技术栈；第 22 轮遗留）
- 端侧模型增量更新与差分量化工程（差分更新精度损失/AB 实验在端侧；手机AI智能体锚，区别于本轮 OTA 广度）
- 多模态 RAG 与文档问答产品（DocAI + RAG 落地；AI Agent框架锚，区别于 [[知识库问答与 Enterprise Search 学习笔记]] 企业级）
- 可解释性评估基准与信任校准（置信度误用/过度信任度量；PM锚，区别于本轮可解释性 UX 广度）
- 自主编程 Agent 的安全评测基准（生成代码漏洞 benchmark/审查闸门 SLA；安全锚，区别于本轮代码安全责任广度）

### 2026-10-06（第 24 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体×1 / AI Agent框架×1 / PM决策层×1 / 安全×1），广度均衡，无单独热点标记。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-05（第 23 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/端侧模型增量更新与差分量化工程 学习笔记.md`（二进制 diff/块级 delta/量化感知 delta 算法 + 差分精度损失与回退 + 端侧 AB 实验跑模型版本 + 带宽/存储收益；刻意区别于 [[端侧模型 OTA 更新与生命周期管理 学习笔记]] OTA 治理；连 5 篇；待核实 5 项）
  2. `AI Agent 框架/多模态 RAG 与文档问答产品 学习笔记.md`（ColPali/ColQwen2 视觉文档检索·page-as-image late interaction + ChatPDF/NotebookLM/AskYourPDF/Glean/Azure/Vertex/达观·合合；刻意区别于 [[知识库问答与 Enterprise Search 学习笔记]] 企业级与 [[多模态文档智能 DocAI 学习笔记]] 解析引擎；连 6 篇；待核实 5 项）
  3. `PM决策层/AI 产品的可访问性 UX for AI 学习笔记.md`（输出可读屏·替代模态·包容性设计·监管基线 WCAG 2.2/EAA/EU AI Act；刻意区别于 [[无障碍 Accessibility 与 GUI Agent 同源技术栈 学习笔记]] 技术栈；连 5 篇；待核实 5 项）
  4. `安全/合成媒体检测与 deepfake 防御 学习笔记.md`（被动检测/取证/防御：生物信号 rPPG·频域痕迹·跨模态不一致·攻防对抗 + deepfake 法规与平台治理；刻意区别于 [[模型水印与内容溯源 学习笔记]] 主动打标与 [[AI 视频与多模态生成 学习笔记]] 生成侧；连 3 篇；待核实 6 项）
- 待核实合计：4 篇共 21 项（厂商口径/未独立复核数字/法规生效日期/研究结论端侧迁移等），均标「待核实」，无编造。
- 状态文件：已追加第 24 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-06 黑名单增量（本轮新入，勿重复立题）
- 端侧模型增量更新与差分量化工程
- 多模态 RAG 与文档问答产品
- AI 产品的可访问性 UX for AI
- 合成媒体检测与 deepfake 防御

### 2026-10-06 下轮候选（库内未覆盖，可直接取用）
- 可解释性评估基准与信任校准（置信度误用/过度信任度量；PM锚，区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX 广度）
- 自主编程 Agent 的安全评测基准（生成代码漏洞 benchmark/审查闸门 SLA；安全锚，区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任广度）
- 端侧模型增量更新工程实测（差分更新精度损失实测曲线/AB 实验在端侧统计显著性/补丁体积 vs 全量收益；手机AI智能体锚，区别于本轮算法工程广度）
- 多模态 RAG 产品实测（ColPali 在真实 PDF 上的 recall/延迟/存储开销；AI Agent框架锚，区别于本轮产品广度）
- AI 产品 a11y 落地实操（读屏兼容测试 SOP/语音替代模态产品化/监管合规检查表；PM锚，区别于本轮基线 UX 广度）
- 合成媒体检测攻防实测（检测绕过 red-team/对抗样本鲁棒性 benchmark/端侧实时检测可行性；安全锚，区别于本轮检测防御广度）

### 2026-10-07（第 25 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体×1 / AI Agent框架×1 / PM决策层×1 / 安全×1），均取自 10-06 下轮候选，广度均衡，无单独热点标记。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-06（第 24 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/端侧模型增量更新工程实测 学习笔记.md`（实测维度：补丁体积/带宽收益·合并后精度损失曲线·端侧 AB 实验统计显著性·弱网/低端设备落地；刻意区别于 [[端侧模型 OTA 更新与生命周期管理 学习笔记]] 治理 / [[端侧模型增量更新与差分量化工程 学习笔记]] 算法；连 5 篇；待核实 9 项）
  2. `AI Agent 框架/多模态 RAG 产品实测 学习笔记.md`（实测维度：ColPali/ColQwen2 真实 PDF recall·延迟/存储开销·与文本 RAG 对照·部署教训；刻意区别于 [[多模态 RAG 与文档问答产品 学习笔记]] 产品广度 / [[知识库问答与 Enterprise Search 学习笔记]] 企业级 / [[多模态文档智能 DocAI 学习笔记]] 解析引擎；连 6 篇；待核实 6 项）
  3. `PM决策层/可解释性评估基准与信任校准 学习笔记.md`（评估基准与信任校准：ECE/reliability diagram·TrustLLM·TruthfulQA·自一致性·over/under-trust·appropriate reliance；刻意区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX 广度；连 4 篇；待核实 6 项）
  4. `安全/自主编程 Agent 的安全评测基准 学习笔记.md`（评测基准：CyberSecEval/SecurityEval/CodeSecEval/RiskBench·自主编码 Agent 红队·安全审查闸门 SLA；刻意区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任广度；连 5 篇；待核实 7 项）
- 待核实合计：4 篇共 28 项（厂商/媒体/竞赛/博客口径数字/监管解读/基准排名），均标「待核实」，无编造。
- 状态文件：已追加第 25 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-07 黑名单增量（本轮新入，勿重复立题）
- 端侧模型增量更新工程实测
- 多模态 RAG 产品实测
- 可解释性评估基准与信任校准
- 自主编程 Agent 的安全评测基准

### 2026-10-07 下轮候选（库内未覆盖，可直接取用）
- AI 产品 a11y 落地实操（读屏兼容测试 SOP/语音替代模态产品化/监管合规检查表；PM锚，区别于 [[AI 产品的可访问性 UX for AI 学习笔记]] 基线 UX 广度）
- 合成媒体检测攻防实测（检测绕过 red-team/对抗样本鲁棒性 benchmark/端侧实时检测可行性；安全锚，区别于 [[合成媒体检测与 deepfake 防御 学习笔记]] 检测防御广度）
- 端侧模型增量更新工程实测深潜（精度损失跨区域/模型族泛化/弱网实测统计 / 端侧 AB 显著性样板；手机AI智能体锚，区别于本轮实测概览）
- 多模态 RAG 端侧化实测（端侧跑 ColPali 的延迟/显存/精度可行性；AI Agent框架锚，区别于本轮云端实测）
- 信任校准产品化实测（over-trust 干预 A/B 真实效果/恰当依赖提升度量；PM锚，区别于本轮基准广度）
- 自主编程 Agent 安全评测落地（企业 CI 安全闸门 SLA 实测/红队自主编码 Agent 失守率；安全锚，区别于本轮基准广度）

### 2026-10-08（第 26 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体×1 全新广度 / AI Agent框架×1 实测 / PM决策层×1 实操 / 安全×1 攻防实测），广度均衡。运行前 Glob 预检发现「端侧模型增量更新工程实测」已于第 25 轮（10-07）入库；原计划「增量更新工程实测深潜」属同一子主题连续 3 轮深潜，违反 BREADTH，故替换为全新广度主题「端侧 AI 与手机计算摄影」。其余 3 主题取自 10-07 下轮候选，无幽灵笔记/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/端侧 AI 与手机计算摄影 学习笔记.md`【全新广度·替换过深主题】（NPU/ISP 协同计算影像管线：HDR 融合/夜景降噪/超分/人像分割虚化/语义感知编辑/端侧照片理解；Google HDR+·Apple Photonic·骁龙 Sight·天玑 Imagiq·华为 XD Fusion；连 7 篇；待核实 7 项）
  2. `AI Agent 框架/多模态 RAG 端侧化实测 学习笔记.md`（ColPali/ColQwen2 与端侧小 VLM 在手机/边缘跑视觉-语言文档 RAG 的延迟·显存·精度三角·视觉编码器量化·多向量存储压缩·本地 RAG 隐私收益；连 6+ 篇；待核实 7 项）
  3. `PM决策层/AI 产品 a11y 落地实操 学习笔记.md`（读屏兼容测试 SOP·语音/替代模态产品化·WCAG 2.2/EAA/EU AI Act 合规检查表·AI 特有 a11y 问题；连 6 篇；待核实 6 项）
  4. `安全/合成媒体检测攻防实测 学习笔记.md`（deepfake 检测器对抗鲁棒性：red-team 绕过+DFDC/FF++/GenImage/CIFAKE/DeepFake-OSS/IEEE VIP Cup+失守率+端侧实时可行；连 6 篇；待核实 6 项）
- 待核实合计：4 篇共 26 项（厂商命名/未公开数字/基准排名/监管日期/媒体口径），均标「待核实」，无编造。
- 状态文件：已追加第 26 轮记录、黑名单增量补入 4 主题、增补下轮候选（含 2 个延续实测 + 4 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-08 黑名单增量（本轮新入，勿重复立题）
- 端侧 AI 与手机计算摄影
- 多模态 RAG 端侧化实测
- AI 产品 a11y 落地实操
- 合成媒体检测攻防实测

### 2026-10-08 下轮候选（库内未覆盖，可直接取用）
- 移动端 AI 基准评测（MLPerf Mobile / AI Benchmark / AndBench / 端侧推理跑分；手机AI智能体锚，区别于 [[多模态评测基准 学习笔记]] 模型能力 与 [[Agent 评测与基准 学习笔记]] 轨迹）
- AI 编程的上下文工程与代码检索增强（repo indexing / code RAG / cursor rules / repo-aware coding；效率工具+Agent框架锚，区别于 [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]] 工具 与 [[Context Engineering 学习笔记]] 概念）
- 企业知识库连接器生态（M365/Salesforce/Slack/Confluence connectors for RAG；AI Agent框架锚，区别于 [[知识库问答与 Enterprise Search 学习笔记]] 检索层）
- 鸿蒙 NEXT 端侧 Agent 与元服务生态（HarmonyOS NEXT app 生态迁移 + 端侧 Agent 能力；手机AI智能体锚，区别于 [[HarmonyOS 元服务 学习笔记]] 功能层）
- 信任校准产品化实测（over-trust 干预 A/B 真实效果/恰当依赖提升度量；PM锚，区别于 [[可解释性评估基准与信任校准 学习笔记]] 基准广度）【延续实测分支】
- 自主编程 Agent 安全评测落地（企业 CI 安全闸门 SLA 实测/红队自主编码 Agent 失守率；安全锚，区别于 [[自主编程 Agent 的安全评测基准 学习笔记]] 基准广度）【延续实测分支】

### 2026-10-09（第 27 轮执行）
- 模式：并行 4 子代理，4 主题均为「相邻外辐射·全新广度」（2 手机AI智能体 + 1 AI Agent框架 + 1 效率工具），广度均衡。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件同步到 10-08（第 26 轮），无滞后/撞车。
- ⚠️ BREADTH 护栏：第 26 轮已转回全新广度，本轮延续该策略，主动剔除第 26 轮「下轮候选」中标注【延续实测分支】的 2 项（信任校准产品化实测 / 自主编程 Agent 安全评测落地），避免连续 3 轮实测深潜，守住 BREADTH > DEPTH 初心。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/移动端 AI 基准评测 学习笔记.md`（MLPerf Mobile v6.0 / ETH AI Benchmark / AndBench / 各 SoC NPU 跑分 / 端侧 LLM tokens-s；连 6 篇；刻意区别于 [[多模态评测基准 学习笔记]] 与 [[Agent 评测与基准 学习笔记]]；待核实 7 项）
  2. `知识管理与效率工具/AI 编程的上下文工程与代码检索增强 学习笔记.md`（repo indexing / code RAG / cursor rules / repo-aware coding / Copilot Workspace·Cody·Aider·Continue·LlamaIndex；连 3 篇；刻意区别于 [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]] 工具 / [[Context Engineering 学习笔记]] 概念；待核实 6 项）
  3. `AI Agent 框架/企业知识库连接器生态 学习笔记.md`（M365·Salesforce·Slack·Confluence·GWorkspace connectors / LlamaHub·Airbyte·unstructured·MCP connectors；连 3 篇；刻意区别于 [[知识库问答与 Enterprise Search 学习笔记]] 检索层；待核实 5 项）
  4. `手机AI智能体/鸿蒙 NEXT 端侧 Agent 与元服务生态 学习笔记.md`（HarmonyOS NEXT 生态迁移 / 小艺智能体 / HMAF / 元服务入口 / 盘古端侧；连 3 篇；刻意区别于 [[HarmonyOS 元服务 学习笔记]] 功能层；待核实 6 项）
- 待核实合计：4 篇共 24 项（厂商自报跑分/华为未公开数据/连接器数量口径/产品策略变动），均标「待核实」，无编造。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-09 黑名单增量（本轮新入，勿重复立题）
- 移动端 AI 基准评测
- AI 编程的上下文工程与代码检索增强
- 企业知识库连接器生态
- 鸿蒙 NEXT 端侧 Agent 与元服务生态

### 2026-10-09 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI 产品的用户反馈回路与纠错机制（human/RLHF-in-product feedback loops / thumbs 信号→改进；PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] 伦理）
- 端侧模型可解释性与特征归因可视化（on-device interpretability / feature attribution / saliency；手机AI智能体锚，区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 产品 UX 层）
- AI Agent 的持久化与状态管理（agent state / checkpoint / resume / 长程记忆落盘；AI Agent框架锚，区别于 [[Agent 记忆系统 学习笔记]] 记忆模型 / [[多智能体协作与编排 学习笔记]] 编排）
- AI 辅助研发效能度量与项目管理（Linear/Jira AI/研发效能/AI for PM；效率工具+PM锚，区别于 [[AI 工作流自动化与编排 学习笔记]] 编排 / [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]] 工具）
- AI 模型供应链安全与开源投毒防护（model/dependency supply chain / SBOM for models / 开源权重投毒；安全锚，区别于 [[模型水印与内容溯源 学习笔记]] 水印 / [[合成数据与模型后训练 学习笔记]] 训练数据污染）
- AI 手机的情境感知与传感器融合（sensor fusion / on-device context awareness / 多模态传感；手机AI智能体锚，区别于 [[端侧多模态 VLM 学习笔记]] 视觉理解 / [[时序事件驱动与 Agent 主动服务 学习笔记]] 事件触发）

### 2026-10-10（第 28 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / PM决策层 / 安全），均取自 10-09 下轮候选中的「全新广度」，无实测纵深、无单独热点标记，广度均衡。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-09（第 27 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/AI 手机的情境感知与传感器融合 学习笔记.md`（多传感器融合→情境状态：IMU/GPS/光感/麦克风/Camera × 端侧轻量模型 + Sensing Hub/OS 感知 API + 低功耗常驻；连 6 篇；刻意区别于 [[端侧多模态 VLM 学习笔记]] 视觉理解 / [[时序事件驱动与 Agent 主动服务 学习笔记]] 事件触发；待核实 3 项）
  2. `AI Agent 框架/AI Agent 的持久化与状态管理 学习笔记.md`（agent state/checkpoint/resume/长程任务状态落盘 + LangGraph checkpointer/Temporal durable execution/各框架 session；连 3 篇；刻意区别于 [[Agent 记忆系统 学习笔记]] 记忆模型 / [[多智能体协作与编排 学习笔记]] 编排；待核实 5 项）
  3. `PM决策层/AI 产品的用户反馈回路与纠错机制 学习笔记.md`（in-product feedback loops：👍👎/隐式行为/自然语言纠错→回流 eval/微调/提示词；含 OpenAI 2025-05 谄媚回退反模式；连 6 篇；刻意区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] 伦理；待核实 5 项）
  4. `安全/AI 模型供应链安全与开源投毒防护 学习笔记.md`（模型/依赖供应链：依赖投毒/权重投毒/训练数据投毒/工具链投毒 + 来源验证/签名/扫描/SBOM + JFrog 100 恶意 pickle/star23/PickleScan CVE-2025-10155 等真实事件；连 3 篇；刻意区别于 [[模型水印与内容溯源 学习笔记]] 水印 / [[合成数据与模型后训练 学习笔记]] 训练数据污染；待核实 2 项）
- 待核实合计：4 篇共 15 项（事件数量/厂商口径/未公开数字/产品策略），均标「待核实」，无编造。
- 状态文件：已追加第 28 轮记录、黑名单增量补入 4 主题、增补下轮候选（6 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-10 黑名单增量（本轮新入，勿重复立题）
- AI 手机的情境感知与传感器融合
- AI Agent 的持久化与状态管理
- AI 产品的用户反馈回路与纠错机制
- AI 模型供应链安全与开源投毒防护

### 2026-10-10 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI Agent 的权限与可撤销委托（agent authorization / OAuth scopes / revocable delegation；AI Agent框架+PM锚，区别于 [[智能体身份与信任 学习笔记]] 身份 / [[Confirmation UI 分级与产品责任边界 学习笔记]] 确认 UX）
- AI 产品的渐进式披露与可纠正性 UX（progressive disclosure / undoable AI actions；PM+交互锚，区别于 [[Agentic UX 交互设计模式 学习笔记]] 范式 / [[AI 产品的用户反馈回路与纠错机制 学习笔记]] 反馈闭环）
- AI 手机 Always-on 低功耗常驻感知（常驻情境模型与功耗预算；手机AI智能体锚，区别于 [[AI 手机的情境感知与传感器融合 学习笔记]] 融合机制 / [[端侧 AI 功耗与散热约束 学习笔记]] 功耗约束）
- AI 辅助个人知识管理的认知负荷与防噪（AI PKM 噪声/信息过载治理；效率工具锚，区别于 [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论 / [[个人知识库 AI 化与本地 RAG 学习笔记]] 本地 RAG）
- AI 产品的失败模式与可用性 SLA（AI 功能可用性/降级体验/错误预算；PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）
- Agent 离线评估与偏好数据集（offline eval / preference datasets；AI Agent框架锚，区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）

### 2026-10-11（第 29 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（AI Agent框架 / PM决策层 / 手机AI智能体 / 知识管理与效率工具），均取自 10-10 下轮候选中的「全新广度」，无实测纵深、无单独热点标记，广度均衡。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-10（第 28 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `AI Agent 框架/AI Agent 的权限与可撤销委托 学习笔记.md`（scope/capability/委托与吊销机制层：AAuth·AAP·MCP scoped auth·A2A·Entra Agent ID·Claude Agent SDK；连 4 篇；刻意区别于 [[智能体身份与信任 学习笔记]] 身份 / [[工具调用安全 学习笔记]] 鉴权 / [[Confirmation UI 分级与产品责任边界 学习笔记]] 确认 UX；待核实 4 项）
  2. `PM决策层/AI 产品的渐进式披露与可纠正性 UX 学习笔记.md`（渐进式披露 vs 可纠正性双概念 + 7 模式速查；刻意区别于 [[Agentic UX 交互设计模式 学习笔记]] 范式 / [[AI 产品的用户反馈回路与纠错机制 学习笔记]] 反馈闭环；连 4 篇；待核实 10 项）
  3. `手机AI智能体/AI 手机 Always-on 低功耗常驻感知 学习笔记.md`（always-on DSP/NPU/Sensing Hub 常驻情境模型 + 隐私指示；连 5 篇；刻意区别于 [[AI 手机的情境感知与传感器融合 学习笔记]] 融合 / [[端侧 AI 功耗与散热约束 学习笔记]] 功耗 / [[时序事件驱动与 Agent 主动服务 学习笔记]] 触发；待核实 12 项）
  4. `知识管理与效率工具/AI 辅助个人知识管理的认知负荷与防噪 学习笔记.md`（AI 生成笔记的认知负荷与噪声治理暗线；连 5 篇；刻意区别于 [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论 / [[个人知识库 AI 化与本地 RAG 学习笔记]] RAG；待核实 5 项）
- 待核实合计：4 篇共 31 项（厂商命名/未公开数字/版本年份/评测出处/产品现状），均标「待核实」，无编造。
- 状态文件：已追加第 29 轮记录、黑名单增量补入 4 主题、增补下轮候选（2 个延续 10-10 候选 + 4 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-11 黑名单增量（本轮新入，勿重复立题）
- AI Agent 的权限与可撤销委托
- AI 产品的渐进式披露与可纠正性 UX
- AI 手机 Always-on 低功耗常驻感知
- AI 辅助个人知识管理的认知负荷与防噪

### 2026-10-11 下轮候选（库内未覆盖，可直接取用）
- AI 产品的失败模式与可用性 SLA（AI 功能可用性/降级体验/错误预算；PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）【10-10 候选延续】
- Agent 离线评估与偏好数据集（offline eval / preference datasets；AI Agent框架锚，区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）【10-10 候选延续】
- 端侧模型与 SoC 协同设计（co-designed NPU models / 为特定 NPU 架构定制算子与量化；手机AI智能体锚，区别于 [[端侧 AI 芯片架构谱系 学习笔记]] 硬件 / [[端侧大模型推理 学习笔记]] 推理）
- Agent 安全护栏模式库（guardrail patterns / 输入-output 护栏 / 策略即代码；AI Agent框架锚，区别于 [[工具调用安全 学习笔记]] 鉴权 / [[AI 评测红队与对齐 学习笔记]] 红队 / [[AI Agent 沙箱与安全执行环境 学习笔记]] 沙箱）
- AI 产品的信任建立与破灭周期（trust lifecycle / 首因效应 / 一次失误信任崩塌；PM锚，区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）
- AI 辅助信息架构与知识组织结构（auto-MOC / auto-tagging / 自动双链建议；效率工具锚，区别于 [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论 / [[AI 辅助个人知识管理的认知负荷与防噪 学习笔记]] 噪声治理）

### 2026-10-13（第 30 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / PM决策层 / 知识管理与效率工具），均取自 10-11 下轮候选中的「全新广度」，无实测纵深、无单独热点标记，广度均衡。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-11（第 29 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/端侧模型与 SoC 协同设计 学习笔记.md`（软硬协同设计：为特定 NPU 架构反向定制量化友好/算子友好模型结构 + 芯片厂自研小模型 + NAS for NPU + co-design；刻意区别于 [[端侧 AI 芯片架构谱系 学习笔记]] 硬件 / [[端侧大模型推理 学习笔记]] 推理 / [[端侧模型量化]] 量化；连 6 篇；待核实 10 项）
  2. `AI Agent 框架/Agent 安全护栏模式库 学习笔记.md`（护栏模式库：输入护栏/输出护栏/策略即代码/语义防火墙/HITL 闸门 + Guardrails AI·NeMo Guardrails·LiteLLM·Azure Prompt Shields·Purple Llama；刻意区别于 [[工具调用安全 学习笔记]] 鉴权 / [[AI Agent 沙箱与安全执行环境 学习笔记]] 隔离 / [[AI 评测红队与对齐 学习笔记]] 红队 / [[AI Agent 的权限与可撤销委托 学习笔记]] 委托；连 8 篇；待核实 5 项）
  3. `PM决策层/AI 产品的信任建立与破灭周期 学习笔记.md`（信任动力学：首因效应/渐进建立/单次失误崩塌/过度-欠信任校准/修复路径；刻意区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI / [[AI 产品的用户反馈回路与纠错机制 学习笔记]] 反馈闭环；连 6 篇；待核实 6 项）
  4. `知识管理与效率工具/AI 辅助信息架构与知识组织结构 学习笔记.md`（AI 自动构建信息架构：auto-MOC/auto-tagging/自动双链建议/语义聚类/知识图谱生成；刻意区别于 [[PKM 方法论与 Obsidian 生态 学习笔记]] 方法论 / [[个人知识库 AI 化与本地 RAG 学习笔记]] RAG / [[AI 辅助个人知识管理的认知负荷与防噪 学习笔记]] 噪声治理；连 5 篇；待核实 7 项）
- 待核实合计：4 篇共 28 项（厂商自报跑分/研究结论定量/市场数字/功能边界等），均标「待核实」，无编造。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-13 黑名单增量（本轮新入，勿重复立题）
- 端侧模型与 SoC 协同设计
- Agent 安全护栏模式库
- AI 产品的信任建立与破灭周期
- AI 辅助信息架构与知识组织结构

### 2026-10-13 下轮候选（库内未覆盖，可直接取用）
- AI 产品的失败模式与可用性 SLA（AI 功能可用性/降级体验/错误预算；PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）【10-10 候选延续】
- Agent 离线评估与偏好数据集（offline eval / preference datasets；AI Agent框架锚，区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）【10-10 候选延续】
- 端侧模型推理可解释性与 saliency 可视化（on-device interpretability / feature attribution；手机AI智能体锚，区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 产品 UX 层）
- AI Agent 评测的对抗鲁棒性持续监控（production guardrail eval drift / 在线护栏衰减；AI Agent框架锚，区别于 [[Agent 安全护栏模式库 学习笔记]] 模式库）
- AI 产品的失败成本与责任归因（单次 AI 失误的用户损失量化/责任归属 UX；PM锚，区别于 [[AI 产品的信任建立与破灭周期 学习笔记]] 信任动力学）
- 多模态知识库的自动组织与跨模态检索结构（图像/音频/视频在 PKM 中的自动归类与索引；效率工具+AI模型锚，区别于 [[AI 辅助信息架构与知识组织结构 学习笔记]] 文本结构）

### 2026-10-15（第 31 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / PM决策层 / 知识管理与效率工具），均取自 10-13 下轮候选中的「全新广度」，无实测纵深、无单独热点标记，广度均衡。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-13（第 30 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/端侧模型推理可解释性与 saliency 可视化 学习笔记.md`（on-device interpretability / feature attribution / saliency：梯度·LIME-SHAP·TCAV·概念瓶颈模型 + Captum/端侧轻量归因；刻意区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 产品 UX 层；连 4 篇；待核实 7 项）
  2. `AI Agent 框架/Agent 离线评估与偏好数据集 学习笔记.md`（offline eval / preference datasets：Web-Shepherd/WebArbiter/AgentRewardBench/AgentBoard/RewardBench 2/UltraFeedback/Nectar；刻意区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程；连 5 篇；待核实 6 项）
  3. `PM决策层/AI 产品的失败模式与可用性 SLA 学习笔记.md`（失败模式分类 + 可用性 SLA/降级/错误预算；刻意区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI / [[AI 产品的信任建立与破灭周期 学习笔记]] 信任动力学；连 6 篇；待核实 7 项）
  4. `知识管理与效率工具/多模态知识库的自动组织与跨模态检索结构 学习笔记.md`（图像/音频/视频自动归类 + 跨模态统一向量索引/多模态 RAG；刻意区别于 [[AI 辅助信息架构与知识组织结构 学习笔记]] 文本结构；连 6+ 篇；待核实 7 项）
- 待核实合计：4 篇共 27 项（媒体口径/未公开数字/基准排名/研究结论定量），均标「待核实」，无编造。
- 状态文件：已追加第 31 轮记录、黑名单增量补入 4 主题、增补下轮候选（6 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-15 黑名单增量（本轮新入，勿重复立题）
- 端侧模型推理可解释性与 saliency 可视化
- Agent 离线评估与偏好数据集
- AI 产品的失败模式与可用性 SLA
- 多模态知识库的自动组织与跨模态检索结构

### 2026-10-15 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI Agent 评测的对抗鲁棒性持续监控（production guardrail eval drift / 在线护栏衰减；AI Agent框架锚，区别于 [[Agent 安全护栏模式库 学习笔记]] 模式库 / [[Agent 离线评估与偏好数据集 学习笔记]] 离线）
- 端侧模型推理的可解释性 UX 落地（saliency 在手机 AI 功能中的可视化呈现/用户可读；手机AI智能体+PM锚，区别于 [[端侧模型推理可解释性与 saliency 可视化 学习笔记]] 算法 / [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 云端 UX）
- AI 产品的失败成本与责任归因（单次 AI 失误的用户损失量化/责任归属 UX；PM锚，区别于 [[AI 产品的失败模式与可用性 SLA 学习笔记]] 失败模式 / [[AI 产品的信任建立与破灭周期 学习笔记]] 信任动力学）
- 多模态知识库的个人本地化与隐私（端侧多模态索引的隐私/离线存储；效率工具+安全锚，区别于 [[多模态知识库的自动组织与跨模态检索结构 学习笔记]] 索引结构 / [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]] 本地推理）
- AI 产品的情境自适应与主动干预边界（情境感知触发下的主动建议频次/打扰预算；手机AI智能体+PM锚，区别于 [[AI 手机的情境感知与传感器融合 学习笔记]] 融合 / [[时序事件驱动与 Agent 主动服务 学习笔记]] 触发）
- 开发者态 Agent 评测与 CI 集成（eval-as-CI / 回归护栏 / 评测即代码；AI Agent框架+效率工具锚，区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）

### 2026-10-16（第 32 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（AI Agent框架 / 手机AI智能体+PM / PM / 效率工具+安全），均取自 10-15 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记；状态文件已同步到 10-15（第 31 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `AI Agent 框架/AI Agent 评测的对抗鲁棒性持续监控 学习笔记.md`（production guardrail eval drift / 在线护栏衰减 / 对抗鲁棒性监控；连 4 篇；待核实 9 项）
  2. `手机AI智能体/端侧模型推理的可解释性 UX 落地 学习笔记.md`（saliency 端侧可视化呈现 / 用户可读归因；连 5+ 篇；待核实 6 项）
  3. `PM决策层/AI 产品的失败成本与责任归因 学习笔记.md`（单次 AI 失误用户损失量化 / 责任归属 UX；连 5 篇；待核实 7 项）
  4. `知识管理与效率工具/多模态知识库的个人本地化与隐私 学习笔记.md`（端侧多模态索引隐私 / 离线存储；连 3 篇；待核实 6 项）
- 待核实合计：4 篇共 28 项（厂商口径/未公开数字/版本年份/评测出处），均标「待核实」，无编造。
- 状态文件：已追加第 32 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-17（第 33 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体+PM / AI Agent框架+效率工具 / AI Agent框架 / 手机AI智能体+安全），均取自 10-16 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记；状态文件已同步到 10-16（第 32 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次校验：落盘 + 修复 1 处断链 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/AI 产品的情境自适应与主动干预边界 学习笔记.md`（情境自适应 vs 主动干预边界 / 自主性光谱 / 战略性沉默；连 5 篇）
  2. `知识管理与效率工具/开发者态 Agent 评测与 CI 集成 学习笔记.md`（Eval-as-Code / eval in CI / 回归门禁；连 5 篇）
  3. `AI Agent 框架/AI Agent 的流式与实时交互架构 学习笔记.md`（流式事件流 / SSE·WebSocket / HITL 实时回路；连 5 篇）
  4. `手机AI智能体/端侧模型的个性化隐私联邦边界 学习笔记.md`（端侧个性化 vs 隐私联邦连续谱；连 5 篇；修复 1 断链）
- 断链修复：第 4 篇初稿误用未存在笔记 [[端侧大模型安全与越狱 学习笔记]]，主代理核实真实文件为 `端侧模型安全与越狱` / `端侧大模型安全芯片级防护`，改为 [[端侧大模型安全芯片级防护 学习笔记]]。
- 待核实合计：4 篇均含厂商口径 / 未公开数字 / 版本年份等「待核实」标注，如实标出，无编造。
- 状态文件：已追加第 33 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-17 黑名单增量（本轮新入，勿重复立题）
- AI 产品的情境自适应与主动干预边界
- 开发者态 Agent 评测与 CI 集成
- AI Agent 的流式与实时交互架构
- 端侧模型的个性化隐私联邦边界

### 2026-10-17 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI 产品的多模态输出责任与合成内容标识 UX（PM+安全锚，区别于 [[模型水印与内容溯源 学习笔记]] 水印 / [[AI 监管与合规落地 学习笔记]] 法规）
- 知识库的语义检索质量与召回评测（效率工具+AI Agent框架锚，区别于 [[向量数据库 学习笔记]] 概览 / [[RAG 详细学习笔记]] 原理 / [[多模态 RAG 与文档问答产品 学习笔记]] 产品）
- 端侧模型的能耗感知调度与绿色推理（手机AI智能体锚，区别于 [[端侧 AI 功耗与散热约束 学习笔记]] 约束本身 / [[端侧推理的动态路由与模型选择 学习笔记]] 路由决策）
- AI 产品的可访问性 a11y 与无障碍智能（PM锚，区别于 [[Agentic UX 交互设计模式 学习笔记]] 交互范式）
- 智能体的人机信任校准与过度依赖防范（PM+AI Agent框架锚，区别于 [[AI 产品的失败成本与责任归因 学习笔记]] 责任归因）
- 跨端跨设备 Agent 协同与上下文迁移（手机AI智能体锚，区别于 [[OS 级系统 Agent 与跨应用自动化 学习笔记]] 系统编排）
- Agent 评测的数据污染与可复现性治理（AI Agent框架锚，区别于 [[Agent 评测与基准 学习笔记]] 基准本身）
- AI 编程助手的代码安全评测基准（效率工具+安全锚，区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任归属）

### 2026-10-16 黑名单增量（本轮新入，勿重复立题）
- AI Agent 评测的对抗鲁棒性持续监控
- 端侧模型推理的可解释性 UX 落地
- AI 产品的失败成本与责任归因
- 多模态知识库的个人本地化与隐私

### 2026-10-16 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI 产品的情境自适应与主动干预边界（情境感知触发下的主动建议频次/打扰预算；手机AI智能体+PM锚，区别于 [[AI 手机的情境感知与传感器融合 学习笔记]] 融合 / [[时序事件驱动与 Agent 主动服务 学习笔记]] 触发）
- 开发者态 Agent 评测与 CI 集成（eval-as-CI / 回归护栏 / 评测即代码；AI Agent框架+效率工具锚，区别于 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）
- AI Agent 的流式与实时交互架构（streaming / realtime agent loop；AI Agent框架锚，区别于 [[语音 Agent 架构 学习笔记]] 语音入口 / [[OS 级系统 Agent 与跨应用自动化 学习笔记]] 系统编排）
- 端侧模型的个性化隐私联邦边界（federated personalization vs 隐私；手机AI智能体+安全锚，区别于 [[端侧模型微调与个性化训练 学习笔记]] 微调 / [[隐私计算与端云协同 学习笔记]] 端云联邦）
- AI 产品的多模态输出责任与合成内容标识 UX（PM+安全锚，区别于 [[模型水印与内容溯源 学习笔记]] 水印 / [[AI 监管与合规落地 学习笔记]] 法规）
- 知识库的语义检索质量与召回评测（效率工具+AI Agent框架锚，区别于 [[向量数据库 学习笔记]] 概览 / [[RAG 详细 学习笔记]] 原理 / [[多模态 RAG 与文档问答产品 学习笔记]] 产品）

### 2026-10-18（第 34 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / 知识管理与效率工具 / PM决策层 / AI Agent框架），均取自 10-17 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件已同步到 10-17（第 33 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功）：
  1. `手机AI智能体/端侧模型的能耗感知调度与绿色推理 学习笔记.md`（DVFS/批处理合并/算子级/按需选择的省电调度 + 碳足迹绿色AI；连 7 篇；刻意区别于 [[端侧 AI 功耗与散热约束 学习笔记]] 约束本身 / [[端侧推理的动态路由与模型选择 学习笔记]] 路由 / [[端侧大模型推理 学习笔记]] 原理；待核实 5 项）
  2. `知识管理与效率工具/知识库的语义检索质量与召回评测 学习笔记.md`（recall@k/MRR/NDCG/噪声chunk/长尾召回 + Ragas/RAGChecker/BEIR/TREC/ARES；连 6 篇；刻意区别于 [[向量数据库 学习笔记]] 概览 / [[RAG 详细学习笔记]] 原理 / [[多模态 RAG 与文档问答产品 学习笔记]] 产品 / [[个人知识库 AI 化与本地 RAG 学习笔记]] 本地库；待核实 6 项）
  3. `PM决策层/AI 产品的多模态输出责任与合成内容标识 UX 学习笔记.md`（C2PA 消费端呈现/平台标识政策/误用责任 UX；连 5 篇；刻意区别于 [[模型水印与内容溯源 学习笔记]] 水印 / [[AI 监管与合规落地 学习笔记]] 法规 / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI / [[合成媒体检测与 deepfake 防御 学习笔记]] 检测；待核实 7 项）
  4. `AI Agent 框架/智能体的人机信任校准与过度依赖防范 学习笔记.md`（appropriate reliance / 置信度披露 / 摩擦设计 / 能力边界提示；连 5+ 篇；刻意区别于 [[AI 产品的信任建立与破灭周期 学习笔记]] 动力学 / [[可解释性评估基准与信任校准 学习笔记]] 基准 / [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX；待核实 6 项）
- 待核实合计：4 篇共 24 项（媒体口径/厂商宣传数字/法规生效日/研究结论定量/版本号），均标「待核实」，无编造。
- 状态文件：已追加第 34 轮记录、黑名单增量补入 4 主题、重建下轮候选（移除已覆盖项 + 增补 2 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-18 黑名单增量（本轮新入，勿重复立题）
- 端侧模型的能耗感知调度与绿色推理
- 知识库的语义检索质量与召回评测
- AI 产品的多模态输出责任与合成内容标识 UX
- 智能体的人机信任校准与过度依赖防范

### 2026-10-18 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- AI 产品的可访问性 a11y 与无障碍智能（PM锚，区别于 [[Agentic UX 交互设计模式 学习笔记]] 交互范式 / [[AI 产品的可解释性 UX 与归因展示 学习笔记]] UX）
- 跨端跨设备 Agent 协同与上下文迁移（手机AI智能体锚，区别于 [[OS 级系统 Agent 与跨应用自动化 学习笔记]] 系统编排 / [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦）
- Agent 评测的数据污染与可复现性治理（AI Agent框架锚，区别于 [[Agent 评测与基准 学习笔记]] 基准本身 / [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 评测工程）
- AI 编程助手的代码安全评测基准（效率工具+安全锚，区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任归属）
- AI 产品的儿童与未成年用户保护设计（PM锚，区别于 [[AI 产品的可访问性 a11y 与无障碍智能 学习笔记]] a11y / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）

### 2026-10-27（第 35 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / 知识管理与效率工具 / PM决策层），均取自 10-18 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。
- 防重修正：运行前 Glob 预检发现 10-18 候选「AI 产品的可访问性 a11y 与无障碍智能」与库内既有 `AI 产品的可访问性 UX for AI 学习笔记.md`（第 24 轮）主题重合，遂剔除该候选，改取第 5 候选「AI 产品的儿童与未成年用户保护设计」，避免重复立题。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/跨端跨设备 Agent 协同与上下文迁移 学习笔记.md`（跨端协同/上下文迁移/Continuity-like 体验；连 4 篇；待核实 6 项）
  2. `AI Agent 框架/Agent 评测的数据污染与可复现性治理 学习笔记.md`（基准污染检测/可复现性治理；连 4 篇；待核实 6 项）
  3. `知识管理与效率工具/AI 编程助手的代码安全评测基准 学习笔记.md`（代码安全评测基准；连 3+ 篇；待核实 5 项）
  4. `PM决策层/AI 产品的儿童与未成年用户保护设计 学习笔记.md`（儿童保护设计/适龄 UX；连 4 篇；待核实 6 项）
- 待核实合计：4 篇共 23 项（厂商版本号/未公开数字/法规状态/研究结论定量），均标「待核实」，无编造。
- 状态文件：已追加第 35 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-27 黑名单增量（本轮新入，勿重复立题）
- 跨端跨设备 Agent 协同与上下文迁移
- Agent 评测的数据污染与可复现性治理
- AI 编程助手的代码安全评测基准
- AI 产品的儿童与未成年用户保护设计

### 2026-10-27 下轮候选（库内未覆盖，可直接取用·均为全新广度）
- 跨端 Agent 协同的上下文格式标准化与协议（context serialization / 跨端统一表示 / 厂商协议互操作；手机AI智能体锚，区别于 [[跨端跨设备 Agent 协同与上下文迁移 学习笔记]] 协同机制）
- Agent 评测的成本归因与评测 ROI（eval cost / 评测投入产出比；AI Agent框架锚，区别于 [[智能体经济学与 AI 成本归因 学习笔记]] 运行成本）
- 代码助手的供应链与依赖安全评测（SBOM for code-gen / 依赖投毒检测；效率工具+安全锚，区别于 [[AI 编程助手的代码安全评测基准 学习笔记]] 生成安全 / [[AI 模型供应链安全与开源投毒防护 学习笔记]] 模型供应链）
- AI 产品的老年用户与数字鸿沟包容性设计（银发/低数字素养 UX；PM锚，区别于 [[AI 产品的可访问性 UX for AI 学习笔记]] a11y / [[AI 产品的儿童与未成年用户保护设计 学习笔记]] 儿童）
- AI 产品的文化适配与本地化（多语言/文化偏见/区域合规；PM锚，区别于 [[AI 翻译与跨语言知识工具生态 学习笔记]] 翻译工具）
- 跨模态统一表示与多模态 embeddings（AI模型基础锚，区别于 [[多模态评测基准 学习笔记]] 评测 / [[多模态 RAG 与文档问答产品 学习笔记]] RAG）

### 2026-10-28（第 36 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / 知识管理与效率工具 / PM决策层），均取自 10-27 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/跨端 Agent 协同的上下文格式标准化与协议 学习笔记.md`（上下文序列化/schema/MCP·A2A·Engram·UCIP·AIP 与厂商私有封包互操作；连 4+ 篇；待核实 9 项）
  2. `AI Agent 框架/Agent 评测的成本归因与评测 ROI 学习笔记.md`（eval cost 构成/归因维度/评测 ROI/降本；连 4 篇；待核实 8 项）
  3. `知识管理与效率工具/代码助手的供应链与依赖安全评测 学习笔记.md`（SBOM for code-gen/依赖投毒/幻觉包/许可证；连 3 篇；待核实 6 项）
  4. `PM决策层/AI 产品的老年用户与数字鸿沟包容性设计 学习笔记.md`（适老化/语音优先/防 AI 诈骗/数字鸿沟；连 4 篇；待核实 6 项）
- 待核实合计：4 篇共 29 项（媒体口径/厂商报告数字/法规状态/研究定量），均标「待核实」，无编造。
- 状态文件：已追加第 36 轮记录、黑名单增量补入 4 主题、增补 6 个下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-28 黑名单增量（本轮新入，勿重复立题）
- 跨端 Agent 协同的上下文格式标准化与协议
- Agent 评测的成本归因与评测 ROI
- 代码助手的供应链与依赖安全评测
- AI 产品的老年用户与数字鸿沟包容性设计

### 2026-10-28 下轮候选（库内未覆盖，可直接取用·全新广度）
- AI 产品的文化适配与本地化（PM锚，区别于 [[AI 翻译与跨语言知识工具生态 学习笔记]] 翻译工具）【10-27 未取延续】
- 跨模态统一表示与多模态 embeddings（AI模型基础锚，区别于 [[多模态评测基准 学习笔记]] 评测 / [[多模态 RAG 与文档问答产品 学习笔记]] RAG）【10-27 未取延续】
- 智能体的可观测性与分布式追踪（AI Agent框架锚，区别于 [[Agent 评测的成本归因与评测 ROI 学习笔记]] 评测成本 / [[模型服务化与 LLM 网关 学习笔记]] 网关可观测）
- AI 产品的"多模态输入"可及性与容错 UX（PM锚，区别于 [[AI 产品的可访问性 UX for AI 学习笔记]] a11y / [[AI 产品的老年用户与数字鸿沟包容性设计 学习笔记]] 适老）
- 端侧模型的"模型卡/数据卡"透明度披露（手机AI智能体+安全锚，区别于 [[端侧模型推理的可解释性 UX 落地 学习笔记]] UX / [[负责任 AI 与 AI 产品伦理落地 学习笔记]] RAI）

### 2026-10-29（第 37 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（AI模型基础 / AI Agent框架 / PM决策层 / 手机AI智能体），均取自 10-28 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记（其中「智能体的可观测性与分布式追踪」与库内既有 `Agent 可观测性 LLM Observability 学习笔记.md` 主题相邻，已强制按"分布式追踪/trace 传播"窄角度差异化，未撞车）；状态文件同步到 10-28（第 36 轮），无滞后。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `AI模型基础/跨模态统一表示与多模态 embeddings 学习笔记.md`（CLIP/ImageBind/UniCL/BGE-M3 统一多模态嵌入；连 3 篇；待核实 6 项）
  2. `AI Agent 框架/智能体的可观测性与分布式追踪 学习笔记.md`（OTel for agents / 跨 agent span 传播 / tool-call 链路追踪；连 3 篇；待核实 6 项；与原 observability 笔记互补）
  3. `PM决策层/AI 产品的文化适配与本地化 学习笔记.md`（本地化≠翻译·五维分类·区域合规；连 4 篇；待核实 3 项）
  4. `手机AI智能体/端侧模型的模型卡与数据卡透明度披露 学习笔记.md`（Model Card/Datasheet/EU Art.50 透明度义务；连 6 篇；待核实 5+2 项）
- 待核实合计：4 篇共 28 项（媒体口径/厂商未公开数据/法规生效日/版本号/研究定量），均标「待核实」，无编造。
- 状态文件：已追加第 37 轮记录、黑名单增量补入 4 主题、增补 6 个全新广度下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-29 黑名单增量（本轮新入，勿重复立题）
- 跨模态统一表示与多模态 embeddings
- 智能体的可观测性与分布式追踪
- AI 产品的文化适配与本地化
- 端侧模型的模型卡/数据卡透明度披露

### 2026-10-29 下轮候选（库内未覆盖，可直接取用·全新广度）
- AI 产品的"多模态输入"可及性与容错 UX（PM锚）【10-28 延续未取】
- 端侧模型的个性化数据本地留存与遗忘权（手机AI智能体+安全锚，区别于 [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦边界）
- AI 编程助手的测试生成与验证闭环（效率工具锚，区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任 / [[AI 编程助手的代码安全评测基准 学习笔记]] 评测）
- 多智能体编排的容错与错误传播隔离（AI Agent框架锚，区别于 [[智能体的可观测性与分布式追踪 学习笔记]] tracing 视角）
- AI 产品的"静默失败"检测与用户告知机制（PM锚，区别于 [[AI 产品的失败成本与责任归因 学习笔记]] 责任归因）
- 端侧语音唤醒与 always-listening 隐私边界（手机AI智能体锚，区别于 [[AI 手机 Always-on 低功耗常驻感知 学习笔记]] 常驻感知）
- 知识管理的"个人知识图谱"自动化构建（效率工具锚，区别于 [[AI 辅助信息架构与知识组织结构 学习笔记]] 信息架构 / [[个人知识库 AI 化与本地 RAG 学习笔记]] 本地 RAG）

### 2026-10-30（第 38 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / PM决策层 / 知识管理与效率工具），均取自 10-29 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选主题无同名幽灵笔记；状态文件同步到 10-29（第 37 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功，长行命中即代表已注册）：
  1. `手机AI智能体/端侧语音唤醒与 always-listening 隐私边界 学习笔记.md`（wake word/低功耗协处理器·Sensing Hub·系统级麦克风指示灯·可关闭设计·Siri/Google/小爱/Bixby 隐私实现；连 3 篇；待核实 7 项）
  2. `AI Agent 框架/多智能体编排的容错与错误传播隔离 学习笔记.md`（cascading failure/blast radius·重试/熔断/降级/超时/补偿·隔离粒度 进程/容器/microVM·OWASP ASI08/LangGraph/CrewAI/AutoGen；连 3 篇；待核实 10 项）
  3. `PM决策层/AI 产品的静默失败检测与用户告知机制 学习笔记.md`（幻觉/截断/静默降级/权限失败·检测+告知 UX·与失败成本/反馈回路差异化；连 3 篇；待核实 8 项）
  4. `知识管理与效率工具/知识管理的个人知识图谱自动化构建 学习笔记.md`（LLM 抽取实体关系·与双链互补·GraphRAG 个人化/Obsidian 插件/Mem/Logseq；连 3+ 篇；待核实 6 项）
- 待核实合计：4 篇共 31 项（厂商和解金额/市场报告数字/论文 preprint/自报功耗等），均标「待核实」，无编造。
- 文件名约束：第 3、4 篇原候选含英文双引号，Windows 文件名禁 `"`，子代理已去掉文件名引号（frontmatter title 保留），MOC 链接同步，Obsidian 双链一致。
- 状态文件：已追加第 38 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-30 黑名单增量（本轮新入，勿重复立题）
- 端侧语音唤醒与 always-listening 隐私边界
- 多智能体编排的容错与错误传播隔离
- AI 产品的静默失败检测与用户告知机制
- 知识管理的个人知识图谱自动化构建

### 2026-10-30 下轮候选（库内未覆盖，可直接取用·全新广度）
- AI 产品的"多模态输入"可及性与容错 UX（PM锚）【10-28 延续未取】
- 端侧模型的个性化数据本地留存与遗忘权（手机AI智能体+安全锚，区别于 [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦边界）
- AI 编程助手的测试生成与验证闭环（效率工具锚，区别于 [[AI 编程助手的代码安全责任 学习笔记]] 责任 / [[AI 编程助手的代码安全评测基准 学习笔记]] 评测）
- AI 产品的"解释性失败"告知——当 AI 解释/理由本身错误时（PM锚，区别于 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 归因展示）
- 端侧模型的"影子模型/蒸馏教师"透明度（手机AI智能体+模型锚，区别于 [[端侧模型与 SoC 协同设计 学习笔记]] 协同）
- 知识图谱的自动维护与破损链接修复（效率工具锚，区别于本轮「个人知识图谱自动化构建」）

### 2026-10-31（第 39 轮执行）
- 模式：并行 4 子代理，4 锚点外辐射（手机AI智能体 / 知识管理与效率工具×2 / PM决策层），均取自 10-30 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记；状态文件同步到 10-30（第 38 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4 处 MOC 注册成功，其中 2 篇注册进同一 效率工具 MOC）：
  1. `手机AI智能体/端侧模型的个性化数据本地留存与遗忘权 学习笔记.md`（GDPR 被遗忘权/EU AI Act Art.10/Apple PCC/Android PCC/联邦遗忘；连 4 篇；待核实 6 项）
  2. `知识管理与效率工具/AI 编程助手的测试生成与验证闭环 学习笔记.md`（SWE-bench Verified/自验证闭环/Codium/Diffblue；连 2 篇；待核实 6 项）
  3. `PM决策层/AI 产品的多模态输入可及性与容错 UX 学习笔记.md`（语音/视觉/触控/文件模态降级×WCAG 3.0/厂商包容原则；连 4 篇；待核实 6 项）
  4. `知识管理与效率工具/知识图谱的自动维护与破损链接修复 学习笔记.md`（schema 漂移/死链/重复/过时/矛盾+LLM 校验修复+Obsidian 插件/Neo4j；连 5 篇；待核实 6 项）
- 待核实合计：4 篇共 24 项（厂商口径/未公开数字/版本年份/法规状态/研究定量），均标「待核实」，无编造。
- 状态文件：已追加第 39 轮记录、黑名单增量补入 4 主题、增补下轮候选（见下方）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-10-31 黑名单增量（本轮新入，勿重复立题）
- 端侧模型的个性化数据本地留存与遗忘权
- AI 编程助手的测试生成与验证闭环
- AI 产品的多模态输入可及性与容错 UX
- 知识图谱的自动维护与破损链接修复

### 2026-10-31 下轮候选（库内未覆盖，可直接取用·全新广度）
- AI 产品的"解释性失败"告知——当 AI 解释/理由本身错误时（PM锚）【10-30 延续未取】
- 端侧模型的"影子模型/蒸馏教师"透明度（手机AI智能体+模型锚，区别于 [[端侧模型与 SoC 协同设计 学习笔记]] 协同）【10-30 延续未取】
- 端侧模型的用户授权与隐私偏好开关（手机AI智能体+PM锚，区别于 [[端侧语音唤醒与 always-listening 隐私边界 学习笔记]] 常驻感知 / [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦边界）
- AI Agent 工具调用的幂等性与副作用管理（AI Agent框架锚，区别于 [[多智能体编排的容错与错误传播隔离 学习笔记]] 容错 / [[AI Agent 的权限与可撤销委托 学习笔记]] 权限委托）
- AI 产品的退出机制与数据可携带设计（PM+安全锚，区别于 [[端侧模型的个性化数据本地留存与遗忘权 学习笔记]] 遗忘权删除）
- AI 辅助的笔记回顾与间隔重复系统（效率工具锚，区别于 [[知识管理的个人知识图谱自动化构建 学习笔记]] 图谱 / [[AI 辅助个人知识管理的认知负荷与防噪 学习笔记]] 认知负荷）

### 2026-11-01（第 40 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / 知识管理与效率工具 / PM决策层），均取自 10-31 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记；状态文件同步到 10-31（第 39 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/端侧模型的影子模型与蒸馏教师透明度 学习笔记.md`（on-device shadow/teacher model transparency：蒸馏教师血缘披露/影子模型监测偏差/训练数据来源透明度 + EU AI Act Art.50 + 模型卡；连 4 篇；待核实 7 项）
  2. `AI Agent 框架/AI Agent 工具调用的幂等性与副作用管理 学习笔记.md`（idempotency key/副作用分类/补偿事务/confirmation 网关 + MCP 工具 Schema/OWASP ASI；连 5 篇；待核实 6 项）
  3. `知识管理与效率工具/AI 辅助的笔记回顾与间隔重复系统 学习笔记.md`（AI 复习调度/自动生成卡片/Obsidian 插件/LLM 回顾提醒 + Anki/RemNote/FSRS/NotebookLM；连 6 篇；待核实 6 项）
  4. `PM决策层/AI 产品的解释性失败告知 学习笔记.md`（当 AI 解释本身错误：虚假归因/引用幻觉/事后合理化 + calibration/来源可验证/合规；连 5 篇；待核实 5 项）
- 待核实合计：4 篇共 24 项（厂商口径/未公开数字/法规生效日/研究定量），均标「待核实」，无编造。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-11-01 黑名单增量（本轮新入，勿重复立题）
- 端侧模型的影子模型与蒸馏教师透明度
- AI Agent 工具调用的幂等性与副作用管理
- AI 辅助的笔记回顾与间隔重复系统
- AI 产品的解释性失败告知

### 2026-11-01 下轮候选（库内未覆盖，可直接取用·全新广度）
- 端侧模型的用户授权与隐私偏好开关（手机AI智能体+PM锚，区别于 [[端侧语音唤醒与 always-listening 隐私边界 学习笔记]] 常驻感知 / [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦边界）【10-31 遗留】
- AI 产品的退出机制与数据可携带设计（PM+安全锚，区别于 [[端侧模型的个性化数据本地留存与遗忘权 学习笔记]] 遗忘权删除）【10-31 遗留】
- 端侧模型的权重加密与端侧推理保护协同（手机AI智能体+安全锚，区别于 [[端侧大模型安全芯片级防护 学习笔记]] 硬件 / [[模型水印与内容溯源 学习笔记]] 水印）
- AI Agent 的长上下文管理与上下文压缩（AI Agent框架锚，区别于 [[Context Engineering 学习笔记]] 概念 / [[AI Agent 的持久化与状态管理 学习笔记]] 状态）
- AI 产品的主动失误恢复与用户补救流程（PM锚，区别于 [[AI 产品的静默失败检测与用户告知机制 学习笔记]] 告知 / [[AI 产品的失败成本与责任归因 学习笔记]] 责任）
- 闪卡复习与 Obsidian 双链笔记的工作流融合（效率工具锚，区别于 [[AI 辅助的笔记回顾与间隔重复系统 学习笔记]] 复习系统本身）

### 2026-11-04（第 41 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体 / AI Agent框架 / 知识管理与效率工具 / PM决策层），广度均衡，无实测纵深、无单独热点标记。
- 防重修正：运行前 Glob 预检发现 11-01 下轮候选中「AI Agent 的长上下文管理与上下文压缩」「闪卡复习与 Obsidian 双链笔记的工作流融合」两候选已在库内存在（无执行记录的幽灵笔记），遂剔除，改用 2 个全新相邻外辐射主题（测试时计算、结构化大纲写作工作流）补位，使 4 锚点全覆盖、无撞车。两幽灵主题已补入本轮黑名单/已覆盖，后续勿重复立题。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/端侧模型的用户授权与隐私偏好开关 学习笔记.md`（OS 隐私面板/细粒度同意开关/数据用途透明告知；连 4 篇；待核实 5+ 项）
  2. `AI Agent 框架/AI Agent 的测试时计算与推理时缩放 学习笔记.md`（o1/R1 长链推理·search/tool-use 即计算·self-consistency·PRM·verifier；连 8 篇；待核实 6 类）
  3. `知识管理与效率工具/AI 辅助的结构化大纲与长文写作工作流 学习笔记.md`（outline-first→起草→AI协作→修订→整合；连 5 篇；待核实 7 项）
  4. `PM决策层/AI 产品的退出机制与数据可携带设计 学习笔记.md`（账号注销 UX·数据导出 GDPR Art.20·记忆删除迁移·anti-lock-in；连 7 篇；待核实 6 项）
- 待核实合计：4 篇共约 24 项（厂商口径/未公开数字/法规生效日/研究定量），均标「待核实」，无编造。
- 状态文件：已追加第 41 轮记录、黑名单增量补入 4 主题（含 2 幽灵）、重建下轮候选（剔除 2 幽灵 + 增补 5 个全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-11-04 黑名单增量（本轮新入，勿重复立题）
- 端侧模型的用户授权与隐私偏好开关
- AI Agent 的测试时计算与推理时缩放
- AI 辅助的结构化大纲与长文写作工作流
- AI 产品的退出机制与数据可携带设计
- AI Agent 的长上下文管理与上下文压缩（幽灵笔记·已存在库内，勿重建）
- 闪卡复习与 Obsidian 双链笔记的工作流融合（幽灵笔记·已存在库内，勿重建）

### 2026-11-04 下轮候选（库内未覆盖，可直接取用·全新广度）
- 端侧模型的权重加密与端侧推理保护协同（手机AI智能体+安全锚，区别于 [[端侧大模型安全芯片级防护 学习笔记]] 硬件 / [[模型水印与内容溯源 学习笔记]] 水印）【11-01 遗留】
- AI 产品的主动失误恢复与用户补救流程（PM锚，区别于 [[AI 产品的静默失败检测与用户告知机制 学习笔记]] 告知 / [[AI 产品的失败成本与责任归因 学习笔记]] 责任）【11-01 遗留】
- AI Agent 的离线优先与弱网降级（AI Agent框架锚，区别于 [[AI Agent 的流式与实时交互架构 学习笔记]] 实时）
- 端侧模型的持续预训练与灾难性遗忘防护（手机AI智能体+模型锚，区别于 [[端侧模型微调与个性化训练 学习笔记]] 微调）
- AI 产品的订阅/计费模式与价值感知设计（PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量）
- 个人知识库的语义搜索重排序与个性化召回（效率工具锚，区别于 [[知识库的语义检索质量与召回评测 学习笔记]] 评测 / [[个人知识库 AI 化与本地 RAG 学习笔记]] 本地RAG）
- AI 辅助的会议纪要自动化与行动项抽取（效率工具锚，区别于 [[AI 原生浏览器与信息摄取 学习笔记]] 摄取）

### 2026-11-05（第 42 轮执行）
- 模式：并行 4 子代理，4 锚点各外辐射 1 主题（手机AI智能体+安全 / PM决策层 / AI Agent框架 / 知识管理与效率工具），均取自 11-04 下轮候选「全新广度」，广度均衡，无实测纵深、无单独热点标记。运行前 Glob 预检 4 候选无同名幽灵笔记，状态文件同步到 11-04（第 41 轮），无滞后/撞车。
- 新增 4 篇广度种子笔记（均 WebSearch/WebFetch 核实，含待核实标注，主代理二次 grep 校验 4/4 文件落盘 + 4/4 MOC 注册成功）：
  1. `手机AI智能体/端侧模型的权重加密与端侧推理保护协同 学习笔记.md`（权重存储态加密/混淆反逆向+TEE屏蔽计算+密钥协同+反提取侧信道+PUF绑定；连 4 篇；待核实 6 项）
  2. `PM决策层/AI 产品的主动失误恢复与用户补救流程 学习笔记.md`（自动回滚/自愈/补偿/Saga/HITL/补救SLA/信任修复；连 7 篇；待核实 5 项）
  3. `AI Agent 框架/AI Agent 的离线优先与弱网降级 学习笔记.md`（local-first/离线队列/冲突解决/优雅降级/重试退避；连 8 篇；待核实 6 项）
  4. `知识管理与效率工具/AI 辅助的会议纪要自动化与行动项抽取 学习笔记.md`（转写→纪要→行动项抽取→任务系统对接闭环；区别于 会议转录纪要Agent；连 5 篇；待核实 5 项）
- 待核实合计：4 篇共 22 项，均标「待核实」，无编造。
- 状态文件：已追加第 42 轮记录、黑名单增量补入 4 主题、重建下轮候选（3 遗留 + 4 全新广度）。
- 未触及：`10-知识飞轮/`、无关文件、删除操作均未执行。

### 2026-11-05 黑名单增量（本轮新入，勿重复立题）
- 端侧模型的权重加密与端侧推理保护协同
- AI 产品的主动失误恢复与用户补救流程
- AI Agent 的离线优先与弱网降级
- AI 辅助的会议纪要自动化与行动项抽取

### 2026-11-05 下轮候选（库内未覆盖，可直接取用·全新广度）
- 端侧模型的持续预训练与灾难性遗忘防护（手机AI智能体+模型锚，区别于 [[端侧模型微调与个性化训练 学习笔记]] 微调）【11-04 遗留】
- AI 产品的订阅/计费模式与价值感知设计（PM锚，区别于 [[数据飞轮与 AI 产品度量 学习笔记]] 度量）【11-04 遗留】
- 个人知识库的语义搜索重排序与个性化召回（效率工具锚，区别于 [[知识库的语义检索质量与召回评测 学习笔记]] 评测 / [[个人知识库 AI 化与本地 RAG 学习笔记]] 本地RAG）【11-04 遗留】
- 端侧 Agent 的隐私计算与联邦推理协同（手机AI智能体+安全锚，区别于 [[端侧模型的个性化隐私联邦边界 学习笔记]] 联邦边界 / [[端侧大模型安全芯片级防护 学习笔记]] 硬件 / [[端侧模型的个性化数据本地留存与遗忘权 学习笔记]] 遗忘权）
- AI Agent 的因果推理与可解释决策（AI Agent框架锚，区别于 [[端侧模型推理的可解释性 UX 落地 学习笔记]] 仅UX / [[AI 产品的解释性失败告知 学习笔记]] 告知）
- AI 产品的可组合性与 API 生态设计（PM锚，区别于 [[智能体商店与 Agent 分发平台生态 学习笔记]] 分发 / [[AI 产品的商业模式与定价策略 学习笔记]] 定价）
- 个人知识库的语音与多模态捕获入口（效率工具锚，区别于 [[AI 辅助阅读与信息摄取工具生态 学习笔记]] 阅读摄取 / [[AI 辅助的会议纪要自动化与行动项抽取 学习笔记]] 会议）
