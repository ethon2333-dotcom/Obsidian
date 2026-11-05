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

## 反例与边界（隔离执行的盲区）

- **合法权限读不可信数据**：进程/账号隔离管的是「执行主体」，管不了「Agent 有合法权限却读到被污染原文」——Stored IPI 在 Dual LLM 下仍有 53.3% 命中（见 [[Dual View 智能体数据视图隔离]]）。隔离必须叠加**数据形态隔离**才闭环。
- **隔离 ≠ 免疫注入**：隔离把爆炸半径锁死，但 Agent 在隔离域内仍可能被注入并执行域内动作；须与 [[Confirmation UI 安全机制]]（敏感操作确认）+ 流量级检测（[[Agent Data Injection 数据注入攻击]] 的 Project Perception）组合。
- **实现成本门槛**：独立低权限账号 + 签名 + ACL 在移动端接口形态未标准化，Android / iOS 能否直接复用 Windows 范式待补（见上方待办）。

## 2026-09-13 增补：Microsoft Execution Containers 把隔离升为容器级（来源 [[AppIntent 每日情报 2026-09-13]]）

> 接续 08-03 的「数据形态隔离是正交维度」与 08-04 的「Project Perception 流量级检查」。本期 Windows 在 IFA 2026 公布的 **Microsoft Execution Containers** 把本笔记「独立低权限账号 + ACL」的进程/账号隔离进一步落为**内建沙箱容器**——隔离粒度更明确，且强制企业安全策略 + 全量活动日志。

- 这是四平台里**最明确的 OS 内建 Agent 容器隔离原语**：此前 Windows 用「独立账号 + ACL + 受控文件夹」（07 月四支柱），现在命名并强化了容器层；与 Apple（Extensions 经 App Review + Confirmations）、Android（系统代持一次性授权 + EXECUTE_APP_FUNCTIONS blanket）、HarmonyOS（芯片级可信根）形成对照。详见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 09-13 增补 + [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- ⚠️ 仍待 Microsoft 官方文档确认：Execution Containers 是否复用 Agent Workspace 容器、是否受 `Experimental agentic features` 同一 opt-in 管控、与 ODR 注册关系。

## 关联

- 索引：[[意图框架·跨体系索引 MOC]]
- 来源：[[AppIntent 跨平台情报简报 2026-07-30]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]
- 安全：[[Confirmation UI 安全机制]] ｜ [[XPIA 跨提示注入]] ｜ [[Dual View 智能体数据视图隔离]]

## 2026-09-15 增补：Agent 代码签名 + 证书校验/吊销把隔离范式补上「身份可信」（来源 [[AppIntent 每日情报 2026-09-15]]）

> 接续 09-13 的「Microsoft Execution Containers 容器级隔离」。本期 Windows 在隔离范式上补了**身份级**一块：Agent 二进制须数字签名 + 证书校验，被入侵或行为不当可吊销。

- 此前本笔记记录的 Windows 隔离范式 = 独立低权限账号 + ACL + 受控文件夹 + 容器级 Execution Containers（09-13）；本次新增**签名/吊销**意味着隔离不仅是「跑在哪儿、权限多大」，还管「**这个 Agent 主体本身是否可信、能否被撤销**」——把 07 月「Agent 须数字签名」从一句话落成可撤销的身份机制。
- 与 Android（系统特权签名 `EXECUTE_APP_FUNCTIONS_TRUSTED`）、HarmonyOS（芯片级可信根 TEE）形成对照：三者都用「签名/可信根」给 Agent 主体背书，但 Windows 额外强调**运行时可吊销**，是身份级治理最显式的样本。详见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 09-15 增补 + [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- ⚠️ 仍待 Microsoft 官方文档确认：签名/吊销是否纳入 ODR 注册信任链、是否受同一 opt-in 开关管控。

## 2026-10-08 增补：MXC GA 把隔离升为 GA 级「五档可调」容器级（来源 [[AppIntent 每日情报 2026-10-08]]）

> 接续 09-13「Microsoft Execution Containers 把隔离升为容器级」与 09-15「签名/吊销补身份可信」。本期 MXC 由 preview 升 **GA**，把本笔记「独立低权限账号 + ACL + 受控文件夹 + 容器级」再推进为**五档可调的 GA 级隔离栈**。

- **五档隔离粒度（GA 官方确认）**：进程 / 会话 / WSL 容器（WSLc，Build 2026 随 WSL 3）/ 虚拟机 / Windows 365 for Agents——组织按 workload 选隔离形状，而非「一种沙箱 fits all」。
- **身份分离是隔离的第二支柱**：每个动作归到 agent 而非用户，IT 可区分两者；GitHub Copilot 演示中 Defender 拦截恶意网页指令并切断 agent 的 SharePoint 访问、不影响用户——把「隔离域内的爆炸半径」与「可归因于哪个主体」解耦，是隔离范式的身份级补全（与 09-15 签名/吊销同方向但不同机制：吊销针对 agent 二进制，身份分离针对运行时动作归属）。
- **沙箱外盲区（诚实标注）**：内置文件工具、远程 MCP server 不在 OS 级沙箱内——意味着「隔离执行」对这两类动作不保证 OS 强制边界，须叠加 [[Confirmation UI 安全机制]]（敏感动作确认）+ 流量级检测（Project Perception）。
- → 对四平台对照：Windows 现以 **GA 级五档容器隔离 + 运行时身份分离** 领先（Apple Extensions 经 App Review + Confirmations / Android 系统特权签名 `EXECUTE_APP_FUNCTIONS_TRUSTED` / HarmonyOS 芯片级可信根 TEE 均为不同层级的隔离/可信原语）。详见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 10-08 增补 + [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- ⚠️ 仍待 Microsoft 官方文档确认：MXC 与既有 Agent Workspace 容器/独立账号的关系（复用还是并列）、是否受 08-02 `Experimental agentic features` 同一 opt-in 管控、沙箱外两类动作的治理归属。

#标签/隔离执行 #标签/AgentWorkspace #标签/安全

## 2026-09-26 增补：Copilot Managed Runtime = 租户内沙盒执行总线的 SaaS 侧样板（来源 [[AppIntent 每日情报 2026-09-26-晚]]）

> 接续 09-13「Microsoft Execution Containers 容器级隔离」与 09-15「Agent 代码签名/吊销」。本期把微软 09-25 Copilot 重架构中的 **Copilot Managed Runtime** 映射到本笔记「隔离执行」范式——它是 SaaS 层而非 OS 层的隔离产物。

- **Managed Runtime 把「隔离 + 身份 + 审计」落到租户级**：Code 生成的 App 跑在 M365 租户内的**隔离环境**，由 IT 治理、出现在 M365 管理中心供策略审查；这与本笔记 07 月「独立低权限账号 + ACL + 受控文件夹」、09-13「Execution Containers 容器级」构成**跨层级呼应**——隔离范式的核心三件套（跑在哪儿/权限多大/能否被审计吊销）在 SaaS 侧被微软产品化。
- **与四平台 OS 隔离范式对照**：Windows（Agent Workspace 容器 + 独立账号 + 签名/吊销）/ Android（系统特权签名 `EXECUTE_APP_FUNCTIONS_TRUSTED`）/ HarmonyOS（芯片级可信根 TEE）/ **M365 Managed Runtime（租户沙箱）**——四者都在回答「agent 在哪跑、权限多大、能否被治理」，但层级不同（OS 内核级 vs SaaS 租户级）。
- ⚠️ 层级纪律：Managed Runtime 属 M365/Entra 治理与执行层，**不是 Windows OS 执行总线（ODR/Agent Workspace）的扩展**；勿写成「Windows OS 已内建托管运行时」。来源为微软 09-25 官方博文转述（byteiota/codiot/gadgetbond），沙箱语法/SDK 与 GA 日期待 learn.microsoft.com 复核。

## 2026-10-02 增补：连接器白名单 = 执行边界，consent 时长 = 授权窗口（来源 [[AppIntent 每日情报 2026-10-02]]）

> 接续 09-26「Copilot Managed Runtime 租户级隔离」。本期 Windows 在 26H2 中首次公开 **agent 连接器治理策略项**，把本笔记的「隔离 = 执行边界」进一步落到可配置控制面。

- **`AgentConnectorAccessPolicy`（连接器白名单）**：限制 Agent 可访问的 MCP server/host 范围——本质是**把「隔离边界」从账号/文件夹级推进到「工具/连接器级」**：Agent 即使被注入，能调用的外部工具也被策略收窄，直接压低 XPIA 横向移动面。与 09-13 Execution Containers（容器级）、07 月「独立账号 + ACL + 受控文件夹」构成**账号→文件夹→容器→连接器**四层收窄的隔离栈。
- **`AgentConsentDuration`（授权持久化时长）**：控制 consent 决定保留多久——把 [[Confirmation UI 安全机制]] 的「每次敏感动作显式同意」从「每次」变成「可设窗口」，是确认机制的**持久化治理维度**；窗口越长，被劫持后的行动窗口越大，需与最小权限权衡。
- **版本割裂**：上述两项 + `ConfigureAgentConnectors` + `DisableSettingsAgent` **仅企业版/教育版/IoT 企业版**可配置；家庭版/专业版无法关闭或白名单化连接器——意味着「隔离边界可治理」在消费市场实际缺位，与 EU AI Act Article 15 抗注入可举证性要求存在落差（见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 10-02 增补）。
- ⚠️ 层级纪律：来源 cnBeta/163 引 Neowin，**待 learn.microsoft.com 逐字复核**策略项命名与版本限制。
