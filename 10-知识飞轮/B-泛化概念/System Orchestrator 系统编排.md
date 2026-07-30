---
type: concept
status: draft
derived_from: "[[OS PM 近一月情报简报 2026-07-31]]"
tags:
  - OS-Agent
  - Apple
  - SystemOrchestrator
  - 架构范式
---

# System Orchestrator 系统编排者

> 全新概念（2026-07 检索新增）。聚焦 iOS 27 把"跨 App 动作决策权"上收给系统级编排者的设计。相关平台卡见 [[Apple AppIntents Schema Protocol 2026]]；安全机制见 [[Confirmation UI 安全机制]]。

## 一句话定义

**System Orchestrator（系统编排者）** 是 OS 内的一层统一协调器：各 App 通过 App Intents 暴露能力，但 **App 之间不直接互相调用**，所有跨 App 动作统一由系统编排者解析、决策与执行——这一"不直接驱动"是**刻意为隐私与安全**的设计。

## 为什么重要

- **权限与隐私边界清晰**：动作由系统而非某个第三方 App 发起，Apple Intelligence 的用户个人化与私密性不被单个 App 打破。
- **编排权上收 OS 是 2026 共性范式**：Apple（System Orchestrator）、Windows（Agent Workspace 独立账号 + ODR）、HarmonyOS（小艺中枢）殊途同归——把"谁决定跨 App 动作"收归系统层。
- **为端侧语义路由提供落点**：编排者 + Spotlight 语义索引 + App Toolbox 共同完成跨 App 意图路由（见 [[Intent Router 语义路由]]）。

## 适用边界

- Apple 语境下与 Siri / Shortcuts 强绑定；跨平台对应物形态不同（Windows=Agent Workspace 会话隔离，HarmonyOS=小艺 Agentic 自演进架构）。
- 编排者本身不替代 Confirmation UI：高危动作仍由系统级确认拦截（见 [[Confirmation UI 安全机制]]）。

## 证据与例子

- WWDC26 Apple 智能小组实验室原话："a system orchestrator can take actions from many apps' App Intents across the system — apps don't drive each other directly. This routing is deliberate for privacy and safety."
- 路由链路：用户自然语言 → System Orchestrator → 解析意图 → 经 Spotlight 语义索引匹配实体 → 调度对应 App 的 App Intent 执行；多 App 复合任务由编排者串联。
- Platforms State of the Union 明确 App Intents 与 **System Orchestrator + Spotlight 语义索引 + App Toolbox** 协同。

## 可复用启发

- OS PM 在设计 Agent 平台时，应把"编排/决策"与"能力执行"解耦：App 只声明能力，系统层持有编排权与审计权。
- 把"App 不直接互驱"作为隐私默认姿态，可天然限制恶意 App 的横向移动（与 [[XPIA 跨提示注入]] 缓解思路一致）。

## 关联

- 来源：[[OS PM 近一月情报简报 2026-07-31]]
- 平台卡：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- 路由：[[Intent Router 语义路由]] ｜ 安全：[[Confirmation UI 安全机制]] ｜ [[XPIA 跨提示注入]]

#标签/OSAgent #标签/Apple #标签/SystemOrchestrator
