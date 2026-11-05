---
date: 2026-10-05
tags:
  - AppIntent
  - 每日情报
  - Android
  - AppFunctions
  - AndroidContextEngine
  - 端侧意图路由
source:
  - https://byteiota.com/android-dev-summit-2026-developer-guide
  - https://dev.to/artemgarazha/android-18-is-turning-into-an-intelligence-system-im-not-sure-whether-to-be-excited-or-worried-28d0
  - https://gadgets.beebom.com/news/google-teases-android-18-ahead-of-dev-summit-2026
  - https://www.streamingmeme.com/articles/google-teases-android-18-graphics-features-for-october-developer-summit
  - https://developer.android.com/ai/appfunctions
  - https://test.aiagentstore.ai/ai-agent-news/this-week
importance_score: "★★★☆☆（6/10）"
intent_category: "端侧意图路由 / Android 设备侧MCP proactive caller"
---

# AppIntent 每日情报 2026-10-05（窗口 2026-10-03 → 10-05，约 48h）

> [!abstract] 30 秒速览
> **核心突破（唯一 OS 级真增量，★6/10）**：Android 18（借 Android Dev Summit 2026 / 10-28~29 公告摆上台面）引入 **Android Context Engine**——一个追踪用户意图 / 屏幕上下文 / 应用任务的后台服务，**在用户开口前就主动调用 AppFunctions**。这是 AppFunctions 继 Gemini、第三方 `EXECUTE_APP_FUNCTIONS` 授权 agent 之后的**第三类（OS 原生 proactive）调用方**。
> **关键指标 / 框架信号**：Android 18 被 Google 正式定位为「Intelligence System」；Gemini Nano v3 驻留内存（12GB RAM 下限）；旧 Google Assistant 组件 deprecation，Gemini 成系统服务底层。
> **OS Agent 场景**：手机从「被动响应用户指令」转为「主动观测上下文并提议/执行」——与 Apple 主动式 App Intents 分发、Windows Copilot Vision、鸿蒙小艺导航条「复制即触发」收敛为四平台**主动式意图路由**的 Android 落点。
> **其余三平台 + BFCL + XPIA 本窗口零净新增**（详见「已复核·无净新增」），与前 ~30 轮「OS 框架不日更」结论连续一致。

## ① Schema 定义与语义路由机制

- **AppFunctions caller 集扩张**：此前 caller 集 = {Gemini, 持 `EXECUTE_APP_FUNCTIONS` 的第三方 agent}；现加入 **Android Context Engine（OS 原生的 proactive 编排者）**。
- **Context Engine 机制**：后台服务持续观测 user intent / screen context / app tasks，**proactively** 发起跨 App 编排。例：notes app 看到购物清单 → 主动提议加购物车；检测到下班发伴侣消息 → 主动提议自动化。它不是 chatbot 响应 prompt，而是「OS 级 agent 看着并行动」。
- **Android 18 = Intelligence System 框架**：Gemini Nano v3 作为 resident on-device model 与常驻 App 并列驻内存（12GB RAM floor）；应用通过 `@AppFunction` + `@AppFunctionSerializable` 声明能力 → KSP 生成 XML schema → OS 索引 → agent 经 `AppFunctionManager` 发现执行（机制不变，仅 caller 多出 Context Engine）。
- **DMA 锚点 consolidation**：欧盟 2026-07-16 绑定规格决定，11 项 Android AI 能力（含 AppFunctions）须于 **Android 18 前、2027-08-01 前**向第三方认证助手开放；并发 hotword 检测推至 Android 19（2028-08-01）。已录于 [[AppFunctions 跨助手可发现性与 DMA 强制开放 2026]]，本次补「deadline 锚定 Android 18」具体日期。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **权限仍 blanket grant**：`EXECUTE_APP_FUNCTIONS` 是「一次性授权、非 per-function」。在 **proactive-before-ask** 语境下，Context Engine 可能基于上下文发起调用而用户未显式授权该次动作，**确认边界更模糊**——这是 Android 路线（确认下放 App）在主动式场景下的风险放大。
- **与 Microsoft Taxonomy v2.0 consent-architecture hardening 直接呼应**（该文档实为 2026-04/06，非本窗口，见校正段）：deterministic invocation（agent 不应自己决定何时弹确认）、compound-action decomposition（拆解多步动作逐子动作审批）、semantic summarization of approval（不要照念 agent 自身的动作描述，要从底层 tool call 摘要以防 description laundering）、tiered approval（按可逆性/波及面分级）。→ 映射 [[确认机制]] [[Confirmation UI 安全机制]]。
- **隔离 / 防注入**：AppFunctions 执行仍在 App 进程内（端侧 MCP）；但官方「system agents may process queries on server」依旧成立。Context Engine 主动抓取更多 notes/消息/屏幕上下文，**反而扩大 XPIA 攻击面**——它读取的内容即潜在注入载体（如一份夹带指令的购物清单）。→ [[XPIA 跨提示注入]]。

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27.1 首个 beta 仍未发布（Macworld 10-05 确认「None, but iOS 27.1 beta should be available soon」），无新 `@AppIntent(schema:)` Schema API；macOS Full Disk Access 收紧（Apple FDA）于 10-04 周报（test.aiagentstore.ai「Week of Oct 4」）被二次报道，属 10-03 已收录项复述，**无新事实**。
- **HarmonyOS**：DevEco Code 上线 + 1200+ 系统能力 Skill 化（意图即服务，pingwest）为开发工具/生态叙述强化，**无新 OS API**；7.0 Beta1 的 On-Device A2A / 内核快启为既有内容（besthub.dev）。
- **Windows**：Hey Copilot / Copilot Actions / Agent Workspace 于 10-04~05 多家媒体复述（techbloat / positioniseverything / geekchamp），均属已收录项，**无新 Registry API**；「Microsoft turning Windows into agentic OS」为题的均为概念/营销文，非框架 API 变更。
- **跨平台 BFCL v4**：端侧 Planner **无新入榜**；FunctionGemma-270m 27.03 / Qwen3-0.6B 54.08 维持（HF LittleLamb 卡引 Google model card 09-04 数据）；无新端侧模型评测。
- **XPIA**：窗口内无新 CVE/研究突破。`CVE-2026-104120`（mcp-server-fetch SSRF）属 MCP 工具链、非四 OS 框架执行总线，丢弃。

## 诚实校正（库内已知参考，非本窗口新）

- **Microsoft agentic security 文档版本校正**：本库 09-16 跑记「Windows agentic security 文档 2025-12-05 后再无更新」为**误判**——实际 Microsoft AI Red Team 已于 **2026-04（PDF 标注）/ 2026-06-04（Security Blog 发布）** 推出 **Taxonomy v2.0**，新增七类失败模式 + 四项缓解族（含上述 consent-architecture hardening、supply-chain SBOM for agents、zero-trust inter-agent、XPIA 内容信任标记）。该文档不在本 24h 窗口，作库内权威参考，相关映射见 [[Confirmation UI 安全机制]] [[隔离执行]] [[XPIA 跨提示注入]]。后续跑勿将其当「新发布」重复收录。

## 诚实标注 / 待补

- Android 18 仍 Canary / 未 GA；Android Context Engine 为 Dev Summit 公告 + 第三方解读（dev.to / byteiota / beebom / streamingmeme），**非 Android 开发者文档逐字 API**。
- Context Engine 具体 API 名、是否独立系统 service、与 `AppFunctionManager` 调用关系、是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束，**待 developer.android.com/ai/appfunctions 官方文档确认**。
- Dev Summit 为 2026-10-28 召开、非已发生发布；「production readiness for Android 18」为 summit session 预期信号，非 GA 承诺。
- 沿用：Per-Intent Privacy Manifest 官方逐字 / iOS 27.1 正式 beta Schema / Watch OS 26 / AppFunctions alpha13 / A2UI alpha02 / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / NowSecure / AgentAntibody / Chrome Origin Sets。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
