---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags:
  - AppIntent
  - Apple
  - SchemaProtocol
---

# Apple AppIntents Schema Protocol（2026）

> 概念基础见 [[Apple Intelligence 与 App Intents]]（Schemas / Entities / View API 三组件模型与跨应用案例）。本文聚焦 **WWDC26 新增的 Schema Protocol API 与端侧路由细节**，不重复概念铺垫。

## 一句话定义

Apple 在 iOS 26/27 将 App Intents 从「自定义 Action」升级为 **系统级 Schema Protocol**：开发者用 `@AppIntent(schema:)` 把能力对齐到 Apple 预定义的系统 Schema（messages / photos / calendar / audio…），Siri 由此获得跨 App 语言理解、免训练短语与端侧语义路由。

## 为什么重要

- **免训练短语**：对齐系统 Schema 后，Siri 不针对具体 App 训练即可理解「把这首歌加到播放列表」，跨 App 泛化。
- **语义级匹配**：用 `IndexedEntity` + `indexingKey` 写入 Spotlight 语义索引，做「含义级」匹配而非字符串匹配。
- **端侧闭环**：小模型 Planner + Schema 微调即可本地完成意图路由，避免每请求上云。

## 适用边界

- 仅覆盖 Apple 生态（iOS / iPadOS / macOS）；跨平台需各自适配（见 [[Intent Schema Protocol 意图模式规范]]）。
- 高危动作（支付、删除、发信）仍由系统级 Confirmation UI 拦截，开发者无法绕过（见 [[Confirmation UI 安全机制]]）。

## 证据与例子

```swift
@AppIntent(schema: .audio.addToPlaylist)        // 对齐系统 audio Schema
struct AddToPlaylistIntent { ... }

@AppEntity(schema: .messages.message)            // 实体对齐 messages Schema
struct MessageEntity { ... }

@AppEnum(schema: .photos.assetType)              // 枚举对齐 photos Schema
enum AssetType { ... }
```

- **参数槽补全**：`$label.requestValue("想加到哪个播放列表？")` 在 Intent 执行中反向追问缺失槽位（Parameter Slot-filling）。
- **意图捐赠**：`IntentDonationManager.donate(intent:result:)` 把参数与结果回捐系统，让 Siri 学习用户偏好、降低后续追问。
- **归属判定**：`OwnershipProvidingEntity`（EntityOwnership `.shared` / `.public` / `.unknown`）区分实体归属，Confirmation UI 据此差异化提示。
- **Agentic Macro**：Shortcuts 2.0 借 MCP 让 Slack / Notion 等把 Internal Actions 暴露给 Siri Intelligence，App 退化为 headless 服务；`isAssistantOnly` 为过渡开关；Passwords App 可代理执行改密等系统动作。

## 2026-07 增补（iOS 27 / WWDC26，来源 [[OS PM 近一月情报简报 2026-07-31]]）

- **System Orchestrator（系统编排者）**：跨 App 动作统一由系统编排者路由，**App 之间不直接互相驱动**——这是刻意为隐私与安全的设计（详见 [[System Orchestrator 系统编排]]）。
- **前台/后台速率限制**：on-device 模型前台**无速率限制**，后台高负载时限流、无固定预算数字。
- **SiriKit 正式弃用**：App Intents 成 Siri 强制集成面，约 2~3 年迁移窗口；早期伙伴含 Uber / Amazon / YouTube / WhatsApp / AllTrails。
- **新框架族**：Foundation Models（原生 Swift API，可切换 Apple/Claude/Gemini）、Core AI（自带模型上设备）、Evaluations、App Intents Testing。
- **路由链路**：App Intents 与 **System Orchestrator + Spotlight 语义索引 + App Toolbox** 协同跨 App 路由。
- **新增 Schema 类型**：`ValueRepresentation` / `RelevantEntities` / `EntityCollection` / `SyncableEntity` / `LongRunningIntent` / `ExecutionTargets` 等（细节以官方文档为准）。

## 2026-07-31 增补（iOS 27 第三方 App Intents 首次实测生效，来源 [[AppIntent 每日情报 2026-07-31]]）

- **🔑 首个野外实测证据（2026-07-06，iOS 27 developer beta 3）**：Siri AI 已能从**第三方 App 拉取实时数据**（如电动车电量），**查询前弹出权限确认**再作答。开发者实测 **Tessie**、**Ford 官方 App** 可用，而 **Tesla 官方 App 反而不行** —— 说明可用性取决于**各家 App Intents 适配质量**，而非 Apple 白名单；同时也印证「支持仍不稳定、处于 beta 阶段」。
- **时间线**：WWDC26（6-08/09）Siri AI 发布 + **SiriKit 正式弃用**（2~3 年迁移窗口）→ 开发者 Beta 走**候补名单**（Settings → Apple Intelligence opt-in，放行约 **4~48 小时**）→ **7-13 公测**（与 dev beta 3 同一构建）→ **9-14 正式发布**。开发者 Beta 需 iPhone 15 Pro / 16 / 17；iOS 27 本身支持 iPhone 11 起。
- **区域差异**：**欧盟因 DMA，iOS 27 / iPadOS 27 的 Siri AI 延迟上线**。
- **成本侧（影响端云路由决策）**：App Store 小企业计划成员（**累计下载 < 200 万**）可在 **Private Cloud Compute 上以 $0 云 API 费**调用下一代 Foundation Models —— 对小团队而言「上云推理」的边际成本被抹平，会改变本地优先/云端升级的权衡（对照 [[Function Calling 端侧工具调用]]）。
- **模型侧**：Apple 采「端侧模型 + 更大模型处理复杂请求」的混合方案，多方报道称由**定制版 Google Gemini** 承担较重推理；Apple 未明确拆分口径（**待补**）。对开发者而言接口不变，仍是 App Intents。
- **边界重申（2026 开发者文档）**：App 须经 App Intents **主动声明**可被 Apple Intelligence / Siri 调用的动作与数据；**应用界面中的私有内容不会自动向系统开放**；敏感或破坏性操作可要求用户再次确认（见 [[Confirmation UI 安全机制]]）。

## 可复用启发

- 平台方应通过「声明式宏 + AI 辅助生成」把 App 接入成本压到极低（Apple `isAssistantOnly` 过渡）。
- 先固化统一的 Schema / Tool 描述规范（实体类型、Parameter Slot、EntityOwnership），这是跨 App 可被发现与编排的前提（见 [[Intent Schema Protocol 意图模式规范]]）。
- **Schema 的壁垒不在「动作名」而在「参数签名」**：Apple 把每个 domain schema 的参数表写死（见下「一手来源」），等于用类型系统锁定语义。做 OS 级意图规范应**先定参数签名再定动作名**，反过来一定失控。
- **内容曝光要设三条正交路径**（Spotlight 可搜 / 交互捐献学规律 / RelevantEntities 声明情境相关），比只给一个「注册接口」更能让系统在不同时机找到你——本质是把分发权部分还给开发者。

## 2026-08-01 增补：WWDC26 Session 345 代码级细节补齐（来源 [[AppIntent 每日情报 2026-08-01]]）

> 此前只记录了 API 名称，本次补齐**用法、机制与性能语义**。⚠️ Apple 原视频只说「2027 年的新版本」，**未给具体系统版本号（待补）**；Session 345 **无新增用户确认 API**，仅涉 GPU 后台授权与 Widget 只读数据设计。

| API | 解决什么问题 | 用法要点 |
|---|---|---|
| `ValueRepresentation` | Transferable 只能传有文件格式的数据，无法跨 App 传无格式结构化类型（如地标坐标给 Maps） | 与 Transferable 表示并列添加；可用闭包导出 `PlaceDescriptor`（GeoToolbox），实体已有该 `@Property` 则直接用 key path |
| `RelevantEntities` | 全新内容没被搜过、也无交互可捐献，系统无从推荐 | 确定实体 → 建上下文（如 `AppEntityContext.audio(.workout(activityType: .running))`）→ `updateEntities` 注册；`removeAllEntities(for:)` 移除 |
| `EntityCollection` | Intent 执行前系统会解析每一个实体（调查询、填全属性），批量场景灾难 | 参数类型从 `[PhotoEntity]` 改为 `EntityCollection<PhotoEntity>`，**只传标识符**给 `perform`；官方演示「查找并标记 1000 张照片」改后近乎瞬时（⚠️ 原视频未给具体秒数） |
| `SyncableEntity` | 各设备本地生成 ID 不同，Siri 跨设备续接找不到同一实体 | ID 已稳定（服务器 UUID / CloudKit record ID）则只需加协议；本地 ID 用 `SyncableEntityIdentifier<Local, Stable>` 配对 |
| `@UnionValue` | 一个参数需代表「多选一」不同类型 | 宏定义枚举，各 case 包装不同实体类型；提供 `typeDisplayRepresentation` 与 `caseDisplayRepresentations`；宏自动生成选择器 |
| `LongRunningIntent` + `CancellableIntent` | Intent 默认 30 秒上限，大文件上传做不完 | `performBackgroundTask { }` 包裹，循环内 `Task.checkCancellation()`；进度自动以 **Live Activity** 呈现；`onCancel` 含用户停止 / 系统超时 / 资源回收原因；支持后台 GPU（需授权添加 GPU 访问） |
| `ExecutionTargets` | 多进程（主 App / AppIntents 扩展 / Widget 扩展）写同一存储冲突 | `static var allowedExecutionTargets: ExecutionTargets`，取值 `.main` / `.appIntentsExtension` / `.widgetKitExtension` 或数组；**写操作指定 `.main`**，Widget 给只读 |
| 原生参数类型扩展 | 免自定义 | 新增 `Duration`（原生时间选择器）、`PersonNameComponents`（结构化姓名），自带 Siri 理解与本地化 |

- **三条内容曝光路径的官方分工**（对做分发的 PM 直接有用）：**Spotlight** = 让内容可被搜索并被 Siri 检索；**IntentDonationManager 交互捐献** = 让系统学习用户规律、推荐可能重复的操作；**RelevantEntities** = 主动告诉系统「什么内容在什么情境下相关」。
- **结构性观察**：`EntityCollection` 把「**解析实体本身是有成本的**」写进 Schema 设计——Intent 应区分「需完整实体的语义操作」与「只需标识符的批量操作」；`SyncableEntity` 与荣耀「统一记忆+任务迁移」、Step「统一语义数据层」殊途同归，共同承认「**上下文归属人而非设备**」（见 [[Agentic OS 意图调度内核]]）。

## 2026-08-02 增补：Session 343 深入 + App Intents 2.0（来源 [[AppIntent 每日情报 2026-08-02]]）

> 此前（08-01）只补了 Session 345 的代码级 API 表。本次补齐 **Session 343** 的章节结构与「屏幕感知 / 结构化搜索 / 确认与实体归属」三大机制，并补 **App Intents 2.0** 的流式/多轮能力。⚠️ 均属 **WWDC26（2026-06）**，超 7 日窗口，按库内空白补漏补齐。

- **Session 343 官方章节**：自定 Siri 响应 → 视觉响应 → 互动上报 → **确认和实体所有权** → IndexedEntity 语义索引 → **IntentValueQuery 结构化搜索** → App 内搜索 → **屏幕感知（Onscreen awareness）** → 利用现有整合（UserNotifications/NowPlaying/AlarmKit 实体标注）。
- **View Annotations（屏幕感知核心）**：`.siriAnnotation`（标记视图为 Siri 可理解情境）/ `.appEntityIdentifier`（关联 AppEntity）/ `appEntityIdentifier(forSelectionType:)`（选区映射实体）/ **集合标注**（整块区域标注为一组成实体）。价值：Siri 从「猜屏幕上的第三项」升级为「App 主动声明语义锚点」——再次验证 [[Intent Schema Protocol 意图模式规范]] 质量决定端侧路由上限；且与「App 界面私有内容不自动开放」边界一致（需开发者显式 opt-in）。
- **IntentValueQuery**：把 App 结构化查询能力暴露给 Siri/Spotlight，做「意图级」检索而非字符串匹配，与 IndexedEntity 语义索引互补。
- **Confirmations and entity ownership（确认与实体归属）**：声明实体归属（`shared`/`public`/`unknown`），**Confirmation UI 据此差异化提示**（删别人的 vs 删自己的）——回填 [[Confirmation UI 安全机制]] 的 Apple 侧落地。
- **App Intents 2.0（与 Session 343 同期，多源交叉确认）**：① **Streaming responses**（边算边回传，改善搜索类感知延迟）；② **更富实体类型**（Siri 从关键词匹配升级为在 App 数据模型上做意图理解）；③ **Conversational follow-ups**（单次调用内多轮细化，一等公民模式）。迁移**增量式**，旧 Intent 继续工作，按意图 opt-in。
- **隐私治理侧（Extensions）**：Claude/GPT/Gemini 作 **Extensions** 直连 Siri，切换对用户透明，但**任何提供商建 Extension 须经 App Review + App Store 分发**——把多模型路由纳入 Apple 审查治理，与 [[Agent Workspace 隔离执行]] 的「受控发现 + 审批」同构。
- ⚠️ 未独立确认：「Per-Intent Privacy Manifest」作为独立 API 名称本次一手检索未能从 Apple 官方文档确认（Apple 有 PrivacyInfo.xcprivacy 隐私清单机制，但是否有「按意图粒度」专用清单 API 待官方文档确认）。

## 2026-08-09 增补：NowSecure iOS 27 App Intents 攻击面（来源 [[AppIntent 每日情报 2026-08-09]]）

> 此前本笔记聚焦「Apple 怎么定义/路由 Intent」，本期补一个**攻方视角**：移动 AppSec 厂商 NowSecure（2026-08-05 博客）把「App Intents → agentic Siri → iOS 27」的攻击面落到可测清单，与本笔记 08-02 记的 Session 347 威胁模型一致。

**NowSecure 给 AppSec 团队的三条 actionable 指引**
- **盘 App Intents 与 app schemas**：明确应用暴露了哪些能力、哪些动作需要鉴权或用户确认（直接对应本笔记的 Confirmation UI / EntityOwnership 机制）。
- **测完整 workflow，不只测 UI**：传统 UI 测试暴露不了每个 AI 交互；要验证 AI 驱动的端到端交互，而非只测屏幕。
- **监控数据流向**：哪些模型收到了应用数据、如何随时间变化、敏感信息是否流向了非预期 provider。

**与 Apple Session 347 威胁模型的映射（NowSecure 2026-06-11 更早一文）**
- 间接提示注入经**工具输出 / 日历数据 / 通知内容**等不可信上下文注入；锁屏无需解锁即可触发 Siri 动作；agentic 数据外泄。
- 对应 Apple 自家缓解面：App Attest（密钥生成/存储/校验计数）、锁屏 Siri intent 的鉴权策略审计（含非 Apple schema 的自定义 intent）、AI 模型供应链分析（Core AI 模型文件/Metal kernel/量化影响）、跨模型边界的数据流追踪（`.historyTransform` 脱敏逻辑）。

**对 OS PM 的含义**
- App Intents 让「应用变成一组可被调用的能力，而非孤立 UI」——这与 Android AppFunctions（[[Android AppFunctions 设备侧意图 2026]]）方向一致，只是实现不同；安全团队要理解「AI agent 能发现什么能力、能调用什么动作、用什么上下文」三个问题，而非只看应用本身。
- ⚠️ 诚实标注：NowSecure 是**移动 AppSec 厂商（卖测试平台）**，其指引带 advocacy 属性；技术映射（间接 PI 经工具输出/日历/锁屏触发）与 Apple Session 347 一致，但「具体漏洞统计/客户数据」未独立核验，**待官方/第三方复现**。

## 最新进展 / 一手来源（2026）

- **WWDC26 Session 240《使用 App Schemas 打造智能 Siri 体验》才是 Schema 主线课**（本库此前只记了 343/345）：官方主线为 App Entities 建模数据 → App Schemas 对齐系统操作 → 语义搜索 / 跨 App 执行 / 屏幕感知 / 内容传输；明确「27 版本 Siri 在三方面变强：访问 App 内实体、理解内容、据此采取操作」。来源：<https://developer.apple.com/cn/videos/play/wwdc2026/240/>
- **Session 343 官方章节与代码片段已可公开核对**（自定义 `IntentDialog`、`$label.requestValue` 单意图内追问、`OwnershipProvidingEntity` 按 `attendees.isEmpty` 计算 `.shared/.public/.unknown`、`IntentDonationManager.shared.donate(intent:result:)`），本笔记 08-02 节的记录与官方章节表一致。来源：<https://developer.apple.com/fr/videos/play/wwdc2026/343/>
- **🔑 Schema 目录已进公开文档并标注 iOS/iPadOS/macOS/visionOS 27.0+ Beta，且是「参数签名级」而非「动作名级」对齐**：`AppSchema` 按域展开，每个 schema 给出必填/可选参数签名——如 `.messages.draftMessage`（destination / subject / content / attachments / audioMessage / `[GeoToolbox.PlaceDescriptor]` / links / scheduledDate）、`.reminders.createReminder`（含 `Calendar.RecurrenceRule` recurrence 与 locationTrigger）。⚠️ 检索命中的是 Apple 文档 CDN 镜像域（示例 `msc-kobol-public-prod.apple.com/documentation/appintents/appschema/messagesintent/draftmessage`），**canonical `developer.apple.com` 路径待补**。

## 反例与边界

- **Schema 覆盖不到的地方是断崖，不是斜坡**：系统 Schema 是按域枚举的封闭集合，App 的差异化能力若不落在任何域内，只能退回自定义 AppIntent——拿不到免训练短语与跨 App 泛化，等于回到 SiriKit「一 App 一训练」。**Schema 越标准，长尾越吃亏**，这与「为什么重要」里的泛化收益是同一枚硬币的两面。
- **「适配质量决定可用性」是把风险转嫁给开发者**：07-31 实测中 Tesla 官方 App 不可用而第三方 Tessie 可用，用户感知到的却是「Siri 不行」。平台拿走分发权、却把可靠性责任留在 App 侧，是 Apple 的品牌风险，也是开发者无法用营销弥补的隐性缺陷。
- **「端侧闭环」在成本上已被自己削弱**：小企业计划在 PCC 上 $0 云 API 费，实质是补贴上云；当云推理边际成本为 0，「本地优先」就从成本驱动退化为隐私叙事（对照 [[Function Calling 端侧工具调用]]）。
- **不适用**：需实时双向交互、需绕过系统确认的高频批量操作、必须自绘复杂 UI 的场景——30 秒执行上限 + Snippet View 表达力限制决定 App Intents 不是通用 RPC（`LongRunningIntent` 只覆盖长任务，不覆盖长交互）。

## 开放问题 / 未决

- [ ] Session 345 所说「2027 年的新版本」对应哪个系统版本号？Apple 未给（**待补**）。
- [ ] Apple 是否有等价于 Android `setAppFunctionEnabled` 的**运行时动态可见性 API**？目前四平台仅 Android 有公开 API（见 [[Android AppFunctions 设备侧意图 2026]] 08-03 节），Apple 侧**待补**。
- [ ] 混合推理中「定制版 Google Gemini」承担多少比例、在链路哪一层介入？Apple 未公开拆分口径（**待补**）；「Per-Intent Privacy Manifest」是否为独立 API 亦**待补**。

## 与其他概念的关系

- **上游**：[[Intent Schema Protocol 意图模式规范]]——Apple 是该规范目前最强的实现样本（唯一做到参数签名级对齐）；索引见 [[意图框架·跨体系索引 MOC]] 与 [[Intent Routing Stack 六方意图路由分层对照 2026]]。
- **对立（路线分歧）**：[[Android AppFunctions 设备侧意图 2026]]——破坏性动作确认**下放给 App 自实现**，Apple 走**系统级 Confirmation UI + EntityOwnership**，两者责任边界完全相反（见 [[Confirmation UI 安全机制]]）。
- **互补**：[[System Orchestrator 系统编排]]（App 之间不直接互驱，统一由系统编排者路由）｜ [[Intent Router 语义路由]]（Schema 质量决定端侧 Planner 能做多小）。
- **特例**：[[Agent Skills 技能范式 2026]] 在 Apple 侧没有独立 Skill 包形态，被 App Intents + Shortcuts 2.0 + MCP Extensions 吸收——是「技能范式」的平台内化特例。

## 2026-08-15 增补：iOS 27 Beta 5 App Intents / Core AI 逐字变更（官方 Release Notes）

> 来源：[[AppIntent 每日情报 2026-08-15]]。以下为 iOS 27 Beta 5 Release Notes（developer.apple.com，2026-08 窗口内）逐字提取，是继 WWDC26 Session 343/345 之后 Apple 官方给出的**又一层 Schema 级可核实变更**。

**① App Intents — New Features（新增 Schema 能力）**
- "You can now pass a name parameter of type `AttributedString` to the `notes.createNote` and `notes.updateNote` schemas." (173431080) —— 笔记类 Schema 现在接受富文本（带样式/链接）的 name 字段，系统级语义索引可纳入更细的实体命名信号。

**② App Intents — Resolved / Deprecations**
- Fixed: The `notes.appendText` schema erroneously disappeared from the SDK. (182532125) —— 此前从 SDK 掉线的 appendText 已恢复。
- Deprecations: `calendar.deleteEvents` schema renamed to `calendar.deleteEvent`. (176751155) —— 复数命名收敛为单数，旧名进入弃用。
- 另修复：Set 类型参数默认值不生效、RelevantEntities 健身音频上下文不出现在建议、reminders.updateReminder 调用偶发失败等（175534195 / 177996973 / 181212609）。

**③ App Intents — Known Issues（落地约束）**
- AppEntity 实例累计大小上限 **10MB**（含所有子属性），超限 app 可能崩溃并记日志 (181763422)。
- 既有 `@AppEntity(schema: .photos.asset)` 在 27 SDK 因 schema 新增属性可能**不再编译**，须用 availability check 包住新增属性 (181800016)。

**④ Core AI — 后台 Neural Engine 需新 entitlement（对端侧 Planner 托管最关键）**
- "iOS 27 includes Neural Engine improvements... The system now restricts background access to the Neural Engine, similar to GPU usage restrictions. Large model loading (over 1 GB) performance is improved on the Neural Engine." (174796039)
- **"Access to the Neural engine when your app is in the background requires the new entitlement: `com.apple.developer.background-tasks.continued-processing.inference`."** (179282606)

→ **对 OS Agent 的含义**：若系统级 agent 要在后台跑本地 Planner / 端侧推理（如 Foundation Models），现在**必须声明该后台推理 entitlement**，且 OS 对后台 NE 访问做了类似 GPU 的硬性限制。这与 Android `FEATURE_NEURAL_PROCESSING_UNIT`、Windows Agent Workspace 的隔离账号思路同源——**端侧推理不再是「随便跑」，而是受 OS 权限与前台/后台上下文约束的执行动作**。该 entitlement 是 Apple 侧对「端侧 Planner 托管」的第一个显式治理信号。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]]（互补：一手日报 → 本概念沉淀）
- 索引：[[意图框架·跨体系索引 MOC]]（上游枢纽）
- 概念基础：[[Apple Intelligence 与 App Intents]]（上游：Schemas / Entities / View API 三组件模型）
- 跨平台对比：[[Intent Schema Protocol 意图模式规范]]（上游规范）｜ [[Intent Router 语义路由]]（互补：路由层）｜ [[Agentic OS 意图调度内核]]（上游范式）
- 安全：[[Confirmation UI 安全机制]]（互补：执行护栏）

## 2026-08-16 增补：Session 347 安全视角 —— 意图风险元数据 + 鉴权棘轮（来源 [[AppIntent 每日情报 2026-08-16]]）

> 此前本笔记聚焦「Apple 怎么定义/路由 Intent」（343/345/240/Beta 5）。本期补一个**安全治理视角**，但**完整技术内容已落到独立节点 [[意图风险元数据与鉴权策略棘轮 2026]]**，此处只记落点与交叉索引，不重复。

- **Session 347《Secure your app: mitigate risks to agentic features》**给出 Apple 对「agentic App Intents」的官方威胁模型与系统护栏：① 风险元数据（risk metadata）随 `@AppIntent(schema:)` **自动继承** schema 的**副作用轴（side-effect axis）**分类（destructive / exfiltration / shared-content update）；② `authenticationPolicy` **棘轮**——schema 有默认鉴权策略，开发者可覆盖但**只能更严、不能更松**（更弱→编译报错）；③ `createTimer` 的**持久化注入**反例：可选 String label 由模型填参、被 prompt injection 设为攻击者值，后续「list timers」把它拉回上下文污染新上下文。
- **对 OS PM 的含义**：Apple 在「意图风险」上走的仍是**系统级强制层**（与 Confirmation UI / EntityOwnership 一脉），且把「副作用分类 + 鉴权策略」写进 Schema 协议本身——这是本库「Schema 质量决定路由上限」主张的**安全侧延伸**。副作用轴已解决，但**来源/溯源轴（provenance）仍空白**（见 [[Agent Data Injection 数据注入攻击]] 的待办演进）。
- 一手来源：<https://developer.apple.com/videos/play/wwdc2026/347/>

## 2026-08-17 增补：Core AI 框架 + Dynamic Profiles + 多模型 Foundation Models + Evaluations 框架（来源 [[AppIntent 每日情报 2026-08-17]]）

> 接续 08-15 节的 Core AI Neural Engine entitlement。本期补齐 iOS 27 官方指南（developer.apple.com/wwdc26/guides/ios，WWDC26/2026-06，属**库内空白补漏**，非 24h 新公告）给出的**框架级**新增，此前本笔记只零散提到「Core AI（自带模型上设备）」「Foundation Models 可切换 Apple/Claude/Gemini」。

- **Core AI 框架（全新 OS 框架，专为 Apple Silicon）**：用内存安全 Swift API 把「你自己的模型」直接跑在设备端——加载、特化（specialize）、运行全部 on-device，**零服务器依赖、零 token 成本**；模型按硬件**自动特化**（ahead-of-time 编译，快速加载），提供 inference 内存细粒度控制、零拷贝数据路径、stateful 执行。这是本库「端侧 Planner 托管」主题的**第一个 OS 级模型运行时框架**（对照 [[Function Calling 端侧工具调用]] 的端侧 router 评测）。
- **Foundation Models 多模型路由**：原生 Swift API 现在支持**任意语言模型**——Apple Foundation Models、云端模型（Claude、Gemini 等）只要遵循 `Language Model` 协议即可接入；多模态（图+文）；**Dynamic Profiles** 允许在**连续会话内实时切换模型/工具/instructions**，App 行为可在会话中途自适应。
- **Evaluations 框架**：新框架，用于验证 AI 功能在**动态条件**下行为正确（超越单元测试）——直接服务端侧 Planner 的回归测试。
- **成本侧（影响端云路由）**：App Store 小企业计划（累计下载 < 200 万）可在 **Private Cloud Compute 上以 $0 云 API 费**调用下一代 Apple Foundation Models（08-31 节已记，此处重申其路由含义）。

→ **对 OS PM 的含义**：Core AI = 苹果把「端侧推理运行时」从 FM 框架里抽出来变成一等公民框架，意味着**第三方 OS 级 agent 也能自带模型上设备**；Dynamic Profiles 则把「端侧→云端升级」从架构决策降级为运行时旋钮——与 [[端侧 Router 置信度门控与工具可达性收缩 2026]] 的「置信阈值 = 系统确定性触发器」同构。⚠️ 上述均来自 iOS 27 官方指南（2026-06），以正式文档为准；Core AI 具体 API 名与最低系统版本待补。

## 2026-08-26 增补：App Intents Testing 框架（iOS 27 Beta，来源 [[AppIntent 每日情报 2026-08-26]]）

> 接续 08-17 的 Core AI / Evaluations 框架。本期补 App Intents 2.0 体系的**官方验证闭环** —— 这是本笔记此前只零散提到「Evaluations 框架」之后，Apple 给出的**另一条**质量/安全左移路径（进程外、按真实系统路径测意图集成）。

- **App Intents Testing 框架（iOS 27.0+ Beta，官方 `developer.apple.com/documentation/AppIntentsTesting`）**：让开发者**进程外**运行并测试 app intents / entities / enums / query 逻辑，以及它们与 Siri / Spotlight 等系统能力的集成；提供**类型擦除 API**（`AnyAppIntent` / `AnyAppEntity` / `AnyEntityQuery` / `AnyAppEnum` / `AnyTransientAppEntity`），可按名引用意图、设参、运行，**无需 link 到 app target**；`IntentDefinitions` 汇总 app 的意图/枚举/实体/查询目录；`ViewAnnotation` 测试把视图标注为实体供系统感知。
- **价值（对 OS PM 最关键）**：把「意图集成质量 + 安全（参数错配 / 实体解析失败 / 跨 App 联动断裂）」**左移到发布前**，无需 UI 自动化即可早发现——补齐本库长期记录的「Apple 侧无运行时动态可见性 API（[[Android AppFunctions 设备侧意图 2026]] 08-03 节）」之外的**另一短板：可测试性**。与 [[Confirmation UI 安全机制]] 的「运行时拦截」正交，形成「发布前测试 + 运行时确认」双层。
- **与 Evaluations / Core AI 的集群关系（iOS 27 官方指南 `developer.apple.com/wwdc26/guides/ios` 确认）**：App Intents 框架 = Siri 连接更多 App 操作 + 实体架构贡献 Spotlight 语义索引 + **View Annotations（视图→实体映射）** + **App Intents Testing（真实系统路径验证）**；Core AI = 自带模型上设备；Evaluations = 动态条件下验证 AI 功能。四者共同构成 iOS 27 的「声明 → 索引 → 感知 → 验证」闭环。
- ⚠️ 诚实标注：本轮命中为 Apple CDN 镜像域（`msc-kobol-public-prod.apple.com` / `ma-kobol-public-prod.apple.com`），**canonical `developer.apple.com` 路径与最小 Beta 版本号待补**；框架随 iOS 27 Beta，具体 GA 对应版本未独立确认。

→ **对 OS PM 的含义**：做 OS 级意图框架时，「可测试性」与「运行时护栏」同等重要——Registry 里声明了能力不等于能力被正确集成，Apple 用进程外测试框架把集成验证变成一等公民，是端侧意图总线成熟度的一个新标杆。

#标签/Apple #标签/AppIntent #标签/SchemaProtocol

## 2026-09-15 增补：iOS 27 正式版（09-14）post-GA 框架确认 + Foundation Models 多模型路由 + Per-Intent 路由待办重开（来源 [[AppIntent 每日情报 2026-09-15]]）

> 接续 08-26 的 App Intents Testing + 08-17 的 Core AI / Foundation Models 多模型。本期是 **iOS 27 正式版（2026-09-14）落地**后的官方 post-GA 确认，把 WWDC26 已宣布的能力升为 GA 级，并**重开 08-31 的 Per-Intent Privacy Manifest 证伪结论**。

**① iOS 27 官方 post-GA 确认的 App Intents 框架能力（developer.apple.com/ios/whats-new，2026-09-14）**
- **Entity schemas**：把 App 内容贡献进 **Spotlight 语义索引**，Siri 可带「归属回 App」呈现——与 08-15/08-02 记的 `IndexedEntity` + `indexingKey` 语义索引一致，本次为 GA 级官方表述。
- **Intent schemas**：让用户对内容「自然地采取动作」，**无需定义特定短语、随 Siri 语言理解演进/扩方言免改码**——与 07 月「免训练短语」主张一致，本次为 GA 确认。
- **View Annotations API（新命名 GA）**：把视图映射为实体，让用户**对话式引用/操作屏幕上的内容**——与 08-02 Session 343 的 `.siriAnnotation` / `.appEntityIdentifier` / `appEntityIdentifier(forSelectionType:)` 一致，本次以「View Annotations API」正式命名 GA。
- **App Intents Testing 框架（GA）**：已在 08-26 记录，本次随 GA 页确认。
- → 上述四项均为 **WWDC26 已宣布、本次 GA 落地**，非 WWDC 之外的全新 API；本笔记 08-02/08-26 已覆盖其核心机制。

**② 🔑 Foundation Models 框架：OS 级 Planner 首次把「多模型路由」写进一等公民框架**
- 官方 post-GA 页明确：Foundation Models 原生 Swift API 现在支持**任意语言模型**——Apple Foundation Models、云端模型（**Claude、Gemini**）或任何**遵循 `Language Model` 协议**的 provider 均可接入；多模态（图+文）；**Dynamic Profiles** 允许在**连续会话内实时切换模型/工具/instructions**，App 行为可在会话中途自适应；**Evaluations 框架**验证 AI 功能在动态条件下行为正确。
- 与 08-17 已记「Foundation Models 可切换 Apple/Claude/Gemini」一致，本次为 **GA 确认升级**并明确「任何遵循 Language Model 协议者」——**端云路由从架构决策降为运行时旋钮**，与 [[端侧 Router 置信度门控与工具可达性收缩 2026]]「置信阈值=系统确定性触发器」同构，但发生在**模型层**而非工具层。
- → 对 OS PM：**OS 级意图框架的 Planner 不再被绑定到单一厂商模型**；Apple 把「本地优先 + 低置信/复杂升级云端」从 App 策略升为框架原语。⚠️ 08-31 节「Per-Intent Privacy Manifest」与「混合推理中定制版 Gemini 承担多少」两项仍待补——本次 GA 确认多模型可接入，但未拆分具体链路占比。

**③ Per-Intent Privacy Manifest 待办重开（校正 08-31「证伪」结论）**
- **08-31 结论回顾**：本笔记 08-31 经官方文档直查判定「Per-Intent Privacy Manifest / 按意图粒度声明云-端路由」**不存在**（第三方博客误读 iOS 17 通用隐私清单）；当时注明「若 iOS 27 正式版新增此类 API 需重新评估」。
- **GA 后新证据**：WWDC 2026 多源报道（Lushbinary / ByteIota / TechTimes / AlgeriaTech，2026-06-08 起）一致称 Apple 引入 **per-intent privacy manifest declarations**，让开发者**按意图声明「Siri 交互可否路由上云 / 必须留端」**，作为受监管数据（健康/法律/金融）的合规控制。
- **诚实判定**：官方 post-GA「What's New in iOS 27」页**未逐字列出该 API**（仅列 Entity/Intent schemas、View Annotations、Testing、Foundation Models 多模型等）。→ 由「confirmed non-existent」升为 **「GA 后多源一致报道、但官方页未确认 → 待官方文档逐字复核」**。
- **对来源轴结论的影响**：即便最终确认，它也是**数据路由目的地（cloud vs on-device）声明**，与 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 08-17/08-31 证伪的「来源/可信度 provenance」**不同轴**——不推翻「意图 Registry 来源/可信度轴全空白」结论，但会为 Apple 补一条「路由轴」声明，待确认后评估。详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 09-15 增补。

**④ 沿用结论**：iOS 27 框架层 GA 无 WWDC 之外的全新 API；多模型 Foundation Models + Dynamic Profiles 是本次 GA 确认的架构级信号；Per-Intent 路由待办由「证伪」重开为「待官方复核」。

## 2026-09-20 增补：iOS 27.1 beta 在即（预期 2026-09-21~23，未发布·窗口外前瞻，来源 [[AppIntent 每日情报 2026-09-20]]）

> 接续 09-15 的 iOS 27 GA 确认与 09-18 的「iOS 27.1 beta 尚未发布」校正。本期更新该待办的前瞻状态——**作为窗口外前瞻登记，非 24h 净新增 API**。

- **发布时间窗（第三方基于 MacRumors 口径）**：首个 **iOS 27.1 developer beta 预期 2026-09-21~23** 放出；公开版随 **iPhone Duo（折叠屏）10-23 发布**预装，预期 10-19~21 向全体推送。Macworld 09-20 仍确认「Apple 尚未放出首个 iOS 27.1 beta」——**截至本窗口结束（09-20 21:00）无新 App Intents API 信号**。
- **已知 27.1 内容（与 App Intents 框架相关）**：
  - **Siri AI 新增 5 种语言**（法语 / 日语 / 韩语 / 葡萄牙语 / 西班牙语）——属 09-15 已录「Foundation Models 多模型 + Dynamic Profiles」之上的**本地化扩张**，非新 Schema API。
  - **Messages 任务建议回炉（iOS 27 推迟的两功能之一）**：「发照片 / 执行任务」类对话触发**一键『加到提醒事项』/『加到备忘录』**——这是 **App Intents 驱动的主动式（proactive）能力分发**，等于把 `reminders.createReminder` / `notes.createNote` schema 以**零短语主动建议**形态推到 Messages 内（与 08-02「App Intents 2.0 conversational follow-ups」+ 08-15 `notes.createNote` 富文本参数同源）。**对 OS Agent 含义**：App Intents 正从「用户说 → Siri 做」扩展到「用户在别处说 → 系统主动建议调 App Intent」——proactive 触发面扩大，也意味着 [[XPIA 跨提示注入]] 08-09晚警告的「主动触发场景确认点更难布」问题更突出。
  - **自动修复弱/复用密码（Passwords App）**：Apple Intelligence + Safari 后台改密——属系统级动作，走既有 Confirmation UI。
- **对 OS PM 的跟踪意义**：**iOS 27.1 是否带新 `@AppIntent(schema:)` / App Intents Domains 细节**，是下一窗口头号跟踪项（延续 09-18 待办）；当前所有 27.1 报道均未提及新 Schema API，预期为 GA 能力补全 + 本地化，非框架级新增。
- ⚠️ 诚实标注：上述发布日期与功能清单均来自 MacRumors / appauxin 等第三方前瞻（非 Apple 官方公告），精确 beta 日期与最终功能集待 Apple 官方发布后逐字复核。

## 2026-09-21 增补：iOS 27.1 beta 已放出（Duo SDK，无新 Schema API）+ Model Delegation 反编译信号（来源 [[AppIntent 每日情报 2026-09-21]]）

> 接续 09-20 的「iOS 27.1 beta 预期 09-21~23、尚未发布·窗口外前瞻」。本期**关闭该前瞻待办**——Xcode 27.1 beta（含 iOS 27.1 SDK）已于约 **09-18/19** 放出（早于 09-20 估计窗），但内容为 **iPhone Duo 折叠屏适配 SDK**，非 App Intents 框架新增。

- **iOS 27.1 beta / Xcode 27.1 Beta 1 已放出（约 09-18/19）**：含 Swift 6.4 与 iOS 27.1 / iPadOS 27 / tvOS 27 / watchOS 27 / macOS 27 / visionOS 27 SDK；核心增量是 **iPhone Duo（首款折叠屏）适配工具**——Canvas 新增 Display 分组预览另一块屏、iPhone Duo 模拟器、折叠几何（size classes）+ 保留区域（`reservedRegions`，折痕 division / 摄像头 occlusion）API。→ **App Intents 框架侧无新 `@AppIntent(schema:)` / App Intents Domains API 信号**，与 09-20 前瞻「预期为 GA 能力补全 + 本地化、非框架级新增」一致。**含义：09-20 跟踪项「iOS 27.1 是否带新 Schema API」结论 = 已放出、Duo 向、无 schema 新增**（仍须正式 beta 发布说明逐字复核）。
- **Model Delegation API 反编译信号（★5/10，非官方）**：开发者 pdfu 在 iOS 27 / macOS 27 代码中发现 **App Intents 内的 Model Delegation API** 机制——允许外部模型（演示含 Claude、GPT-5.6 Terra）作为 Siri 扩展出现，接收 Siri 提示与 tool 定义、处理系统动作并取回结果；另在 **Model Manager Services** 中发现可替换 Siri 服务器端运行模型。→ 与 09-15 已录「Foundation Models 框架支持任意遵循 `Language Model` 协议者」**互为印证**，但本次为**代码级证据、Apple 未官方宣布「用户可选外部模型」**；若未来成为正式功能，将是「外部模型接管部分推理与任务执行」的架构级信号（Siri 从「模型驱动助手」→「可路由到不同模型的接口」）。
- → 对 OS PM：Apple 侧仍是「App Intents Schema Protocol 框架稳定、多模型路由 GA、无 27.1 schema 新增」；外部模型接入从「官方 GA 多模型」到「代码级 Model Delegation」是值得跟踪的演进方向，但**须 Apple 官方公告后才可收录为框架级信号**。
⚠️ 诚实标注：Xcode 27.1 beta 日期/功能来自 blakecrosley.com / woozad（开发者博客，09-18~19）/ 网易·163 09-19 转述；Model Delegation 来自 nabamart（09-21）对开发者 pdfu 反编译的转述，Apple 未官方确认。

## 2026-10-08 增补：Apple 跳过 iOS 27.1 beta、直发 iOS 27.2 beta 3（无新 Schema API，来源 [[AppIntent 每日情报 2026-10-08]]）

> 接续 09-20「iOS 27.1 beta 在即（预期 09-21~23）」与 09-21「iOS 27.1 beta 已放出（Duo SDK，无新 Schema）」。本期**更新并收口该跟踪项**——事实比此前预期更明确：Apple **未发布 iOS 27.1 的任何 developer/public beta**，27.1 是 **iPhone Duo（首款折叠屏）专属预装正式版**，常规 iPhone 直接跳到 **iOS 27.2** beta 线。

- **事实更正（关闭 09-20/09-21 跟踪项）**：Apple 于 **2026-09-17 直接放出 iOS 27.2 beta 1**（build 24B5084k），**跳过 iOS 27.1**；最新为 **iOS 27.2 beta 3（build 24B5099f，约 10-05/06 放出）**。多家媒体（9to5Mac / MacRumors / AppleInsider / 网易 / 新浪）一致解读：跳过是为**防止开发者解包 27.1 beta 泄露 iPhone Duo 硬件参数与双屏专属代码**（Duo 10-23 上市、预装 iOS 27.1 正式版）。
- **对 App Intents Schema Protocol 的含义（关键）**：iOS 27.2 beta 线（含 beta 3）**不含新的 `@AppIntent(schema:)` / App Intents Domains API**——27.2 beta 内容为「被清洗过」的常规更新（redesigned Health app / Group FaceTime 双摄 / Siri 多语言 / Apple TV profiles / AutoLock 防盗），**所有 Duo 相关代码被排除在外**；而真正含 Duo 适配的 **iOS 27.1 不开放 beta、随 Duo 首发**。→ 本窗口（及连续多轮）**Apple 侧无新 Schema Protocol API 净新增**，与「OS 框架不日更」一致；此前 09-21「已放出、Duo 向、无 schema 新增」结论维持。
- **Xcode 27.1 仍含 Duo SDK**：Apple 要求开发者用 **Xcode 27.1** 重编译适配 Duo（DeviceHub 工具查看折叠/展开/横竖屏姿态）；2027-04 起 App Store 上架须含 Duo 截图——这是**设备形态适配**，非 App Intents 框架 API 新增。
- → 对 OS PM：Apple 用「跳号 + 清洗 beta」把折叠屏专属系统锁在 27.1 正式版内，是产品保密驱动的版本策略，**不影响 App Intents Schema Protocol 框架稳定性**；下一观察点是 **iOS 27.1 正式版（10-23 随 Duo）是否带来 Duo 双屏场景的新 intent/entity schema**（如双屏分栏布局相关的 App Intents 适配），纳入下轮跟踪。

⚠️ 诚实标注：跳号与 Duo 保密动机来自 9to5Mac / MacRumors / AppleInsider / 网易 / 新浪等媒体综合；Apple 官方未发「跳过 27.1」公告，上述为媒体共识解读。iOS 27.1 正式版（10-23）是否含 App Intents 新 Schema 待 Apple 官方发布后逐字复核（延续 09-21 待办）。

## 2026-10-16 增补：Apple 官方澄清「iOS 27.1 发 beta、本月晚些时候」——修订 10-08「跳过 27.1 beta」旧结论（来源 [[AppIntent 每日情报 2026-10-16]]）

> 接续 10-08「Apple 跳过 iOS 27.1 beta、直发 27.2 beta 3」的收口结论。本期**修订该结论**——Apple 官方开发者新闻（developer.apple.com/news）亲口确认 27.1 **会发 developer beta**，此前「跳过」系媒体共识、现被官方表述覆盖。⚠️ 修订仅涉及**发布节奏**，不涉及任何新 Schema API。

- **官方原文要点（developer.apple.com/news，2026-10 当期）**：
  - **「When iPhone Duo becomes available on October 23, it will run iOS 27.1. This version builds on the foundation of iOS 27 and introduces features that were purpose-built for the new foldable design.」** —— 确认 Duo 10-23 上市、预装 iOS 27.1（折叠屏专属设计）。
  - **「Xcode 27.1 will add development support for iPhone Duo… A beta version will be available later this month.」** —— 明确 **iOS 27.1 的 developer beta 将于「本月晚些时候」放出**（面向 Duo 适配），不向常规直板机 beta 线开放。
  - 同期给出 Bundles & Suites、Multiseat 购买、EU ATT 替代系统提示等 27.2 生态能力（10-22/冬季陆续上线），均非 App Intents 框架变更。
- **对 10-08 旧结论的修订**：
  - 10-08→10-15 连续四轮采信「Apple 跳过 27.1 beta、直发 27.2」的媒体共识——**该结论现被 Apple 官方澄清推翻**：27.1 **会发 beta**（Duo 开发用），只是独立于常规 27.2 beta 线。
  - **不变的部分**：iOS 27.2 beta 线（含 beta 4 = 24B5110a、beta 5 预期 Late October）**不含新 `@AppIntent(schema:)` Schema**；App Intents Updates 官方页最新条目仍停在 **June 2026**（SyncableEntity / OwnershipProvidingEntity / LongRunningIntent 等已录项）；「OS 框架不日更」结论维持。
- **对 OS PM 的含义 / 跟踪窗口前移**：
  - 头号跟踪项「**iOS 27.1 是否带双屏场景新 intent/entity Schema**」此前预期在 10-23 正式版才揭晓；现在 **27.1 beta「本月晚些时候」即可能暴露 Duo 双屏专属 Schema/Entity**（如双屏分栏布局相关的 App Intents 适配）——跟踪窗口提前。
  - 产品保密动机（防 Duo 硬件参数经 27.1 beta 解包泄露）从「不发 27.1 beta」修正为「发 27.1 beta 但独立于 27.2 线、且清洗常规线」——仍是保密驱动，但 Apple 现在给 Duo 开发者留了合法 beta 通道。
- ⚠️ 诚实标注：官方仅写「later this month」，**未给 27.1 beta 精确日期**；27.1 beta 是否真含双屏新 Schema 待 beta 推送后逐字复核（延续 09-21 / 10-08 待办，窗口前移）。Jetpack 侧 alpha13 仍为 Android 最新（10-13 三处直查），与 Apple 侧澄清无关。

## 2026-10-18 增补：iOS 27.1 无设备公开 beta、以 Duo 出厂/设置 build 交付——撤回 10-16「跟踪窗口前移」推论（来源 [[AppIntent 每日情报 2026-10-18]]）

> 接续 10-16「Apple 官方澄清 iOS 27.1 发 beta、本月晚些时候」的修订段。本期**再修订 10-16 的推论**——10-16 据 Apple 09-16 开发者新闻「A beta version will be available later this month」把「iOS 27.1 双屏 Schema」跟踪窗口前移到「本月晚些 beta」；**本期第三方（apfelpatient，2026-10-17，基于 Apple 公告整理）确认：iOS 27.1 没有设备公开 beta 阶段，该「beta」实为 Xcode 27.1 工具链 beta（09-18 已放出），跟踪窗口回退到 10-23 Duo 出厂正式版**。⚠️ 修订仅涉及**发布节奏与跟踪窗口定位**，不涉及任何新 Schema API。

- **第三方澄清要点（apfelpatient，2026-10-17，多家果粉媒体一致复述）**：
  - **iOS 27.1 没有公开 beta 测试阶段**——「The betas continued directly with iOS 27.2」；Duo 预装 iOS 27.1（build 24A94232 出厂），**10-12 起 Apple 放出更新 build 24A94425，设备在首次设置时下载安装**，无 changelog。
  - **Apple 09-16 说的「A beta version will be available later this month」实为 Xcode 27.1 beta（已于 09-18 放出）**——是给 Duo 开发者的**工具链 beta**，并非面向常规 iPhone 的设备 iOS 27.1 beta（applescoop / guofenchaxun / 今日头条数码知更鸟均复述「iOS 27.1 不开放测试、直接迎来 iOS 27.2」）。
  - **对 10-16 推论的修订**：10-16 跑据此把「iOS 27.1 双屏 Schema」跟踪窗口从「10-23 正式版」前移到「本月晚些 beta」。现在看**根本没有设备 27.1 beta**，双屏专属 intent/entity Schema（若有）只在 10-23 出厂正式版揭晓——**跟踪窗口回退到 10-23**，10-16 的「前移」推论被撤回（非错误、是信息更完整后的修正）。
- **对 App Intents Schema Protocol 的含义（关键）**：iOS 27.1 设备版以**出厂/首次设置 build（24A94232 → 24A94425）**形态交付、无公开 beta，等于**双屏专属 Schema（若有）在 10-23 前完全不进入公开可解包基线**——比「发 Duo 专属 beta」更彻底地锁死；iOS 27.2 beta 线（beta 4 = 24B5110a，10-13；beta 5 预期 Late October）**仍无新 `@AppIntent(schema:)` Schema**，App Intents Updates 官方页最新条目仍停在 **June 2026**。→ 本窗口（及连续多轮）**Apple 侧无新 Schema Protocol API 净新增**，「OS 框架不日更」结论维持。
- **对 OS PM 的含义 / 跟踪窗口回退**：头号跟踪项「**iOS 27.1 是否带双屏场景新 intent/entity Schema**」跟踪窗口**从「本月晚些 beta」回退到 10-23 Duo 出厂正式版**（与 10-16「前移」相反方向修正）；下一观察点 = 10-23 出厂正式版 + 设置期更新 build 是否暴露 Duo 双屏专属 Schema/Entity。
- ⚠️ 诚实标注：iOS 27.1 无设备公开 beta、以 Duo 出厂/设置 build 交付（24A94232 出厂 → 24A94425 更新自 10-12）来自 apfelpatient（2026-10-17，德国果粉媒体，基于 Apple 公告整理）；「Apple 09-16 本月晚些 beta = Xcode 27.1 beta（09-18 已出）」由该文 + Apple 09-16 开发者新闻原文交叉确认。Apple 开发者新闻（developer.apple.com/news?id=5042016a，09-16）原文确写「Xcode 27.1 will add development support for iPhone Duo… A beta version will be available later this month」，其上下文指 Xcode 27.1 开发支持，与 apfelpatient 解读一致。10-16 段未删除（保留推断链），本段显式标注修订，避免下次重复「前移」。

## 2026-10-26 增补：iOS 27.1 随 Duo 10-23 正式发布——双屏由布局/铰链 API 处理，无新 `@AppIntent(schema:)` Schema（头号跟踪项收口，来源 [[AppIntent 每日情报 2026-10-26]]）

> 接续 10-18「跟踪窗口回退到 10-23 Duo 出厂正式版」的待办。本期**关闭该头号跟踪项**——iOS 27.1 已于 2026-10-23 随 iPhone Duo 正式发布，经 Apple 官方 newsroom + 开发者指南 + App Intents Updates 官方页逐字核验，**Duo 双屏适配走 SwiftUI/UIKit 布局 API，而非任何新的意图 Schema**。

**① 事实核验（关闭 09-21→10-18 连续多轮的「双屏新 Schema」跟踪）**
- **iOS 27.1 的 Duo 适配 API = 布局/形态层，非 App Intents Schema 层**：Apple newsroom（2026-10-23，developer.apple.com.cn/cn/newsroom）明示开发者用「iOS 27.1 SDK 中新 API 和更新版 API」适配 Duo，具体包括：**新的布局和保留区域 API（arrangement & reserved region APIs）**、**新的铰链 API（hinge API）**、**场景配件（scene accessories，双屏同时显示内容）**、**新的摄像头 API**、**Xcode 27.1 的 Device Hub（模拟开合/折叠/旋转）**。→ 这些全部是 SwiftUI/UIKit 的**空间布局与姿态感知原语**，**没有任何 `@AppIntent(schema:)` / App Entities 双屏专属 Schema 或 Entity 信号**。
- **App Intents Updates 官方页最新条目仍停在 June 2026**（SyncableEntity / OwnershipProvidingEntity / LongRunningIntent 等已录项；developer.apple.com/documentation/Updates/AppIntents 直查）——**27.1 未在 App Intents 框架层带来任何新 Schema/Entity/枚举**。
- **结论**：自 09-21（iOS 27.1 beta 已放出·Duo SDK）经 10-08（跳过 27.1 beta）/ 10-16（官方澄清发 beta）/ 10-18（撤回前移、回退到 10-23）一路跟踪的「iOS 27.1 双屏是否带新 intent/entity Schema」问题，**最终答案 = 否**：双屏折叠形态被 Apple 当作**显示/布局问题**而非**意图语义问题**处理——这与本库长期主张「Schema 覆盖不到的地方是断崖」及 Apple「用布局 API 而非新意图 Schema 应对新硬件形态」的工程取舍一致。

**② iOS 27.2 RC（10-19）经核实也无新 Schema**
- iOS 27.2 于 2026-10-19 放出 **Release Candidate（RC）**（比 beta 4 = 24B5110a 早一周），公开版预期 ~10-26；内容 = **Siri AI 新增 5 语言（法/日/韩/葡/西）+ 六款 App 功能补全（Messages 建议动作 / Apple TV profiles / FaceTime 双摄 / Podcasts / Home 锁门提醒 / Music 图标）+ EU ATT 替代系统提示 +  redesigned Health app（后续 beta 才回）**。
- **App Intents Schema Protocol 层零变更**：27.2 RC 未引入任何新 `@AppIntent(schema:)` Domain；27.1/Duo 与 27.2 均不触及 App Intents 框架 API，「OS 框架不日更」结论维持。
- **相关但低于新节点阈值**：iOS 27 已内置、于 27.2 RC 中现身的 **Impersonation Risk Detection（冒名风险检测，默认关，Settings > Privacy & Security > Share with App Developers）**——检测通话/消息中「冒充银行诱导转账」等 scams，向受支持 App 仅提供风险等级而非用户数据（Apple 支持文档明确该特性「从 iOS 27 开始提供」，非 27.2 新增）。它属于**通信反诈骗 / 社会工程检测**，与 [[XPIA 跨提示注入]] 及 [[Trust Insights 意图 coercion 检测框架 2026]]「意图真实性」主题相邻但**非意图框架 API**，且为 off-by-default 通信安全特性，不构成 App Intents Schema Protocol 变更，本次仅作关联观察、不升新节点。

→ **对 OS PM 的含义**：Apple 用「布局/铰链/scene-accessory API」而非「新意图 Schema」承载折叠屏双屏，是一个值得记取的范式选择——**新硬件形态优先用显示层原语而非语义层原语处理**，避免了为每种设备形态膨胀 Schema 域；同时再次印证 App Intents Schema Protocol 框架在 27.x 周期已进入**稳定维护期**（无新增 Schema 域），跟踪重点应从「新 Schema」转向「27.2 的 agentic 安全与多模型路由落地」。

⚠️ 诚实标注：iOS 27.1 Duo 适配 API 来自 Apple newsroom（2026-10-23，developer.apple.com.cn/cn/newsroom/2026/10/developers-bring-incredible-new-app-experiences-to-iphone-duo）+ 第三方（udn/iclarified）对开发者指南的整理；App Intents Updates 官方页（developer.apple.com/documentation/Updates/AppIntents）直查最新条目仍 June 2026；iOS 27.2 RC（10-19）与 Impersonation Risk Detection 来自 Times of India / Apple 开发者新闻（developer.apple.com/news/?id=0l3nh5gd）交叉确认。Duo 双屏无新 Schema 为「官方页未列 + 适配 API 全为布局层」推断，非逐 Schema 反编译确认。

## 2026-10-28 增补：iOS 27.2 正式版（框架零变更·官方页直查仍 June 2026）+ 「排除的 App」消费者层意图访问治理细化 + 160 CVE 安全事件（来源 [[AppIntent 每日情报 2026-10-28]]）

> 接续 10-26「iOS 27.1/Duo 双屏无新 Schema、头号跟踪项收口」。本期把 10-26 对 iOS 27.2 RC 的「无新 Schema」推断**升级为正式版发布后的官方页逐字确认**，并捕获 iOS 27.2 一个消费者层意图访问治理细化。

**① iOS 27.2 正式版（2026-10-26/27，24B119；Duo 专属 24B91020）——App Intents Schema Protocol 框架层零变更**
- 本运行 **WebFetch 直查 `developer.apple.com/documentation/updates/appintents`** 确认最新条目仍 **June 2026**（SyncableEntity / OwnershipProvidingEntity / LongRunningIntent 等已录项），**iOS 27.2 未在 App Intents 框架层引入任何新 `@AppIntent(schema:)` Schema/Entity/枚举**。这把 10-26 对 27.2 RC 的「无新 Schema」从推断升级为正式版发布后的官方页逐字确认。
- 27.2 消费者功能 = Siri AI 记忆此前对话 + 更广个人上下文（信息照片附件/日历参与者/语音留言/Safari 历史）+ 5 种新语言（法/日/韩/葡/西，EU 与中国大陆不可用）+ Messages/Photos/FaceTime 建议动作 + SynthID 水印识别 + Apple Music/Podcasts/Apple TV redesign。→ 全部为 GA 能力补全与本地化扩张，**非 App Intents 框架 API 新增**。
- Duo 专属（24B91020）：Apple Pencil 支持 + 边缘光效（弱光视频通话）；**国行**新增「限制运动数据」遏制「摇一摇」广告跳转（隐私控制，仅中国区账号可见）。均非 App Intents 框架。

**② 🔑 唯一 OS 级治理细化（★6/10，消费者层意图访问治理）＝「排除的 App」（Excluded Apps）统一设置**
- iOS 27.2 新增**统一隐私设置**，用户可集中选择**哪些 App 不能被 Siri、搜索（Search）和建议（Suggestions）访问**。这是 Apple 侧一个**系统级「意图访问排除清单」**——把「系统 agent（Siri/Search/Suggestions）可调用哪些 App 的能力与数据」的控制权以**消费者隐私开关**形态落地。
- 与 Android `setAppFunctionsPolicy` / `APP_FUNCTIONS_DISABLED`（企业 MDM 层，详见 [[Android AppFunctions 设备侧意图 2026]]）**同源**，但落在**消费者隐私层**——补齐了本库「agent 执行边界 = OS 权限/访问边界」跨平台收敛的**消费者层拼图**（详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 10-28 增补）。
- ⚠️ 属用户隐私开关、**非开发者框架 API**，不构成 Schema Protocol 新 API；但它是 Apple 在 27.x 周期内对「意图访问治理」最明确的一次消费者层补强。是否影响开发者侧 intent 注册可见性待 Apple 开发者文档逐字确认。

**③ 重大 OS 安全事件（XPIA 相邻，低于新节点阈值）＝iOS 27.2 修复 160+ CVE（含 Apple Intelligence 远程数据访问漏洞）**
- iOS 27.2 修复 **160+ 安全漏洞（163 个可追踪 CVE）**，含一个 **Apple Intelligence 漏洞（远程攻击者可能访问敏感数据）** 与「隐藏邮件地址（Hide My Email）」真实邮箱泄露缺陷；30+ WebKit、约 15 个内核漏洞。
- Apple Intelligence **远程数据访问类漏洞**属 **agentic 数据安全相邻面**（OS 智能层把敏感数据暴露给非预期远程方），与 [[XPIA 跨提示注入]] 及 [[Agent Data Injection 数据注入攻击]] 主题相邻，但为 **CVE 修复而非新框架机制**，低于新节点阈值，仅作关联观察（延续 0 新建 B 节点纪律）。

→ **对 OS PM 的含义**：App Intents Schema Protocol 在 27.x 周期已确认进入**稳定维护期**（无新增 Schema 域），跟踪重点应从「新 Schema」转向「27.2 的 agentic 安全与多模型路由落地 + 消费者层意图访问治理」。

⚠️ 诚实标注：iOS 27.2 无新 App Intents Schema 经本运行 WebFetch 直查 `developer.apple.com/documentation/updates/appintents` 确认（最新仍 June 2026）；「排除的 App」来自 iOS 27.2 媒体功能清单（IT之家 10-27）；160+ CVE / Apple Intelligence 漏洞来自网易 TechWeb 10-27 报道，CVE 编号与 Apple 安全通告逐条对应待补。

## 2026-11-05 增补：Siri AI 开发者预览（iOS 27.3）—— @AppIntent(.tool) + Skills + 语义索引任意实体 + Siri Evaluations（来源 [[AppIntent 每日情报 2026-11-05]]）

> 接续 10-28「iOS 27.x 进入稳定维护期、跟踪重点转向 agentic 安全与多模型路由」。本期捕获 iOS 27.3 开发者预览（2026-11-03 美/11-04 中）带来的 **App Intents 接入面最大一次扩展**——是既有机制的能力放大，非新 schema 域。

**① 新 API / 宏（开发者接入面放宽）**
- **`@AppIntent(.tool)` 宏**：给 intent 加 `ToolIntent` 一致性，把它变成 Siri 的「工具」（agent 的「手」）；对**既有与新 intent 均生效**；Siri 从 intent 的 title + description 读用途、做消歧。与原先「仅对齐 system schema 才可被 Siri 调用」相比，降低接入门槛。
- **Skills（`SKILL.md` 子集）**：教 Siri 把多步动作串成单体验；每个 skill 是 `Skills.skillsbundle` 内独立文件夹中的 `SKILL.md`，body ≤10,000 字符；**仅是 Agent Skills 标准的子集**（name + description + Markdown body，**无 scripts / references / 其他字段**）；一个 app target 一个 bundle；依赖脚本的 skill 需为 Gemini 重写。→ 与 [[Agent Skills 技能范式 2026]] 跨平台 `SKILL.md` 收敛信号对齐。
- **Spotlight 语义索引「可浮现任意实体」**：**「Siri AI can now surface any entity in the Spotlight semantic index, not just the ones that fit an existing schema」**——语义路由从「仅 schema 内实体」放宽到「任意 App Intents 暴露的实体」，**介于封闭 schema 与 schema-less 之间**（详见 [[Intent Router 语义路由]] 11-05 增补）。
- **Siri Integration Advisor（Xcode）+ Siri Evaluations 框架**：前者给接入建议，后者跑脚本化请求、测意图集成改动后的响应漂移；与 08-26 App Intents Testing / 08-17 Evaluations 形成「发布前 + 运行时」双测试闭环。

**② 执行安全（确认 / 认证策略）关键约束**
- **Skills 不保证确定性顺序（★8/10，确认机制相关）**：Apple 明确「Siri AI does not necessarily run the intents listed in a skill in sequence」；**保序步骤（如确认购买）必须在 intent 实现内部加检查，不能依赖 skill 文案顺序**——首次官方确认「技能编排 ≠ 确定性执行」，冲击「用 skills 串多步含确认流程」的朴素假设（呼应 [[Confirmation UI 安全机制]]）。
- **认证策略 + beta 已知缺陷**：默认 entity 不需认证；敏感信息须设 `authenticationPolicy`，结果含敏感信息的 intent 须在 intent 级也设策略（单属性 `internal` 仅作用于 Siri 响应）；**iOS/iPadOS 27.3 known issue：即便定义了要求解锁的策略，Siri AI 仍可能在未解锁时显示该实体**——beta 期认证策略执行缺口，内部测试建议暂不用真实数据（与 08-02/08-16 EntityOwnership + authenticationPolicy 棘轮互补）。

**③ 发布边界（隔离相关但非新机制）**
- 预览仅在**开发签名构建 + 内部 TestFlight** 生效，外部测试者/App Store 版本暂不可用；customer availability「几个月后」、App Store 提交「春季」。
- 中国区：Writing Tools/Genmoji/Priority Notifications/Clean Up/Visual Intelligence/Live Translation(AirPods) 本版进中国（与 11-03 中国 Qwen 端侧底座互为表里）；agentic Siri AI + Image Playground 仍不进中国。EU（iOS/iPadOS/watchOS）仍不可用；<13 岁不可用。

→ **对 OS PM 的含义**：Apple 把 App Intents 从「schema 对齐」推进到「工具 + 技能 + 任意实体」三层，但**未膨胀 schema 域**——是「接入面放宽而非语义层重构」；跨平台 `SKILL.md` 收敛 + 「skills 不保序」的官方确认，是做 OS 级技能编排时**必须内建确定性护栏**的实证。⚠️ `@AppIntent(.tool)` 是否新 API 名或 ToolIntent 宏糖衣、`Skills.skillsbundle` 打包约束、GA 日期（预览期「数月后」/提交「春季」）待官方文档逐字段确认。
