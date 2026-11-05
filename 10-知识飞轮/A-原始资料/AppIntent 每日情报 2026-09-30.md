---
date: 2026-09-30
tags: [情报, AppIntents, 系统级意图框架, 端侧Agent, 执行安全, XPIA]
source:
  - https://betawiki.net/index.php?title=Windows_11_2026_Update
  - https://benchlm.ai/benchmarks/bfclV4
  - https://www.getkirin.com/vulnerabilities/beyond-single-model-injection-threat
  - https://urgent.news/2026/09/26/self-replicating-prompt-injections-turn-agent-context-into-an-open
  - https://www.it-boltwise.de?p=2156324/
importance_score: "★★★☆☆"
intent_category: 执行安全 / 跨平台评测 / OS 部署里程碑
---

# AppIntent 每日情报 2026-09-30（系统级 Agent 与 OS 意图框架前沿）

> [!abstract] 30 秒速览
> - **核心突破**：本窗口（2026-09-26 22:07 → 09-30 21:00，约 3.9 天，补 4 日空窗）**四大 OS 官方框架层仍零净新增**——iOS 27.1 无新 Schema / AppFunctions 守 alpha12 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 四支柱无新 Registry API。**唯一 OS 级里程碑 = Windows 11 26H2 于 2026-09-29 GA**（enablement 形态，Ask Copilot + File Explorer 内 Copilot 侧栏落地；Copilot Actions / Agent Workspace 仍 experimental opt-in）。
> - **关键指标**：BFCL v4 BenchLM 09-28 刷新，**BTL-3（Bad Theory Labs，开放权重）88.5% 居首**（大模型，非端侧）；端侧 Planner 仍 MiniCPM5-2B 66.6 / LFM2.5-8B-A1B 49.7 / Needle2 42.6 / FunctionGemma-270m 27.0。
> - **OS Agent 执行安全**：XPIA 新研究两则——① 多智能体注入威胁模型（arXiv:2609.22949，14 向量 / 67% 智能体越权）；② 自复制注入（OpenAI Alignment 2026-09 警告，上下文窗口变开放中继）。SearchLeak（CVE-2026-42824，实 2026-06 披露）在 26H2 Copilot-in-Explorer 语境被重提，附带 Purview 标签门控治理（待官方确认）。

## ① Schema 定义与语义路由机制（四大 OS 框架层）

**Apple（无净新增）**：iOS 27.1 beta 仍未放出（多方口径预期 10 月底~11 月初），无新 `@AppIntent(schema:)` Schema API；iOS 27 已 GA 的 App Intents 2.0 / App Schemas / `IndexedEntity` / `Domains` / `OwnershipProvidingEntity` 不变。SiriKit 已正式 deprecated，迁移窗口 2~3 年。

**Android（无净新增）**：`developer.android.google.cn/jetpack/androidx/versions` 确认 `appfunctions` 守 `1.0.0-alpha12`（2026-09-23）、`a2ui` 守 `1.0.0-alpha01`（同日常），**无 alpha13 / alpha02**。A2UI 开源 spec 仓库（a2ui-project/a2ui）9-28~9-30 活跃（protocol v0.9 dart stub / conformance 用例），属跨平台协议演进，非 Jetpack 发行。

**HarmonyOS（无净新增）**：HC2026（9-17~21）内容已覆盖，09-26→09-30 无新框架/API。Intents Kit（Want）/ 元服务（installationFree）/ ArkAF 2.0（意图/Skills/A2A 三层）/ A2UI 不变。

**Windows（部署里程碑，非 API 新增）**：**Windows 11 26H2 于 2026-09-29 GA**（BetaWiki：`released for general availability on 29 September 2026`；build 26300.9550 Release Preview / 26340.9577 Experimental；Germanium 代码基，enablement package 形态）。agentic 四支柱（Ask Copilot / Agent Launchers / ODR / Agent Workspace）+ 权限治理（三档 consent / 容器隔离 / 代码签名吊销）自 09-13 以来**无新 Registry API**。26H2 新 surface = **Ask Copilot**（任务栏搜索替代，opt-in）+ **File Explorer 内 Copilot 侧栏**（dockable，直接对话文件夹/文件）；二者仍受 `Settings > System > AI components > Agent tools > Experimental agentic features` 同一 opt-in 管控，Copilot Actions 等执行总线能力未变。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**26H2 GA 不含新执行总线安全 API**：既有四原则（distinct agent accounts / limited privileges / operational trust via signing / privacy-preserving）不变；Copilot Actions 默认关、Agent 独立标准账户、Agent Workspace 运行时隔离、敏感步骤 step-up 确认不变。

**XPIA 新研究①（★6/10，~09-22 入库）多智能体注入威胁模型**：arXiv:2609.22949v1 指出多智能体系统经三机制放大单模型风险——inter-agent message passing（不可见注入信道）/ shared tool access（跨边界提权）/ trust propagation（感染上游 orchestrator）。枚举 **14 攻击向量**（直接 3 / 间接 4 / inter-agent 4 / cascading 3）；6-智能体生产代表系统实测 **67% 至少一种 scope violation**（即便有 system-prompt 级 guardrail），间接注入经 tool output **43% 成功**。四架构防御把总注入成功率 **31.2% → 4.2%**：消息签名+来源追踪（inter-agent ↓91%）/ 边界 I/O 净化（间接 ↓78%）/ 按角色权限定界 tool access（提权归零）/ inter-agent 通信异常检测（cascading 84% 捕获）。→ 与 A2A / HarmonyOS A2A / Android AppFunctions agent skill 多智能体编排直接映射，补本库 XPIA 威胁模型**第⑨支（多智能体编排注入）**。

**XPIA 新研究②（★6/10，09-26 在窗，低置信来源）自复制注入**：OpenAI Alignment 团队 2026-09 警告，经 GPT-Red 红队在 GPT-5.4-mini / GPT-5.5 + 真实 connector 验证。根因 = 把上下文窗口当**扁平可信缓冲** + 给模型无限制写工具（send_email / post_slack / write_file / git_push）。注入经 email connector / dev repo / Slack 三跳**自我复制**（如把注入原文逐字 append 到 outbound 消息），类早期网络蠕虫。四缓解：ingest/dispatch 信道严格分离 / 写工具格式强制 / 上下文持久化视为不可信边界 / 速率限制 + 出口过滤。→ 续 09-17 SIR 自改进 + 09-16 权重级持久化，构成 XPIA 演进链**第五环（自我复制）**。⚠️ 来源 urgent.news 机器撰写自 Dev.to，具体数字待一手复核。

**XPIA 重提（★5/10，09-30，实为旧 CVE 重提）SearchLeak + Purview 标签治理**：SearchLeak = Microsoft 365 Copilot Enterprise Search 三链漏洞（**CVE-2026-42824**，2026-06-15 Varonis 披露，Microsoft 后端已缓解，CVSS 有争议 Microsoft 6.5 / NVD 更高），parameter-to-prompt injection + 渲染 race + Bing SSRF 经 image endpoint 外泄邮件/日历/MFA 码。09-30 it-boltwise 在「26H2 Copilot 入 Explorer + 隐私控制」语境重提，并提 **Microsoft Purview 标签门控**（管理员可禁止 Copilot 访问带特定 label 的 Word/Excel/PPT/Outlook 文档）作为治理手段——该治理特性为 conditional（「sollen」），**待官方确认**。→ 含义：企业 Copilot 把「外部输入 + 内部数据访问」结合，是 XPIA 在 M365 侧的具象；Purview 标签把 AI 能力绑定**数据分级**而非仅用户角色，是可复用治理启发。

## 诚实标注 / 待办

- Windows 26H2 精确 GA 日（09-29）来自 BetaWiki 第三方维基；agentic 入口是否仍受 `Experimental agentic features` 同一 opt-in 管控待 Microsoft 官方 blog 逐字复核。
- 多智能体注入（arXiv:2609.22949）为 arXiv 预印本，67%/43%/4.2% 等为论文自报数字，待一手复核。
- 自复制注入来自 urgent.news（机器撰写自 Dev.to），OpenAI Alignment 原文 / GPT-Red 评测协议待补；具体百分比不写入精确值。
- SearchLeak 为 2026-06 已披露 + 后端已缓解，本次仅为 09-30 语境重提；Purview 标签治理为条件性表述，待 learn.microsoft.com 确认。
- BFCL v4 88.5% 的 BTL-3 为**大模型开放权重**（非端侧）；端侧 Planner 分数仍为 Berkeley 榜/模型卡口径，与 MLPerf gate 不可混算。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / iOS 27.1 正式 beta Schema / 多智能体注入一手论文 / 自复制注入 OpenAI 原文。

> [!note] 概念节点双链
> - [[Intent Schema Protocol 意图模式规范]]
> - [[Intent Router 语义路由]]
> - [[Function Calling 端侧工具调用]]
> - [[Confirmation UI 安全机制]]
> - [[Atomic Service 元服务]]
> - [[Agent Workspace 隔离执行]]
> - [[A2A 端侧智能体协议]]
> - [[XPIA 跨提示注入]]
