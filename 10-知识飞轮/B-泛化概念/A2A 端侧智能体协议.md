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

## 2026-08-01 增补（HarmonyOS 端侧/云侧 A2A 双模，HDD 西安站，来源 [[AppIntent 每日情报 2026-08-02]]）

- **双模路由判据首次清晰化**：HarmonyOS 7（小艺开放平台）把 A2A 接入显式分为**端侧 A2A**（低时延 + 数据不出端）与**云侧 A2A**（复杂深度推理），开发者按业务场景选。
- **落地实证**：头部银行 App 经端侧 A2A 覆盖 1000+ 意图、多步执行、隐私不出端；O2O App 经云侧 A2A 走完「问答→选座→购票→支付」端到端闭环。
- **对范式的修正**：原「端侧直连优先」应升级为「**按时延/隐私 vs 推理深度划界**」——并非所有 Agent 协作都该在端侧。详见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- ⚠️ 待补：端侧 A2A 多 Agent 互写互调时的 XPIA 类别级评估（四平台均无）。

## 深化补充

- **重要区分（概念纠偏）**：本笔记原把 A2A 框定为「端侧多 Agent 直连」，但 **Agent2Agent（A2A）作为技术协议**，主体是 **Google 提出、2025-04 捐赠 Linux 基金会、2026-03 发布 v1.0** 的 **HTTP/JSON 跨框架网络协议**，与 HarmonyOS 的「端侧 A2A」是不同层级——前者解决「异构 Agent 框架如何跨网络对话」，后者是鸿蒙设备内/云侧的编排实现。
- **v1.0 关键形态**：
  - **AgentCard**：发布于 `/.well-known/agent.json`，机器可读地声明能力、技能、鉴权；v1.0 起支持**签名 AgentCard**（防伪造）。
  - **任务生命周期**：5 状态机 `submitted → working → input-required → completed / failed`，远端流式推送进度。
  - 与 MCP 互补：MCP 管「Agent 调工具」，A2A 管「Agent 调 Agent」（见 [[端侧执行通道 GUI 与 MCP 路线之争]]）。
- **与国标的关系**：A2A 的 AgentCard 能力描述段，与 [[智能体互联国家标准与 AIP]]「五段式」中的「能力描述 / 协同交互」高度同构，可作为跨厂商互认的技术底座之一。

- [ ] A2A v1.0 的「签名 AgentCard」能否直接对接 [[Agent 身份与硬件级审批]] 的硬件级信任根？待核实。
- [ ] HarmonyOS 端侧 A2A 与 Google A2A 协议是否互通？还是各自私有？需一手源。
- [ ] A2A 多 Agent 消息传递时的 provenance 链（见 [[数据溯源分级与单调棘轮]]）如何实现？v1.0 是否定义？待补。

## 反例与边界（何时 A2A 不成立）

- **强一致事务场景**：若任务需要跨 Agent 的原子性与回滚（如「下单且冻结库存」必须同时成功/失败），端侧 A2A 的分布式协作会放大一致性难题，此时集中式 Planner（见 [[System Orchestrator 系统编排]]）更合适。
- **跨厂商互信缺失**：HarmonyOS 端侧 A2A 与 Google A2A 协议是否互通尚未证实；缺乏统一 AgentCard 互认前，跨生态 A2A 易退化为私有总线孤岛。
- **敏感写回未隔离**：A2A 解决「谁调谁」，不解决「被调方是否被注入」——多 Agent 互写互调须叠加 [[Agent Data Injection 数据注入攻击]] 的元数据来源校验，否则反而放大攻击面。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]
- 范式：[[Atomic Service 元服务]] ｜ [[Intent Schema Protocol 意图模式规范]]

#标签/A2A #标签/多智能体 #标签/端侧
