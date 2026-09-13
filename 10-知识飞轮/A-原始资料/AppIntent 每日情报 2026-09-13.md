---
date: 2026-09-13
tags: [AppIntent, 每日情报, 端侧Planner, 执行安全, 跨平台]
source: "https://www.datalearner.com/en/benchmarks/bfcl-v4 | http://securityonline.info/unmetered-intelligence-vision | https://biz.ifeng.com/c/8wENZ13tWh6 | https://www.macobserver.com/news/ios-27-release-candidate-build-24a435-explained"
importance_score: "★★★★☆"
intent_category: "跨平台评测 / 执行安全"
---

# AppIntent 每日情报 2026-09-13

> [!abstract]
> **30 秒速览（窗口 2026-09-06 → 09-13）**
> - **核心突破**：① **BFCL v4 官方榜单上线**（Berkeley Gorilla 维护，DataLearner 镜像 2026-09-07 更新）——SOTA **MiniCPM5-2B（OpenBMB）66.60**，2.5B、免费商用，意味着**端侧级小模型首次登上官方 v4 榜首**，端侧 Planner 评测有了权威锚点；② **Windows IFA 2026 发布 Microsoft Execution Containers**——把 Agent 隔离从「独立账号 + ACL」升级为**内建沙箱容器**，强制企业安全策略 + 全量活动日志。
> - **关键指标**：MiniCPM5-2B 66.60（BFCL v4 Overall）；HarmonyOS 7 确认 **API 26**（关闭 26-vs-23 冲突待办）；iOS 27 RC build **24A435**，GA 锁定 **09-14**。
> - **OS Agent 场景**：四大 OS 框架层本窗口**无净新增 API**（iOS 27 RC=Beta 5 收尾、AppFunctions 守 alpha11、鸿蒙框架同 HDC2026、Windows 四支柱 + Execution Containers）；真正增量在「评测权威化」与「执行安全加固」两处。

## 索引（每条 1 行：重要性 + 原子笔记 + 枢纽 + 一手来源）

- ★★★★☆ **BFCL v4 官方榜单上线，MiniCPM5-2B 66.60 登顶** → [[Function Calling 端侧工具调用]]（#跨平台评测）｜ 来源 <https://www.datalearner.com/en/benchmarks/bfcl-v4>（DataLearnerAI，更新 2026-09-07）
- ★★★★☆ **Windows IFA 2026 发布 Microsoft Execution Containers（Agent 沙箱容器隔离）** → [[Windows Copilot Actions 与 Agent Workspace 2026]] ＋ [[Agent Workspace 隔离执行]]（#执行安全）｜ 来源 <http://securityonline.info/unmetered-intelligence-vision>（IFA 2026，2026-09）
- ★★★☆ **HarmonyOS 7 确认 API 26 + 安全相机2.0 数字内容溯源 / 数字身份 DID（provenance-at-source）** → [[HarmonyOS Intents Kit 与 ArkAF 2026]]（#来源轴）｜ 来源 <https://biz.ifeng.com/c/8wENZ13tWh6>（HarmonyOS 7 API 26 版本说明）
- ★★★☆ **iOS 27 RC（build 24A435，09-09）发布，GA 09-14 待核查 per-intent 路由 API** → [[Apple AppIntents Schema Protocol 2026]]（#iOS27）｜ 来源 <https://www.macobserver.com/news/ios-27-release-candidate-build-24a435-explained>（2026-09-09）

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27.0 RC build **24A435**（2026-09-09）为 beta 周期终点，App Intents Schema Protocol 与 08-15 已录 Beta 5 逐字一致，**无新 API**；GA 2026-09-14 尚未到，per-intent 路由/来源声明 API 待 GA 后核查。
- **Android**：AppFunctions Jetpack 仍 **alpha11**（2026-08-26），窗口内**无 alpha12**；开发者一手记（alpha08→alpha10 破坏性变更、EXECUTE_APP_FUNCTIONS 单 blanket 授权、无速率限制）仅 corroborate 既有结论，非新 API。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 框架同 HDC2026 与 09-07 消费版，**无新意图框架 API**；API 26 为冲突澄清（非新增）。
- **Windows**：Copilot Actions / Agent Workspace / ODR / Agent Launchers 四支柱安全设计自 08-09 以来无变化；新增 Execution Containers 属隔离实现加固（已落 B 增补），非新 Registry API。

> [!note]
> 概念节点：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[确认机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
