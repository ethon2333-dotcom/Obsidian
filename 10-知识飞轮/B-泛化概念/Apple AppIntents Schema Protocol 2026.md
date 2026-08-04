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
- **View Annotations（屏幕感知核心）**：`.siriAnnotation`（标记视图为 Siri 可理解情境）/ `.appEntityIdentifier`（关联 AppEntity）/ `appEntityIdentifier(forSelectionType:)`（选区映射实体）/ **集合标注**（整块区域标注为一组成实体）。价值：Siri 从「猜屏幕上的第三项」升级为「App 主动声明语义锚点」——再次验证 [[意图模式规范]] 质量决定端侧路由上限；且与「App 界面私有内容不自动开放」边界一致（需开发者显式 opt-in）。
- **IntentValueQuery**：把 App 结构化查询能力暴露给 Siri/Spotlight，做「意图级」检索而非字符串匹配，与 IndexedEntity 语义索引互补。
- **Confirmations and entity ownership（确认与实体归属）**：声明实体归属（`shared`/`public`/`unknown`），**Confirmation UI 据此差异化提示**（删别人的 vs 删自己的）——回填 [[Confirmation UI 安全机制]] 的 Apple 侧落地。
- **App Intents 2.0（与 Session 343 同期，多源交叉确认）**：① **Streaming responses**（边算边回传，改善搜索类感知延迟）；② **更富实体类型**（Siri 从关键词匹配升级为在 App 数据模型上做意图理解）；③ **Conversational follow-ups**（单次调用内多轮细化，一等公民模式）。迁移**增量式**，旧 Intent 继续工作，按意图 opt-in。
- **隐私治理侧（Extensions）**：Claude/GPT/Gemini 作 **Extensions** 直连 Siri，切换对用户透明，但**任何提供商建 Extension 须经 App Review + App Store 分发**——把多模型路由纳入 Apple 审查治理，与 [[Agent Workspace 隔离执行]] 的「受控发现 + 审批」同构。
- ⚠️ 未独立确认：「Per-Intent Privacy Manifest」作为独立 API 名称本次一手检索未能从 Apple 官方文档确认（Apple 有 PrivacyInfo.xcprivacy 隐私清单机制，但是否有「按意图粒度」专用清单 API 待官方文档确认）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]]
- 概念基础：[[Apple Intelligence 与 App Intents]]
- 跨平台对比：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Agentic OS 意图调度内核]]
- 安全：[[Confirmation UI 安全机制]]
- 概念基础：[[Apple Intelligence 与 App Intents]]
- 跨平台对比：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]]
- 安全：[[Confirmation UI 安全机制]]

#标签/Apple #标签/AppIntent #标签/SchemaProtocol
