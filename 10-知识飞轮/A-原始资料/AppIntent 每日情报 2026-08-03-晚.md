---
type: daily-index
status: index
captured: 2026-08-03
window: "7 日滚动窗口 2026-07-27 → 2026-08-03（仅记 09:00 版之后的净新增）"
intent_category: "端侧 Planner 评测口径 / 意图授权与支付执行"
importance_score: "★★★☆☆（7/10，21:00 增补跑，窗口内真增量 2 条，单条最高 7/10）"
tags: [AppIntent, 情报, 索引, 2026-08-03]
---

# AppIntent 每日情报 2026-08-03·晚间增补（索引）

> [!abstract]
> 本篇为 2026-08-03 **21:00 增补跑**，去重基线为同日 09:00 版（[[AppIntent 每日情报 2026-08-03]]），四大 OS 官方渠道在这半天内**无新增可核实动作**。**两条真增量**：① Bonsai 1-bit 量化模型第三方实测——**BFCL 73.3% 但 NexusRaven 仅 43.8%**，同族 FP16 版反而只有 25.3%，证明「1-bit QAT 压的是结构化输出而非知识」，且**BFCL 高分 ≠ 会用 API**；② 银联 **APOP/AVOP** 智能体支付生态里程碑（40+ 机构接入），是首个把「意图授权→执行→清算」全链路标准化的国内协议。**最高价值判据**：端侧 Planner 量化选型应按「保 Schema 合规」而非「保精度」，且单一 BFCL 分数不足以支撑跨应用编排选型。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 7/10 | Bonsai 1-bit（PrismML）BFCL v3 实测：Bonsai-8B 1.15GB → **73.3%**，反超 FP16 的 Qwen3.5-9B（64.0%）/ Gemma 4 E4B（65.3%）；同族 Bonsai-4B FP16 仅 **25.3%**；Bonsai-1.7B 0.25GB / 0.4s / 55% 刷新端侧体积下限 | [[Function Calling 端侧工具调用]]（含完整分项表、规模阶梯、口径警示） | [[端侧意图框架 学习笔记]] · [[端侧工具调用]] | [HF `Manojb/small-llm-tool-use-bench`](https://huggingface.co/datasets/Manojb/small-llm-tool-use-bench) ｜ [BFCL 官方榜（对照基线）](https://gorilla.cs.berkeley.edu/leaderboard.html) |
| 7/10 | **BFCL / NexusRaven 分裂**：同一 Bonsai-8B，BFCL 73.3% vs NexusRaven 43.8%，与 Qwen3.5-9B（64.0% / 75–77.1%）排名完全倒转 → BFCL 测格式合规、NexusRaven 测 API 语义理解，评测 SOP 需并列两列 | [[Function Calling 端侧工具调用]] · [[通用 AI Agent 评测基准 2026]] | [[Intent Router 语义路由]] · [[端侧工具调用]] | [HF `Manojb/small-llm-tool-use-bench`](https://huggingface.co/datasets/Manojb/small-llm-tool-use-bench) |
| 6/10 | 银联 **APOP / AVOP** 生态里程碑：40+ 机构接入，新增「支付 Skills 开发技能包」，接入周期 5–7 天 → 分钟级；协议本体发布于 2026-04-02，覆盖意图管理 / 身份与授权 / 风控 / 清算 | [[意图支付授权协议 APOP]]（含凭证四要素、与四大 OS 对照表） | [[确认机制]] · [[意图模式规范]] · [[XPIA 跨提示注入]] | [中国电子银行网 2026-08-03](https://www.cebnet.com.cn/20260803/103160089.html) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：WWDC26 / iOS 27 App Intents（Spotlight 语义索引、`AppIntentsTesting`、Foundation Models、Core AI、Evaluations、欧盟 DMA 延迟上线）→ 本次 WebFetch [官方 App Intents 文档](https://developer.apple.com/documentation/appintents)逐条比对**无变化**；已录于 [[Apple AppIntents Schema Protocol 2026]]。
- **Android**：AppFunctions `alpha10` / Registry / `EXECUTE_APP_FUNCTIONS` 权限模型 → 09:00 版已详录，[官方文档](https://developer.android.google.cn/ai/appfunctions)无新增；见 [[Android AppFunctions 设备侧意图 2026]]。
- **HarmonyOS**：HMAF 2.0 / Graph Reasoning Engine / A2A 端云双模 / A2UI → 已录于 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **Windows**：Copilot Actions / Agent Workspace / Agent 账户 / ACL → 本次 WebFetch 微软 agentic security 文档，四支柱（User Control / Agent accounts / Agent workspace / User Transparency）表述**与既有记录一致**；见 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
- **端侧模型**：FunctionGemma 270M、qwen3-0.6b-tool-router、Needle 26M、LFM2.5-8B-A1B → 均已入 [[Function Calling 端侧工具调用]]。

## 排除项

- AVOP 协议细节本身（2026-07-27 报道已出现，08-03 属**生态进展**而非协议变更）——不重复登记，仅在 [[意图支付授权协议 APOP]] 内标注。
- 采集过程元信息：本轮 Horizon MCP **未连接**（连接器全 disconnected），全程 WebSearch / WebFetch 直取官方源——属流程记录，不入知识层。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- Bonsai 的 **1-bit QAT 训练配方**是否公开？PrismML 官方技术报告与官方模型卡分数待补（若可复现，是端侧 Planner 选型的范式级结论）→ [[Function Calling 端侧工具调用]]
- **NexusRaven 是否应进本库评测标准列**（评测 SOP 加「语义理解分」一列）→ [[通用 AI Agent 评测基准 2026]] · [[Function Calling 端侧工具调用]]
- 口径待核：本条为**第三方个人测评仓**，硬件 Mac Mini M4 **非手机 SoC**，用 BFCL **v3 非 v4**，不可与 Berkeley 官方榜单行并列 → [[Function Calling 端侧工具调用]]
- **APOP 凭证能否与 Apple/Android Intent Schema 对接**（AppFunctions 调起支付时可否携带 APOP 凭证）；其确认 UI 与二次授权形态、是否做到「意图内容与凭证绑定」→ [[意图支付授权协议 APOP]]
- 【连续第 2 日未解·最高优先】四平台 **ADI（Agent Data Injection）分级评估** / intent-metadata 来源可信度，官方文档中未见分级定义 → [[Agent Data Injection 数据注入攻击]] · [[数据溯源分级与单调棘轮]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[端侧意图框架 学习笔记]] · [[Intent Router 语义路由]] · [[意图模式规范]] · [[端侧工具调用]] · [[确认机制]] · [[Atomic Service 元服务]] · [[Agent Workspace 隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[Function Calling 端侧工具调用]] · [[意图支付授权协议 APOP]] · [[通用 AI Agent 评测基准 2026]]

#标签/AppIntent #标签/端侧Planner #标签/BFCL #标签/意图支付
