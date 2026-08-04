---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, SchemaProtocol, 概念]
aliases: [意图模式规范]
---

# Intent Schema Protocol 意图模式规范

## 一句话定义

**意图模式规范（Schema Protocol）** 是一套系统级、强类型的「应用能力描述契约」：开发者声明实体类型、参数槽（Parameter Slot）与归属（EntityOwnership），System Broker 据此完成 Discovery 与 Routing。它是「意图即服务」可被跨 App 发现与编排的前提。

## 为什么重要

- 没有统一 Schema，App 能力就是黑盒，系统 Agent 无法理解、无法编排。
- Schema 标准化程度决定生态黏性——率先占据系统级 Schema 与 Registry 的平台掌控意图分发入口（开发者从「抢应用商店排名」转向「拼意图匹配质量」）。

## 适用边界

- 四平台均采纳但协议独立，需各自适配；跨平台开发者成本仍高（呼应 [[国内安卓厂商做 App Intent 的阻力]] 的碎片化问题）。
- Schema 关注「能力描述」，不解决「端侧如何路由」（见 [[Intent Router 语义路由]]）与「如何安全执行」（见 [[Confirmation UI 安全机制]]）。

## 证据与例子（四平台对照）

| 平台 | Schema 机制 | 关键 API / 概念 |
|------|------------|----------------|
| Apple | 系统预定义 Schema + 声明式宏 | `@AppIntent(schema: .audio.addToPlaylist)`、`@AppEntity(schema: .messages.message)`（见 [[Apple AppIntents Schema Protocol 2026]]） |
| Android | 设备端 MCP 工具 + OS Registry | AppFunction 注册进 Android Registry，需 `EXECUTE_APP_FUNCTIONS`（见 [[Android AppFunctions 设备侧意图 2026]]） |
| HarmonyOS | `Want` + 元服务 | 意图对象承载 action/bundle，拉起 `installationFree` 元服务（见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]） |
| Windows | ODR 注册 MCP 连接器 | On-Device Registry 受控发现（见 [[Windows Copilot Actions 与 Agent Workspace 2026]]） |

## 可复用启发

- OS 设计应尽早固化统一的 Schema / Tool 描述规范：实体类型、Parameter Slot、EntityOwnership 三件套。
- 「声明式宏 + AI 辅助生成」把接入成本压到极低，是生态起量的关键杠杆。

## 深化补充

- **各平台 Schema 的机器可读落点（具体形态）**：
  - Apple：`@AppIntent(schema: .audio.addToPlaylist)` 声明式宏 + `EntityOwnership`（`.shared` / `.public` / `.unknown`）决定归属提示（见 [[Apple AppIntents Schema Protocol 2026]]、[[Confirmation UI 安全机制]]）。
  - Android：`@AppFunction` / `@AppFunctionServiceEntryPoint` 注解经 KDoc 编译产出 `AppFunctionMetadata`，注册进 Android Registry 需 `EXECUTE_APP_FUNCTIONS` 权限（见 [[Android AppFunctions 设备侧意图 2026]]）。
  - HarmonyOS：`insight_intent.json` 声明 `IntentActionInfo` / `IntentEntityInfo`，`Want` 承载 action/bundle（见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]）。
  - Windows：ODR 注册 MCP 连接器，受控发现（见 [[Windows Copilot Actions 与 Agent Workspace 2026]]）。
- **Schema 缺的第三列**：四平台 Schema 都描述「能力是什么」，但据 [[数据溯源分级与单调棘轮]] 复核，**均无 `source.type` / `classification` 字段**——即 Schema 不回答「这条能力声明能被伪造吗」，这是 ADI 攻击面（见 [[Agent Data Injection 数据注入攻击]]）。

- [ ] 能否把「来源类型枚举」作为 Schema 标准的可选扩展列，让各 OS 的 Registry 自带 provenance？需先验证四平台是否接受第三方元数据。
- [ ] Schema Protocol 与 [[智能体互联国家标准与 AIP]] 的「五段式」能力描述段如何映射？国标是否提供可迁移的字段定义？
- [ ] EntityOwnership 的 `.unknown` 在路由时如何处置——默认拒绝还是默认允许？待一手源核实。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 路由：[[Intent Router 语义路由]] ｜ 执行：[[Function Calling 端侧工具调用]] ｜ 安全：[[Confirmation UI 安全机制]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]]

#标签/SchemaProtocol #标签/AppIntent #标签/意图模式
