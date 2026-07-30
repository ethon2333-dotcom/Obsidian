---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags:
  - AppIntent
  - Windows
  - CopilotActions
  - AgentWorkspace
---

# Windows Copilot Actions 与 Agent Workspace（2026）

> 全新主题，库内此前无对应笔记。聚焦 Windows 的「系统级 Agent 执行总线」：Copilot Actions + Agent Workspace + ODR + XPIA 防护。

## 一句话定义

Windows 以 **Copilot Actions**（跨 App + 云连接器链式执行）+ **Agent Workspace**（隔离桌面会话）+ **On-Device Registry (ODR)**（受控发现 MCP 连接器）构建系统级 Agent 执行总线，并把 **XPIA（跨提示注入）** 列为头号新型风险。

## 为什么重要

- **隔离执行最成体系**：Agent Workspace 为独立隔离桌面会话，每个 Agent 以专属低权限账号运行，受 ACL / 审计 / 吊销约束，Agent 须数字签名。
- **受控发现**：连接器注册于 ODR，避免任意 Agent 被随意调用（缓解 XPIA 横向移动）。
- **用户始终在环**：敏感步骤（如购买）显式征求同意，连接器走 OAuth（Outlook / OneDrive / Gmail）。

## 适用边界

- 限定 Windows 桌面 / Copilot 生态。
- Copilot Vision 为 session-bound、显式 opt-in 的屏幕 OCR / UI 检测，非默认开启。

## 证据与例子

- **Copilot Actions**：在 Agent Workspace 内跨 App + 云连接器链式执行（如整理邮件 → 存 OneDrive → 起草回复）。
- **Agent Workspace**：隔离桌面会话、低权限账号、ACL / 审计 / 吊销、Agent 数字签名。
- **ODR（On-Device Registry）**：MCP 连接器注册于此，受控发现；未注册连接器不可被 Agent 调用。
- **XPIA**：UI / 文档中嵌入恶意指令劫持 Agent，是新型攻击面；缓解 = ODR 受控发现 + 会话隔离 + 用户中断（见 [[XPIA 跨提示注入]]）。
- **Copilot Vision**：session-bound、显式 opt-in 的屏幕感知，与 Android UI Automation（[[工业级 GUI Agent 架构（VLM+无障碍树）]]）思路互补。

## 可复用启发

- 「隔离会话 + 低权限账号 + 签名 + ACL」是本地 Agent 安全执行的标杆范式，可迁移到任何 OS Agent（见 [[Agent Workspace 隔离执行]]）。
- 高危动作必须显式同意 + OAuth，不能静默（见 [[Confirmation UI 安全机制]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 安全：[[Agent Workspace 隔离执行]] ｜ [[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]]
- 跨平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]

#标签/Windows #标签/CopilotActions #标签/AgentWorkspace #标签/XPIA
