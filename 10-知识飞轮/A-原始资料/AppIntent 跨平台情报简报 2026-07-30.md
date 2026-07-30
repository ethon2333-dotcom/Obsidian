---
type: raw
status: inbox
source: "Apple WWDC26 AppIntents (developer.apple.com/videos/play/wwdc2026/343); Android AppFunctions (developer.android.google.cn/ai/appfunctions); HarmonyOS Intents Kit (developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-introduction); Windows Agentic Security (learn.microsoft.com/windows/security/book/operating-system-agentic-security)"
captured: 2026-07-30
tags: [AppIntent, OS-Agent, 跨平台2026]
---

# AppIntent 跨平台情报简报（2026-07-30）

> 本文件为「原始资料」层：保留来源与原始语境，不追求整洁。已据此提炼出 B 泛化概念 12 篇、C 可复用方法 1 篇、D 输出 1 篇。

## 原始内容

**核心突破**：Apple / Android / HarmonyOS / Windows 同步将 App Intent 从「命令映射」升级为 **Schema Protocol + 端侧 Agent 执行总线**——应用以自描述工具（AppIntent / AppFunction / Intent / Agent Connector）向系统注册，由 System Broker 统一做意图解析、路由与跨应用编排。

**关键指标**：
- Apple：系统级 Schema（messages / photos / calendar / audio 等）+ `IndexedEntity` 语义索引。
- Android AppFunctions = 设备端 MCP（需 `EXECUTE_APP_FUNCTIONS` 权限）。
- 端侧 Planner：FunctionGemma 270M 微调后 Tool Choice 准确率 46%→90%、Pixel 7 上 ~2000 tok/s；qwen3-0.6b-tool-router BFCL Multi-Turn Base 90.42%。

**OS Agent 场景**：一句话跨 App 执行（Apple App Actions / HarmonyOS 意图即服务）+ 屏幕感知自动操作（Windows Copilot Vision + Android UI Automation）+ 多应用 Intent Chaining 工作流。

### Schema 定义与语义路由
- 四平台共识：**开发者声明 Schema/Tool，System Broker 负责 Discovery 与 Routing**。Apple `@AppIntent(schema: .audio.addToPlaylist)`；Android AppFunctions 暴露为设备端 MCP 工具注册进 OS 内置 Registry；HarmonyOS `Want` + 元服务（`installationFree: true`）；Windows 经 On-Device Registry (ODR) 注册 MCP 连接器。
- 端侧路由：FunctionGemma 270M 经单应用 Schema 微调后 46%→90%（LiteRT-LM, Pixel 7 ~2000 tok/s）；qwen3-0.6b-tool-router（0.6B、禁 CoT、严格 JSON）作确定性 edge router，BFCL Multi-Turn Base 90.42% / Relevance 90.89%。混合架构（FunctionGemma 本地 + 低置信升级 Gemini Flash + Qwen3-Embedding-0.6B 语义缓存学习环）实现本地优先、随时间降云端依赖。
- 跨应用 Chaining：Apple Siri App Actions 多 App 编排；Shortcuts 2.0「Agentic Macro」借 MCP 让 Slack/Notion 暴露 Internal Actions，App 退化为 headless 服务；HarmonyOS ArkAF 三层（意图框架+Skills 框架+端侧 A2A）配 A2UI 动态 UI 实现「意图即服务」；Windows Copilot Actions 在 Agent Workspace 跨 App + 云连接器链式执行。

### 系统安全与确认
- 确认机制：Apple `OwnershipProvidingEntity`（EntityOwnership `.shared`/`.public`/`.unknown`）+ 系统级确认拦截高危 Intent；Windows Agent Workspace 隔离桌面会话、低权限账号、ACL/审计/吊销、Agent 须签名、敏感步骤显式同意、连接器走 OAuth；Android UI Automation 对购买等敏感动作「执行前预警」。
- 错误恢复与防注入：Apple `IntentDonationManager.donate(intent:result:)` 回捐系统学习偏好；Windows 将 XPIA（Cross-Prompt Injection）列为新型风险，要求连接器注册于 ODR 受控发现，会话隔离 + 用户始终在环缓解。

## 值得保留的点

- 四平台殊途同归：**声明式 Schema/Tool + System Broker 语义路由**，是「意图即服务」分发入口之争。
- 端侧小模型 Planner 实测可用（FunctionGemma 46%→90%），把路由延迟/成本压到端侧是趋势。
- 安全范式分化：Apple 走 EntityOwnership 归属判定，Windows 走隔离会话 + 签名 + ACL，HarmonyOS 走可信设备协商。

## 我的问题

- iOS 27 / Android 17 / HarmonyOS 7 / Windows Agentic 正式版落地差异？
- 四平台 Registry / 权限模型横向对比，能否提炼 OS Agent 设计 Checklist？
- Gemma 4 / Qwen3-Coder-Next 端侧路由实测数据？（当前仅 FunctionGemma / qwen3-0.6b 有实测）

## 后续动作

- [x] 提炼为概念（→ B 泛化概念 12 篇：4 平台卡 + 8 概念节点）
- [x] 关联已有方法（→ C 系统级 Intent 路由评估 SOP；→ 已有 [[手机AI智能体知识库]]）
- [ ] 跟踪四平台正式版差异（回流 A）
- [ ] 补 Gemma 4 / Qwen3-Coder-Next 实测（回流 A）

#标签/AppIntent #标签/OSAgent #标签/跨平台2026
