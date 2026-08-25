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
- **把 Agent 当「用户」而不是「进程」来建模**：微软用「独立账号 + ACL 共享文件夹」复用了 40 年的多用户权限模型，而不是发明新的 Agent 权限体系。迁移结论：**能复用既有授权原语就别新造**——用户已经理解「给同事共享一个文件夹」，不需要再学一套 Agent 权限概念。
- **隔离、检查、打标是三件不同的事，别互相当替身**：Agent Workspace 管「炸不到系统」，Project Perception 管「路上被拦下」，来源分级管「读进来的东西可不可信」。做 OS Agent 安全路线图时应按这三层独立排期，否则会用隔离的完成度掩盖检查的缺失。

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

## 2026-08-05 增补 · Windows Agent Launchers：系统级 Agent 注册表（来源 [[AppIntent 每日情报 2026-08-05]]）

> ⚠️ **补一块此前认知缺口**：本笔记 07/08 两月记录里，Windows 的「系统级意图框架」只覆盖 **ODR 的 MCP 连接器注册**（注册「能调什么工具/服务」）。本期发现 Windows 还有**第二层注册表**——Agent Launchers，注册「系统里有哪些可用的 agent 实体」。

**是什么**：在 **App Actions 框架**之上的一层 agent registry，打包应用据此把「自己提供的 agent」发布到系统，供 M365 Copilot（Analyst / Researcher 等）发现与调用。

**已核实技术细节（learn.microsoft.com `/windows/ai/agent-launchers/` 与 `agents-get-started`，官方文档）**：

- AppExtension 名：`com.microsoft.windows.ai.agentInfo`
- 注册清单 `agentRegistration.json`：`manifest_version` / `version` / `name` / `display_name` / `description` / `placeholder_text` / `icon` / `action_id`（**须匹配一个已定义的 App Action id**）
- ODR 命令：`odr.exe agent-info add "<path>"` ｜ `odr agent-info remove "<path>"` ｜ `odr agent-info list`
- 底层 = App Actions（需 `agentName` + `prompt` 输入，可选 `attachedFile`）；支持静态（install-time）/ 动态（runtime）注册
- 约束：动态 ODR 注册需打包应用具备 **package identity**；官方文档**未提额外 Capability 声明**

**对四平台对比的意义（重要）**：补齐后，Windows 现与另三家在「**应用向系统声明可被调用的能力**」这一层首次对齐——

| 平台 | 应用发布物 | 注册机制 |
|---|---|---|
| Apple | App Intent | App Intents 框架（系统发现） |
| Android | App Function | AppFunctions Registry（`BIND_APP_FUNCTION_SERVICE` / app_metadata） |
| HarmonyOS | Intent / Want | Intents Kit（SKILL.md / 元服务） |
| **Windows** | **Agent 实体** | **Agent Launchers（`com.microsoft.windows.ai.agentInfo`）+ ODR** |

差异：Windows 当前颗粒度是 **agent 实体**，而非 Apple/Android/HarmonyOS 的细粒度 intent/function；但「声明→注册→受控发现」的骨架已齐。

**待补/存疑（诚实标注）**：
- Agent Launchers 具体 Insider build 号与发布日期待补（官方文档页无日期）。
- 动态注册的安全闸口（是否需签名、是否受 08-02 记的 `Settings > System > AI components > Agent tools > Experimental agentic features` 同一 opt-in 开关管控）**待确认**。
- 宿主调用注册 agent 的信任链（谁批准、是否用户可审计、XPIA 缓解如何覆盖 agent 实体而非仅工具调用）**待补**。

## 2026-08-09 增补 · Build 2026 完整 OS Agent 执行框架（来源 [[AppIntent 每日情报 2026-08-09]]）

> 本笔记 07/08 两月只记录了 Windows agent 安全的**四块拼图**（Copilot Actions / Agent Workspace / ODR / Agent Launchers）。本期把 Build 2026（2026-06-02）发布的**完整 OS Agent 执行框架**串成独立节点 [[Windows Agent Framework 端侧 Agent 执行框架 2026]]，此处只记与本笔记安全视角的衔接点：

- **本笔记的「四支柱安全」是那个框架的「安全子集」**：Copilot Actions / Agent accounts / Agent Workspace / User Transparency 仍成立，但放到 Build 2026 框架里，它们只是 Runtime（OS 宿主）+ Store（分发）+ Mesh（联邦控制面）这一更大栈里的「运行时与权限」一层。
- **新补的 OS 级拼图对安全的增量**：① Windows Agent Runtime 把 agent 注册为**系统服务**+沙箱（移动端式权限，安装时审阅），是 Agent accounts/Workspace 的**底座**；② Azure Agent Mesh 用 **Ed25519 DID + IATP + 动态信任评分**做 agent 间零信任，是跨设备执行的信任层（对接 EU AI Act 高风险）；③ Agent Store 的 85/15 分成 + 安全评审是**分发层**的准入闸。
- **命名澄清**：官方叫 **Microsoft Agent Framework（MAF，SDK，2026-04-02 达 1.0 GA，合并 SK+AutoGen）**；「Windows Agent Framework」是第三方对 Build 2026 OS 栈的俗称。二者是「写 agent 的 SDK」vs「跑 agent 的 OS 宿主」两层，详见新节点。
- ⚠️ 待补：MAF 官方 MIT 许可页、Runtime 具体 Insider build 号、Mesh GA 具体日期（均待官方源确认）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-04]] ｜ [[AppIntent 每日情报 2026-08-05]] ｜ [[AppIntent 每日情报 2026-08-09]]
- 安全：[[Agent Workspace 隔离执行]] ｜ [[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[数据溯源分级与单调棘轮]] ｜ [[Agent Data Injection 数据注入攻击]]
- 跨平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[Windows Agent Framework 端侧 Agent 执行框架 2026]]（Build 2026 完整 OS agent 栈 + MAF SDK）

## 2026-08-16 增补：第三方综述 corroboration（来源 [[AppIntent 每日情报 2026-08-16]]）

> 本窗口（2026-08-10→08-16）Windows 官方渠道**无新增 API**。本期补一份 **2026-08-13 第三方 tracker（agentinterface.app）** 的 corroboration，与本笔记既有记录互证；仅为综述，非官方 API 变更。

- tracker 确认两点：① **Copilot Actions 正面向 Windows Insiders 在 Agent Workspace 之上铺开，仍 opt-in、默认关**——与本笔记 07 月「默认关闭 + 需 opt-in」一致；② **Apple 借 WWDC26 正式弃用 SiriKit，App Intents 成第三方 App 进 Siri 的唯一路径**——跨平台对照：Apple 走「系统级意图协议强制」，Windows 走「受控发现 + 隔离账号」，两条机制相反但都比「早期」成熟。
- ⚠️ **层级纪律（延续）**：该 tracker 是第三方产品界面综述站，非 OS 官方文档；其「Copilot Actions 铺开」信号须以 Microsoft 官方 blog/build 说明复核（具体 Insider build 号待补，见本笔记 08-05 待补项）。
- 四大 OS 意图框架在「意图元数据来源分级」维度仍全空白（详见 [[Agent Data Injection 数据注入攻击]] 08-16 演进）。

#标签/Windows #标签/CopilotActions #标签/AgentWorkspace #标签/XPIA
