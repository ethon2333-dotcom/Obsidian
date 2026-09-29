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

## 2026-09-03 增补：26H2 档期 + Ask Copilot 意图搜索 + Sysmon 内置（来源 [[AppIntent 每日情报 2026-09-03]]）

> 接续 08-16 的「Copilot Actions 仍 opt-in 默认关」。本期补 **26H2 具体 GA 窗口**与两个此前未记录的框架层意图入口/安全件。

- **26H2 GA 窗口**：Windows 11 26H2 预计 **2026 年 9 月下旬~10 月初**以 **enablement package**（轻量特性开关，非重装）交付；消费版支持 24 个月、企业版 36 个月。来源：<https://www.pcworld.com/article/3063498/windows-11-26h2-is-coming-meet-all-the-new-features.html>（PCWorld / TechRepublic / WinCentral 多源一致）。
- **🔑 Ask Copilot（搜索层意图路由入口，新机制）**：经典任务栏搜索框可替换为可选的「Ask Copilot」自然语言搜索——**Copilot 解读用户意图并将查询链接到 apps / files / 系统设置（如「调亮屏幕」「打开 Downloads」）**，底层仍是 Windows 搜索索引，但加了**意图理解层**；文件/图片上传 + Copilot Vision（读打开的应用内容）后续扩展。⚠️ 这是**搜索层的意图理解**，非新 Registry API；与 08-05 记的 Agent Launchers / ODR 是不同层（搜索分发 vs agent/工具注册），二者互补而非替代。
- **Sysinternals System Monitor（Sysmon）内置**：原第三方威胁检测套件变为 Windows 可选组件，记录系统事件入 Windows 事件库、可配置文件过滤，用于隐藏威胁与系统错误检测——是 agent 行为审计 Telemetry 的**系统级补齐**（与本笔记 08-04「Project Perception 检查 agent loop」同方向，但 Sysmon 在 OS 内、Perception 在 Defender 端点侧）。
- ⚠️ **层级纪律（延续）**：26H2 为路线图/预览汇总，非新 API 公告；具体 Insider build 号、Ask Copilot 是否受 08-02 同一 `Settings > System > AI components > Agent tools > Experimental agentic features` opt-in 开关管控仍待补。Copilot Actions / Agent Workspace / ODR 四支柱安全设计自 08-09 以来无变化。
- → 对 OS PM：**Windows 的「系统级意图框架」现在有四层可对照**——搜索意图（Ask Copilot）/ agent 注册（Agent Launchers）/ 工具注册（ODR）/ 执行隔离（Agent Workspace）；其「用现有多用户权限原语建模 Agent」的范式（本笔记 07 月「能复用既有权限就别新造」）在 26H2 延续。

## 2026-09-12 增补：具体 Insider build 号 + Settings「Agents」面板 +「@」调 Agent + 悬停监控（来源 [[AppIntent 每日情报 2026-09-12]]）

> 接续 09-03 的「26H2 GA 窗口 + Ask Copilot + Sysmon」。本期补**第三方 tracker 披露的具体 build 号与交互细节**，把此前「默认关、需 opt-in」的抽象描述落到可验证的工程面。⚠️ 来源为 petri.com / gbhackers.com / mundobytes.com 等第三方媒体，**非 Microsoft 官方 blog**；具体 build 号与 GA 对应版本仍待官方源确认（见本笔记 08-05 待补项）。

**① 具体 build 号（首次进入公开视野）**
- Agentic 体验（任务栏 Agent）随 **Build 26200.8313**（Release Preview 通道）铺开。
- **Agent Workspace** 在实验特性中见 **Build 26220.7262**（为独立 Windows 会话，专属账号 + 虚拟化桌面）。

**② Settings 面板路径细化**
- 此前记 `Settings > System > AI components > Agent tools > Experimental agentic features`；本期 tracker 给出更细的 **`Settings > System > AI Components > Agents`** 路径，每个 Agent 可单独配置「能做什么 / 禁触哪些文件」，Documents/Pictures/Desktop 等敏感文件夹 consent 三档（Allow Always / Ask every time / Never allow）——与 07 月「scoped file access 六文件夹 + 三档同意」一致，仅面板命名细化。

**③ 交互细节（用户始终在环的具象化）**
- **「@」调 Agent**：在 Copilot 搜索框 / 工具菜单用「@」唤起特定 Agent（如 `@Researcher`），列本机可用 Agent 清单——把 08-05 的 Agent Launchers 注册表变成用户可感知的入口。
- **悬停监控**：Agent 运行进任务栏后，鼠标悬停 Copilot 图标即看实时进度，无需切到 Agent 窗口——把「用户可观测」做成零摩擦交互。
- **首个内建 MCP 服务器**：File Explorer + System Settings（与 08-05 ODR 连接器一致），Agent 经 ODR 受控访问核心体验。

→ **对 OS PM 的含义**：Windows 把「隔离执行 + 受控发现 + 用户始终在环」从安全白皮书落成**可点可配的交互**（@ 唤起 / 悬停进度 / 文件夹级 consent），是四平台里**用户侧可感知度最高**的 Agent 执行总线实现；其「复用既有多用户权限原语建模 Agent」范式（本笔记 07 月「能复用既有权限就别新造」）在本窗口无变化。⚠️ 仍待 Microsoft 官方 blog 复核 build 号与 `Experimental agentic features` 同一 opt-in 开关是否覆盖上述交互。

## 2026-09-13 增补：IFA 2026 Microsoft Execution Containers（Agent 沙箱容器隔离，来源 [[AppIntent 每日情报 2026-09-13]]）

> 接续 09-12 的「具体 build 号 + @ 唤起 + 悬停监控」。本期补 **IFA 2026（2026-09）微软公布的 OS 内建 Agent 隔离新原语**——把本笔记「四支柱安全」（Agent accounts / Agent Workspace / ODR / User Transparency）里的「隔离」从「独立账号+ACL」升级为**容器级**。详见 [[Agent Workspace 隔离执行]] 09-13 增补。

**① Microsoft Execution Containers（新命名隔离原语）**
- IFA 2026 披露：Windows 内建 **Microsoft Execution Containers**，把 AI Agent **隔离在沙箱容器内**，严格执行企业安全策略 + **记录全部活动日志**。这是比 07 月「独立低权限账号 + ACL」更明确的**容器隔离**表述，且把 08-04 记的「Project Perception 检查 agent loop」与「Agent Workspace 隔离会话」收拢为一个内建安全机制。
- 同期整合第三方 agent 框架：**NVIDIA OpenShell / Hermes Agent / OpenClaw** 直接接入 Execution Containers。
- → 对 OS PM：四平台里 Windows 现拥有**最明确的 OS 内建 Agent 容器隔离原语**（非仅 Defender 端点侧检查），与 Apple（Extensions 经 App Review + Confirmations）、Android（系统代持一次性授权）、HarmonyOS（芯片级可信根）形成对照。详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。

**② IFA 2026「Unmetered Intelligence」定位（非意图框架增量，仅作背景）**
- Mark Linton 提出「unmetered intelligence」：把日常 AI 负载从云端 token 经济移到本地 PC；RTX Spark（NVIDIA，1 PFLOP / 128GB 统一内存）/ **Project Zenith**（9-4 公布，64GB 统一内存 + 250GB/s 带宽门槛，本地跑 30B+ 参数）属**硬件/定位**，不计入意图框架 API 增量（按规则丢弃泛 AI 营销稿，仅 Execution Containers 入表）。

⚠️ **层级纪律（延续）**：IFA 2026 为微软高层 keynote + 安全媒体转述，**非 Windows agentic security 官方文档逐字**；Execution Containers 的具体实现（是否复用 Agent Workspace 容器、是否受 08-02 `Experimental agentic features` 同一 opt-in 管控、与 ODR 注册关系）仍待 Microsoft 官方 blog/learn 文档复核（见本笔记 08-05 待补项）。四平台意图 Registry 来源轴空白结论不变（见 [[Agent Data Injection 数据注入攻击]]）。

#标签/Windows #标签/CopilotActions #标签/AgentWorkspace #标签/XPIA

## 2026-09-15 增补：Agent 代码签名 + 证书校验/吊销（执行安全三原则落地，来源 [[AppIntent 每日情报 2026-09-15]]）

> 接续 09-13 的 IFA 2026 Microsoft Execution Containers。本期补**执行安全的身份级机制**（容器隔离之外的第三块拼图），把本笔记 07 月「Agent 须数字签名」记录补全为「签名 + 证书校验 + 吊销」。

**① 执行安全三原则（Microsoft 官方表述 corroborated by 第三方综述，2026-09）**
- **Non-repudiation（不可抵赖）**：Agent 的**每个动作须在日志中可见、可追溯**，相关到 Agent 主体而非交互用户——与 07 月「Agent 账号 + ACL + 审计」一致。
- **Confidentiality（机密性）**：Agent 访问敏感数据的标准**不低于人类用户**；敏感数据访问须显式、带上下文的批准。
- **Authorization（授权）**：每个数据查询或特权动作**执行前须用户或管理策略批准**。

**② 🔑 Agent 代码签名 + 证书校验 / 吊销（新机制细节）**
- 综述明确：Agent 二进制须**数字签名 + 证书校验**，若签名 Agent 被入侵或行为不当可**吊销**——这是本库此前「Agent 须数字签名」记录的**吊销/证书校验补全**，把执行安全从「进程/账号隔离（Agent Workspace）+ 容器隔离（Execution Containers）」再推进到「**身份级可信**」。
- → 与 [[Agent Workspace 隔离执行]] 09-15 增补同主题；与 Android `EXECUTE_APP_FUNCTIONS` 系统特权签名、HarmonyOS 芯片级可信根形成四平台对照（见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。
- → 对 OS PM：隔离解决「炸不到系统」，签名/吊销解决「谁是可信任的 Agent 主体」——两者正交，做安全路线图应并列排期（延续 08-04「隔离 ≠ 检查」的层级纪律）。

⚠️ **层级纪律（延续）**：来源为 windowsforum 第三方综述（聚合 Microsoft Insider 文档与博客），**非 learn.microsoft.com 逐字**；签名/吊销的具体实现（是否纳入 ODR 注册信任链、是否受 08-02 `Experimental agentic features` 同一 opt-in 开关管控）仍待 Microsoft 官方文档复核。四平台意图 Registry 来源轴空白结论不变。

## 2026-09-16 增补：Agent 代码签名/吊销由第三方升为官方确认（来源 [[AppIntent 每日情报 2026-09-16]]）

> 接续 09-15 的「Agent 代码签名 + 证书校验/吊销（第三方综述）」。本期用 **learn.microsoft.com 官方 agentic security 文档**核验，把该机制从「windowsforum 第三方综述」升格为「**Microsoft 官方确认的 OS agentic security 四大原则之一**」。

**① 官方逐字确认（learn.microsoft.com/en-gb/windows/security/book/operating-system-agentic-security）**
- 文档将执行安全原则列为四大：**Distinct agent accounts（专属 agent 账号）/ Limited agentic privileges（最小权限）/ Operational trust（操作信任）/ Privacy-preserving design（隐私保护设计）**。
- **Operational trust 原文**：「Agents that integrate with Windows must be signed by a trusted source so that maliciously or poorly behaved agents can be revoked and blocked with a range of defense-in-depth measures like certificate validation and antivirus.」
- → 本笔记 09-15 记的「Agent 须数字签名 + 证书校验/吊销可阻断」获 **官方背书**，从第三方口径升为产品原则层表述（与 07 月「Agent 须数字签名」记录闭环）。

**② 对四平台对照的含义**
- 执行安全从「进程/账号隔离（Agent Workspace）+ 容器隔离（Execution Containers）」推进到「**身份级可信**」——隔离解决「炸不到系统」，签名/吊销解决「谁是可信任的 Agent 主体」，二者正交（延续 08-04「隔离 ≠ 检查」层级纪律）。
- 与 Android `EXECUTE_APP_FUNCTIONS` 系统特权签名、HarmonyOS 芯片级可信根形成四平台「身份可信」对照，见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]。

⚠️ **层级纪律（延续）**：签名/吊销的具体实现（是否纳入 ODR 注册信任链、是否受 08-02 `Experimental agentic features` 同一 opt-in 开关管控）**仍待 learn.microsoft.com 逐字复核**（官方文档只确认原则，未给注册/信任链衔接细节）。四平台意图 Registry 来源轴空白结论不变。

## 2026-09-17 增补：ODR Agent Connectors 权限模式具象化（build 26100.7344+，来源 [[AppIntent 每日情报 2026-09-17]]）

> 接续 09-05/09-16 的 Agent 代码签名 + ODR 受控发现。本期补**第三方实操教程披露的 ODR Agent Connector 权限治理细节**，把「受控发现 + 用户授权」从原则落到可配置形态（⚠️ 第三方教程，非 learn.microsoft.com 逐字）。

- **Agent Connectors 默认关进 Agent Workspace**：自预览 build **26100.7344+**，所有 ODR 注册的 agent connectors（本质是 MCP server）**默认在 Agent Workspace 隔离环境内执行**；Windows 先取得用户许可，才让 agent 运行这些连接器——与 08-05 `odr.exe agent-info add` 注册表 + 09-16 代码签名构成「注册 → 签名 → 隔离 → 授权」闭环。
- **三档权限模式（连接器/文件夹级）**：教程披露 consent 三态：**Ask every time（每次询问）/ Allow always（始终允许）/ Never allow（永不许可）**——与 07 月「scoped file access 六文件夹 + 三档同意（Allow Always / Ask every time / Never allow）」一致，本次补的是「连接器」维度的同构三档。
- **头号风险仍为 XPIA**：教程直引官方警告——XPIA 让攻击者不必碰设备，只需让 agent 读到一份夹带恶意指令的文件/UI 元素即可劫持；隔离解「出事后能搞多大」、不解「会不会出事」。与 [[XPIA 跨提示注入]] 元判断「假定注入必然发生，用边界压爆炸半径」一致。
- → 对 OS PM：Windows 的「系统级意图框架」四层（搜索意图 Ask Copilot / agent 注册 Agent Launchers / 工具注册 ODR / 执行隔离 Agent Workspace）现在在**权限治理**层也齐了——连接器默认隔离 + 三档 consent，是四平台里**用户侧可配置度最高**的 agent 执行总线。

⚠️ 层级纪律（延续）：来源 adersaytech 第三方教程（聚合 learn.microsoft.com + 支持文档），**build 26100.7344+ 与三档权限模式待 Microsoft 官方文档逐字复核**；是否与 08-02 `Experimental agentic features` 同一 opt-in 开关管控仍待补。

## 2026-09-18 增补：Copilot Actions 向 Insiders 分批推送（部署里程碑，非 API 新增，来源 [[AppIntent 每日情报 2026-09-18]]）

> 接续 09-17 的「ODR 连接器权限模式具象化」。本期**无框架 API 净新增**（四平台官方框架层 + BFCL v4 榜本窗口均无 24h 增量，见 [[AppIntent 每日情报 2026-09-18]] 已复核清单）。唯一低于收录阈值的进展是**部署推进**：

- **Insider 分批推送「Now Available」**：据 msftnewsnow（2026-09-18 报道），Copilot Actions 已随 Copilot app 更新 **v1.25112.74+** 经 Microsoft Store 向 Windows Insiders **分批推送可用**；启用路径不变（管理员开 `Settings > System > AI components > Agent tools > Experimental agentic features` → 在 Copilot 作曲器用「Take Action」→ Agent Workspace 内可见可中断执行）。
- **性质判定（★5/10，低于收录阈值）**：这是**已记录预览能力的部署推进**，能力清单（打开 app / 点 UI / PDF 表提取 / 批量修图 / 邮件起草 / Agent Workspace 内可观测可中断）与 08-02 起记录完全一致，**无新框架 API**。故本期**未新建 B 节点**，仅在此追加状态行。
- → 对 OS PM：Windows 的 agentic OS 从「能演示的预览」进入「Insider 可装」阶段，但 GA 仍锚定 26H2（9 月下旬~10 月初，enablement package）。其「系统级意图框架四层（Ask Copilot / Agent Launchers / ODR / Agent Workspace）+ 权限治理三档 + 容器隔离 + 身份签名吊销」范式自 09-13/09-16/09-17 以来**无变化**。

⚠️ 层级纪律（延续）：msftnewsnow 为第三方媒体，app v1.25112.74+ 精确发布日期与是否仍受 08-02 `Experimental agentic features` 同一 opt-in 开关管控待 Microsoft 官方 blog 复核。

## 2026-09-25 增补：统一 Copilot 桌面 app 9 月中旬铺开（部署里程碑，非 OS API 新增，来源 [[AppIntent 每日情报 2026-09-25]]）

> 接续 09-18 的「Copilot Actions 向 Insiders 分批推送（v1.25112.74+）」。本期**无框架 API 净新增**（四平台官方框架层 + BFCL v4 榜本窗口无增量，见 [[AppIntent 每日情报 2026-09-25]] 已复核清单）。一个低于收录阈值的进展是**应用层部署推进**：

- **统一 Copilot 桌面 app 9 月中旬铺开**：自 2026-08-18 起管理员可 opt-in 测试、2026 年 **9 月中旬**起向商业/消费用户 broad rollout；新 app 为 **Chromium 架构**，把消费版 Microsoft Copilot 与工作版 Microsoft 365 Copilot **合并为单一 app**（个人/工作 Entra ID 账户同一界面切换、数据不互流）；应用 ID 不变、现有策略继续生效；由 **EdgeUpdate** 机制管理（非 Microsoft Store），要求 EdgeUpdate ≥ 1.3.253.25。来源：<https://simoncarter.ai/posts/microsoft-s-unified-copilot-desktop-app-rolls-out-to-commercial>（MC1457084 时间线 corroboration）。
- **性质判定（★5/10，低于收录阈值）**：这是**应用层产品合并/分发变更**，**非 OS 执行总线 API 新增**——Copilot Actions / Agent Workspace / ODR / Execution Containers / Agent 代码签名等 OS 框架层自 09-13/09-16/09-17 以来**无变化**。按任务「丢弃应用层、聚焦 OS 级框架」规则，本项**不计入情报增量**，仅在此追加状态行保持连续性。
- → 对 OS PM：Windows 的 agentic OS 进入「统一 Copilot app 分发」阶段，但**执行总线范式未变**；GA 仍锚定 26H2（9 月下旬~10 月初 enablement package）。

## 2026-09-26 增补：26H2 仍以 enablement package 形态临近铺开（部署里程碑，非 API 新增，来源 [[AppIntent 每日情报 2026-09-26]]）

> 接续 09-25 的「统一 Copilot 桌面 app 9 月中旬铺开」。本期**无框架 API 净新增**（四平台官方框架层本窗口无增量，见 [[AppIntent 每日情报 2026-09-26]] 已复核清单）。一个低于收录阈值的进展是 **26H2 部署时间窗进一步具象化**：

- **Windows 11 26H2**：PCWorld / Windows Central / windowsforum（9-25）一致确认 26H2 以** enablement package** 形态于** 9 月下旬~10 月初**铺开（基于 25H2、仅切版本号+激活已内置功能，不重装）；支持期消费版 +24 月 / 商业版 +36 月。
- **agentic 入口层补强（搜索/文件层，非执行总线 API）**：**Ask Copilot** 任务栏搜索替代（opt-in，AI 撰写搜索框 + 本地文件/设置自然语言 + 后续接文件/图上传与 Copilot Vision）；**File Explorer 内 Copilot 侧栏**（dockable，直接对话文件夹/文件、文档摘要，不转发到 Copilot app）；另提「Agentic AI functions in the system」。
- **性质判定（★5/10，低于收录阈值）**：上述为**消费级部署推进 + 搜索/文件层的 agentic 入口**，Copilot Actions / Agent Workspace / ODR / Execution Containers / 代码签名等 OS 执行总线自 09-13/09-16/09-17/09-25 以来**无新 Registry API**。按任务「丢弃应用层、聚焦 OS 级框架」，本项**不计入情报增量**，仅追加状态行保持连续性。
- → 对 OS PM：Windows agentic OS 进入「26H2 enablement 铺开 + 统一 Copilot app + 搜索/文件层 agentic 入口」阶段，但**执行总线范式未变**；企业可从 25H2 月度更新已陆续收到这些功能、26H2 仅正式启用。

⚠️ 层级纪律（延续）：PCWorld/WindowsCentral/windowsforum 为第三方媒体，26H2 精确 GA 日与 agentic 入口是否仍受 08-02 `Experimental agentic features` 同一 opt-in 管控待 Microsoft 官方 blog 复核。
