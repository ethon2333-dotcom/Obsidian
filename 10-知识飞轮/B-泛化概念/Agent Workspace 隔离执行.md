---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, Windows, 隔离执行, 安全, 概念]
aliases: [隔离执行]
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

## 2026-08-03 增补：数据形态隔离是进程隔离的正交维度（来源 [[AppIntent 每日情报 2026-08-03]]）

DualView（arXiv 2607.03821）提出了一个比进程/账号隔离**粒度更细**的防护原语——**隔离数据的可见形态而非执行主体**：

- Windows Agent Workspace 隔离的是**执行主体**（低权限账号 + ACL + 独立会话）；DualView 隔离的是**数据形态**（AgentView 恒为符号 / HumanView 保原文）。两者**正交**，且后者覆盖前者盲区——**Agent 有合法权限读写的文件，内容本身却不可信**。
- 量化盲区：传统 Dual LLM 对即时型 IPI ASR≈0，但 **Stored IPI（存储型）仍 53.3%**（Claude Haiku 4.5）——攻击没绕过隔离机制，绕过的是隔离机制的**生命周期**（数据落盘还原后符号关系消失，被后续任务重读时高权限 LLM 直读原文）。
- 工程可行：OpenClaw 插件、仅用 tool hooks、不改 tool-call 逻辑、Git worktrees 双文件环境、可用性接近基线。**不需要重写 OS 即可落地**。
- 本库可主动提出的 OS 层产品建议：**是否把「Agent 视图文件系统」做成一等公民？** 四平台目前均无此设计。详见 [[Dual View 智能体数据视图隔离]]。

## 深化补充

- **Windows 的具体形态（一手源）**：Agentic 能力由「**实验性代理功能**」开关控制（默认**关闭**，需管理员在企业策略中显式启用）；每个 Agent 以**独立低权限账号**运行，文件访问被限制在**少量受控文件夹**，且 Agent 二进制须**数字签名**才能注册连接器；连接器经 **ODR** 受控发现，未注册不可被调用（见 [[Windows Copilot Actions 与 Agent Workspace 2026]]）。
- **与端点检测互补**：据 [[Agent Data Injection 数据注入攻击]] 2026-08-04 增补，**Project Perception（Defender for Endpoint）** 首次把「agent loop 的用户提示 / 工具调用 / 工具响应」当作可检查流量，在执行前阻断——把隔离从「进程/账号」推进到「流量级」。
- **数据形态隔离是正交维度**：[[Dual View 智能体数据视图隔离]] 指出进程隔离覆盖不了「Agent 有合法权限却读到不可信原文」，需 AgentView / HumanView 双视图补位。

- [ ] Windows 的「受控文件夹」具体清单与可配置性如何？待一手源核实。
- [ ] 隔离会话内的 Agent 输出能否被审计留存并对接 [[数据溯源分级与单调棘轮]] 的单调棘轮？
- [ ] 移动端（Android / iOS）能否复用「独立低权限账号 + 数字签名」隔离范式？接口形态待补。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]
- 安全：[[Confirmation UI 安全机制]] ｜ [[XPIA 跨提示注入]]

#标签/隔离执行 #标签/AgentWorkspace #标签/安全
