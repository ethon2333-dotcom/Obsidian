---
type: concept
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

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[HarmonyOS Intents Kit 与 ArkAF 2026]]
- 范式：[[Intent Schema Protocol 意图模式规范]] ｜ [[A2A 端侧智能体协议]]

#标签/元服务 #标签/HarmonyOS #标签/AtomicService
