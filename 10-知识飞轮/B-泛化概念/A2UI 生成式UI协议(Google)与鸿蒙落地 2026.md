---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-09-12]]"
tags: [AppIntent, A2UI, 生成式UI, HarmonyOS, 跨平台]
aliases: [A2UI, 生成式UI协议, AGenUI]
---

# A2UI 生成式 UI 协议（Google）与鸿蒙落地（2026）

> 全新主题，库内此前无对应笔记。聚焦「意图即服务」里被长期忽略的一环——**Agent 产出物如何渲染成 UI**。Google 提出 A2UI（Agent-to-UI）协议，高德在鸿蒙侧给出首个跨平台落地样本 AGenUI。

## 一句话定义

**A2UI（Agent-to-UI）** 是一套让 AI 大模型把「界面意图（UI intent）」以**结构化协议**输出、由宿主端原生渲染的规范——模型只生成「要什么界面」，不生成像素/HTML，宿主按自身组件体系渲染，实现「一次生成、多端原生适配」。

## 为什么重要

- **补上「意图即服务」的最后一环**：HarmonyOS 的 ArkAF（意图框架 + Skills + 端侧 A2A）解决了「理解意图→调度能力」，但「结果怎么呈现」长期靠 A2UI 概念占位；A2UI 把「动态 UI 渲染」从概念落成机制。
- **跨平台可迁移**：A2UI 是 Google 主导的开放协议，理论上同一份 UI intent 可被 Android / HarmonyOS / Web 各自原生渲染——这是四平台意图框架里**唯一明确跨平台（非厂商锁定的）UI 层协议**。
- **控成本 + 控安全**：模型不吐完整前端代码，只吐结构化 intent，体积/延迟远低于直接生成 HTML/JS，也降低了「模型生成可执行 UI」带来的注入面。

## 适用边界

- 适用：Agent 返回**结构化结果需可视化**的场景（列表、卡片、表单、地图标记等）；多端（手机/车机/XR/桌面）需一致语义但不同渲染。
- 不适用：需要精确定制视觉/交互的复杂页面（A2UI 管「语义骨架」不管「美术细节」）；富交互表单仍由宿主组件承载。
- 依赖：宿主端必须有「UI intent → 原生组件」的映射表与渲染器（高德 AGenUI 即鸿蒙侧的该渲染器）。

## 证据与例子

- **Google A2UI 协议（上游）**：以 C++ 跨平台引擎为核心，把大模型生成的「界面意图」直接转化为目标平台原生组件；定位为开放协议，非单厂商私有格式。
- **高德 AGenUI（鸿蒙首个落地，2026-09 窗口）**：鸿蒙首个生成式 UI 开源框架，**明确基于 Google A2UI 协议**，以 C++ 跨平台引擎为核心，将 AI 大模型生成的界面意图直接转化为**鸿蒙原生组件**渲染，**无需为不同设备单独适配调试**。来源：<https://baike.baidu.com/item/%E9%B8%BF%E8%92%99%E5%BA%94%E7%94%A8%E7%94%9F%E6%80%81/67746673>（百度百科，媒体口径，**待高德官方仓库/文档核验协议字段是否逐字遵循 A2UI**）。
- 对照：HarmonyOS 自有 A2UI 概念（[[HarmonyOS Intents Kit 与 ArkAF 2026]] 08-17 节「A2UI = 根据 Skill 返回的结构化数据动态渲染界面」）此前是鸿蒙内闭环；AGenUI 的意义在于**首次把外部开放协议（Google A2UI）接进鸿蒙原生渲染**，使「意图即服务」的 UI 层具备跨平台可迁移性。

## 可复用启发

- 做 OS 级意图框架时，**UI 渲染层应协议化、与生成层解耦**——模型产出「UI intent」而非「UI 代码」，宿主负责原生渲染，是兼顾跨端、成本、安全的范式（与 [[Intent Schema Protocol 意图模式规范]] 的「参数签名级解耦」同源）。
- **跨平台机会点**：四平台里 Apple/Android/Windows 的意图框架都未公开 UI 渲染协议；A2UI 作为 Google 主导的开放协议，是潜在的「跨 OS Agent UI 互操作」枢纽（类似 MCP 之于工具、A2A 之于 Agent）。

## 与其他概念的关系

- **上游**：[[Intent Schema Protocol 意图模式规范]]（UI intent 是意图.schema 的渲染延伸）｜ [[意图框架·跨体系索引 MOC]]。
- **互补**：[[HarmonyOS Intents Kit 与 ArkAF 2026]]（AGenUI 是其中 A2UI 层的跨平台落地）｜ [[Atomic Service 元服务]]（元服务的「免安装界面」天然适配 A2UI 动态渲染）。
- **跨平台**：[[A2A 端侧智能体协议]]（A2UI 是 Agent 间的「UI 协商」层，与 A2A 的「能力协商」互补）。

## 开放问题 / 未决

- [ ] 高德 AGenUI 是否逐字遵循 Google A2UI 协议字段？当前仅百度百科媒体口径，待官方仓库/文档核验（**待补**）。
- [ ] A2UI 与 Apple App Intents 的 `View Annotations` / SwiftUI 渲染、Windows Copilot Vision 的屏幕感知渲染，三者能否映射到同一 UI-intent schema？（**待补**，跨平台对比缺口）。

#标签/A2UI #标签/生成式UI #标签/HarmonyOS #标签/跨平台
