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

## 可复用启发

- 平台方应通过「声明式宏 + AI 辅助生成」把 App 接入成本压到极低（Apple `isAssistantOnly` 过渡）。
- 先固化统一的 Schema / Tool 描述规范（实体类型、Parameter Slot、EntityOwnership），这是跨 App 可被发现与编排的前提（见 [[Intent Schema Protocol 意图模式规范]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 概念基础：[[Apple Intelligence 与 App Intents]]
- 跨平台对比：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]]
- 安全：[[Confirmation UI 安全机制]]

#标签/Apple #标签/AppIntent #标签/SchemaProtocol
