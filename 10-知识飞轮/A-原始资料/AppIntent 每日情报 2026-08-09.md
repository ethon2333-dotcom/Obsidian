---
type: daily-index
status: index
captured: 2026-08-09
window: "7 日滚动窗口 2026-08-03 → 2026-08-09"
intent_category: "系统级 Agent 执行总线 / 执行安全 XPIA / 端侧 Planner 意图路由"
importance_score: "★★★☆☆（7/10，窗口内真增量 2 条 + 库内空白补漏 1 条）"
tags: [AppIntent, 情报, 索引, 2026-08-09]
---

# AppIntent 每日情报 2026-08-09（索引）

> [!abstract]
> 窗口内四大 OS 官方渠道经逐条复核**无新增可执行 API**；**两条真增量** + **一条库内空白补漏**：① **Windows Agent Framework / Microsoft Agent Framework 端侧 Agent 执行框架**（Build 2026-06-02 的 OS 级栈 Runtime/Store/Mesh/Copilot Workspace/Polaris + 2026-04-02 SDK 合并 SK+AutoGen，本库此前无对应权威节点，属「库内空白补漏」，标真实日期不冒充当日新闻）② **NowSecure iOS 27 App Intents 攻击面**（2026-08-05，AppSec 厂商视角把 App Intents→agentic Siri→iOS 27 威胁模型落到实处）③ **AgentAntibody**（arXiv 2608.04053，2026-08-04，XPIA 的「学习型防御」分支，补本库静态防御之外的缺口）。**最高价值判据**：Windows 在 2026 年已不只是「应用声明能力」，而是提供了「OS 内建 agent 宿主 + 联邦执行 + 分发市场」的完整 agent 执行框架，与另三家路线分叉（应用声明 vs OS 宿主）。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 7–8/10 | Windows Agent Framework / Microsoft Agent Framework：端侧 Agent 执行框架（Build 2026-06-02 OS 级栈 + 2026-04-02 SDK 合并 SK+AutoGen，库内空白补漏） | [[Windows Agent Framework 端侧 Agent 执行框架 2026]] | [[Intent Router 语义路由]] · [[意图框架·跨体系索引 MOC]] | [Microsoft Build 2026 / Agent Framework 官方](https://aka.ms/Build2026MicrosoftAgentFramework) · [Agent Framework 概述(learn)](https://learn.microsoft.com/en-us/agent-framework/) |
| 7/10 | NowSecure iOS 27 App Intents 攻击面（AppSec 视角，2026-08-05，关联 Session 347 威胁模型） | [[Apple AppIntents Schema Protocol 2026#2026-08-09 增补]] · [[XPIA 跨提示注入]] | [[XPIA 跨提示注入]] · [[确认机制]] | [NowSecure blog 2026-08-05](https://www.nowsecure.com/blog/2026/08/05/what-appsec-teams-need-to-know-about-app-intents-siri-ai-and-the-new-ios-27-attack-surface) |
| 6–7/10 | AgentAntibody：自适应免疫防御（arXiv 2608.04053，2026-08-04，XPIA 学习型防御分支） | [[AgentAntibody 自适应免疫防御 2026]] · [[XPIA 跨提示注入]] | [[XPIA 跨提示注入]] · [[确认机制]] | [arXiv 2608.04053](https://arxiv.org/abs/2608.04053) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：App Intents 2.0（Session 345/343/240）均为既有记录，窗口内无新增 API；NowSecure 攻击面属「AppSec 视角补充」，已在条目 2 单独记录。
- **Android**：AppFunctions 仍 experimental / private preview（alpha10），无新 API。
- **HarmonyOS**：ArkAF 2.0 / HMAF 2.0 为 06 月 HDC 内容，窗口外，已在既有笔记。
- **Windows**：agentic security 四支柱 + Project Perception（检查） + Agent Launchers（注册表）与 08-05 一致；本次只是把 Build 2026 的 Runtime/Store/Mesh/Copilot Workspace/Polaris + MAF SDK 串成完整框架节点（条目 1）。
- **评测**：BFCL v4 权重已 08-05 经 EvalScope 官方文档确认；LFM2.5 系列已录；窗口内大模型新发布（Qwen3.7/Ling 3.0 等）低于阈值，见排除项。

## 排除项

- **大模型发布（低于阈值）**：Qwen3.7 Max / Qwen3.7 Plus / Ling 3.0 Flash 等多为大参数或纯模型发布，非直接用于端侧意图路由，不收录（端侧小模型仅 LFM2.5 系列在库）。
- 营销稿 / 概念-only 文章 / 非 OS 级应用层 agent 新闻（如某 App 接入 Copilot）已在检索阶段丢弃。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- 【连续第 6 日未解·最高优先】四平台意图元数据来源分级（Apple `.appEntityIdentifier` 来源绑定 / 签名仍待补）→ [[Agent Data Injection 数据注入攻击]]
- Windows Agent Framework 官方 MIT 许可页 / Agent Runtime 具体 Insider build 号 / Agent Mesh GA 具体日期 → [[Windows Agent Framework 端侧 Agent 执行框架 2026]]
- NowSecure 为移动 AppSec 厂商视角，其技术映射（间接 PI 经工具输出/日历/锁屏触发）需独立核验 → [[XPIA 跨提示注入]]
- AgentAntibody 预印本数字未在独立榜复现 → [[AgentAntibody 自适应免疫防御 2026]]
- Berkeley 官方 BFCL v4 博客原文逐字确认 → [[通用 AI Agent 评测基准 2026]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[Windows Agent Framework 端侧 Agent 执行框架 2026]] · [[AgentAntibody 自适应免疫防御 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[XPIA 跨提示注入]]
