---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, Windows, 隔离执行, 安全, 概念]
---

# Agent Workspace 隔离执行

## 一句话定义

**隔离执行（Isolated Execution）** 是本地 Agent 的安全运行范式：Agent 在独立隔离的会话/沙箱中运行，以专属低权限账号、受 ACL/审计/吊销约束、且须数字签名，确保即使 Agent 被劫持也不会横向泄漏。

## 为什么重要

- 本地 Agent 拥有操作系统的真实权限，一旦被注入（[[XPIA 跨提示注入]]）危害极大；隔离是把爆炸半径锁死的关键。
- Windows Agent Workspace 是当前最成体系的实现，可作为其他 OS Agent 的安全设计标杆。

## 适用边界

- 桌面/移动 OS 均适用；实现成本高于「直接给 Agent 全权限」，但安全收益压倒性。
- 隔离解决「执行域泄漏」，与 Confirmation UI（见 [[Confirmation UI 安全机制]]）互补。

## 证据与例子

- **Windows Agent Workspace**：隔离桌面会话 + 每个 Agent 专属低权限账号 + ACL/审计/吊销 + Agent 须数字签名。
- **受控发现**：连接器注册于 ODR，未注册不可被调用，限制注入后的横向移动。
- **用户中断**：会话隔离 + 用户始终在环（interruptible）是 XPIA 主要缓解手段。

## 可复用启发

- OS Agent 安全 Checklist：隔离会话 + 低权限账号 + 签名 + ACL/审计 + 受控发现。
- 把「隔离 + 签名 + 受控发现」作为平台强制层，而非 App 自选。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]
- 安全：[[Confirmation UI 安全机制]] ｜ [[XPIA 跨提示注入]]

#标签/隔离执行 #标签/AgentWorkspace #标签/安全
