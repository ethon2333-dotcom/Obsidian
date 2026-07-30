---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, 安全, XPIA, 注入, 概念]
---

# XPIA 跨提示注入

## 一句话定义

**XPIA（Cross-Prompt Injection Attack）** 是在 UI、文档、网页或屏幕内容中嵌入恶意指令，劫持正在运行的操作系统 Agent，使其执行非用户本意的操作（如借 Agent 权限发消息、转账、泄露数据）。

## 为什么重要

- 系统级 Agent 拥有真实的跨 App 操作权限，XPIA 是其头号新型攻击面（Windows 已将其单列风险）。
- 与传统 prompt injection 不同：XPIA 来源是「环境上下文」（屏幕/文档），而非用户对话，更难靠对话过滤拦截。

## 适用边界

- 任何具备屏幕感知（Copilot Vision / Android UI Automation）或多源输入的 OS Agent 都暴露此风险。
- 缓解不能只靠模型对齐，必须架构层防护。

## 证据与例子（四平台防护对照）

| 平台 | 主要缓解手段 |
|------|--------------|
| Windows | ODR 受控发现 + Agent Workspace 隔离会话 + 用户始终在环（interruptible） |
| Apple | 系统级 Confirmation UI 拦截高危 Intent；`OwnershipProvidingEntity` 差异化提示 |
| HarmonyOS | 可信设备能力协商；上下文充足免二次确认；跨设备安全通道 |
| Android | UI Automation 敏感动作「执行前预警」+ 用户接管 |

## 可复用启发

- OS Agent 设计 Checklist：受控发现（ODR）+ 隔离执行（[[Agent Workspace 隔离执行]]）+ 高危确认（[[Confirmation UI 安全机制]]）+ 用户可中断。
- 对屏幕感知能力（Copilot Vision 类）默认 session-bound + 显式 opt-in。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 确认：[[Confirmation UI 安全机制]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]

#标签/XPIA #标签/安全 #标签/注入
