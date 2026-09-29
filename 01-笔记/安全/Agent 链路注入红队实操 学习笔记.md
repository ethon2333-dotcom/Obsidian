---
title: Agent 链路注入红队实操 学习笔记
tags: [广度种子, 知识拓展Loop, Agent安全, 红队, 提示注入, 安全]
created: 2026-09-21
source: WebSearch/WebFetch 核实（AgentDojo inspect 实现、InjecAgent/ToolEmu 论文、Zylos/Invariant/PromptGuardrails 等公开资料），含待核实项
---

> 心智模型一句话：链路注入不是"能不能被攻破"的学术问题，而是"失守率多少、用什么工具能拦、在哪一层拦"的工程问题——本篇只摆实测数据与可落地防御，深度留白给 Ethon。

## 与已覆盖笔记的差异

本篇聚焦**链路注入的实操数据与防御落地**（失守率数字、工具投毒扫描、多 Agent 传播阻断、可落地防御 playbook），区别于 [[AI 评测红队 Agent 链路注入 学习笔记]]（概念/攻防框架广度）、[[AI Agent 沙箱与安全执行环境 学习笔记]]（隔离技术）、[[AI 评测红队与对齐 学习笔记]]（模型层对齐）。一句话：**那三篇讲"是什么/为什么/怎么隔离"，本篇讲"实战掉多少血、怎么止血"。**

## 广度覆盖（点到为止，BREADTH > DEPTH）

### 1. 定义 / 是什么

| 概念 | 一句话 | 落地含义 |
|---|---|---|
| 链路注入（Agentic PI） | 攻击指令藏进 Agent 会读取的检索内容/工具返回/外部网页/MCP 描述，而非用户 prompt | 授权无误但语义被劫持 |
| 工具投毒（Tool Poisoning） | 恶意指令藏在 MCP 工具描述字段，模型读即信、信即执行 | 「工具文档即代码」，一次注册即长期受害 |
| 多 Agent 传播 | 注入沿 Agent 间消息/共享记忆横向扩散 | 单点失守→指数级感染 |

### 2. 分类与主流方案（攻击实测 vs 防御实测 vs 评测基准）

| 类别 | 代表基准 / 工具 / 方案 | 要点 |
|---|---|---|
| **评测基准（攻击实测）** | AgentDojo（ETH+Invariant, NeurIPS'24）、InjecAgent（UIUC+Stanford, ACL'24）、ToolEmu（ICLR'24）、OfficeBench、Agent-SafetyBench、TRAP'25、Agent Security Bench/ASB（ICLR'25）、TAMAS'25 | 量化失守率，见下节 |
| **工具投毒检测** | MCP-Scan（Invariant, 2025-04，现 Snyk Agent Scan）、工具 pinning/hash 校验、cross-origin shadowing 检测 | 把「工具描述」当可执行代码扫描（见 [[工具调用安全 学习笔记]] 的凭据托管呼应） |
| **多 Agent 传播阻断** | Agent Identity 签名消息、Trust Tiers、隔离沙箱、safety/referee agent、provenance ledger、graph 异常检测 | 限制横向移动（lateral movement） |
| **防御实测（模型层）** | StruQ（BAIR, 2025-04）、SecAlign（DPO 偏好优化）、Instruction Hierarchy（OpenAI, 2024-04）、CaMeL（DeepMind, 2025-03） | 见下节 |
| **防御实测（架构/护栏层）** | 4 层护栏架构、输出校验、权限最小化、人类确认 | 见 [[AI Agent 沙箱与安全执行环境 学习笔记]]、[[Confirmation UI 分级与产品责任边界]] |

### 3. 2025-2026 关键进展（含可引用失守率，标待核实）

| 来源 | 关键数据 | 口径/待核实 |
|---|---|---|
| **AgentDojo（inspect 实现，2025-06）** | Claude 3.7 Sonnet(20250219) 良性效用 83.3%、UUA 71.9%、**目标 ASR 8.5%**；GPT-4o(20240513) **ASR 31.4%** | inspect 复现口径，非原论文；具体版本 ASR 待核实 |
| **AgentDojo（原论文）** | 最佳 agent 被攻破 **<25%**；检测器防御降到 ~8%，工具过滤 ~7.5%；**无攻击时模型仅完成 <66% 良性任务** | 原论文数据，已核实方向；精确数值待查原表 |
| **AGENTVIGIL（EMNLP'25）** | 对 o3-mini **71%**、GPT-4o **70%** 攻击成功率（AgentDojo/VWA-adv） | 自动化黑盒攻击，近乎翻倍于手写基线；待核实复现 |
| **InjecAgent** | ReAct-GPT-4 被攻破 **24%**，加「hacking prompt」强化后近翻倍 ≈**47%**；微调 GPT-4 降到 7.1%；Llama-2-70B >**80%** | 1054 用例/17 用户工具/62 攻击者工具/30 个 LLM agent；数字来自论文摘要，已核实 |
| **ToolEmu** | 识别的失败中 **68.8%** 为真实世界有效失败；最安全 LM agent 仍 **23.9%** 用例失败 | 36 高风险工具/144 用例/9 类风险；已核实 |
| **TRAP 基准（2025）** | 6 模型/3780 次运行，平均成功率 **25%**，DeepSeek-R1 达 **43%** | 媒体二次引用（Zylos），待查原始论文 |
| **Agent Security Bench/ASB（ICLR'25）** | 27 攻防方法/~90K 用例，**最高 ASR 84.30%** | 综合多 Agent 基准，已核实方向 |
| **OpenHands（Invariant 2025）** | 无护栏时 100 例中 **67 例**执行有害行为 | 厂商研究，待独立验证 |
| **防御实测（StruQ/SecAlign）** | StruQ 无优化攻击 ASR≈**0%**、优化攻击≈**45%**（效用降 ~4.5%）；SecAlign 优化攻击≈**8%**、对自适应攻击近 0% | BAIR 实验室数据；2025-07 有论文用架构感知攻击绕过 SecAlign，待核实细节 |
| **CaMeL（DeepMind, 2025-03）** | 挡下 **67%** AgentDojo 攻击、GPT-4o 配置近零；代价 2.7–2.8x token | 双 LLM + 信息流控制，形式化保证方向；代价与可落地性待核实 |
| **OWASP Agentic Top 10（ASI01–10）** | 2025-12 发布，首个 agent 风险基线；ASI01 目标劫持/ASI04 供应链/ASI05 意外代码执行直接相关 | 发布月份多记 2025-12，个别媒体写 2026 初，待官方确认 |
| **MCP 工具投毒检测** | Invariant MCP-Scan（2025-04）扫描工具描述/rug pull/cross-origin shadowing；Snyk 2025-06 收购 Invariant → Snyk Agent Scan；ThoughtWorks Radar Vol.33 列 Assess | 检测覆盖率/误报率未公开，待核实 |

> 一句话收口：**所有基准都指向同一结论——防御有价值（约减半失守率），但没有任何方案把残余风险降到 0**；基准 ASR 是「昨天攻击」的下界，不是「安全百分比」。

### 4. 可落地防御 Playbook（广度罗列）

| 防御层 | 做法 | 代表 |
|---|---|---|
| 输入隔离 | 结构化查询 / delimiter + spotlighting，区分可信/不可信内容 | StruQ、SecAlign、Azure Prompt Shields |
| 工具投毒检测（供应链） | 注册前扫描 MCP 工具描述、hash pinning 防 rug pull、cross-origin 检测 | MCP-Scan / Snyk Agent Scan（见 [[工具调用安全 学习笔记]]） |
| 多 Agent 传播阻断 | Agent 身份签名消息、信任分级（Orchestrator>Sub>Tool）、工具作用域隔离、safety/referee agent  oversee | 架构层（见 [[AI 评测红队 Agent 链路注入 学习笔记]]） |
| 4 层护栏 | ①执行前输入扫描 ②工具输出当敌意扫描 ③执行前动作校验（对照原始意图） ④运行时行为监控（intent drift/渗出信号） | PromptGuardrails 4-layer（媒体/厂商框架） |
| 权限最小化 | 最小 scope OAuth、任务级回收、默认只读 | OWASP ASI03；见 [[AI Agent 沙箱与安全执行环境 学习笔记]] |
| 输出校验 | 动作级策略校验、形式化验证、egress 过滤（密文/图像外泄通道） | Bedrock Automated Reasoning（GA 2025-08，待核实）；egress 过滤实践 |
| 人类确认 | L1/L2 分级确认不可逆动作 | [[Confirmation UI 分级与产品责任边界]] |
| 提示护栏库 | 实时 PI 检测/拦截（I/O 双端） | Lakera（98%+ 检测/<50ms，厂商口径待核实）、NVIDIA NeMo Guardrails、Meta Prompt Guard 2、Rebuff（2025-05 归档） |

### 5. 代表产品 / 玩家

| 类别 | 代表 | 说明 |
|---|---|---|
| 工具投毒扫描 | Invariant MCP-Scan → Snyk Agent Scan | 开源 CLI，CI 可接入；Snyk 2025-06 收购 |
| 实时 PI 护栏 | Lakera（2025 被 Check Point 收购）、Protect AI、Cisco AI Defense | 应用层分类器，对抗性样本有绕过风险 |
| 框架护栏 | LangChain/LangGraph、NVIDIA NeMo Guardrails、Meta Prompt Guard 2 | 框架内置 I/O 护栏 |
| 形式化/架构防御 | DeepMind CaMeL、IBM/ETH/Google/Microsoft Design Patterns | 把安全做成结构属性而非过滤器 |
| 多 Agent 治理 | 运行时可观测（Explorer/Gateway）、Agent 身份 DID、kill-switch | 见 [[AI 评测红队与对齐 学习笔记]] 治理侧 |

## 深度盲区（待 Ethon 补）

- [ ] AgentDojo 各模型 2026 版 ASR 趋势：Claude 3.7/Opus 4、GPT-5 系列、Gemini 的失守率排行与「合成鲁棒 vs 真实红队」落差？
- [ ] 工具投毒在「端侧 OS 托管工具（如 Android AppFunctions）」下是否成立？OS 级 Registry 能否天然挡住描述投毒？（连 [[工具调用安全 学习笔记]] 与 [[Android AppFunctions 设备侧意图 2026]]）
- [ ] 多 Agent 传播有没有可量化的「感染率/传播速度」基准，能像 ASB 84.30% 那样横向对比？
- [ ] StruQ/SecAlign 这类微调防御在**端侧小模型（on-device）**上效用是否同样成立，还是仅云侧大模型有效？
- [ ] 「4 层护栏」在真实生产检索量下的误拦率（FP）与延迟成本是多少？厂商只报拦截率不报 FP。
- [ ] CaMeL 的 2.7–2.8x token 代价，在长任务/多工具 Agent 里是否经济可行？有无轻量替代？
- [ ] MCP rug pull（注册后篡改描述）在「一次性审批」模型下的责任归属——用户、客户端、registry 各担多少？（连 [[工具调用安全 学习笔记]]）
- [ ] 「输出校验 + egress 过滤」能否挡住 Markdown 图像外泄这类「响应后通道」？现有方案覆盖到哪一层？

## 库内关联

- 概念/攻防框架广度：[[AI 评测红队 Agent 链路注入 学习笔记]]
- 隔离技术：[[AI Agent 沙箱与安全执行环境 学习笔记]]
- 模型层对齐/红队：[[AI 评测红队与对齐 学习笔记]]
- 工具鉴权/供应链：[[工具调用安全 学习笔记]]
- 确认分级/责任边界：[[Confirmation UI 分级与产品责任边界]]
- 执行安全总览（PM 视角）：[[Agent 执行安全（PM视角）]]

## 附：来源清单

- AgentDojo inspect 实现与结果：https://github.com/PranshuSrivastava/inspect_evals （Claude 3.7 Sonnet 8.5% / GPT-4o 31.4% ASR，2025-06 复现）
- AgentDojo 原论文/官网：arXiv:2406.13352 / https://agentdojo.spylab.ai/
- InjecAgent 论文：arXiv:2403.02691（UIUC+Stanford, ACL'24 Findings），1054 用例，ReAct-GPT-4 24%→47%
- ToolEmu 论文：arXiv:2309.15817（ICLR'24），68.8% 失败为真实、最安全 agent 23.9% 失败
- AGENTVIGIL：arXiv/EMNLP 2025 Findings（DOI 10.18653/v1/2025.findings-emnlp.1258），o3-mini 71% / GPT-4o 70%
- CaMeL（DeepMind "Defeating Prompt Injections by Design"）：arXiv:2503.18813（2025-03）
- StruQ/SecAlign（BAIR）：StruQ USENIX'25、SecAlign CCS'25；Instruction Hierarchy arXiv:2404.13208
- MCP-Scan / 工具投毒：Invariant Labs（2025-04）、Snyk 收购（2025-06）、Stytch 深度文、ThoughtWorks Radar Vol.33
- 多 Agent 安全：Agent Smith（ICML'24）、Agent Security Bench/ASB（ICLR'25, 84.30% ASR）、OpenHands 67/100（Invariant 2025）
- 4 层护栏框架与防御综述：PromptGuardrails Enterprise Guide、Zylos Research（2026-06）、arXiv:2510.06445（Agentic Security Survey, 2025）

## ⚠️ 待核实清单

- AgentDojo 中 Claude 3.7 Sonnet 8.5% ASR 的 inspect 复现口径与原论文差异（原论文最佳 agent <25% 为另一口径）。
- AGENTVIGIL 71%/70% 为自动化黑盒攻击结果，泛化到生产环境需复现验证。
- InjecAgent「强化后≈47%」的原始表述为「nearly doubling」24%→约 47%，精确值待查原表。
- TRAP 基准 25% 平均 / DeepSeek-R1 43% 来自 Zylos 媒体二次引用，未查原始论文。
- ASB 84.30% 最高 ASR 为综合多 Agent 基准极值，具体模型/配置待查。
- StruQ/SecAlign 效用降幅（4.5%）与「2025-07 架构感知攻击绕过 SecAlign」的具体论文与可复现性待核实。
- CaMeL 67% 防御率与 2.7–2.8x token 代价为 DeepMind 论文口径，生产经济性与可落地边界待核实。
- OWASP Agentic Top 10 发布月份（2025-12 vs 2026 初）待官方公告确认。
- Lakera「98%+ 检测 / <50ms」、Bedrock Automated Reasoning「准确率口径」均为厂商口径，未独立验证。
- MCP-Scan 检测覆盖率/误报率未公开披露，CI 接入的实际 FP 成本待核实。
- Rebuff 2025-05 归档为媒体陈述，具体归档原因与替代方案待核实。
- OfficeBench（GPT-4o 47% / 人 93.3%）数据引自既有笔记，本轮未单独复核原始论文，标待核实。

#标签/广度种子 #标签/Agent安全 #标签/红队 #标签/提示注入 #标签/安全
