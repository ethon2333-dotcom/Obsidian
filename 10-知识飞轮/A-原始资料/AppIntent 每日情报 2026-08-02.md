---
type: daily-index
status: index
captured: 2026-08-02
window: "7 日滚动窗口 2026-07-26 → 2026-08-02"
intent_category: "系统级意图框架 / 端侧 Planner 意图路由 / 跨应用 Intent 工作流 / 执行安全（XPIA / 合规）"
importance_score: "★★★★☆（8/10，窗口内真增量 2 条 + 库内空白补漏 2 条，含一条法规级分水岭）"
tags: [AppIntent, 情报, 索引, 2026-08-02]
---

# AppIntent 每日情报 2026-08-02（索引）

> [!abstract]
> 本日最高价值是**法规级分水岭**：EU AI Act **Article 15 于 2026-08-02 正式生效**，第 15(5) 条点名 prompt injection / 对抗样本 / 投毒，使四平台的 XPIA 防护、隔离执行、确认机制从「产品选择」变为**强制合规底线**（罚则 €15M 或全球营业额 3%）。窗口内第二条真增量是 **HarmonyOS 7（HDD 西安站 08-01）** 把 A2A 显式拆成**端侧 / 云侧双模**并给出落地实证（银行 1000+ 意图端侧、O2O 端到端闭环云侧），首次给出比「端侧优先」更可执行的路由判据。另补齐两条库内空白：**Apple WWDC26 Session 343**（View Annotations / IntentValueQuery / 确认与实体归属 + App Intents 2.0）与 **Android AppFunctions 官方 Agent Skill 四步生命周期**。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 9–10/10 | EU AI Act Article 15 今日生效：执行安全首次成为法规地板（15(5) 点名 prompt injection / 对抗样本 / 数据投毒 / 模型投毒；15(4) 韧性与反馈回路；Art.12 不可篡改日志 + Art.14 人类监督；罚则 €15M / 3%） | [[Windows Copilot Actions 与 Agent Workspace 2026]] · [[XPIA 跨提示注入]] · [[Agent Workspace 隔离执行]] · [[Confirmation UI 安全机制]] | [[端侧意图框架 学习笔记]] | [artificialintelligenceact.eu · Article 15](https://artificialintelligenceact.eu/article/15/) |
| 8/10 | HarmonyOS 7（HDD 西安站 08-01）：小艺升级为 **Agentic 自演进架构**系统级智慧大脑；A2A **端侧（低时延+数据不出端）/ 云侧（复杂深度推理）双模**；头部银行 App 端侧 A2A 覆盖 1000+ 意图、隐私不出端，O2O App 云侧 A2A 走完「问答→选座→购票→支付」闭环；「奇妙工具箱」一周完成 Agent 接入（120 万+ 用户 / 7 万+ 五星） | [[A2A 端侧智能体协议]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] | [[HarmonyOS 元服务 学习笔记]] | [HDD 西安站 · HarmonyOS 7 新特性（2026-08-01）](https://china.qianlong.com/2026/0801/8706085.shtml) |
| 8/10 | Apple WWDC26 Session 343 深入（2026-06，库内空白补漏）：九章节清单；**View Annotations**（`.siriAnnotation` / `.appEntityIdentifier` / `forSelectionType:` / 集合标注）解决「屏幕上的第三项」；**IntentValueQuery** 结构化搜索；**Confirmations and entity ownership**（`shared`/`public`/`unknown` 差异化确认）；**App Intents 2.0** = streaming + 更富实体 + 多轮追问（增量式迁移）；Extensions（Claude/GPT/Gemini）须经 App Review + App Store 分发 | [[Apple AppIntents Schema Protocol 2026]] · [[Confirmation UI 安全机制]] | [[Apple Intelligence 与 App Intents]] | [WWDC26 Session 343](https://developer.apple.com/cn/videos/play/wwdc2026/343/) ｜ [App Intents 2.0 streaming/multi-turn](https://www.techtimes.com/articles/318005/20260608/wwdc-2026-app-intents-replaces-sirikit-gemini-siri-migration-clock-starts.htm) ｜ [Extensions 隐私架构](https://dev.to/akaranjkar08/apple-wwdc-2026-rebuilt-siri-the-extensions-api-and-what-claude-on-14-billion-iphones-means-for-1c1l) |
| 7/10 | Android AppFunctions 官方 **Agent Skill 四步生命周期**（Android 17 同期，官方文档验证）：Discovery → Implementation & Configuration → **KDoc Refinement** → Testing & Debugging；技能仓 github.com/android/skills 下 device-ai/appfunctions；官方澄清 AppFunctions = Android 专属 / OS 级 / 本地执行 hook，vs 标准 MCP server = 平台无关 / 云端执行 + 网络往返；仍为实验性，EAP `goo.gle/eap-af`，验证 `adb shell cmd app_function list-app-functions` | [[Android AppFunctions 设备侧意图 2026]] · [[Agent Skills 技能范式 2026]] | [[MCP 与设备侧 MCP]] · [[App Intent 的核心作用]] | [developer.android.com · appfunctions](https://developer.android.com/ai/appfunctions) ｜ [Android 17 is here](https://developer.android.google.cn/blog/posts/android-17-is-here) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

> [!info] 口径留存（B 笔记未逐字收录的法规细节，保留在此以防丢失）
> - **Annex III 高风险八类**：生物识别 / 关键基础设施 / 教育 / 就业与用工管理 / 必要服务获取与信用评分 / 执法 / 移民边境 / 司法与民主程序。
> - **Article 15(2)(3)**：准确性须在技术文档（**Annex IV**）中声明**可测量指标**，并鼓励制定基准与测量方法。生效依据为 **Article 113** 实施时间线。
> - **Digital Omnibus 冲突口径**：拟把 Annex III 独立系统合规期限推迟至 **2027-12-02**、嵌入式系统至 **2028-08-02**，但截至 2026-08-02 仅为「临时政治协议」、**尚未正式通过**，原 08-02 仍是现行有效合规日（Gibson Dunn / White & Case 均如此提示）。
> - **HarmonyOS 口径**：银行「1000+ 意图」、O2O 端到端闭环均为华为现场披露口径，App 名称 / 意图清单 / 成功率**未独立核验**；HDD 西安站为官方通稿转载，与 HDC 2026 表述一致（小艺 1.8 亿 DAU、日均唤醒 30 亿+、2100+ 系统能力 Skill 化、500+ 伙伴精选 Skill、2000+ 鸿蒙智能体）。
> - **Apple 未确认项**：「Per-Intent Privacy Manifest」作为独立 API 名称本次一手检索**未能从官方文档确认**，本库不记为已确认 API。
> - **Android 日期待补**：Agent Skill 具体发布日官方未单独给出，随 Android 17（2026-06-16 GA）文档在线。

## 已复核·无净新增（避免重复检索）

- **信息源口径**：Horizon MCP 全部 disconnected，本期改用 WebSearch / WebFetch 直取官方源（developer.android.com、developer.apple.com、artificialintelligenceact.eu、HDD 西安站官方通稿转载）；厂商 / 媒体自述数据一律标注口径，未独立核验项标「待补」。
- **补漏口径**：Apple Session 343 与 Android Agent Skill 均超出 7 日窗口（分别为 2026-06、Android 17 同期），按「库内空白 / 已述待补」逐条标真实日期登记，不冒充当日新闻。
- **流程改进（已执行）**：本日起**正式切换为 7 日滚动窗口**，保留「首次进入本库」判定做去重。
- **本期净新增 B 节点 0 个**：四条信息全部以「既有 B-note 增补」形式落库，未新建概念节点。

## 排除项

- **M365 Copilot Agentic 模式扩大可用（2026-08-01）** —— 属办公应用 / SaaS 层智能体，不构成 OS 级意图框架 / Registry / 权限模型变化，低于 ≥6/10 的 OS 级相关性阈值，按过滤规则排除。若未来其 Agent 在 Windows 桌面级获得系统调用权，则重新纳入。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- Article 15 对四平台 OS Agent 的**具体合规触发条件**：小艺 / App Intents+Extensions / AppFunctions / Agent Workspace 各自是否落入 Annex III 高风险？还是主要约束「嵌入产品的 AI 安全组件」（2027-08-02 才到）→ [[Windows Copilot Actions 与 Agent Workspace 2026]]
- Digital Omnibus 正式文本是否通过 → 决定是否更新 Article 15 生效日口径 → [[Windows Copilot Actions 与 Agent Workspace 2026]]
- 端侧 A2A 多 Agent 互写互调时，被污染 Agent 能否把载荷写回另一个？蠕虫式 XPIA 是否可在端侧 A2A 链繁殖（四平台均无类别级评估）→ [[A2A 端侧智能体协议]] · [[文档型 XPIA 自传播蠕虫]]
- HarmonyOS 银行 App 具体名称 / 1000+ 意图清单 / O2O 闭环成功率核验 → [[HarmonyOS Intents Kit 与 ArkAF 2026]]
- 「Per-Intent Privacy Manifest」是否为真实 Apple API；Apple Extensions 的 App Review **具体审什么**（审意图声明安全性还是仅审分发）→ [[Apple AppIntents Schema Protocol 2026]]
- Agent Skill 自动生成的 KDoc 是否受 App Review / Play 审核约束？工具描述出错谁负责；Agent Skill 发布日期回填 → [[Android AppFunctions 设备侧意图 2026]]
- 延续待办：四平台 / 六方 Registry + 权限横向 Checklist（AgenticOS / Step AOS 未入表）→ [[Agentic OS 意图调度内核]]；荣耀 Robot Phone 8 月发布、Word 蠕虫类别级缓解 → [[文档型 XPIA 自传播蠕虫]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[端侧意图框架 学习笔记]] · [[HarmonyOS 元服务 学习笔记]] · [[Apple Intelligence 与 App Intents]] · [[MCP 与设备侧 MCP]] · [[App Intent 的核心作用]] · [[手机AI智能体知识库]]
> **本期原子笔记**：[[Windows Copilot Actions 与 Agent Workspace 2026]] · [[XPIA 跨提示注入]] · [[Agent Workspace 隔离执行]] · [[Confirmation UI 安全机制]] · [[A2A 端侧智能体协议]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[Android AppFunctions 设备侧意图 2026]] · [[Agent Skills 技能范式 2026]]
> **概念节点**：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Atomic Service 元服务]]
