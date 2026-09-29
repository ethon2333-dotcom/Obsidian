---
date: 2026-09-21
tags: [AppIntent, 每日情报, 速览]
source:
  - "https://www.huawei.com/cn/news/2026/9/hc-agentic-era-harmonyos"
  - "https://cybersecuritynews.com/bragjack-ai-agent-hijacking/"
  - "https://blog.csdn.net/qq_39427511/article/details/166075976"
  - "https://www.ai.jp.net/article/android-gets-a-safety-cage-google-prepares-smartphones-for-ai-agents-de7477"
importance_score: "★★★★☆（7/10）"
intent_category: "跨平台·OS Agent 框架 / 执行安全"
---

# AppIntent 每日情报速览 2026-09-21

> [!abstract] 30 秒速览
- **核心突破**：华为 HC2026 披露**鸿蒙智能体框架 2.0 端云混合规划**把复杂任务成功率推至 **90%+**——四平台中首个由 OS 厂商给出量化的端云协同规划成功率；同期 **BragJack「Prompt Forcing」** 揭示 AI 助手**信道劫持**新攻击面（CVE-2026-0628 / 55945）；**Microsoft Foundry** 给托管智能体加**网络出网控制**。
- **关键指标**：鸿蒙生态 **8500 万终端 / 1100 万开发者 / 36.8 亿日均 AI 调用**；BragJack 跨 **5 款浏览器**、五厂商 **$20k+** 赏金；iOS 27.1 beta 已放出（Duo 向、无 Schema 新增）。
- **OS Agent 场景**：端云 Planner 路由从「路由原语」走向「量化成功率」；执行安全从「模型过滤」走向「信道信任 + 边界」；治理层出网控制把「边界压爆炸半径」落到组织级。

## ① Schema 定义与语义路由机制
- **鸿蒙 ArkAF 2.0 端云混合规划**：按「任务复杂度 + 设备资源分配计算」决定本地/云端分工；**Skill（确定性简单任务）** 与 **A2A（多轮复杂场景）** 均支持**端侧与云侧两种接入模式**——四平台中唯一公开点名规划引擎结构（图推理 DAG）且给出**量化成功率**（对照 iOS 27 Foundation Models 多模型路由、Android I/O '26 Hybrid Inference 仅给路由原语、未给成功率）。
- **iOS 27.1 beta 已放出但为 Duo 适配 SDK**：Xcode 27.1 Beta 1 含 iPhone Duo 折叠屏适配（size classes + 保留区域 `reservedRegions` API），**无新 App Intents Schema**；代码级 **Model Delegation API** 反编译信号（外部模型可作 Siri 扩展）与 09-15 多模型路由 GA 互为印证、非官方。
- **Android AppFunctions 仍 alpha11 无 alpha12**；Google「App Functions Manager safety cage」为低置信执行安全信号（待官方复核，可能=既有 `AppFunctionState` 门控复述）。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）
- **BragJack「Prompt Forcing」**：单一恶意浏览器扩展经 Chromium `declarativeNetRequest` 跨入 AI 助手**特权控制平面**，直接控制完整 prompt 与后续指令，**绕过模型级安全过滤**；根因是**授权与消息信道信任**（confused deputy），EDR 也无信号——动作由浏览器自身合法 AI agent 用其合法提权执行。防御要点（厂商共识）：严格 origin 校验 + 最小权限 + 隔离命令信道 + 敏感动作显式确认 + 可审计日志，与 [[Confirmation UI 安全机制]] / [[Agent Workspace 隔离执行]] / [[Chrome Agent Origin Sets 与用户对齐评判器 2026]] 三件套正交互补。
- **Plugin4Shell**（强化 09-20 主题）：Claude Code / Codex / Copilot / Gemini CLI 零点击 RCE，经 **Git branch/commit hash 碰撞**绕过插件 SHA pinning；同日 Google ADK 曝 CVSS 10.0 RCE。进一步坐实「**Skill / 插件供应链投毒**」是跨 OS 统一攻击面，OS 级 Skill Registry 来源校验（09-20 第⑦支）优先级再升。
- **Microsoft Foundry 出网控制**：托管智能体按 **FQDN 通配 + 四动作（允许 / 拒绝 / 改写出站头 / 改写目的地）** 约束运行时出网——治理层对 [[XPIA 跨提示注入]]「假定注入必然发生、用边界压爆炸半径」元判断的组织级落地（对照 [[Chrome Agent Origin Sets 与用户对齐评判器 2026]] 客户端读写源集）。
- **诚实标注**：HC2026 数字与 CVE 来自官方/媒体转述，待一手复核；BragJack 为 09-16 公开、非本窗口 24h 首发；Android「safety cage」与 iOS 27.1 Model Delegation 均为二次分析/反编译，Apple/Google 未官方确认。

> [!note] 8 概念节点双链
- [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
