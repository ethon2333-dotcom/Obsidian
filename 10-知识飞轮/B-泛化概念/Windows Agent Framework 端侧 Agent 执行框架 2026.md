---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-08-09]]"
tags:
  - AppIntent
  - Windows
  - AgentFramework
  - AgentRuntime
  - AzureAgentMesh
---

# Windows Agent Framework 端侧 Agent 执行框架（2026）

> 库内空白补漏：此前本库只记录了 Windows 的「Copilot Actions / Agent Workspace / ODR / Agent Launchers」四块（见 [[Windows Copilot Actions 与 Agent Workspace 2026]]），但**缺一个把 2026 年 Windows「整套 Agent 执行框架」串起来的权威节点**。Build 2026（2026-06-02）把 Windows 正式定位为「agent 运行时的 OS」，本笔记补齐这一层。

## 一句话定义

Windows 在 2026 年形成一套**端侧 Agent 执行框架**：开发侧是 **Microsoft Agent Framework**（合并 Semantic Kernel + AutoGen 的官方开源 SDK，2026-04-02 达 1.0 GA）；运行侧是 Build 2026 发布的 **Windows Agent Runtime（OS 级宿主）+ Windows Agent Store（分发）+ Azure Agent Mesh（联邦控制面）+ Copilot Workspace（GA）+ Project Polaris（自研编码模型）**。

## 命名澄清（重要，避免混淆）

- **官方名称是「Microsoft Agent Framework」（MAF）**，不是「Windows Agent Framework」——后者是第三方博客（如 byteiota.com）对 Build 2026 OS 级栈的俗称。**本库记 MAF 为开发 SDK，记「Windows Agent 执行栈」为 OS 级运行时/分发/控制面**。
- MAF 与 Windows Agent Runtime 是**两层**：MAF 是写 agent 的 SDK（在 .NET / Python / Go 上一致 API），Windows Agent Runtime 是让这些 agent 以「OS 一等公民」身份跑起来的宿主。二者通过共享 runtime 概念衔接。

## 为什么重要

- **Windows 从「应用 OS」变「Agent 运行时 OS」**：Agent 不再是跑在 Copilot 里的功能，而是具备独立生命周期、内存、权限边界的**系统级实体**（与 Apple App Intents / Android AppFunctions / HarmonyOS 元服务 同一战略层级，但路径是「OS 内建 agent 宿主」而非「应用声明能力」）。
- **权限模型复用 40 年多用户原语**：Agent 以独立账号 + ACL 共享文件夹运行，用户已理解「给同事共享文件夹」，无需新学一套 Agent 权限概念（见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 的可复用启发）。
- **联邦执行**：同一份 agent 代码可在笔记本 / Cloud PC / 边缘设备间按延迟与 GPU 可用性路由（Azure Agent Mesh），是跨端侧-云的真正可移植性。

## 适用边界

- 限定 Windows / Azure 生态；与 Apple / Android / HarmonyOS 的「应用声明显式能力」路线不同，Windows 走「OS 内建 agent 宿主 + 声明式 YAML manifest」路线。
- **预览态限制**：Windows Agent Runtime 初始预览仅支持**文本 agent（JSON / XML / PDF 结构化数据）**；视觉 agent（读屏/UI 自动化）**排到 2027**。硬件下限 **40 TOPS NPU（Copilot+ PC）**。
- 部分生态组件（MXC 隔离谱 / Entra Agent Identity / Agent 365 等）来自第三方解读（zylos.ai / vendordeep.com），属生态合成，**待官方确认**，本笔记不据为已确认事实。

## 证据与例子（Build 2026，2026-06-02）

**① 开发 SDK：Microsoft Agent Framework（MAF）1.0 GA（2026-04-02）**
- 合并 **Semantic Kernel（企业级 SDK）+ AutoGen（研究向多 agent 编排）**；AutoGen 进入维护模式，新功能只在 MAF。
- 四核心原语：**Agent / AgentGroup / AgentRuntime / ToolRegistry**；五种编排模式：sequential / concurrent / handoff / group chat / **Magentic-One**（分层多 agent）。
- Agent 用 **YAML 声明式定义**，纳入 Git 版本管理；**MCP 原生支持**（数千个现成 MCP server 直接当工具）；Provider 覆盖 Azure OpenAI / OpenAI / Anthropic / Bedrock / Gemini / Ollama（切换一行）。
- 包：`agent-framework`（Python）/ `Microsoft.Agents.AI.Foundry`（.NET，依据迁移指南）/ `agent-framework-go`（Go 公测）。
- 许可：**开源**；第三方博客称 **MIT**（官方许可页未在本轮直读，**待官方许可页确认**）。

**② Windows Agent Runtime（Insider 预览，2026-06）**
- agent 注册为**系统服务**，含任务栏集成、日历/文件系统事件订阅、Defender 可见。
- 沙箱模型**镜像移动端权限**：按能力授权（文件系统范围 / 网络访问 / 应用启动），用户安装时审阅并批准。
- 初始预览 = **文本 agent**；视觉 agent 排 2027。

**③ Windows Agent Store（预览，2026-06）**
- 开发者**收入分成 85/15**（优于 Apple 70/30）；上架安全评审镜像 Microsoft Store 认证（能力披露 / 数据处理声明 / 沙箱合规）。Adobe、Zoom 为初始设计伙伴。

**④ Azure Agent Mesh（预览，GA 目标 Q4 2026）**
- **联邦控制面**：跨本地 Windows / Windows 365 Cloud PC / Azure Arc 边缘自动路由 agent 任务。
- 零信任安全：**每 agent 一个 Ed25519 去中心化身份（DID）** + **IATP（Inter-Agent Trust Protocol，agent 间加密通信）** + **动态信任评分**（随行为调整，对接 EU AI Act 高风险要求）。
- 计费：按消费（per-agent invocation / per-tool call）。

**⑤ Copilot Workspace GA**：Fleet 模式（CLI 自主操作）/ Autopilot 模式（定时后台）/ 多文件编辑；集成 Jira / Datadog / ServiceNow。

**⑥ Project Polaris**：微软自研 MoE 编码模型，**2026-08 起替换 GitHub Copilot 的 GPT-4 Turbo** 为默认引擎；100K 上下文；3 个月回退窗口。

**⑦ AI Foundry for Windows SDK**（NuGet）：打包 ONNX Runtime + DirectML + Copilot Runtime，端侧推理成 .NET 一等公民。

## 与四平台对齐（给 OS PM）

| 平台 | 路线 | agent 成为系统实体的方式 |
|---|---|---|
| Apple | 应用声明能力 | App Intents（系统发现）+ System Orchestrator 路由 |
| Android | 应用声明能力 | AppFunctions Registry（`BIND_APP_FUNCTION_SERVICE`） |
| HarmonyOS | 应用声明能力 | Intents Kit / 元服务（SKILL.md） |
| **Windows** | **OS 内建 agent 宿主** | **Windows Agent Runtime（系统服务 + 沙箱）+ Agent Store + Agent Launchers 注册** |

差异：前三者是「应用向系统声明能力，系统负责发现/路由」；Windows 额外提供「OS 级 agent 宿主 + 联邦执行 + 分发市场」，agent 的**生命周期与权限由 OS 直接托管**，路径更重但更完整。

## 可复用启发

- **做端侧 Agent 框架时，「写 agent 的 SDK」与「跑 agent 的 OS 宿主」是两件事，要分开设计**：MAF 解决开发一致性，Windows Agent Runtime 解决运行时隔离与权限；混淆二者会既写不出可移植 agent、又管不住执行面。
- **声明式 YAML manifest + 版本管理是 agent 可治理的前提**：Windows 把 agent 定义当代码（Git），这与「意图框架应可版本化」的 PM 直觉一致。
- **联邦执行（Mesh）把「端侧 vs 云」从架构抉择变成运行时路由**：同一份 agent 代码按延迟/GPU 自动落点，对「端云协同」产品是直接可用的范式（对照 [[Android AppFunctions 设备侧意图 2026]] 的「理解可能在云端」）。
- **权限默认下沉到 OS**：Windows 用独立账号 + ACL 复用多用户模型，再次验证「能复用既有授权原语就别新造」（见 [[Windows Copilot Actions 与 Agent Workspace 2026]]）。

## 反例与边界

- **Runtime 预览只支持文本 agent**：2026 年内 Windows Agent Runtime **不能做 UI 自动化/屏幕理解**（视觉 agent 2027），与 Android UI Automation / Apple 屏幕感知（View Annotations）当前不在一个起跑线——别把「agent OS」误读成「能操作任意 GUI」。
- **MXC / Entra Agent Identity / Agent 365 等是第三方解读**：本笔记只据官方 Build 2026 公告（Runtime/Store/Mesh/Copilot Workspace/Polaris）与 MAF 官方文档记，生态拼图类说法**待官方确认**。
- **许可与具体 build 号待补**：MIT 许可、Agent Mesh GA 具体日期、Runtime 具体 Insider build 号均**待官方源确认**。

## 开放问题 / 未决

- [ ] Microsoft Agent Framework 的官方许可页（MIT 与否）→ **待官方确认**。
- [ ] Windows Agent Runtime 具体 Insider build 号与正式 GA 日期 → **待补**。
- [ ] Azure Agent Mesh 是否真在 Q4 2026 GA、动态信任评分算法公开口径 → **待补**。
- [ ] 视觉 agent（2027）的沙箱模型是否与文本 agent 同构 → **待补**。

## 关联

- 来源：[[AppIntent 每日情报 2026-08-09]]（库内空白补漏）
- 同族（本库四块既有）：[[Windows Copilot Actions 与 Agent Workspace 2026]]（Copilot Actions / Agent Workspace / ODR / XPIA 四支柱）｜ [[Windows Copilot Actions 与 Agent Workspace 2026#2026-08-05 增补]]（Agent Launchers 第二层注册表）
- 跨平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- 安全：[[Agent Workspace 隔离执行]] ｜ [[XPIA 跨提示注入]] ｜ [[确认机制]] ｜ [[数据溯源分级与单调棘轮]]
- 上游枢纽：[[意图框架·跨体系索引 MOC]] ｜ [[Intent Routing Stack 六方意图路由分层对照 2026]]

#标签/Windows #标签/AgentFramework #标签/AgentRuntime #标签/AzureAgentMesh
