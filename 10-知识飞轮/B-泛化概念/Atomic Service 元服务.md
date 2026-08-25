---
type: concept
aliases: [元服务]
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, HarmonyOS, 元服务, 概念]
---

# Atomic Service 元服务

## 一句话定义

**元服务（Atomic Service）** 是 HarmonyOS 的「免安装能力单元」：声明 `installationFree: true`，系统凭 `Want` 意图直接拉起，用户无需下载安装 App 即可被意图触发并完成任务闭环。

## 为什么重要

- 把 App 拆成可被发现的能力单元，是「意图即服务」的载体——零开 App 完成编排。
- 与 Apple headless / Android 设备端 MCP 殊途同归：App 退化为可被系统 Agent 调度的能力（见 [[Intent Schema Protocol 意图模式规范]]）。

## 适用边界

- 限定 HarmonyOS / 鸿蒙生态；其他平台用等价机制（Apple App Intent / Android AppFunction）承载。
- 依赖 ArkAF 三层框架与 A2UI 动态 UI 才能完整编排（见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]）。

## 证据与例子

- **`installationFree: true`**：免安装即被意图触发。
- **`Want` 拉起**：标准意图对象承载 action/bundle/实体，系统据此发现并拉起目标元服务。
- **编排实例**：菜单规划 → 叮咚买菜 Agent 加购 → 下单，全程零开 App。

## 可复用启发

- 「免安装能力单元」降低用户触达摩擦，是意图生态的加速器。
- 与 A2A 配合可实现多服务直连编排（见 [[A2A 端侧智能体协议]]）。

## 深化补充

- **具体能力声明形态**：除 `installationFree: true` 外，元服务通过 `insight_intent.json` 声明 `@InsightIntentEntry` / `@InsightIntentEntity`，暴露 `IntentActionInfo`（动作）与 `IntentEntityInfo`（实体）；`executeMode` 区分 **foreground（用户可见）** 与 **background（无界面执行）**，系统据此决定是否需 Confirmation UI（见 [[Confirmation UI 安全机制]]）。
- **跨服务传播入口**：`shareIntent` 是元服务对外共享意图的 API，但受平台配额约束（实测**单 App 单日 ≤20 次、单条目 ≤50KB**），这是「多服务直连编排」的隐形天花板，也是 [[A2A 端侧智能体协议]] 端侧多 Agent 协作的可行性判据之一。
- **与 Android 对照**：Android `AppFunctions` 无等价免安装单元，仍走「已安装 App + 声明能力」（见 [[Android AppFunctions 设备侧意图 2026]]）；元服务的 `installationFree` 是鸿蒙独有的低摩擦形态。

- [ ] HarmonyOS 元服务的 `IntentActionInfo` / `IntentEntityInfo` 是否携带来源/分级字段？若否，则落入 [[数据溯源分级与单调棘轮]] 指出「四大 OS 元数据无 provenance」的靶面。
- [ ] `executeMode: background` 的无界面元服务如何做「人类在环」确认？复用 Confirmation UI 还是另有通道？
- [ ] 端侧 A2A 多三元服务互写互调时，元服务能否成为 [[文档型 XPIA 自传播蠕虫]] 的写回载体？四平台均无公开评估。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[HarmonyOS Intents Kit 与 ArkAF 2026]]
- 范式：[[Intent Schema Protocol 意图模式规范]] ｜ [[A2A 端侧智能体协议]]

#标签/元服务 #标签/HarmonyOS #标签/AtomicService
