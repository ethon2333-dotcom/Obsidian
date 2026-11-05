---
type: output
status: draft
created: 2026-10-29
method_used: "WebSearch + WebFetch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线），Android Dev Summit 2026（10-28）官方公告 + The Prompt Insider/腾讯新闻/Pivot News/Zendoric 多方核验；Jetpack Release Notes 直查 AppFunctions beta01；GitHub 官方 changelog（Copilot Fusion 本地路由）；rlresearch BFCL v4 镜像 + xibilus LFM3 聚合；本运行完成 10-29 窗口复核并落库"
tags:
  - AppIntent
  - 每日情报速览
  - AndroidDevSummit
  - ConnectedAppsPlatform
  - MLKitAgenticAPI
  - GeminiNano4
  - 跨应用Intent工作流
  - GitHubCopilotFusion
  - 本地模型路由
  - LFM3
  - 来源轴延续
---

# AppIntent 每日情报速览 2026-10-29

## 目标读者与目标

- 读者：Ethon（OS PM，关注系统级意图框架 / 端侧 Agent 执行总线）。
- 目标：24h 窗口（2026-10-28 21:00 → 10-29 21:00）内四平台官方框架层 + 跨平台 BFCL + XPIA 的速读版；结论先行，附「唯一 OS 级真增量来自 Android Dev Summit：Connected Apps Platform（AppFunctions 挂到 Search+Gemini）+ ML Kit Agentic API（Gemini Nano 4 端侧函数调用）」。

## 正文 / 速览表

| 平台/维度 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | iOS 27.2 已 10-26/27 GA 且框架层零变更（10-28 WebFetch 直查 App Intents Updates 页仍 June 2026）；本窗口仅消费者功能复述，**无新 `@AppIntent` Schema** | ★★☆☆☆（无净新增） | 已复核·无净新增（10-28 已落档） |
| Android | **① Connected Apps Platform（预览，10-28 Dev Summit）：AppFunctions + Android MCP 经 Connected Console 注册后可达 Gemini app + Search AI Mode（"enable once, run Google-wide"）★7**；**② ML Kit Agentic API（alpha，Gemini Nano 4）：端侧函数调用 + 对话历史 + 执行流控 ★6** | ★★★★☆ | 已捕获·2 处真增量（B 增补） |
| HarmonyOS | 无新 OS 框架 API（CEIC 1024 深圳 10-24 生态复盘，无新 API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无新端侧 Planner official entry；**LFM3-1.7B（Liquid AI，1.7B）BFCL V4 71.39 新出**（端侧 agentic 模型，待官方复核） | ★★☆☆☆（LFM3 ☆5） | 已捕获 LFM3 端侧模型（B 增补） |
| Windows | 无新 OS 执行总线 API；**GitHub Copilot Fusion 本地模型路由落地实验预览（10-28）= 关闭「HydraFusion 10 月底实验预览」跟踪项**，但属编码 harness，非 OS bus | ★5☆☆☆ | 状态更新·非 OS API |
| XPIA | MCP tool server 命令注入一波（CVE-2026-117558~573，10-27）为 MCP 工具链层漏洞，非四平台 OS 框架，按口径丢弃 | — | 丢弃（非 OS 总线） |

**一句话**：本窗口四平台**唯一 OS 级真增量来自 Android Dev Summit（10-28）两项官方公告**——**Connected Apps Platform（预览）**把 AppFunctions/Android MCP 同时挂到 **Gemini app 与 Search AI Mode**（首个把设备侧意图框架接入系统级搜索入口的官方能力，★7），与 **ML Kit Agentic API（alpha，Gemini Nano 4）**端侧函数调用/对话历史/执行流控（★6）共同补强 Android 端侧意图执行总线的「工具层 + 模型层」。**其余平台零净新增**：Apple（27.2 GA 已落档、框架零变更）、HarmonyOS（仅生态复盘）、Windows（无新 OS API，仅 GitHub Copilot Fusion 本地路由实验预览落地、编码 harness 非 OS bus）、BFCL v4（无新端侧 Planner official entry，但 LFM3-1.7B 端侧模型新出）。**本运行 0 新建 B 节点、3 处 B 既有增补**（[[Android AppFunctions 设备侧意图 2026]] / [[Function Calling 端侧工具调用]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。

## 使用的方法

- 逐平台核验「是否出新 API」：Apple 沿用 10-28 已 WebFetch 直查的 App Intents Updates 页（June 2026，零变更）+ 27.2 消费者复述识别；Android 走 Android Dev Summit 10-28 官方公告 + The Prompt Insider/腾讯/Pivot/Zendoric 多方交叉 + Jetpack Release Notes 直查（beta01 仍最新）；Windows 走 GitHub 官方 changelog（Copilot Fusion 本地路由）；BFCL 走 rlresearch 镜像（10-25 快照，104 模型）+ xibilus（LFM3）。
- 去重与阈值：Connected Apps Platform / ML Kit Agentic API 按 **★7/★6** 落 B 增补；GitHub Copilot Fusion 本地路由按 **★5 编码 harness 状态更新**标记（关闭 HydraFusion 跟踪项、非 OS bus）；XPIA MCP 工具链一波 / Android Studio BYOA / HarmonyOS CEIC 复盘 / Apex-35B 按「非四平台 OS 框架执行总线 / 非端侧 / 落窗口外」丢弃，不升净新增、不改 B（仅 3 处既有 B 增补）。
- 诚实：本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch + WebFetch 直查官方源 + 权威媒体完成逐平台核验；Dev Summit 公告（10-28）处窗口起点边缘、10-28 运行未记录，本运行作诚实边界补捕。

## 发布反馈 / 复盘

- **有效的部分**：捕获了 Android Dev Summit 两项 OS 级真增量，尤其是 **Connected Apps Platform**——它把 AppFunctions 的「跨应用 Intent 工作流」从 Gemini app 内扩到系统级 Search 入口，是四平台里该方向的首个官方能力；与既有 [[Android AppFunctions 设备侧意图 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]] 形成 discovery-surface 维度补强。
- **需要改进的部分**：Dev Summit 公告（10-28）恰在本窗口起点边缘，10-28 运行未覆盖；后续若遇「大会日」应把大会公告单列优先核验，避免边界漏捕。
- **回流到 A 的新问题或素材**：本运行产出 A 索引 + D 速览各 1；**B 既有增补 3 处**（[[Android AppFunctions 设备侧意图 2026]] 追加 10-29 Connected Apps Platform + ML Kit Agentic API 段 / [[Function Calling 端侧工具调用]] 追加 10-29 ML Kit Agentic API + LFM3-1.7B 段 / [[四平台意图 Registry 来源轴与权限模型对比 2026]] 追加 10-29 discovery-surface + 来源轴延续段）。待办顺延：**【最高优先·来源轴仍空白】四平台意图 Registry 来源/provenance 轴仍全空白（confirmed）**；`@AppFunctionAccessLevel` 级别语义（待 developer.android.com/ai/appfunctions）；AppFunctions GA 日期；Connected Apps Platform 是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门（待官方）；ML Kit Agentic API SDK 形态/权限边界（待官方）；LFM3-1.7B 确切官宣日期 + BFCL 官方榜复核；GitHub Copilot Fusion 本地路由是否向 Windows OS Copilot Actions 下沉（当前仅编码 harness）；Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / Berkeley 官方 BFCL v4 博客原文 / A2UI alpha02 / Per-Intent Privacy Manifest 官方逐字 / 高通 NPU exact specs。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]] [[MCP 与设备侧 MCP]] [[意图框架·跨体系索引 MOC]]
