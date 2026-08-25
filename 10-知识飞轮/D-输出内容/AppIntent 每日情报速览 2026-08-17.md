---
type: output
status: draft
created: 2026-08-17
derived_from: "[[AppIntent 每日情报 2026-08-17]]"
method_used: "[[系统级 Intent 路由评估 SOP]]"
source:
  - https://developer.apple.com/wwdc26/guides/ios
  - https://developer.apple.com/videos/play/wwdc2026/347
  - https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web
  - https://developer.android.google.cn/blog/posts/android-17-is-here
  - https://developer.huawei.com/consumer/cn/blog/topic/03220919589498064
  - https://developer.microsoft.com/en-nz/windows/agentic/
importance_score: "★★★★☆"
intent_category: "四平台意图 Registry 来源轴 / Apple Core AI 与多模型路由 / 执行安全确认机制"
tags: [AppIntent, 速览, 2026-08-17]
---

# AppIntent 每日情报速览 2026-08-17

> [!abstract]
> **30 秒速览**：本期四大 OS 官方执行总线**无新增 API**，最高价值落在「**连续第 8 日最高优先待办收口**」——逐平台核验后确认 **Apple / Android / HarmonyOS / Windows 的意图 Registry 层均不记录实体/意图数据的「来源 / 可信度」字段**，来源轴空白从「待查」升级为「架构性空白（confirmed）」。配套补漏：Apple **Core AI 框架 + Dynamic Profiles + 多模型 Foundation Models（Claude/Gemini 经 Language Model 协议）+ Evaluations 框架**；HarmonyOS **A2UI 生成式 UI**；Apple **Secure Enclave 硬件确认锚点**。
> **关键指标**：四平台来源轴 provenance 字段 = 0/4；Apple 副作用轴风险元数据 = 已解（schema 继承 + 棘轮）；端侧 Planner BFCL v4 仍维持「v3 格式合规 / NexusRaven 语义 / v4 多轮」三列并存口径。
> **OS Agent 场景**：做 OS 级意图 Registry 时，副作用分级可照抄 Apple，来源分级须原创；隔离以 Windows Agent Workspace 最完整，确认以 Apple 确定性触发器 + Secure Enclave 硬件根为最强。

## ① Schema 定义与语义路由机制

- **Apple**：`Core AI` 框架把「端侧模型运行时」从 Foundation Models 里抽出来成为**一等公民 OS 框架**（内存安全 Swift API、AOT 编译、零服务器依赖、零 token 成本），意味着**第三方 OS 级 agent 也能自带模型上设备**；`Foundation Models` 现支持**任意语言模型**（Apple FM / Claude / Gemini 经 `Language Model` 协议）+ **Dynamic Profiles**（会话内实时切换模型/工具/instructions），把「端侧→云端升级」从架构决策降级为运行时旋钮。App Intents Schema Protocol 仍靠 `@AppIntent(schema:)` 的**参数签名级对齐**做语义路由（[[Intent Schema Protocol 意图模式规范]]）。
- **Android**：AppFunctions 仍 `@AppFunction` → 编译期 `app_function_v2.xml` → OS AppSearch registry，调用方须持 `EXECUTE_APP_FUNCTIONS`；语义路由由 Gemini 私测承担，无新 API。
- **HarmonyOS**：意图框架「**意图定义 → 意图注册 → 意图执行**」三步 + `InsightIntentEntryExecutor`；**A2UI（生成式 UI）**= 小艺侧据 Skill 返回的结构化数据动态渲染界面，开发者无需为每种展示写页面。ArkAF 三层（意图/Skill/A2A）继续作为生态起量杠杆。
- **Windows**：ODR 注册 MCP Agent connectors + Agent ID（审计身份）；语义路由在 connector 层，无新 API。
- **跨平台端侧 Planner**：评测表维持（FunctionGemma 270M / LFM2.5 家族 / Needle 2 等）；BFCL v4 权重（Agentic 40% / Multi-Turn 30% / Live+NonLive+Hallucination 各 10%）已核实。⚠️ FunctionGemma 270M 第三方 BFCL v4 聚合分 **27.03** 与 Google 自报分项（Simple 61.6 等）口径不直接可比、且来源日期晚于本运行日，**标待补**，不可与官方榜并列。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **确认机制（Confirmation）**：Apple 用**副作用轴风险元数据**（schema 继承 + `authenticationPolicy` 棘轮：只能更严）+ 锁屏鉴权做**确定性触发器**；本期补 **Secure Enclave「Secure intent」硬件锚点**——物理按键（Face ID 双击 / Touch ID）直连 Secure Enclave，**绕过 OS 与 Application Processor、root/内核级软件无法伪造**，是「最强档（带外/不可被模型影响）」的硬件根。Android 把破坏性动作确认**下放 App 自实现**；HarmonyOS 上下文充足时**免二次确认**（信任式）；Windows 靠 Agent Workspace 隔离 + 用户批准查询/动作。
- **隔离（Isolation）**：Windows **Agent Workspace** 最完整——独立会话 + 低权限账号 + ACL + Agent ID 审计；Apple 用锁屏鉴权 + 后台 Neural Engine entitlement 治理；HarmonyOS 用端侧 A2A「隐私数据不出端」；Android 最薄（权限 + App 自确认 + 动态门控）。
- **防注入（XPIA / ADI）**：Session 347 逐字稿补 Foundation Models 侧**确定性护栏**——`.onToolCall`（执行前拦截、抛错即阻断）+ `.historyTransform`（给不可信工具输出加 spotlighting 分隔符 + 脱敏 PII）。**最高价值收口**：从 ADI 视角看，四平台意图 Registry **来源轴全空白（confirmed）**——当前无任何 OS 能因「这条意图的数据来自不可信网页/日历」自动降级或加闸，ADI 防护全靠应用层/治理层（[[数据溯源分级与单调棘轮]]），OS 总线层无对应物。

> [!note] 概念节点双链
> [[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
