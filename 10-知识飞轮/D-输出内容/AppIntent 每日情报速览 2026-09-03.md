---
date: 2026-09-03
tags: [AppIntent, 情报, 速览]
source: "https://www.techoper.com/blog/huawei-mate-xt-2-harmonyos-7-launch-september-7 | https://www.pcworld.com/article/3063498/windows-11-26h2-is-coming-meet-all-the-new-features.html | https://www.luxand.com/llm-sdk/benchmarks/"
importance_score: "★★★★☆"
intent_category: 跨平台框架GA / 端侧Planner评测
---

# AppIntent 每日情报速览 2026-09-03

> [!abstract] 30 秒速览
> 过去 24–48h（2026-09-02→09-03），四大 OS 在**系统级意图框架 API 层无净新增**，真增量是**消费级 GA 日期集体锁定** + 一份新第三方 BFCL v4 端侧快照。**核心突破**：HarmonyOS 7 于 **9-7** 随 Mate XT 2 向消费者铺开（ArkAF 2.0「意图即服务」成为消费者默认可用）；Windows 11 26H2 于 **9 月下旬~10 月初**以 enablement package 交付，带来搜索层意图入口「Ask Copilot」+ Sysmon 内置审计；iOS 27 于 **9-14** GA（框架不变）。**关键指标**：Luxand BFCL v4 端侧 Agentic Score 快照——Qwen3.6-35B-A3B 73.4% / Gemma4-26B-A4B 71.8% / Qwen3.5-4B 67.0% / LFM2.5-8B-A1B 62.3%（第三方，待官方复核）。**OS Agent 场景**：四平台 agentic 框架同步进入「发布前最后冲刺」，本库「意图元数据来源轴四平台全空白」结论不变，仍须各 App 自行补 `readOrWrite` 声明位。

## ① Schema 定义与语义路由机制

- **HarmonyOS 7（9-7 消费版）**：`Want` + Intents Kit + 元服务（`installationFree`）+ ArkAF 三层（意图框架 / Skills 框架 / 端侧 A2A）从开发者 Beta 转消费者默认可用；「意图即服务」= 用户说需求 → 系统理解意图 → 直接匹配 Agent/Skill，跳过「打开 App」。路由由盘古 6.0 端侧意图理解 + 图推理引擎（子任务 DAG 并行调度）完成（详见 [[HarmonyOS Intents Kit 与 ArkAF 2026]]）。
- **Windows 26H2「Ask Copilot」**：新增**搜索层意图理解入口**——任务栏搜索框可替换为 Ask Copilot，Copilot 把自然语言查询链接到 apps / files / 系统设置（如「调亮屏幕」）。这是搜索分发的意图层，与 Agent Launchers / ODR（agent/工具注册）互补，是 Windows「系统级意图框架」的第四层（搜索意图 / agent 注册 / 工具注册 / 执行隔离）。
- **Apple / Android**：iOS 27 RC 沿用 Beta 5 已录 `@AppIntent(schema:)` 体系（无新 API）；Android AppFunctions 守 alpha11，Registry/权限模型同 09-01 已录。
- **跨平台端侧 Planner**：Luxand BFCL v4 端侧快照显示 4B 级（Qwen3.5-4B 67%）成为新甜点下沿；但 v4 加权最重的 agentic+multi-turn 恰是端侧小模型最弱处，跨应用意图路由仍靠门控而非准确率（详见 [[Function Calling 端侧工具调用]]、[[端侧 Router 置信度门控与工具可达性收缩 2026]]）。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- **隔离执行**：Windows Agent Workspace（独立低权限账号 + 6 known folders 作用域 + ACL + 签名 + 会话隔离）自 08-09 以来无变化；26H2 新增 Sysmon 内置，把 agent/系统行为审计 Telemetry 补到 OS 内（与 08-04 Project Perception 端点侧检查同方向）。
- **确认与授权**：四大 OS 高危动作仍走显式用户同意（Apple Confirmations + entity ownership / Android 系统代持一次性授权 + HarmonyOS 场景化任务处理 + Windows OAuth）；无新确认 UI 机制。
- **防注入（XPIA / ADI）**：Windows agentic security 四支柱一致；本库延续结论——**意图元数据来源轴（provenance）四平台 OS intent 层仍全空白**，只靠位置权限（文件夹白名单）不够，须各 App 自行打 `readOrWrite` 来源声明位（详见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]、[[Agent Data Injection 数据注入攻击]]）。
- **用户始终在环**：HarmonyOS 上下文充足时免二次确认、跨设备走安全通道；Apple 后台 FM 无速率限制、前台无限流、后台节流靠捕获错误——均延续既有设计。

> [!note] 概念节点
> - [[意图模式规范]]
> - [[语义路由]]
> - [[端侧工具调用]]
> - [[确认机制]]
> - [[元服务]]
> - [[隔离执行]]
> - [[A2A 端侧智能体协议]]
> - [[XPIA 跨提示注入]]
