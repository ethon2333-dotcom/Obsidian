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
