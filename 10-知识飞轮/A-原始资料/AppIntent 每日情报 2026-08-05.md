---
type: daily-index
status: index
captured: 2026-08-05
window: "7 日滚动窗口 2026-07-30 → 2026-08-05"
intent_category: "系统级 Agent 执行总线 / 端侧 Planner 意图路由 / 评测口径"
importance_score: "★★★☆☆（7/10，窗口内真增量 2 条 + 1 条口径待办关闭）"
tags: [AppIntent, 情报, 索引, 2026-08-05]
---

# AppIntent 每日情报 2026-08-05（索引）

> [!abstract]
> 窗口内四大 OS 官方渠道经逐条复核**无新增可执行 API**；**两条真增量**：① Windows Agent Launchers 系统级 agent 注册表（补齐 Windows「应用向系统声明可调用能力」的注册层，四平台首次在「能力声明」层对齐）② LFM2.5-2.6B 端侧 agentic 小模型（LFM2.5 家族 230M / 450M / 2.6B / 8B-A1B 规模阶梯完整）。另关闭一条延续待办：BFCL v4 权重公式经 EvalScope 官方文档确认。**最高价值判据**：Windows 不再是「只有工具注册」，而是具备「应用声明能力 → 系统受控发现」的完整骨架，只是颗粒度目前是 agent 而非细粒度 intent/function。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 7–8/10 | Windows Agent Launchers：系统级 agent 注册表（`com.microsoft.windows.ai.agentInfo` / `odr.exe agent-info`） | [[Windows Copilot Actions 与 Agent Workspace 2026#2026-08-05 增补]] | [[Intent Router 语义路由]] · [[意图模式规范]] | [learn.microsoft.com · agent-launchers](https://learn.microsoft.com/windows/ai/agent-launchers/) |
| 7/10 | LFM2.5-2.6B：端侧 agentic 小模型（2.6B / <2.5GB / 手机≈30 tok/s） | [[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] | [[端侧工具调用]] · [[Agent Skills 技能范式 2026]] | [Liquid AI 官方博客 2026-08-04](https://www.liquid.ai/blog) |
| 6/10 | BFCL v4 权重公式核实（Agentic 40% / Multi-Turn 30% / Live+NonLive+Hallucination 各 10%） | [[Function Calling 端侧工具调用]] · [[通用 AI Agent 评测基准 2026]] | [[端侧工具调用]] | [EvalScope 官方文档](https://evalscope.readthedocs.io/) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：App Intents 2.0（Session 345/343）均为既有记录，窗口内无新增 API。
- **Android**：AppFunctions 仍 experimental / private preview，无新 API。
- **HarmonyOS**：ArkAF 相关文章发表日 2026-06-17，在窗口外，已并入既有笔记不重复登记。
- **Windows**：agentic security 四支柱与 08-04 一致；Agent Launchers 属 ODR / App Actions 框架补全，已在条目 1 单独记录。

## 排除项

- 无非 OS 级 / 纯营销 / 概念-only 论文需排除；低于 6/10 的窗口内碎片已在检索阶段丢弃。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- Agent Launchers 具体 Insider build 号 / 发布日期 / opt-in 开关归属 → [[Windows Copilot Actions 与 Agent Workspace 2026]]
- LFM2.5-2.6B 的 BFCLv4 绝对值（厂商 + 镜像站 56.9%，需官方榜复核）→ [[Function Calling 端侧工具调用]]
- 【连续第 5 日未解·最高优先】四平台意图元数据来源分级（Apple `.appEntityIdentifier` 来源绑定 / 签名仍待补）→ [[Agent Data Injection 数据注入攻击]]
- Berkeley 官方 BFCL v4 博客原文逐字确认 → [[通用 AI Agent 评测基准 2026]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[Intent Router 语义路由]] · [[意图模式规范]] · [[端侧工具调用]] · [[Agent Skills 技能范式 2026]] · [[XPIA 跨提示注入]] · [[确认机制]]
> **本期原子笔记**：[[Windows Copilot Actions 与 Agent Workspace 2026]] · [[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] · [[通用 AI Agent 评测基准 2026]]
