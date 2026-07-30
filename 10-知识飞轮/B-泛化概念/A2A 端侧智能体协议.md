---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, A2A, 多智能体, 概念]
---

# A2A 端侧智能体协议

## 一句话定义

**端侧 Agent-to-Agent（A2A）** 是多个本地 Agent / 元服务之间直接对话、编排任务的底层协议，让「意图即服务」从「单 Agent 调一个工具」升级为「多能力单元协同完成复合任务」。

## 为什么重要

- 复合任务（如规划菜单 → 加购 → 下单）需要多服务协作，A2A 是跨元服务编排的骨架。
- 端侧直连降低延迟与云端依赖，也利好隐私（数据不出设备）。

## 适用边界

- 需配合意图框架 + Skills 框架（如 HarmonyOS ArkAF 三层）才能完整运作。
- 跨设备 A2A 依赖可信设备能力协商 + 安全通道。

## 证据与例子

- **HarmonyOS ArkAF**：意图框架 + Skills 框架 + 端侧 A2A 框架三层；A2UI 动态生成 UI。
- **编排实例**：菜单规划 Agent → 叮咚买菜 Agent 加购 → 下单 Agent，全程零开 App。
- **Android 思路**：Agent Bus 思路可作为设备侧多 Agent 协作参照。

## 可复用启发

- 多 Agent 协作应优先端侧直连（低延迟/隐私），跨设备再走安全通道。
- A2A 与 Schema Protocol（[[Intent Schema Protocol 意图模式规范]]）结合：能力先被描述，再被 A2A 编排。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]
- 范式：[[Atomic Service 元服务]] ｜ [[Intent Schema Protocol 意图模式规范]]

#标签/A2A #标签/多智能体 #标签/端侧
