---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-09-01]]"
source:
  - "https://ecorpit.com/eu-dma-android-ai-assistant-interoperability-plan-2027"
  - "https://developer.android.google.cn/ai/appfunctions"
  - "https://developer.android.google.cn/blog/posts/android-17-is-here"
importance_score: "★★★★☆（7/10）"
intent_category: "跨平台 Registry 可发现性 / 监管强制开放"
tags: [概念, AppFunctions, DMA, 跨助手可发现性, Registry, 监管, 2026-09-01]
aliases: [AppFunctions跨助手开放, DMA强制开放, 意图Registry可发现性]
---

# AppFunctions 跨助手可发现性与 DMA 强制开放（2026）

## 一句话定义

欧盟 **DMA（Digital Markets Act）** 决策要求 Google 在 **2027-08 前**向竞品 AI 助手（ChatGPT / Claude / 欧洲本土助手等）开放指定 Android AI 能力；**AppFunctions 的 OS 内置 Registry 正是该「开放」的技术载体**——一个经 `@AppFunction` 声明的函数，在合规语境下应可被**任一通过认证的助手**发现与调用，而非仅 Gemini。这把「意图 Registry 的跨助手可发现性」从产品选择升级为**监管义务**。

## 为什么重要

- **Registry 可发现性首次被外力强制**：此前四平台 Registry 的「谁能发现我的能力」都由平台方（Apple Siri / Google Gemini / 华为小艺 / Windows Copilot）自行决定；DMA 首次用监管把 Android 侧的「单一 Gemini 集成」假设打破，要求 plural assistants。
- **`EXECUTE_APP_FUNCTIONS` 权限边界成为「认证闸门」**：在 EU 语境下，调用方是否持该权限不再只是技术门禁，而是「是否被认定为合规认证助手」的代理——与 Apple 的 App Review / Windows 的 Agent ID 审批构成不同路线的「受控发现」。
- **对 OS PM 的设计前提改变**：做 Android 端意图框架时，不能假设「只有一个系统助手会调我」，必须按「多助手并发可发现」设计（命名冲突裁决、权限分级、能力去重）。

## 适用边界

- 仅约束 **Android / Google 受 DMA 约束的「守门人」身份**；国内安卓（无 GMS/Gemini、各厂商自建 Registry）不受此路径影响（见 [[国内安卓厂商做 App Intent 的阻力]]）。
- 适用范围是「AI 功能/能力」而非全部 App——具体 11 项清单以欧盟官方决策文本为准（**待补**）。
-  enforcement 走「非合规案」慢通道（与 2025-04 对 Apple/Meta 的 €5亿/€2亿罚款同源），deadline 有软约束空间。

## 证据与例子

- **官方 AppFunctions 文档口径**：AppFunctions 把应用能力注册进 Android OS 内置 Registry；调用方须持 `EXECUTE_APP_FUNCTIONS`，可为智能体/应用/Gemini 等助手。这一「注册即系统可发现」机制，正是 DMA 要求的「开放给竞品助手」的天然落点（见 [[Android AppFunctions 设备侧意图 2026]]）。
- **ecorpit 对 DMA 决策的分析**：Google 须在 2027-08 前开放 11 项 Android AI 能力；认证助手（含 ChatGPT/Claude）可持 hotword、读端侧上下文、驱动 App；AppFunctions 使能力「可被设备上任一认证助手发现，而非仅 Gemini」。
- **对照：Apple / Windows 的「受控发现」路线**：Apple 走 App Review + App Store 分发（Extensions 直连 Siri 须过审）；Windows 走 Agent ID（唯一身份 + 审计）；Android/DMA 则是**监管强制的横向开放**，三者目标同（受控发现）、触发机制异（平台治理 vs 监管）。

## 可复用启发

- **做意图 Registry 时，「可发现性」要作为一等维度单列**：谁能发现、发现后能否调用、多助手并发时如何裁决——不能只在「功能描述质量」上优化（呼应 [[Intent Router 语义路由]] 的冲突裁决缺口）。
- **监管可在一夜之间改写「平台默认集成」假设**：OS PM 评估竞品/生态风险时，应把「DMA 类监管强制开放」列为情景变量，而非恒定「单助手」。
- **`EXECUTE_APP_FUNCTIONS` 这类权限边界的语义会随监管漂移**：今天是技术门禁，明天可能是认证代理；设计时不要把它当死值。

## 与其他概念的关系

- **上游/同构**：[[Android AppFunctions 设备侧意图 2026]]（技术载体）｜ [[四平台意图 Registry 来源轴与权限模型对比 2026]]（跨平台 Registry/权限模型，本节点为其「可发现性」维度的展开）。
- **互补**：[[Agent 365 与 Entra Agent ID 智能体控制平面与身份基座 2026]]（Windows 受控发现）｜ [[Apple AppIntents Schema Protocol 2026]]（Apple 受控发现：App Review）｜ [[Confirmation UI 安全机制]]（调用前授权）。
- **对立/张力**：[[国内安卓厂商做 App Intent 的阻力]]（国内无 GMS，DMA 路径不生效，反而强化厂商自建）。
- **索引**：[[意图框架·跨体系索引 MOC]]。

## 开放问题 / 未决

- [ ] 欧盟 DMA 决策官方文本中「11 项 Android AI 能力」的确切清单与 2027-08 deadline 的精确措辞（**待补官方文本**）。
- [ ] AppFunctions Registry 在 DMA 语境下是否要求新的「跨助手身份协商」协议（如 OAuth/互信证书），还是直接复用 `EXECUTE_APP_FUNCTIONS` 权限（**待一手核实**）。
- [ ] 若多认证助手同时发现同一 AppFunction，排序/裁决由 OS 还是应用决定（呼应 [[Intent Router 语义路由]] 的冲突裁决缺口）。

#标签/AppFunctions #标签/DMA #标签/跨助手可发现性 #标签/Registry #标签/监管
