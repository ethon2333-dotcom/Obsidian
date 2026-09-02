---
type: raw
status: inbox
date: 2026-08-26
source:
  - "https://developer.apple.com/documentation/AppIntentsTesting"
  - "https://developer.apple.com/wwdc26/guides/ios"
  - "https://arxiv.org/html/2608.22472v1"
  - "https://benchlm.ai/benchmarks/bfclV4"
  - "https://www.distillabs.ai/learn/on-device-llm-inference-in-2026"
  - "https://safeguard.sh/resources/blog/indirect-prompt-injection-goes-operational-2026"
  - "https://developer.huawei.com/consumer/cn/doc/guidebook/solution3-0000002601693439"
  - "https://www.fonearena.com/blog?p=476208"
importance_score: "★★★☆☆（7/10）"
intent_category: "系统级意图框架 / 端侧 Agent 执行总线 / 执行安全（XPIA）· 7 日滚动窗口 2026-08-19→08-26"
tags: [情报, AppIntent, 每日情报, AppIntentsTesting, IFFC, BFCLv4, XPIA, 2026-08-26]
---

# AppIntent 每日情报 2026-08-26

> [!abstract] 30 秒速览
> - **核心突破（两条 ★7/10）**：① **Apple App Intents Testing 框架（iOS 27 Beta）** —— 首个让开发者用「真实系统路径」验证整个意图集成（intents/entities/queries/Siri/Spotlight）的**进程外测试框架**，无需 UI 自动化即可早发现集成缺陷，是 App Intents 质量/安全验证的官方闭环；② **IFFC 解耦路由范式（arXiv 2608.22472，2026-08）** —— 把工具选择从主 LLM 解耦为独立 SRM（0.5B–15B）+ 用「指令遵循上下文」替代「工具调用上下文」提升小模型路由准确率，为端侧 Planner 给出**架构级**而非纯模型级解法。
> - **关键指标**：App Intents Testing 提供 `AnyAppIntent/AnyAppEntity/AnyEntityQuery` 类型擦除 API + `ViewAnnotation` 测试；IFFC 在 Qwen-3 0.6B/1.7B/4B/8B 上验证「指令遵循」优于「工具调用」上下文（BFCL V3 口径）；BFCL v4 公开榜（2026-08-22 快照）端侧模型：LFM2.5-2.6B 56.9% / Needle 2 45M 42.6% / Nexus-TinyFunction-1.2B 94.25% simple。
> - **OS Agent 场景**：Apple 补齐「意图集成可测试性」短板（质量门前置到发布前）；IFFC 为四平台端侧意图路由提供可落地的「小 SRM + 主模型」分工样板；CSA 实测「间接提示注入已成 web 级现象（月爬 20–30 亿页、恶意注入页 11→2 月相对 +32%）」把 XPIA 威胁从 demo 推为 operational，直接抬高 OS Agent 读路径治理优先级。

## 正文拆解

### ① Schema 定义与语义路由机制

本期窗口内**四平台 OS 级意图 schema 层无新增 API**（iOS 27 Beta 7 仅修 Bug、Android AppFunctions 守 alpha10、HarmonyOS 7 SP8 推消费版无新 API、Windows agentic security 四支柱一致），但有两处**邻近层**增量值得 OS PM 吸收：

- **Apple App Intents Testing 框架（iOS 27 Beta，官方 `developer.apple.com/documentation/AppIntentsTesting`）**：App Intents 2.0 体系补上**验证闭环**——用类型擦除 API（`AnyAppIntent`/`AnyAppEntity`/`AnyEntityQuery`/`AnyAppEnum`/`AnyTransientAppEntity`）按名引用意图、设参、运行，**进程外**复现 Siri/Shortcuts 的真实调用路径；并支持 `ViewAnnotation` 测试（把视图标注为实体供系统感知）。含义：把意图集成的质量与**安全**（参数错配、实体解析失败、跨 App 联动断裂）左移到发布前，而非靠用户线上踩坑。详见 [[Apple AppIntents Schema Protocol 2026]]。
- **IFFC 解耦路由（端侧 Planner 范式）**：工具选择逻辑从主 LLM 抽离为独立 SRM，SRM 上下文与主模型对话上下文**完全隔离**——既避免「工具 schema 污染对话推理」（论文指出的 context pollution），也让 SRM 可激进量化（Q4KM 把 Gemma-3 12B 从 24.3GB→8.1GB）部署到边缘。与库内 [[Simple Attention Network 无FFN端侧路由]]（去 FFN）、[[端侧 Router 置信度门控与工具可达性收缩 2026]]（置信度门控）构成端侧路由「解耦 + 轻量 + 门控」三件套。详见 [[端侧函数调用解耦路由与指令遵循范式 IFFC 2026]]。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **XPIA 从 demo 推为 operational（威胁模型再强化）**：CSA 研究笔记引 Google 安全数据，每月爬取 **20–30 亿页**中携带恶意注入指令的页面占比在 **2025-11→2026-02 相对 +32%**；Black Hat USA 2026 报告「**被分析的每一个 AI 浏览器都易受提示注入**」。结论与库内 [[XPIA 跨提示注入]] 的「NCSC 定性为 confused deputy、架构缺陷非可修 bug」一致——OS Agent 的读路径（屏幕/Copilot Vision/索引/文档）治理优先级应上调。详见 [[XPIA 跨提示注入]]。
- **HarmonyOS 端侧 Skill 实操约束（开发者视角）**：端侧 Skill 与云端 Skill **同名冲突时系统静默优先端侧、无警告**；端侧 Skill **执行超时约 3 秒**（需异步化或拆 Skill）；A2UI Schema **旧系统字段静默失败（空白卡片）**。这些是鸿蒙「意图即服务」在真机上的硬约束，OS PM 设计端侧 A2A 时须内置超时/命名隔离/A2UI 版本协商。详见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
- **Android AppFunctions 真机落地实证**：Samsung Gallery + Gemini 在 Galaxy S26 上跑通「用户说一句话→Gemini 触发 AppFunction→结果回 Gemini 内」的闭环，是 AppFunctions 首个公开真机部署样本；配套的 **UI Automation 框架**（长按电源键、Gemini app 内 beta、外卖/生鲜/打车，限美韩）为未适配长尾兜底。详见 [[Android AppFunctions 设备侧意图 2026]]。

### 已复核·无净新增（避免下次重复检索）

| 平台 | 复核对象 | 结论 |
|---|---|---|
| Apple | iOS 27 Beta 7（build 24A5424a，2026-08-24/25） | 收尾期仅修 Bug + 性能打磨；快捷指令新增 Else-If 分支（workflow 层，非 App Intents schema API）；App Intents 2.0 schema 无新 API。 |
| Android | AppFunctions（Jetpack 1.0.0-alpha10，2026-07-21 末次更新） | alpha10 稳定，无新发布；Galaxy S26/Pixel 10 真机有限预览已单独入 B 笔记。 |
| HarmonyOS | HarmonyOS 7.0.0.102 SP8（2026-08-17 推） | 消费版系统更新（3D 壁纸/AI 变声检测/端侧 AI 可视化），无意图框架新 API；ArkAF 仍 HDC2026 口径。 |
| Windows | OS agentic security 四支柱 + ODR + Agent Workspace | 官方 learn.microsoft.com 四支柱一致；Copilot Actions/Agent Workspace 仍 Insider 预览默认关；File Explorer Copilot Chat 为实验特性。 |

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]

## 值得保留的点（索引）

- **★7/10 · 净新增**：Apple App Intents Testing 框架（iOS 27 Beta，进程外验证意图集成） —— 原子笔记 → [[Apple AppIntents Schema Protocol 2026]] ｜ 主题枢纽 → [[意图框架·跨体系索引 MOC]]
- **★7/10 · 净新增**：IFFC 解耦路由 + 指令遵循上下文范式（arXiv 2608.22472） —— 原子笔记 → [[端侧函数调用解耦路由与指令遵循范式 IFFC 2026]] ｜ 主题枢纽 → [[Intent Router 语义路由]]
- **★6/10 · 上下文（评测）**：BFCL v4 公开榜（2026-08-22 快照）端侧模型分数（LFM2.5-2.6B 56.9% / Needle 2 42.6% / Nexus-TinyFunction-1.2B 94.25% simple）+ LFM2.5-350M 微调后 96–98% 追平 120B teacher —— 原子笔记 → [[Function Calling 端侧工具调用]]
- **★6/10 · 上下文（安全）**：CSA web 级 IPI 实测（月 20–30 亿页、恶意注入 +32%）+ Black Hat「每个 AI 浏览器都脆弱」 —— 原子笔记 → [[XPIA 跨提示注入]]
- **★6/10 · 上下文（平台约束）**：HarmonyOS 端侧 Skill 同名冲突/3 秒超时/A2UI 静默失败 —— 原子笔记 → [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- **★6/10 · 上下文（真机实证）**：Samsung Gallery + Gemini AppFunctions 闭环 + UI Automation 兜底框架 —— 原子笔记 → [[Android AppFunctions 设备侧意图 2026]]
- **★0/10 · 已复核无净新增**：iOS 27 Beta 7 / AppFunctions alpha10 / HarmonyOS 7 SP8 / Windows 四支柱 —— 见上表，下次不再重复检索。

## 后续动作

- [ ] 核验 App Intents Testing 框架的最小 iOS 27 Beta 版本号与 canonical `developer.apple.com` 路径（本轮命中 CDN 镜像域 `msc-/ma-kobol-public-prod.apple.com`）。
- [ ] 复核 IFFC 论文是否给出 BFCL **v4** 数字（当前仅 v3）；评估「解耦 SRM + 置信度门控」组合在跨应用意图路由上的误触发率。
- [ ] 把 CSA 的「月 20–30 亿页 / +32%」作为 XPIA 读路径治理的量化论据，回流到 [[Agent 读入路径可信数据边界 SOP]]。
- [ ] 延续待办：Berkeley 官方 BFCL v4 博客原文；Watch OS 26 是否 Trust Insights 类；NowSecure/AgentAntibody 独立核验；Chrome Origin Sets 官方 URL 逐字复核。
