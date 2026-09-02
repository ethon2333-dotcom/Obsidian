---
type: output
status: draft
created: 2026-08-26
method_used: "WebSearch/WebFetch 直取官方源 + 本 Agent 综合（Horizon MCP 连续 20+ 日 disconnected）；7 日滚动窗口 08-19→08-26"
derived_from: "[[AppIntent 每日情报 2026-08-26]]"
tags: [速览, AppIntent, 每日情报, AppIntentsTesting, IFFC, BFCLv4, XPIA, 2026-08-26]
---

# AppIntent 每日情报速览 2026-08-26

## 目标读者与目标

OS 产品经理 / 端侧 Agent 框架设计者。今日目标：在四平台 OS 官方框架层集体「无净新增」的窗口里，定位两条 ★7/10 真增量（Apple 意图测试框架、IFFC 解耦路由范式），并把 BFCL v4 公开榜、XPIA web 级实测、鸿蒙端侧 Skill 约束、Android 真机实证等 ★6/10 上下文补入对应 B 笔记。

## 正文（速览）

**① Apple App Intents Testing 框架（★7/10，iOS 27 Beta）**
- 性质：App Intents 2.0 的**官方验证闭环**，进程外、按真实系统路径（Siri/Shortcuts/Spotlight）跑意图/实体/查询，类型擦除 API + `ViewAnnotation` 测试。
- 价值：把意图集成质量与安全左移到发布前，补齐本库长期记录的「Apple 侧无运行时动态可见性 API」之外的另一短板（可测试性）。
- 深度：[[Apple AppIntents Schema Protocol 2026]]

**② IFFC 解耦路由范式（★7/10，arXiv 2608.22472）**
- 性质：把工具选择从主 LLM 解耦为独立 SRM（0.5B–15B），用「指令遵循上下文」替代「工具调用上下文」提升小模型路由准确率；SRM 可激进量化部署边缘。
- 价值：端侧 Planner 的**架构级**解法，与库内 SAN（去 FFN）、Needle 2（置信度门控）构成「解耦 + 轻量 + 门控」三件套。
- 深度：[[端侧函数调用解耦路由与指令遵循范式 IFFC 2026]]

**③ BFCL v4 公开榜 + 端侧模型分数（★6/10，2026-08-22 快照）**
- LFM2.5-2.6B 56.9% / Needle 2 45M 42.6%（Cactus 自报）/ Nexus-TinyFunction-1.2B 94.25% simple（HF Q8_0，约 700MB，可跑 Android/PI）；LFM2.5-350M 微调后 98.0% shell / 96.7% smart home / 95.9% banking 追平 120B teacher。
- 深度：[[Function Calling 端侧工具调用]]

**④ XPIA 已成 web 级 operational 威胁（★6/10）**
- CSA：月爬 20–30 亿页，恶意注入页 2025-11→2026-02 相对 +32%；Black Hat USA 2026「每个 AI 浏览器都脆弱」。→ OS Agent 读路径治理优先级上调。
- 深度：[[XPIA 跨提示注入]]

**⑤ 平台约束与真机实证（★6/10）**
- HarmonyOS 端侧 Skill 同名冲突静默优先端侧 / 3 秒超时 / A2UI 静默失败 → [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- Samsung Gallery + Gemini AppFunctions 闭环 + UI Automation 兜底 → [[Android AppFunctions 设备侧意图 2026]]

**四大 OS 官方渠道复核 — 无净新增（避免重复检索）**
- Apple：iOS 27 Beta 7（24A5424a，08-24/25）仅修 Bug，快捷指令 Else-If 属 workflow 层非 schema；→ [[Apple AppIntents Schema Protocol 2026]]
- Android：AppFunctions 守 alpha10；→ [[Android AppFunctions 设备侧意图 2026]]
- HarmonyOS：7 SP8 消费版更新无新 API；→ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- Windows：agentic security 四支柱一致；→ [[Windows Copilot Actions 与 Agent Workspace 2026]]

## 使用的方法

- 7 日滚动窗口（08-19→08-26），因 08-18 已覆盖至当日，本轮取窗口内净增量 + 库内空白补漏。
- 分类纪律：先判「新事实 vs 口径变化 vs 邻近层（测试/路由范式）vs OS 层」，把 App Intents Testing 与 IFFC 归为「邻近层高价值增量」而非「OS schema 新 API」。
- 诚实纪律：BFCL 数字标 v3/v4 版本与镜像站 vs 官方榜；IFFC 仅 v3；CSA/Black Hat 为安全研究口径，标待官方复现。

## 复盘

### 有效的部分
- 延续「无净新增显式列表」避免重复检索；延续「每分标版本」纪律。
- 把「邻近层增量」（测试框架、路由范式）与「OS schema 新 API」区分开，避免误报。

### 需要改进的部分
- App Intents Testing 框架命中的是 Apple CDN 镜像域，canonical 路径与最小 Beta 版本待补。
- IFFC 仅 BFCL v3 数字，缺 v4，跨应用意图路由结论需谨慎外推。

### 回流到 A 的新问题或素材
- 待核验 App Intents Testing canonical 路径；IFFC v4 数字；CSA 数据回流至读路径 SOP；延续 BFCL v4 官方原文、Watch OS 26 Trust Insights、NowSecure/AgentAntibody 复核。

## 关联
- 原子：[[Apple AppIntents Schema Protocol 2026]] ｜ [[端侧函数调用解耦路由与指令遵循范式 IFFC 2026]] ｜ [[Function Calling 端侧工具调用]] ｜ [[XPIA 跨提示注入]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]
- 对比：[[四平台意图 Registry 来源轴与权限模型对比 2026]] ｜ 解耦同构：[[Simple Attention Network 无FFN端侧路由]] ｜ 门控：[[端侧 Router 置信度门控与工具可达性收缩 2026]]
- 枢纽：[[意图框架·跨体系索引 MOC]] · [[语义路由]] · [[确认机制]] · [[XPIA 跨提示注入]]
