---
date: 2026-09-30
tags: [情报速览, AppIntents, 系统级意图框架, 执行安全]
method_used: 直查官方源（WebSearch/WebFetch，Horizon MCP 未连接）
intent_category: 执行安全 / 跨平台评测 / OS 部署里程碑
---

# AppIntent 每日情报速览 2026-09-30

## 目标读者与目标
OS PM / 端侧 Agent 框架研究者；快速掌握 2026-09-26 22:07 → 09-30 21:00 窗口内四大 OS 意图框架 + 执行安全新进展。

## 正文（一句话结论 + 速览表）

**窗口结论**：四大 OS 官方框架层 API 仍零净新增（延续「OS 框架不日更」规律）；唯一 OS 级里程碑 = **Windows 11 26H2 于 2026-09-29 GA**（enablement 形态，Ask Copilot + File Explorer 内 Copilot 侧栏落地，Copilot Actions/Agent Workspace 仍 experimental opt-in）。真正增量集中在**执行安全（XPIA）**与**跨平台评测刷新**。

| 平台/主题 | 本窗口状态 | 重要性 | 落点 |
|---|---|---|---|
| Apple AppIntents | iOS 27.1 无新 Schema；SiriKit deprecated 迁移窗口 2~3 年 | ★3 | 已覆盖，无新增 |
| Android AppFunctions / A2UI | 守 alpha12 / alpha01，无 alpha13/alpha02 | ★3 | 已覆盖，无新增 |
| HarmonyOS Intents Kit / ArkAF | 无新 API（HC2026 已覆盖） | ★3 | 已覆盖，无新增 |
| Windows 26H2 | **09-29 GA**（enablement）；Ask Copilot + File Explorer Copilot 侧栏新 surface | ★6 | [[Windows Copilot Actions 与 Agent Workspace 2026]] |
| BFCL v4 评测 | BenchLM 09-28 刷新；BTL-3 88.5% 居首（大模型非端侧） | ★5 | [[Function Calling 端侧工具调用]] |
| XPIA·多智能体注入 | arXiv:2609.22949，14 向量/67% 越权，四防御 31.2%→4.2% | ★6 | [[XPIA 跨提示注入]] |
| XPIA·自复制注入 | OpenAI Alignment 09-26 警告，上下文窗口变开放中继 | ★6 | [[XPIA 跨提示注入]] |
| XPIA·SearchLeak 重提 | CVE-2026-42824（2026-06 已缓解）+ Purview 标签门控（待确认） | ★5 | [[XPIA 跨提示注入]] |

## 使用的方法
WebSearch/WebFetch 直查官方/权威源（BetaWiki / developer.android.google.cn / BenchLM / arXiv 转述 / 安全媒体）；未调用 Horizon MCP（环境仅 `agent-mail` 在线）。

## 复盘
- **有效**：窗口无 OS 框架 API 净新增，与连续多轮结论一致，本日 0 新建 B 节点（全部追加既有笔记）。
- **改进**：XPIA 两则新研究来源置信度参差（arXiv 预印本 / 机器撰写媒体），已逐条标注待一手复核。
- **回流到 A 的新问题**：多智能体注入一手论文、自复制注入 OpenAI 原文、Purview 标签治理官方确认、26H2 agentic 入口 opt-in 管控官方逐字。
