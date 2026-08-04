---
type: output
status: draft
created: 2026-08-02
method_used: "每日情报自动化（7 日滚动窗口）+ WebSearch/WebFetch 直取官方源 + 飞轮四层落库"
tags: [AppIntent, OS-Agent, 执行安全, XPIA, 合规, 每日情报, 跨平台2026]
---

# AppIntent 每日情报速览（2026-08-02）

## 目标读者与目标

- **读者**：OS PM / 系统级 Agent 框架负责人 / 关注四平台（Apple / Android / HarmonyOS / Windows）意图框架与执行安全的从业者。
- **目标**：用一份速览讲清本日（及近 7 日）四平台在「系统级意图框架 / 端侧 Planner 路由 / 跨应用 Intent 工作流 / 执行安全」的**真实进展**，并落到知识飞轮可复用节点。

## 正文或成品链接

本期三条主线：

1. **执行安全分水岭（今日生效）**：EU AI Act Article 15 于 2026-08-02 正式生效，把 prompt-injection 韧性、动作层网络安全、不可篡改日志、人类监督**写进高风险 AI 系统强制合规**。这是本库记录的第二处分水岭（第一处是 08-01 的 Word 文档型 XPIA 蠕虫）。→ 详见 [[AppIntent 每日情报 2026-08-02]] 与 [[Windows Copilot Actions 与 Agent Workspace 2026]]。
2. **HarmonyOS 端侧/云侧 A2A 双模落地（08-01）**：小艺升为 Agentic 自演进系统级大脑；头部银行经端侧 A2A 覆盖 1000+ 意图、隐私不出端，O2O 经云侧 A2A 走完端到端闭环。→ 详见 [[A2A 端侧智能体协议]] 与 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。
3. **Apple Schema Protocol 深化（WWDC26 补漏）**：Session 343 的 View Annotations / IntentValueQuery / Confirmations+entity ownership；App Intents 2.0 的 streaming / 富实体 / 多轮。→ 详见 [[Apple AppIntents Schema Protocol 2026]]。
4. **Android Agent Skill 验证（补漏）**：官方 Agent Skill 四步生命周期（发现/实现/ KDoc 优化/测试）经官方文档验证。→ 详见 [[Android AppFunctions 设备侧意图 2026]]。

**被排除项（展示过滤纪律）**：M365 Copilot Agentic 模式扩大可用（08-01）属应用/M365 层，非 OS 级执行总线，低于 OS 级相关性阈值，排除。

## 使用的方法

- **7 日滚动窗口**（依记忆文件建议，从 24h 改为 2026-07-26→08-02），保留「首次入库存量判定」做去重。
- **官方源优先**：Horizon MCP 全部 disconnected，改用 WebSearch/WebFetch 直取 developer.android.com / developer.apple.com / artificialintelligenceact.eu / 华为 HDD 西安站官方通稿。
- **诚实标注**：厂商口径（银行 1000+ 意图、O2O 闭环成功率）标「待补」；「Per-Intent Privacy Manifest」未从一手源独立确认，不记为已确认 API；Digital Omnibus 推迟风险明确标注「尚未正式通过」。

## 发布反馈

- 自动化运行，暂无人工反馈。待用户回看后回流到 A。

## 复盘

- **本日质量**：4 条有效增量 + 1 条排除，信息密度高于 08-01（仅 1 条硬命中）。7 日窗口策略见效，缓解「24h 过薄凑数」问题。
- **最高价值**：EU AI Act Article 15 生效——它让四平台既有的 XPIA/隔离/确认三条防线从「产品选择」变成「法律义务」，对 OS PM 的合规优先级有直接影响。
- **待改进**：四平台对 Article 15 的具体合规触发条件仍未厘清（尤其是否落入 Annex III 高风险）；HarmonyOS 端侧 A2A 的跨 Agent 写回安全边界无公开评估——均列入后续动作。
- **方法论沉淀**：本日未新建 C 层 SOP（执行安全合规动机已并入既有 [[XPIA 跨提示注入]] / [[Agent Workspace 隔离执行]] / [[Confirmation UI 安全机制]]）；也未新建独立 B 节点，全部以「既有 B 追加」形式落库，避免重复——符合飞轮「一条笔记一个概念」纪律。
