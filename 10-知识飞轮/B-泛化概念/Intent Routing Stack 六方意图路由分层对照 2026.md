---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-01]]"
tags: [AppIntent, 路由分层, 跨平台对照, IntentRoutingStack, 概念]
aliases: [意图路由分层, 六方路由对照]
---

# Intent Routing Stack 六方意图路由分层对照 2026

## 一句话定义

**Intent Routing Stack（意图路由栈）** 是把「一句自然语言 → 正确 App 能力 + 正确参数 + 正确设备」的完整链路拆成 **六个可比较的层**——**能力声明 / 发现与索引 / 相关性提示 / 路由决策 / 参数填充 / 跨设备**——用同一张表横向对齐 Apple、Android、HarmonyOS、Windows 与新出现的第五类玩家（荣耀 AgenticOS、阶跃 Step AOS、卓易 DroiClaw），使各平台差异从「术语不同」还原为「同一层的不同实现」。

## 为什么重要

- 四平台各自造词（Schema / AppFunction / Skill / MCP 连接器），横向比较长期靠感觉。**分层后才能判断「谁在哪一层缺件」**，而不是比谁的发布会更响。
- 2026 年第五类玩家（Agentic OS）加入后，「四平台对照」必须升级为「**六方对照**」——本库长期挂起的「Registry / 权限横向 Checklist」正应按此六层×六方展开（见 [[Agentic OS 意图调度内核]]）。
- 分层直接暴露**共识与缺口**：能力声明层四家已趋同，**相关性提示层与跨设备层只有 Apple 与新玩家给出机制，Android / Windows 仍空白（待补）**。

## 适用边界

- 本矩阵是**结构对照工具**，不是评分表；各家在同一层的成熟度差异巨大（如 Windows 的颗粒度是 agent 而非细粒度 intent）。
- 新玩家一列为**厂商口径**，多数无开发者文档与第三方验证，仅可作结构定位，不可作能力承诺。
- 层与层之间并非严格串行：端侧 Planner 可能把「发现」与「路由决策」合并在一次前向里（见 [[Simple Attention Network 无FFN端侧路由]]）。

## 证据与例子（六层 × 六方矩阵，来源 [[AppIntent 每日情报 2026-08-01]]）

| 层 | Apple | Android | HarmonyOS | Windows | 新一类（AgenticOS / Step AOS / DroiClaw） |
|---|---|---|---|---|---|
| 能力声明 | App Intents + Schema | `@AppFunction` + KDoc | Skill（`describe`/`execute`）+ 意图框架 | MCP / 连接器 | 原子能力引擎（Step）/ 生态层（荣耀） |
| 发现与索引 | Spotlight / IndexedEntity | OS Registry | 意图框架注册工具能力 | ODR 受控发现 | 统一语义数据层（Step） |
| 相关性提示 | **`RelevantEntities`（新）** | 待补 | 负一屏近场感知 + LBS | 待补 | 认知记忆自适应沉淀（荣耀） |
| 路由决策 | 端侧模型 + 云端大模型 | Gemini（私测） | 图推理引擎（子任务 DAG 并行） | Copilot | **意图/任务成为内核调度单元** |
| 参数填充 | Slot-filling / `$label.requestValue` | 结构化参数 | Want 参数 | 连接器 schema | 语义文件 |
| 跨设备 | **`SyncableEntity`（新）** | 待补 | 分布式软总线 / 端 A2A | 待补 | 统一记忆 + 任务迁移（荣耀） |

- **跨设备层的 2026 共识**：Apple 用 `SyncableEntity` 解决「跨设备指同一个实体」，荣耀用「统一记忆 + 任务迁移 + 失败换端重试」，Step AOS 用「统一语义数据层」——**三家路径不同，但都承认『上下文必须归属于人，而不是归属于某台设备』**。
- **能力声明层的收敛方向：越薄越好、越结构化越好**。Needle 证明既然工具 schema 本来就写在 prompt 里，Planner 就不需要世界知识，可砍掉 FFN——从模型架构侧反向验证 [[Intent Schema Protocol 意图模式规范]]：**Schema 越规范自解释，Planner 可以越小**；反过来 Schema 写得含糊（如 AppFunctions 的 KDoc 写成给人看的注释），再大的模型也救不回来。
- **性能语义开始进入 Schema 设计**：`EntityCollection` 是被低估的信号——Apple 明确承认「**解析实体本身是有成本的**」，并给出「只传 ID 不解析」的逃生门（见 [[Apple AppIntents Schema Protocol 2026]]）。

## 可复用启发

- 做 OS 侧 Schema 规范时，应把「**需要完整实体的语义操作**」与「**只需标识符的批量操作**」的二分**写进规范**，而不是等开发者踩坑。
- 任何新平台入场，先用这六层定位它「补了哪层、缺了哪层」，再判断其叙事含金量。
- 「相关性提示」层是当前最容易被忽略、也最能拉开体验差距的一层：它决定系统能否在用户开口前把对的内容送到对的情境。

- [ ] Android / Windows 在「相关性提示」与「跨设备」两层是否有未公开机制？待一手源核实。
- [ ] 新玩家的「意图注册」属于哪一层的权限模型——能力声明层还是发现层？谁能注册、需何审核（见 [[Agentic OS 意图调度内核]]）。
- [ ] 六层中是否应补第七层「**执行后可逆**」（见 [[Confirmation UI 安全机制]] 的「可逆」维度）？

## 关联

- 来源：[[AppIntent 每日情报 2026-08-01]]
- 规范：[[Intent Schema Protocol 意图模式规范]] ｜ 路由：[[Intent Router 语义路由]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Agentic OS 意图调度内核]]
- 执行通道：[[端侧执行通道 GUI 与 MCP 路线之争]] ｜ 端侧模型：[[Simple Attention Network 无FFN端侧路由]]

#标签/路由分层 #标签/跨平台对照 #标签/AppIntent
