---
type: output
status: draft
created: 2026-10-05
method_used: "WebSearch/WebFetch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
tags:
  - AppIntent
  - 每日情报速览
  - Android
  - AndroidContextEngine
---

# AppIntent 每日情报速览 2026-10-05

## 目标读者与目标

- 读者：Ethon（OS PM，关注系统级意图框架 / 端侧 Agent 执行总线）。
- 目标：48h 窗口（2026-10-03 → 10-05）内四平台官方框架层新进展的速读版，结论先行、附去重与诚实标注。

## 正文 / 速览表

| 平台 | 本窗口净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | 无（iOS 27.1 beta 未发；FDA 收紧为 10-03 已收录项复述） | — | 已复核·无净新增 |
| Android | **Android Context Engine**（Android 18 proactive caller of AppFunctions）+ Android 18 = Intelligence System 框架 | ★6/10 | **A 索引 + B 既有增补** |
| HarmonyOS | 无（DevEco Code/1200+ Skill 化为生态叙述强化） | — | 已复核·无净新增 |
| Windows | 无（Hey Copilot/Agent Workspace 为已收录项复述） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新入榜） | — | 已复核·无净新增 |
| XPIA | 无（CVE-2026-104120 属 MCP 工具链，丢弃） | — | 已复核·无净新增 |

**唯一真增量一句话**：Android 18 把「端侧意图路由」从被动响应升级为 **OS 原生主动式**（Context Engine 在用户开口前调用 AppFunctions），是四平台主动式意图路由收敛的 Android 落点；但属前瞻公告、非已发布 API。

## 使用的方法

- 直查官方/权威源（developer.android.com/ai/appfunctions、Dev Summit 公告 cluster、Macworld、test.aiagentstore 周报）；逐平台核验「是否出新 API」而非「是否有新文章」。
- 去重：库内已有 Blocker（Apple FDA / Windows Agent Workspace / HarmonyOS ArkAF）均识别为复述，不重复建节点；仅 Android Context Engine 作为新 caller 维度追加 [[Android AppFunctions 设备侧意图 2026]]。

## 发布反馈 / 复盘

- **有效的部分**：延续「OS 框架不日更」纪律，把媒体复述与真实 API 变更区分开，避免把 Dev Summit 前瞻误判为已发布。
- **需要改进的部分**：Microsoft Taxonomy v2.0 在 09-16 跑被误记为「2025-12-05 后无更新」——本次校正为 2026-04/06，已写入 A 索引「诚实校正」段并建议后续跑勿重复收录。
- **回流到 A 的新问题或素材**：Android Context Engine 是否受 `EXECUTE_APP_FUNCTIONS` 同一闸门约束（proactive 场景的确认边界）待官方文档；Android 18 GA 与 AppFunctions 是否随 18 脱离 experimental 待补。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
