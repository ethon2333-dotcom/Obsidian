---
title: OS 级系统 Agent 与跨应用自动化 学习笔记
tags:
  - os-agent
  - 系统级-agent
  - 跨应用自动化
  - 端侧意图
created: 2026-09-15
source: 库内 MOC 互联 + WebSearch/WebFetch 联网核实（Apple Newsroom、Microsoft Support/Blogs、Google Developers、a2ui.org、行业媒体），媒体口径/未公开数字见文末「⚠️ 待核实清单」
---

**心智模型：OS 级系统 Agent 是「长在操作系统里、能跨 App 替你办事的数字员工」，它把交互入口（语音/视觉/快捷键）与系统能力（App Intents、无障碍、文件系统、权限沙箱）缝合起来，让「以任务为中心」替代「以 App 为中心」；本笔记聚焦平台层能力视角，区别于模型架构与语义路由。**

> 区别于库内已有笔记：
> - 与 [[工业级 GUI Agent 架构（VLM+无障碍树）]] 不同——那篇是「端侧 VLM + 无障碍树」的**技术架构**落地；本文是**平台/OS 视角**的能力与生态博弈。
> - 与 [[端侧意图框架 学习笔记]] 不同——那篇是四平台意图**语义路由**总览；本文是系统 Agent 的「跨 App 执行」与权限模型。
> - 与 [[语音 Agent 架构 学习笔记]] 不同——那篇是语音作为 Agent **入口的工程架构**；本文里语音只是系统 Agent 的多个入口之一。

---

## 1. 定义：什么是 OS / 平台级系统 Agent

| 维度 | 单 App 内 Agent | OS / 平台级系统 Agent |
|---|---|---|
| 作用域 | 被困在单个 App 的进程与数据里 | 横跨系统多个 App、系统服务、文件与设置 |
| 入口 | 应用内聊天框 / 按钮 | 系统级语音唤醒、屏幕理解、快捷键、常驻助手 |
| 执行方式 | 调用本 App 内部 API | 调度 App Intents / 无障碍树 / computer use / 系统自动化 |
| 权限来源 | App 自身声明 | 用户在系统层授权（scoped permission、沙箱工作区） |
| 典型代表 | 每个 App 里的客服机器人 | Siri AI、Gemini Live/Astra、Windows Copilot、Operator |

一句话：**系统 Agent = 入口（多模态） + 意图总线（App Intents / A2UI 等） + 跨 App 编排 + 系统级权限沙箱**。

---

## 2. 形态分类

| 形态 | 说明 | 代表 |
|---|---|---|
| 语音助手演进 | 从「命令式问答」走向「情境感知 + 跨 App 执行」 | Siri AI、Gemini Live、Copilot Voice |
| 屏幕理解型 computer-use | 像人一样看屏、点按、输入，无需 App 预先接 API | Claude Computer Use、OpenAI CUA、Gemini Computer Use |
| 跨 App 编排 | 系统把多个 App 的能力串成一条任务链 | Siri via App Intents、Windows Copilot Actions、A2UI |
| 系统级自动化快捷键 | 用户/系统预置的确定性自动化，触发即执行 | Apple Shortcuts、Android Tasker、MacroDroid、IFTTT |

---

## 3. 主流方案速览

- **Apple：Siri + App Intents + Private Cloud Compute**
  - 在 WWDC26（2026-06）发布「新一代 Apple Intelligence」与 **Siri AI**，随 iOS 27 / iPadOS 27 / macOS 27 / watchOS 27 / visionOS 27 推出。
  - 能力：理解屏幕内容、基于个人情境**跨 App 搜索**、联网获取最新信息、生成回答；并通过「更系统化的 App 操作」完成跨 App 任务。
  - 机制：App 通过 **App Intents** 向 Siri 声明能力，用户按动作逐次授权；简单任务端侧跑，复杂任务上 **Private Cloud Compute**（设计上 Apple 自身也无法读取内容）。
  - 状态：Siri AI 于 2026 下半年以 Beta 提供，先英语；**中国大陆尚不可用**（监管审批待定）。
- **Google：Gemini Live / Project Astra**
  - Project Astra 是 DeepMind 研究原型，能力逐步迁移进 Gemini App、Search、Lens、Maps。
  - Gemini Live 的相机/屏幕共享于 2025 年初向 Android 订阅用户开放、后免费，I/O 2025 扩至 iOS。
  - I/O 2025 起 Astra 获得 **computer control**（点按钮、填表、跨 App 导航、代打电话/订票）。
  - 2025-10 Google 向开发者预览 **Computer Use 模型**（先优化浏览器，称「移动 UI 控制有强潜力」）；Google App 内测出现 "bonobo"/"screen automation" 字符串，指向用已装 App 下单/订行程。
- **Microsoft：Copilot / Windows（Agent Workspace）**
  - 2025-10 提出「让每台 Windows 11 PC 成为 AI PC」：新增 **"Hey Copilot"** 唤醒词、**Copilot Vision**（看屏幕/全桌面分析）。
  - 实验性「**代理工作区（Agent Workspace）**」：每个代理用独立账户、独立会话运行，与用户桌面隔离（运行时隔离 + 限定授权）。
  - **Copilot Actions** 与 **代理连接器（Agent Connectors，即 MCP 服务器）** 经 On-Device Registry（ODR）注册，安全、可管理。
  - Copilot Studio 的 **Computer Use（CUA）** 支持 OpenAI CUA、Anthropic Claude Sonnet 4.5/4.6，虚拟键鼠操作网页/桌面 App。
- **Claude Computer Use（Anthropic）**
  - 2024-10 随 Claude 3.5 Sonnet 开放；感知→推理→行动循环（截图理解、决策、虚拟输入）。
  - 技术路线分四类：云端 API 调用型（Claude Computer Use / OpenAI CUA）、云端虚拟桌型（Manus）、端侧纯视觉型（Mano-P）、混合。
- **OpenAI Operator**
  - 2025-01 发布，核心 **CUA（Computer-Using Agent）** = GPT-4o 视觉 + 强化学习，直接操作 GUI，无需特定 API；后并入 ChatGPT Agent。
- **跨应用自动化工具层**
  - **Apple Shortcuts**：iOS/macOS 内置，时间/位置/App/语音触发，深度集成第一方 App 与第三方 Shortcut Actions（基于 App Intents）。
  - **Android Tasker / MacroDroid / Automate**：本地执行、条件触发（位置、时间、电量、App 状态），Tasker 可模拟点按、读通知，权限粒度极高。
  - **IFTTT / Zapier**：跨服务轻量联动，偏云端。

---

## 4. 2025-2026 进展脉络

- **OS 内嵌 Agent 成主线**：Apple（Siri AI）、Google（Gemini 嵌入 Android/Search/Workspace）、Microsoft（Copilot 进任务栏/资源管理器/设置）均把 Agent 做成「系统层常驻」而非独立 App。
- **跨 App 编排两路并进**：① 声明式标准（Apple App Intents、Google **A2UI** 协议——见下）；② 通用界面操作（computer use）兜底无接口场景。
- **computer use 走向通用界面操作**：巨头与创业公司（Claude CU、OpenAI CUA、Gemini Computer Use、Manus、FDM-1 等）把「看屏→决策→点按」做成通用能力；基准如 OSWorld 分数逐年攀升（具体数值见待核实）。
- **端侧隐私成为卖点**：Apple PCC、Windows 代理工作区隔离、Google 强调本地处理——「能端侧就端侧，上云也要可审计」。
- **新协议层冒头**：Google **A2UI（Agent-to-UI，Apache 2.0）** 让 Agent 发送「声明式 UI 描述」由客户端原生渲染，跨信任边界、防 UI 注入；与 A2A、AG-UI、MCP Apps 互补。

---

## 5. 代表方案对比表

| 平台 / 方案 | 形态 | 跨 App 能力 | 端侧隐私 | 开放生态 | 当前状态（2026-09 口径） |
|---|---|---|---|---|---|
| Apple Siri AI + App Intents | 语音 + 系统编排 | 强（App Intents 逐动作授权） | 强（PCC、端侧优先） | 中（依赖开发者接 Intents） | Beta（英语先，大陆不可用） |
| Google Gemini Live / Astra | 语音 + 视觉 + computer use | 强（含无接口屏幕操作） | 中（云端为主，本地处理强调有限） | 中（A2UI 开源、Gemini API） | 渐进推送，computer use 开发者预览 |
| Microsoft Copilot / Windows | 语音 + 视觉 + 工作区 Agent | 中-强（连接器/MCP、Copilot Actions） | 中（代理工作区隔离、XPIA 防护） | 中（MCP 连接器、Copilot Studio） | Insider/Labs 预览，逐步放量 |
| Claude Computer Use | 屏幕理解型 | 强（任意 GUI，无需 API） | 弱-中（依赖云端模型） | 高（API 开放） | 已开放，持续迭代 |
| OpenAI Operator / CUA | 屏幕理解型 | 强（网页/桌面 GUI） | 弱-中（云端） | 中（并入 ChatGPT Agent） | 已发布并整合 |
| Shortcuts / Tasker 等 | 系统级自动化快捷键 | 中（受沙箱/权限约束） | 高（多本地执行） | 高（用户自建、插件生态） | 成熟可用 |

---

## 6. 与库内笔记互联

- 本文的「跨 App 编排」底座是 [[App Intent 的核心作用]] 与 [[Apple Intelligence 与 App Intents]]——App Intents 是系统 Agent 调度第三方 App 的标准门窗。
- 屏幕理解/computer use 的工程实现可接力 [[工业级 GUI Agent 架构（VLM+无障碍树）]]（端侧 VLM + 无障碍树双引擎）。
- 系统 Agent 的「意图理解」依赖 [[端侧意图框架 学习笔记]] 的语义路由与四平台格局。
- 语音唤醒/全双工入口设计见 [[语音 Agent 架构 学习笔记]]。
- 安卓/HarmonyOS 侧的 OS 级意图与元服务可对照 [[HarmonyOS 元服务 学习笔记]]。

---

## 7. 深度盲区（待解问题）

- [ ] **跨 App 权限模型**：系统 Agent 如何在一句话里安全串联 5 个 App，且「逐动作授权」不把用户烦死、又不偷偷越权？（最小特权 + 可审计 + 可逆）
- [ ] **computer use 的安全边界**：通用界面操作绕过了 App 沙箱，如何防「提示注入（XPIA）」让 Agent 误点钓鱼/误转账？人类监督的触发点设在哪里？
- [ ] **OS Agent 与第三方 App 生态博弈**：当 Siri/Gemini 能直接「看屏代操作」，超级 App（微信/支付宝）会开放接口还是筑墙？Sherlocking（系统吃掉第三方）会重演吗？
- [ ] **端侧 vs 云端的能力分界**：哪些任务必须上云、哪些端侧可闭环？NPU 算力与功耗（见 [[端侧 AI 功耗与散热约束 学习笔记]] 方向）如何约束「常驻系统 Agent」？
- [ ] **A2UI 等声明式协议能否统一**：Google A2UI、MCP Apps、Apple App Intents 三套「Agent↔UI」标准，跨平台会收敛还是长期分裂？

---

## 附：来源清单

1. Apple Newsroom — WWDC26 新一代 Apple Intelligence 与 Siri AI（2026-06）`apple.com.cn/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/`
2. The Brief — Apple's Next-Generation Siri and AI（2026，开发者视角）`thebrief.news`
3. aiwiki.ai — Project Astra 词条（能力迁移与 I/O 2025 节点）
4. 9to5Google — Gemini control to Android（2025-12，computer use 预览、屏幕自动化字符串）
5. Microsoft Support 中文 — 实验性代理功能 / Agent Workspace（2025-10 起多次更新）
6. Windows Experience Blog — Making every Windows 11 PC an AI PC（2025-10-16）
7. Microsoft Learn — Copilot Studio Computer Use（CUA）
8. 百度百科 / 腾讯新闻 — Computer Use 发展脉络与 OSWorld 基准（2024-2026）
9. 新浪财经 / 澎湃 — GUI 是否必要、A2UI 协议、GPT-6 Astra 等（2026）
10. a2ui.org + Google Developers Blog — A2UI：Agent-to-UI 声明式协议（Apache 2.0，v0.8 稳定）
11. 行业媒体（HowToApps / LifeTips / EatHealthy365）— Shortcuts、Tasker、MacroDroid、IFTTT 对比（2025-2026）

---

## ⚠️ 待核实清单

- **Siri 是否用 Google Gemini 做推理后端**：某行业媒体称 Apple 用 Gemini 做复杂推理、端侧保留执行层。该来源可信度低，与 Apple 官方「自研 + PCC」口径冲突，**待核实**。
- **Project Mariner 关闭时间**：有报道称 Google 于 2026-05 关闭 Mariner 并并入 Gemini Agent，仅单一来源，**待核实**。
- **OSWorld 基准具体分数**：Claude Sonnet 4.6「72.5%」、Operator CUA「38.1% / WebVoyager 87%」、早期 3.5 Sonnet「14.9%」等来自二手媒体，需以官方/论文为准，**待核实**。
- **A2UI 时间线与版本**：A2UI 由 Google 创建、Apache 2.0、v0.8 稳定 / v0.9 草案，React 渲染器「Q1 2026」等来自官网与博客，版本演进快，**以 a2ui.org 最新为准**。
- **iOS 版本号口径不一**：部分媒体称「iOS 19 / Apple Intelligence 4.0」，Apple 官方新闻稿称「iOS 27」，以官方为准，**待核实**。

---

#标签/OS级Agent #标签/跨应用自动化 #标签/手机AI智能体
