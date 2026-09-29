---
type: output
status: draft
created: 2026-09-17
method_used: "WebSearch/WebFetch 官方源 + 库内去重（窗口 2026-09-16→09-17，iOS 27 GA 后第 3 日）"
tags: [AppIntent, 速览]
---

# AppIntent 每日情报速览 2026-09-17

## 目标读者与目标
OS PM（Ethon）；30 秒掌握四平台系统级意图框架过去 1 日真增量（重点：XPIA 自改进攻击 SIR + Windows ODR 权限模式实处化 + Android 17 GA 确认）。

## 正文

本期窗口（2026-09-16→09-17）距 iOS 27 GA（09-14）第 3 日，**四大 OS 官方框架层无净新增 API**——符合「OS 框架不日更」规律。真增量 = ① 执行安全研究演进、② 既有信号的实处化。

1. **XPIA 攻击侧首次「自改进」：SIR（★6/10，最高价值项）**：香港中文大学 arXiv 预印本提出 SIR（Self-Improving attack on computer-use agents），把提示注入当可演化攻击框架——失败→诊断→提炼绕过→复用。量化（二次来源，待一手 arXiv 复核）：无迭代反馈时 ASR 为 Gemini 3.5 Flash 0% / Claude Opus 4.8 4%；加迭代反馈后升至 **28% / 24%**。更关键的是**跨模型零反馈迁移**——一款模型上发现的绕过原则直接迁移到不同架构的另一款，说明防御不是模型特定的、是系统性的（与 NCSC「confused deputy / 架构缺陷非可修 bug」同构）。目标层是 **OS 级 CUA**（看屏幕 + 真实 OS 操作），攻击在 agent 完成合法任务的同时并行发生、用户无感。⚠️ 与 08-09 的「④ 学习型防御 AgentAntibody」形成镜像：防御在学用户边界，攻击在学绕过边界。对 OS PM 的含义：① 固定手写注入基准低估自适应对手，评测须用演化式红队；② 既然注入会自我进化，**权限最小化 + 文件系统/服务边界**比「检测注入」更根本（与 [[Agent Workspace 隔离执行]]「隔离压爆炸半径」范式一致）。

2. **Windows ODR Agent Connectors 权限模式具象化（★6/10）**：第三方教程（adersaytech，聚合 learn.microsoft.com + 支持文档）披露，自预览 build **26100.7344+**，所有 ODR 注册的 agent connectors（本质是 MCP server）**默认在 Agent Workspace 隔离环境内执行**，Windows 先取得用户许可才让 agent 运行连接器；consent 三档 **Ask every time / Allow always / Never allow**——与 07 月「scoped file access 六文件夹 + 三档同意」同构，本次补的是「连接器」维度的同构三档。与 08-05 `odr.exe agent-info` 注册 + 09-16 代码签名构成「注册 → 签名 → 隔离 → 授权」闭环。教程同时重申头号风险仍是 XPIA（隔离解「出事后能搞多大」、不解「会不会出事」）。⚠️ 来源为第三方教程，build 号与三档模式待 Microsoft 官方文档逐字复核。

3. **Android 17 GA 确认 + AppFunctions 进智能系统叙事（★6/10，库内空白补漏）**：官方 `developer.android.com/ai/intelligence-system` 将 AppFunctions 与 Remote MCP server、Computer Control 并列为「让系统 agent 跨本地应用与 web 服务安全编排」的三条新能力，AppFunctions 正式纳入 Android 17「Intelligence System」主线。但 **AppFunctions Jetpack 库仍为 Alpha、无 GA 日期**，Gemini 集成仍「受信任测试者私测」；compileSdk 推荐基线由本库 08-03 记的 `≥ API 36` 升为 **37**（targetSdk 36）。窗口内**无 alpha12**——alpha11（2026-08-26）的 `@AppFunctionSignature` 动态注册 + `AppFunctionState` 取代 `isEnabled` 仍是最新净新增。→ 含义：「框架进 OS 主版本」≠「API 稳定」，开发者仍须按 alpha 节奏跟版本（延续「AppFunctions 何时 GA 待补」待办）。

## 使用的方法
WebSearch/WebFetch 直查 developer.android.com/ai/intelligence-system + android-17-is-here、adersaytech Windows agent 权限教程、notatechguy SIR 转述；库内去重：对照 09-16 看板与既有 B 笔记（Apple/Android/HarmonyOS/Windows 均已覆盖 Schema API、alpha11、HDC2026、四支柱），只追加增量、不新建重复节点（本日 0 新建 B 节点）。

## 发布反馈
（待发布后回填）

## 复盘
### 有效的部分
SIR 把 XPIA 威胁模型从 08-09「④ 学习型防御」补上「攻击侧自改进」镜像，是执行安全研究线的实质新增；Windows ODR 权限模式把此前抽象的「受控发现 + 用户授权」落到可配置三档；Android 17 GA 确认填了 09-03 看板「Android 17 GA 待补」空位——三条均低风险高信噪比。

### 需要改进的部分
SIR 来源为二次转述，arXiv ID 与评测协议待一手复核；Windows ODR 权限模式 build 号（26100.7344+）与三档 consent 仍待 learn.microsoft.com 逐字；Android 17 精确 GA 日未从官方博客取得（仅「现已发布」表述）。

### 回流到 A 的新问题或素材
SIR 一手 arXiv ID 与评测协议复核；Windows ODR 权限模式是否受 08-02 `Experimental agentic features` 同一 opt-in 管控；Android 17 精确 GA 日 + AppFunctions GA 日；是否把「演化式红队」纳入 [[Agent 读入路径可信数据边界 SOP]] 的评测方法一节。
