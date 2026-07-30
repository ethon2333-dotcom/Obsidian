---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, 安全, ConfirmationUI, 概念]
---

# Confirmation UI 安全机制

## 一句话定义

**Confirmation UI（确认界面）/ Step-up Auth** 是系统在执行敏感意图（支付、发信、删除）前强制弹出的确认与授权层，确保「人类始终在环」，且沙盒化、声明式授权只响应 App 明确暴露且获许可的能力。

## 为什么重要

- 不经过确认层，AI 控制手机就得依赖「录屏 + 模拟点击」，隐私与误操作风险极大。
- 高危动作的系统级确认应是**平台强制层**，而非交给开发者各自实现（否则会漏）。

## 适用边界

- 区分「可逆/低频动作」（可静默）与「不可逆/高危动作」（必须确认）。
- 与隔离执行互补：确认解决「是否执行」，隔离解决「执行域泄漏」（见 [[Agent Workspace 隔离执行]]）。

## 证据与例子（四平台对照）

| 平台 | 机制 |
|------|------|
| Apple | `OwnershipProvidingEntity`（EntityOwnership `.shared`/`.public`/`.unknown`）差异化提示；高危 Intent 系统级拦截 |
| Windows | Agent Workspace 隔离会话 + 低权限账号 + ACL/审计/吊销；敏感步骤显式同意；连接器 OAuth |
| HarmonyOS | 可信设备能力协商；上下文充足时免二次确认；跨设备安全通道 |
| Android | UI Automation 对购买等敏感动作「执行前预警」；用户可经通知/live view 接管 |

## 可复用启发

- OS Agent 设计 Checklist：高危动作 = 系统级 Confirmation UI + 沙盒授权 + 可中断。
- 归属判定（EntityOwnership）让确认提示更精准，减少误确认。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入防护：[[XPIA 跨提示注入]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]

#标签/安全 #标签/ConfirmationUI #标签/StepUpAuth
