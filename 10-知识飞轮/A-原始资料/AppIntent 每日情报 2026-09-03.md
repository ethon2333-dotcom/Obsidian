---
date: 2026-09-03
tags: [AppIntent, 情报, 每日]
source: "https://www.techoper.com/blog/huawei-mate-xt-2-harmonyos-7-launch-september-7 | https://www.pcworld.com/article/3063498/windows-11-26h2-is-coming-meet-all-the-new-features.html | https://www.luxand.com/llm-sdk/benchmarks/"
importance_score: "★★★★☆"
intent_category: 跨平台框架GA / 端侧Planner评测
---

# AppIntent 每日情报 2026-09-03

> [!abstract] 30 秒速览
> 本窗口（2026-09-02→09-03）四大 OS 官方框架层 API **无净新增**（Apple iOS 27 RC 沿用 Beta 5 已录 schema、Android AppFunctions 守 alpha11、HarmonyOS 7 框架同 HDC2026、Windows agentic security 四支柱一致）。真增量集中在两点：① **三平台消费级 GA 日期锁定**——HarmonyOS 7 于 9-7 随 Mate XT 2 向消费者铺开、Windows 11 26H2 于 9 月下旬~10 月初以 enablement package 交付、iOS 27 于 9-14 GA；② 一份新的第三方 BFCL v4 端侧快照（Luxand LLM SDK）。对 OS PM 的核心含义：四平台 agentic 框架同步进入「发布前最后冲刺」，本库「来源轴四平台全空白」结论不变。

## 净新增（索引 → B 笔记）

| 重要性 | 原子笔记 / 落点 | 主题枢纽 | 一手来源 |
|---|---|---|---|
| ★★★★★ | [[HarmonyOS Intents Kit 与 ArkAF 2026]]（补 9-7 消费版 GA 日期 + ArkAF 2.0 入消费者） | [[意图框架·跨体系索引 MOC]] | https://www.techoper.com/blog/huawei-mate-xt-2-harmonyos-7-launch-september-7 |
| ★★★★ | [[Windows Copilot Actions 与 Agent Workspace 2026]]（补 26H2 GA 窗口 + Ask Copilot 意图搜索 + Sysmon 内置） | [[端侧执行通道 GUI 与 MCP 路线之争]] | https://www.pcworld.com/article/3063498/windows-11-26h2-is-coming-meet-all-the-new-features.html |
| ★★★ | [[Function Calling 端侧工具调用]]（补 Luxand BFCL v4 端侧 Agentic Score 快照） | [[Intent Router 语义路由]] | https://www.luxand.com/llm-sdk/benchmarks/ |

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27 RC 预计 9 月初、GA 9-14（peoplearegeek / ios27beta.com）；App Intents schema 层与 08-15 已录 Beta 5 逐字一致，无新 API；Extensions（第三方模型后端）仍为 dev.to 二手，无官方新文档。
- **Android**：AppFunctions 仍为 `1.0.0-alpha11`（2026-08-26，developer.android.com/jetpack 官方 Release Notes 当前最新），无 alpha12；`EXECUTE_APP_FUNCTIONS` 权限模型同 09-01 已录。
- **HarmonyOS**：7 开发者 Beta / 花粉 Beta 框架同 HDC2026；9-7 为消费版铺开档期，非新 API。
- **Windows**：agentic security 官方文档（learn.microsoft.com/.../operating-system-agentic-security）四支柱（Agent accounts / Agent Workspace / Scoped file / MCP-ODR）与 08-09 以来一致；26H2 的「Ask Copilot」是搜索层意图理解入口，非新 Registry API。

## 我的问题 / 后续动作

- [ ] 用 Berkeley 官方 BFCL v4 榜复核 Luxand 快照（当前为厂商 SDK 自测，非官方行）。
- [ ] 9-7 后回填 HarmonyOS 7 消费版真实 API level（26 vs 23 冲突仍待官方文档）。
- [ ] 9-14 iOS 27 GA 后核查是否新增 per-intent 路由/来源声明 API（将重评 [[四平台意图 Registry 来源轴与权限模型对比 2026]] 来源轴结论）。
- [ ] 延续既有待办：Watch OS 26 是否 Trust Insights 类、NowSecure/AgentAntibody 独立核验、Chrome Origin Sets 官方 URL 逐字复核。
