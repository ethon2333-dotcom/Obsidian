---
type: output
status: draft
created: 2026-09-15
method_used: "WebSearch/WebFetch 官方源 + 库内去重（窗口 2026-09-13→09-15，iOS 27 09-14 GA）"
tags: [AppIntent, 速览]
---

# AppIntent 每日情报速览 2026-09-15

## 目标读者与目标
OS PM（Ethon）；30 秒掌握四平台系统级意图框架过去两日真增量（重点：iOS 27 GA 落地 + 一处路由待办校正 + 一处执行安全机制）。

## 正文
本期窗口（2026-09-13→09-15）是**真·GA 窗口**：iOS 27 于 09-14 正式发布、HarmonyOS 7 消费者版 09-07 已在铺开、Windows 11 26H2 下旬在即。四大 OS 框架层除 iOS 27 GA 确认的 Schema Protocol 能力外无其它净新增 API；真增量 = ① GA 落地确认、② 一处执行安全机制、③ 一处路由待办校正。

1. **iOS 27 GA（09-14）：App Intents Schema Protocol + Foundation Models 多模型路由获官方 post-GA 确认（最高价值）**：Apple 官方「What's New in iOS 27」页确认 iOS 27 的 App Intents 框架能力——**Entity schemas**（把 App 内容贡献进 Spotlight 语义索引、归属回 App）、**Intent schemas**（免特定短语、随 Siri 语言理解演进免改码）、**View Annotations API**（把视图映射为实体，对话式引用/操作屏幕内容）、**App Intents Testing 框架**（真实系统路径验证）。更重要的是 **Foundation Models 框架宣布支持任意语言模型**：Apple FM、云端模型（Claude、Gemini）或任何遵循 `Language Model` 协议者均可接入；**Dynamic Profiles** 允许在连续会话内实时切换模型/工具/instructions；**Evaluations 框架**验证 AI 功能在动态条件下行为正确。意义：① OS 级 Planner 首次把「多模型路由」（含云端大模型）写进一等公民框架，端云路由从架构决策降为运行时旋钮；② 与 08-17 已记「可切换 Apple/Claude/Gemini」一致，本次为 GA 确认升级。⚠️ 上述均为 WWDC26 已宣布、本次 GA 落地的能力，非 WWDC 之外的全新 API。

2. **Per-Intent Privacy Manifest 待办重开（校正，最高优先待办收口进行中）**：本库 08-31 经官方文档直查判定「Per-Intent Privacy Manifest / 按意图粒度声明云-端路由」**不存在**（第三方博客误读 iOS 17 通用隐私清单）。该判定当时已注明「若 iOS 27 正式版新增此类 API 需重新评估」。现 GA 后，**WWDC 2026 多源报道（Lushbinary / ByteIota / TechTimes / AlgeriaTech）一致称 Apple 引入按意图声明「可上云 / 须留端」的隐私清单，作为受监管数据的合规控制**。但**官方 post-GA「What's New in iOS 27」页未逐字列出该 API**。诚实结论：由「已证伪」升为「GA 后多源一致、但官方页未确认 → 待官方文档逐字复核」。即使最终确认，它也是**数据路由目的地（云 vs 端）声明**，与「来源/可信度 provenance」仍属不同轴——不推翻「四平台意图 Registry 来源轴全空白」结论，但会为 Apple 补一条「路由轴」声明，待确认后评估。

3. **Windows：Agent 代码签名 + 证书校验/吊销（执行安全加固，★6/10）**：Windows Agent Workspaces 综述（第三方，2026-09）把微软的执行安全三原则（non-repudiation 可追溯 / confidentiality 不低于人类用户标准 / authorization 所有数据查询与动作须用户或策略批准）落到具体机制，并明确**Agent 二进制须数字签名 + 证书校验，被入侵或行为不当可吊销**——这是此前本库「Agent 须数字签名」记录的**吊销/证书校验细节补全**，是执行安全从「进程/账号隔离」向「身份级可信」再进一步的信号。⚠️ 来源为 windowsforum 第三方综述（聚合 Microsoft Insider 文档与博客），非 learn.microsoft.com 逐字；与 09-13 IFA 的 Execution Containers 容器隔离正交（容器管「炸不到系统」，签名/吊销管「身份可信」）。

4. **HarmonyOS 7 小艺 2.0 / 导航条主动服务入消费者（ArkAF「意图即服务」真机落地，★6/10）**：HarmonyOS 7 消费者版铺开后，**小艺升级为系统级智能体**：可感知 **200+ 项系统级用户数据**、调用 **2100+ 系统能力**、引入四层记忆架构（长时记忆 + 系统数据认识你）、一句话完成订餐厅/预约宠物服务等。新增**小艺导航条主动服务**——复制聊天口令/链接/地址/航班号/快递单号时，导航条流光提醒并一键直达对应 App 与服务（识别淘宝/抖音/京东等十多种主流口令）。这是 ArkAF 2.0「意图即服务」从开发者 Beta 真正触达消费者的样本，也是四平台里**首个系统化「复制即触发意图预测」的 OS 级主动服务 UX**。生态位：HarmonyOS 7（API 26）设备占比 09-06 达 5.27%、HarmonyOS 6.1.1（API 24）86.82%、6.1.0+ 合计 97.59%；鸿蒙 6+7 终端破 8500 万、原生应用破 10 万、可获取应用与服务超 40 万。⚠️ 口径：上述为 09-07 后媒体（东方财富/IT之家/腾讯）整理，厂商/媒体口径，非华为开发者文档逐字；星盾 AI 反诈（芯片级境外转打/AI 变声检测、风险检出率 >90%）为安全能力但非 XPIA/ODR/Confirmation 框架层，作低优先上下文。

5. **BFCL v4：榜单稳定，qwen3-0.6b-tool-router 补子集分（低增量）**：BenchLM 2026-09-08 公开快照 **Qwen3.7 Max 75.0% 领先**，与本库历次快照一致，无净变化；qwen3-0.6b-tool-router（HF 模型卡）补 BFCL 子集分：**Non-Live Parallel AST 83.50% / Multi-Turn Base 90.42%（已录）/ Live Simple AST 62.86% / Live Parallel AST 52.00% / Relevance 90.89%**——补全该 0.6B 确定性边缘 router 的能力画像（并行/实时子集明显弱于离线多轮，印证 v4 加权结构）。

## 使用的方法
WebSearch/WebFetch 直查 Apple 官方 post-GA 页 + 多源交叉；库内去重：对照 09-13 看板与既有 B 笔记，只追加增量、不新建重复节点（本日 0 新建 B 节点）。

## 发布反馈
（待发布后回填）

## 复盘
### 有效的部分
iOS 27 GA 触发的最高级优先待办（per-intent 路由核查）得到诚实处置：未因多源报道直接翻案，而是把 08-31「证伪」重开为「GA 后待官方复核」，并区分「路由轴声明」与「来源/provenance 轴」。Foundation Models 多模型路由获官方 post-GA 确认，是 OS 级 Planner 架构级信号。

### 需要改进的部分
Per-Intent Privacy Manifest 仍缺 Apple 官方文档逐字确认（需抓 developer.apple.com 隐私清单 / App Intents 文档 GA 版）；Windows 代码签名/吊销仍待 learn.microsoft.com 逐字；鸿蒙小艺 2.0 仍缺华为开发者文档逐字（仅媒体整理）。

### 回流到 A 的新问题或素材
若 Per-Intent Privacy Manifest 确认，评估其对 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 的「路由轴」影响（区别于 provenance 轴）；Windows 代码签名/吊销是否纳入 ODR 注册信任链、是否受同一 opt-in 开关管控；鸿蒙 小艺导航条「复制即触发」的预测置信度门控机制（是否等价端侧 Router 置信度门控）待官方文档。
