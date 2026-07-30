---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags:
  - AppIntent
  - HarmonyOS
  - IntentsKit
  - ArkAF
  - 元服务
---

# HarmonyOS Intents Kit 与 ArkAF（2026）

> 全新主题，库内此前无对应笔记。聚焦鸿蒙「意图即服务」技术栈：Intents Kit + 元服务 + ArkAF 三层。

## 一句话定义

HarmonyOS 以 **Intents Kit（`Want` 意图对象）+ 元服务（Atomic Service, `installationFree: true`）+ ArkAF 三层框架（意图框架 + Skills 框架 + 端侧 A2A 框架）** 实现「免安装、跨设备、意图即服务」的 Agent 编排。

## 为什么重要

- **免安装触发**：元服务 `installationFree`，系统凭 `Want` 直接拉起能力，零开 App 完成闭环。
- **端侧 A2A**：ArkAF 的端侧 Agent-to-Agent 框架让多个元服务直接对话编排（如菜单规划 → 叮咚买菜 Agent 加购 → 下单）。
- **动态 UI**：A2UI 根据意图动态生成界面，避免固定 App 壳。

## 适用边界

- 限定 HarmonyOS / 鸿蒙生态；与 Android AppFunctions（[[Android AppFunctions 设备侧意图 2026]]）思路相似但协议独立。
- 跨设备传输依赖可信设备能力协商 + 安全通道。

## 证据与例子

- **`Want`**：标准意图对象，承载 action / bundle / 实体，系统据此发现并拉起目标元服务。
- **元服务**：`installationFree: true`，用户无感安装即可被意图触发（见 [[Atomic Service 元服务]]）。
- **ArkAF 三层**：意图框架（解析调度）+ Skills 框架（能力封装）+ 端侧 A2A 框架（Agent 直连）。
- **A2UI**：意图即服务过程中动态生成 UI，而非跳转固定页面。
- **可信协商**：上下文充足时免二次确认；跨设备走安全通道。
- **AI 辅助**：编码辅助可一句话生成意图，降低接入门槛。

## 可复用启发

- 「元服务 + 意图」是把 App 拆成可被发现的能力单元，与 Apple headless / Android MCP 殊途同归（见 [[Intent Schema Protocol 意图模式规范]]）。
- 端侧 A2A 是多 Agent 协作的底层协议范式（见 [[A2A 端侧智能体协议]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 概念：[[Atomic Service 元服务]] ｜ [[A2A 端侧智能体协议]] ｜ [[Intent Schema Protocol 意图模式规范]]
- 跨平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]

#标签/HarmonyOS #标签/IntentsKit #标签/元服务 #标签/ArkAF
