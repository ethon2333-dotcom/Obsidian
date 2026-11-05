---
type: output
status: draft
created: 2026-10-09
method_used: "WebSearch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线），四平台官方源 + Jetpack alpha-channel/Release Notes + 安全媒体逐条核验"
tags:
  - AppIntent
  - 每日情报速览
  - Android
  - AppFunctions
  - alpha12
  - 版本复核
  - 权限模型
---

# AppIntent 每日情报速览 2026-10-09

## 目标读者与目标

- 读者：Ethon（OS PM，关注系统级意图框架 / 端侧 Agent 执行总线）。
- 目标：24h 窗口（2026-10-08 21:00 → 10-09 21:00）内四平台官方框架层 + 跨平台 BFCL + XPIA 的速读版；结论先行，附去重 / 丢弃与诚实标注。

## 正文 / 速览表

| 平台/维度 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Android | **AppFunctions `1.0.0-alpha13`（10-07）**：`@AppFunctionAccessLevel` 函数侧访问限制 + `@AppFunction`→`AppFunctionDeclaration` 重命名 + `AppFunctionMetadata` 暴露 | ★★★★☆ | **真增量·已收录（纠正 10-08 漏捕）** |
| Apple | 无（iOS 27.2 beta 3 无新 `@AppIntent(schema:)`；AT&T carrier bundle 非框架） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit 稳定；ArkAF 2.0 / A2UI 无新 OS API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新入榜；FunctionGemma/LittleLamb/Qwen3-0.6B 为已知 model card） | — | 已复核·无净新增 |
| Windows | 10-07 事件 10-09 复述：taskbar Search actions + Entra 本地 agent 身份扩展 + MAI Code 1.1 Flash 本地参数 corroboration | — | 已捕获事件补细节（非独立净新增） |
| XPIA | CVE-2026-26133（M365）/ OpenClaw / PraisonAI 经核查非四平台 OS 框架 | — | 去伪·丢弃 |

**一句话**：本窗口唯一 OS 级净新增是 **Android AppFunctions `alpha13`（10-07 发布）**——其 `@AppFunctionAccessLevel` 是设备侧 MCP / 意图 Registry 里**首个函数侧访问限制原语**，把 Android 权限模型补成「caller 权限 + 可见性 scope + 函数侧 access level」三向约束；上一轮（10-08）误判「无 alpha13」本运行已纠正。其余平台与 BFCL 均无净新增；Windows 10-07 事件仅得 3 个补细节；XPIA 命中按「非 OS 执行总线」丢弃。

## 使用的方法

- 逐平台核验「是否出新 API」而非「是否有新文章」：Android 直查 `developer.android.com/jetpack/androidx/releases/appfunctions` + alpha-channel（确认 alpha13 / 2026-10-07）；Apple 走 9to5Mac/developer forum 交叉确认（iOS 27.2 beta 3 无新 Schema、AT&T carrier bundle 非框架）；华为 Intents Kit 官方页（2026-09-14 稳定）；BFCL 走 HF model card + benchlm；XPIA 走 Permiso/LinkedIn/CNCERT/agentfailures 核验落地层。
- 去重：Apple / HarmonyOS / BFCL 均识别为无新增；XPIA 三项（M365 CVE / OpenClaw / PraisonAI）按「非四平台 OS 框架执行总线」丢弃（同 10-06 GitLab AI Gateway、10-05 MCP 工具链 CVE 口径）。

## 发布反馈 / 复盘

- **有效的部分**：延续「OS 框架不日更」纪律，直查官方 Jetpack Release Notes 抓出上一轮（10-08）漏捕的 **alpha13**，并正确识别其 `@AppFunctionAccessLevel` 为权限模型新增维度（而非路由/评测增量）。
- **需要改进的部分**：10-08 跑因未直查 alpha-channel 而误判「alpha12 无 alpha13」——后续每轮对 Android 侧应优先直查 `developer.android.com/jetpack/androidx/versions/alpha-channel` 与 Release Notes，不依赖前一轮结论。
- **回流到 A 的新问题或素材**：新建/增补：A 索引 + D 速览 + B 既有增补 3（Android AppFunctions / 四平台 Registry 对比 / Windows Copilot Actions）。待办顺延（`@AppFunctionAccessLevel` 级别语义 / Berkeley 官方 BFCL v4 博客 / AppFunctions GA / iOS 27.1 正式版 Schema / A2UI alpha02）。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
