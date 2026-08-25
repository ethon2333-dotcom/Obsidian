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

## 已覆盖主题黑名单（库内已有笔记，勿重复立题）

RAG / 向量数据库 / Context Engineering / MCP 与设备侧 MCP / Agent 协议生态 / LangChain / LangGraph / Loop Engineering / Graph Engineering / 端侧量化 / 端侧推理 / 投机采样 / PagedAttention·KV Cache / AI Runtime 调度 / App Intents / HarmonyOS 元服务 / GUI Agent 架构 / 工具调用安全 / Confirmation UI / 用户研究方法 / 增长模型 / Figma / Go / Rust / Agent 评测基准 / 移动端 NPU 编译栈 / PKM 与 Obsidian 生态 / Agentic UX / **端侧 SLM 模型家族** / **语音 ASR·TTS** / **隐私计算·TEE·PCC** / **AI 眼镜与可穿戴** / **数据飞轮与 AI 产品度量** / **AI 编程助手与 Agentic Coding** / **智能座舱与车机 HMI 意图入口** / **合成数据与模型后训练** / **模型蒸馏与师生训练** / **多模态 GUI 理解与 UI Grounding** / **无障碍 Accessibility 与 GUI Agent 同源技术栈** / **时序事件驱动与 Agent 主动服务** / **端侧多模态 VLM** / **端云协同推理与混合部署** / **意图框架开发者生态与平台经济** / **多智能体协作与编排** / **端侧 AI 功耗与散热约束** / **Agent 可观测性 LLM Observability** / **低代码无代码 Agent 搭建平台** / **端侧模型安全与越狱**

### 2026-08-17 补充候选（刷新，移除已覆盖项）
- 端侧 AI 芯片架构谱系（NPU vs GPU vs ASIC vs DSP，区别于 NPU 编译栈与功耗约束）
- Embodied AI / 机器人 Agent（与端侧智能同源，发散图谱外辐射）
- 个性化与端侧用户记忆（on-device personalization，⚠️ 与 `Agent 记忆与个性化意图理解` 区分个性化建模 vs 记忆系统）
- Agent 推理成本优化（cache / batching / prefix sharing，区别于已覆盖的投机采样）
- 世界模型 World Model 与仿真合成环境（合成数据上游技术）
- AI 搜索与 RAG 问答工具（个人知识库 AI 化，⚠️ 查 `RAG 检索增强生成` 重叠度）
- ANN 索引算法专题（HNSW/IVF-PQ/DiskANN 深潜）——⚠️ `向量数据库` 已覆盖概览，需深度差异化
- 提示词工程→上下文工程演进史（⚠️ 查 `Context Engineering 学习笔记` 重叠度）
