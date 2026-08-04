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

## 2026-07 增补（Agent Workspace 预览细则，来源 [[OS PM 近一月情报简报 2026-07-31]]）

- **四大新基元**：① Agent accounts（专属、受限、非交互 Windows 账号，ACL / Intune / MDM / 组策略可治理）；② Agent Workspace（独立轻量桌面会话，运行时隔离，轻于 VM）；③ Scoped file access（默认仅 **6 个 known folders：Documents / Downloads / Desktop / Pictures / Music / Videos**）；④ MCP（经 ODR 注册连接器，显式可审计）。
- **默认关闭 + 需 opt-in**：`Settings > System > AI components > Agent tools > Experimental agentic features`，**默认关**、需管理员开启、设备级生效；文件访问同意三档：Allow Always / Ask every time / Never allow。
- **XPIA（跨提示注入）** 列头号新风险：UI/文档嵌入恶意指令劫持 Agent → 数据外泄/装马；缓解 = 签名 Agent 二进制 + 防篡改日志 + 管理员开关 + 限定文件夹 + 会话隔离。
- **三原则**：Non-repudiation（Agent 行为可区分于用户）/ Confidentiality（不低于所消费数据安全标准）/ Authorization（用户审批所有数据查询与动作）。

## 可复用启发

- 「隔离会话 + 低权限账号 + 签名 + ACL」是本地 Agent 安全执行的标杆范式，可迁移到任何 OS Agent（见 [[Agent Workspace 隔离执行]]）。
- 高危动作必须显式同意 + OAuth，不能静默（见 [[Confirmation UI 安全机制]]）。

## 2026-08-02 增补（EU AI Act Article 15 对 OS Agent 执行安全的合规抬高，来源 [[AppIntent 每日情报 2026-08-02]]）

- **监管触发**：EU AI Act **Article 15（准确性/鲁棒性/网络安全）** 于 **2026-08-02 正式生效**（entry into force，依据 Article 113）。第 15(5) 条明确把 **prompt injection / 对抗样本 / 训练数据投毒 / 模型投毒** 列为高风险 AI 系统须抵御的攻击面；第 15(4) 条要求对「与系统/人交互产生的错误、故障」具备韧性，并防持续学习系统的反馈回路偏置。
- **对本笔记的直接含义**：Windows Agent Workspace（隔离会话 + 低权限账号 + ACL + 签名）+ ODR 受控发现 + 用户中断的 XPIA 缓解设计，此前是**产品 judgment 驱动**；Article 15 生效后，对落入 Annex III 高风险范畴的 EU 部署，这套设计变成**强制合规底线**——须可举证 prompt-injection 韧性、动作层（tool-use/API）网络安全、Article 12 不可篡改日志、Article 14 人类监督。罚则 €15M/3%（Article 99）。
- **跨平台同构**：Apple（Extensions 经 App Review + Confirmations+entity ownership）、Android（系统代持一次性授权 + EAP 受控发现）、HarmonyOS（源头可控/记忆安全/理解可控/计算闭环 + 芯片级可信根）各自的设计，都在 Article 15 下获得监管驱动力，而非仅由产品选择驱动。详见 [[XPIA 跨提示注入]] / [[Confirmation UI 安全机制]]。
- ⚠️ 口径：Digital Omnibus 一揽子修订拟推迟 Annex III 期限至 2027-12-02，但**截至 2026-08-02 尚未正式通过生效**，原 08-02 日期仍现行有效（跟踪正式文本）。

## 2026-08-04 增补（防线从「隔离」延伸到「检查」与「打标」，来源 [[AppIntent 每日情报 2026-08-04]]）

微软本周在 Windows Agent 安全上补了**两块此前空缺的拼图**，但要注意二者**都不在 OS 内建层**：

**① Project Perception（2026-08-03 进入公开预览）—— 端点侧检查 agent loop**

- Defender for Endpoint 直接检查 agent loop 的三段流量：**用户提示 / 工具调用 / 工具响应**，并在动作**执行前**阻断。
- 这在架构上是个转折：Agent Workspace 解决的是「Agent 跑坏了炸不到系统」（隔离），Project Perception 解决的是「Agent 在被骗的路上就被拦下」（检查）。**隔离 ≠ 检查**，此前 Windows 只有前者。
- 配套：红/蓝/绿三色 Agent 演练体系 + MDASH + MAI-Cyber-1-Flash；CyberGym 口径 **95.95–96%**（两处报道口径不一，模型名也有 MAI-Cyber-Flash-1 / MAI-Cyber-1-Flash 两种写法，**待官方确认**）。
- 对 ADI 的意义见 [[Agent Data Injection 数据注入攻击]]：这是首个把「工具调用/响应」当作可检查流量的端点机制。

**② Agent Governance Toolkit —— 数据来源分级（开源治理层，⚠️ 非 Windows 系统能力）**

- 六类来源枚举（`tool_output`/`api_response`/`agent_message`/`user_input`/`database`/`file`）+ 四级分类（`public→internal→confidential→restricted`）+ **单调棘轮**（只升不降）+ 两阶段闸口（`post_tool`/`pre_output`）。详见 [[数据溯源分级与单调棘轮]]。
- **对本笔记的关键校准**：已 WebFetch 复核 Windows agentic security 官方文档，**Windows OS 层至今没有数据来源分级机制**。Agent Workspace 的 scoped file access 管的是「能读哪个文件夹」（**位置**维度），不管「读进来的内容有多敏感、可不可信」（**来源/密级**维度）。这两个维度是正交的，目前 Windows 只覆盖了前者。
- 合规勾稽：AGT 显式对齐 **EU AI Act Article 10（数据治理，与 Article 15 同日 2026-08-02 生效）**。也就是说 08-02 增补里记的合规抬高，其实是**两条**——Article 15 管鲁棒性/抗注入，Article 10 管数据治理/来源可追溯。Windows 侧目前只在前者有对应设计。

**③ 产品判断（给 OS PM）**：如果做 OS 级意图 Registry，「文件夹白名单」这类**位置权限**是最低门槛而非终点；真正防 ADI 的是**给每条读入数据打来源标签并禁止降级**。后者成本远低于 Dual View（约 15× 调用开销），是当前性价比最高的一档。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-04]]
- 安全：[[Agent Workspace 隔离执行]] ｜ [[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[数据溯源分级与单调棘轮]] ｜ [[Agent Data Injection 数据注入攻击]]
- 跨平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]

#标签/Windows #标签/CopilotActions #标签/AgentWorkspace #标签/XPIA
