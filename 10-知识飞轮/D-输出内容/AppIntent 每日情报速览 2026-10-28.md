---
type: output
status: draft
created: 2026-10-28
method_used: "WebSearch + WebFetch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线），四平台官方源 + App Intents Updates 页（WebFetch 直查）+ Jetpack Release Notes + iOS 27.2 发布说明/媒体 + 华为 CSDN 教程 + heise.de Surface 活动 + benchlm.ai/llmboard.ai BFCL v4 镜像榜逐条核验；本运行完成 10-28 窗口复核并落库"
tags:
  - AppIntent
  - 每日情报速览
  - iOS27.2
  - 正式版
  - 无新Schema
  - ExcludedApps
  - 意图访问治理
  - 160CVE
  - Windows
  - Surface事件
  - HydraFusion
  - 无净新增
  - 复核型
---

# AppIntent 每日情报速览 2026-10-28

## 目标读者与目标

- 读者：Ethon（OS PM，关注系统级意图框架 / 端侧 Agent 执行总线）。
- 目标：约 44h 窗口（2026-10-26 22:53 → 10-28 19:03，衔接上轮 10-26 收尾）内四平台官方框架层 + 跨平台 BFCL + XPIA 的速读版；结论先行，附「iOS 27.2 正式版框架零变更、唯一治理细化 = 排除的 App 统一意图访问排除设置」「Windows 10-28 Surface 活动 = HydraFusion 本地路由预览到点、无新 OS API」。

## 正文 / 速览表

| 平台/维度 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | **iOS 27.2 正式版（10-26/27，24B119；Duo 24B91020）发布**，但 App Intents Schema **框架层零变更**（App Intents Updates 页 WebFetch 直查仍 June 2026，无 Oct 条目）；唯一治理细化 = **「排除的 App」统一意图访问排除设置**（消费者层，★6） | ★★★☆☆（GA 发布 + 消费者层意图访问治理细化，非新 Schema API） | 已复核·无新 Schema；捕获 Excluded Apps 治理细化（B 增补） |
| Android | **AppFunctions 仍 `1.0.0-beta01`（10-21）为最新**，无 beta02 / alpha14（Jetpack Release Notes 直查确认） | ★★☆☆☆（无净新增） | 已复核·无净新增 |
| HarmonyOS | 无新 OS 框架 API（CSDN 第14/18 课为教程；DigitalMate 第三方 agent 跑在 HarmonyOS，基于 A2UI 声明式渲染） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无新端侧 Planner official entry；镜像榜稳定（benchlm.ai 10-17 / llmboard.ai 10-23），端侧 LFM2.5-230M 21% / MiniCPM5-2B 66.6% 维持；官方 Berkeley 榜仍停滞（2026-04-12） | — | 已复核·无新端侧 Planner |
| Windows | 10-28 Surface 活动 = **HydraFusion 本地/云端路由实验性预览到点** + MXC GA 再确认（已跟踪节点落地），**无新 OS 执行总线 API**；XPIA 警告为已知重述 | ★5☆☆☆ | 已捕获事件稳定·无净新增 |
| XPIA | iOS 27.2 修复 160+ CVE（含 Apple Intelligence 远程数据访问漏洞）属安全事件；Windows XPIA 警告重述；均无新 OS 框架 CVE | ★5☆☆☆ | 低于阈值·关联观察/丢弃，不升新节点 |

**一句话**：本窗口四平台**官方框架层仍零净新增 API**（iOS 27.2 正式版框架零变更、App Intents Updates 页直查仍 June 2026；Android beta01 仍最新；HarmonyOS 仅教程；BFCL 端侧 Planner 无新 entry；Windows 10-28 Surface 活动无新 API），与连续多轮「OS 框架不日更」结论完全连续。**唯一 OS 级治理细化（★6/10）= iOS 27.2 新增「排除的 App」统一隐私设置**——用户可统一选择哪些 App 不能被 Siri/搜索/建议访问，是 Apple 侧首个系统级「意图访问排除清单」消费者层落地，强化「agent 执行边界 = OS 权限/访问边界」跨平台收敛。**重大 OS 安全事件（XPIA 相邻，低于新节点阈值）= iOS 27.2 修复 160+ CVE（163 个），含 Apple Intelligence 远程数据访问漏洞**。**本运行 0 新建 B 节点、3 处 B 既有增补**（[[Apple AppIntents Schema Protocol 2026]] / [[四平台意图 Registry 来源轴与权限模型对比 2026]] / [[Windows Copilot Actions 与 Agent Workspace 2026]]）。

## 使用的方法

- 逐平台核验「是否出新 API」而非「是否有新文章」：Apple 走 `developer.apple.com/documentation/updates/appintents`（**WebFetch 直查**确认仍 June 2026）+ iOS 27.2 发布说明/媒体；Android 走 Jetpack Release Notes 直查；华为走 CSDN 教程 + 开发者文档；Windows 走 heise.de Surface 活动 + learn.microsoft.com XPIA 文档；BFCL 走 benchlm.ai/llmboard.ai 镜像榜交叉。
- 去重：iOS 27.2（GA 但无新 Schema、捕获 Excluded Apps 治理细化）/ Android（beta01 无新增）/ HarmonyOS / Windows（Surface 活动无新 API、捕获 HydraFusion 预览到点状态）/ BFCL / XPIA 识别为无净新增或低于阈值；「排除的 App」按 **★6 消费者层意图访问治理**落 B 增补，其余按「低于 ★6 阈值 / 非 OS 框架执行总线」标关联观察或丢弃，不升净新增、不改 B（仅 3 处既有 B 增补）。
- 诚实：本运行未使用 Horizon MCP（仅 agent-mail 在线），全部以 WebSearch + WebFetch 直查官方源 + 权威媒体完成逐平台核验；结论均来自官方页 + 权威媒体直接核验。

## 发布反馈 / 复盘

- **有效的部分**：延续「OS 框架不日更」纪律，把「已复核·无净新增」显式落档；并把前几轮「iOS 27.2 是否带新 Schema」的 **RC 推断升级为正式版发布后的官方页逐字确认**（WebFetch 直查 App Intents Updates 页仍是 June 2026）——这是本运行相对 10-26 的核验精度提升；同时捕获 iOS 27.2「排除的 App」这一 Apple 侧消费者层意图访问治理细化，补全了跨平台「agent 执行边界 = OS 权限/访问边界」收敛的消费者层拼图。
- **需要改进的部分**：本运行窗口约 44h（衔接 10-26 收尾），属「自上次跑以来的空档复核」，符合 7 日滚动纪律的精神；后续若再次空档，宜在首跑补「空档期重大里程碑」清单（本次已隐式覆盖）。
- **回流到 A 的新问题或素材**：本运行产出 A 索引 + D 速览各 1；**B 既有增补 3 处**（[[Apple AppIntents Schema Protocol 2026]] 追加 10-28 iOS 27.2 GA·无新 Schema + Excluded Apps 段 / [[四平台意图 Registry 来源轴与权限模型对比 2026]] 追加 10-28 消费者层意图访问排除段 / [[Windows Copilot Actions 与 Agent Workspace 2026]] 追加 10-28 Surface 活动·HydraFusion 预览到点段）。待办顺延：**【最高优先·来源轴仍空白】四平台意图 Registry 来源/provenance 轴仍全空白（confirmed）**，最低成本补丁仍是加 `readOrWrite` 声明位；`@AppFunctionAccessLevel` 级别语义（待 developer.android.com/ai/appfunctions 官方文档）；AppFunctions GA 日期；iOS 27.2 的 agentic 安全与多模型路由落地；iOS 27.2「排除的 App」是否影响开发者侧 intent 注册可见性（待 Apple 开发者文档）；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核；Berkeley 官方 BFCL v4 博客原文。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]] [[MCP 与设备侧 MCP]] [[意图框架·跨体系索引 MOC]]
