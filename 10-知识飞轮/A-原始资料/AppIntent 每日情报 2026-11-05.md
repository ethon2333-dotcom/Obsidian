---
date: 2026-11-05
tags: [AppIntent, 每日情报, SiriAI开发者预览, AppIntent.tool, Skills, 语义索引任意实体, 跨平台SKILL.md, 复核补全]
source: "https://developer.apple.com/news/?id=gdk2umrf ; https://ai.wain.blog/en/apple-siri-ai-developer-preview-app-intents-A72vY8E9 ; https://appleosophy.com/2026/11/03/heres-everything-thats-new-in-ios-27-3-beta-1/ ; https://www.163.com/dy/article/LAU7U46E0556PQ6I.html ; https://www.llmboard.ai/benchmarks/bfcl-64 (Updated Nov 4, 2026) ; WebSearch 直查官方/权威源（无 Horizon MCP，仅 agent-mail 在线）"
importance_score: "★★★★☆（头条 Apple Siri AI 开发者预览 + 新 AppIntents API ≈8/10；其余平台零净新增）"
intent_category: "系统级意图框架 / 端侧 Planner 模型 / 跨平台对比 / 执行安全（确认/认证策略）"
---

# AppIntent 每日情报 2026-11-05

> [!abstract] 30 秒速览
> 本窗口（2026-11-03 23:38 → 11-05 19:12，接续 11-03 运行，覆盖因 11-04 空缺产生的约 44h）**出现一个真正跨阈值的 OS 级框架进展**：Apple 在 iOS 27.3 开发者预览中**把 Siri AI 向所有开发者开放**，并带来一组**新的 App Intents API**——`@AppIntent(.tool)` 宏（把任意 intent 升格为 Siri 的「工具」）、**Skills**（用 `SKILL.md` 把多步动作串成单体验）、**Spotlight 语义索引「可浮现任意实体、不再受既有 schema 约束」**、Xcode Siri Integration Advisor + Siri Evaluations 框架（端侧意图集成回归测试）。这是自 iOS 27 GA 以来 App Intents 框架面**最大的一次扩展**，且首次把 Apple 拉入「`SKILL.md` 跨平台技能格式」阵营（Google 已声明 Gemini 可复制其他平台 skill）。其余平台本窗口**零净新增 API**：Android（AppFunctions 仍 beta01；Google 开放安卓开发工具给 Claude/Codex 属开发者工具链、非消费者意图框架，丢弃）、HarmonyOS（稳定 + 双十一营销/教程）、Windows（MXC 为 10-07 GA reprised；M365 SKILL.md/EMBRACE 为 M365/工具层，非 OS bus）、BFCL v4（LLMBoard 11-04 刷新仍全云级、端侧 Planner 仍不在榜）。本运行**对 3 个既有 B 笔记追加新进展（@AppIntent(.tool)/语义索引任意实体/Skills 跨平台收敛），0 新建 B 节点**，与「概念已存在则追加」去重纪律一致。
> **与 11-03 的衔接**：11-03 已录 iOS 27.3 beta 落地 + 中国 Qwen 端侧底座（模型层）；本运行补全同一事件的 **App Intents 框架层深度**（11-03 因快速命中未解包的 API 细节），并关闭 11-03 待办「iOS 27.3 是否新增公开 App Intents Schema 待 dev release notes 解析」。

## ① Schema 定义与语义路由机制（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | **Siri AI 开发者预览（iOS 27.3 beta，11-03 美/11-04 中）**：① `@AppIntent(.tool)` 宏给 intent 加 ToolIntent 一致性、变 Siri「工具」（对既有/新 intent 均生效）；② **Skills** = `SKILL.md`（body ≤10,000 字符，仅 name/description/Markdown、无 scripts/references）教 Siri 组合多步动作；③ **Spotlight 语义索引可浮现任意实体、不再限既有 schema**；④ Xcode Siri Integration Advisor + Siri Evaluations 框架 | ★★★★☆（★8/10，OS 框架级扩展，跨阈值） | 既 B 追加 3 节点（Apple Schema / 语义路由 / Skills 范式） |
| Android | AppFunctions 仍 `1.0.0-beta01`（10-21）无 beta02；`developer.android.com/ai/appfunctions/add-appfunctions` 为既有「破坏性操作须 App 自行确认」指南复述；Google 开放安卓 dev tools 给 Claude/Codex（11-04 腾讯新闻）= **开发者工具链/AI 编程智能体**，非消费者端侧意图框架 | ★★☆☆☆（无净新增；dev-tools 项丢弃） | 已复核·无净新增 |
| HarmonyOS | Intents Kit / ArkAF 稳定；双十一「小艺+元服务」消费营销 + 元服务开发教程，无窗口内新 OS 框架 API | — | 已复核·无净新增 |
| 跨平台 BFCL | LLMBoard 11-04 刷新（bfcl-64，11 模型）仍**全云级**（Llama 3.1 405B 88.5% 居首）；FunctionGemma 270M / qwen3-0.6b-tool-router **仍不在精选榜**，无新 ≤数 B 端侧 Planner official entry | ★★☆☆☆ | 已复核·无端侧净新增 |

要点：
- **🔑 头条 = Apple 把 App Intents 从「schema 对齐」推进到「工具 + 技能 + 任意实体」三层扩展**：`@AppIntent(.tool)` 让开发者用一行宏把既有或新 intent 变成 Siri 可调用的「工具」（agent 的「手」）；Skills（`SKILL.md`）把多步动作编排成单体验；Spotlight 语义索引从「只索引符合 schema 的实体」放宽到「可浮现任意实体」——**这是语义路由层的范式松动**：过去 Apple 的路由被封闭的 system schema 域锁死（本库长期记「schema 覆盖不到是断崖」），现在 Apple 允许 Siri 在 schema 之外通过 App Intents 暴露的能力直接触达任意实体，**介于「封闭 schema」与「完全 schema-less」之间**。
- **无新 entitlement / 无新 `@AppIntent(schema:)` 域**：本窗口 Apple 的扩展是**既有 App Intents 机制的能力放大**，而非新增 schema 域或新的系统 Schema 类型（App Intents Updates 官方页仍 June 2026 条目）；这与 10-26「iOS 27.x 进入稳定维护期」结论不冲突——本次是**开发者接入面放宽**，不是 schema 域膨胀。
- **跨平台 `SKILL.md` 收敛信号（重要）**：wain.blog 明确——**Google 已声明在其他平台写的 skill 可复制到 Gemini，且同样用 `SKILL.md`**；Apple 本次的 Skills 是 Agent Skills（`SKILL.md`）标准的**子集**（仅 name/description/Markdown body，无 scripts/references）。→ Apple + Google 在「技能描述格式」上**首次对齐到同一文件格式**，与 [[Agent Skills 技能范式 2026]]「SKILL.md 成为事实最广兼容格式」主张互为印证，是四平台意图框架之外**技能分发层的跨厂商收敛**。
- **诚实标注**：iOS 27.3 开发者预览的 `@AppIntent(.tool)` / Skills / 语义索引任意实体 API 细节来自 Apple 官方新闻稿（developer.apple.com/news/?id=gdk2umrf）+ wain.blog 对官方文档的深度解读（11-03/04）；Apple 何时把这些能力正式 GA（预览期「几个月后面向用户」、App Store 提交「春季」）待官方；`@AppIntent(.tool)` 是否对应新 API 名或仅是已有 ToolIntent 的宏糖衣、`Skills.skillsbundle` 具体打包约束待官方文档逐字段确认。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

### 窗口内命中（OS 框架级，已作诚实边界标注）
- **🔑 确认机制关键约束（★8/10，安全相关）**：wain.blog 逐字——Apple **明确声明 app skills 不能保证确定性行为**：「Siri AI does not necessarily run the intents listed in a skill in sequence」。**对必须保序的步骤（如确认购买），不能依赖 skill 文案顺序，必须在 intent 实现内部加检查**（如购买确认）。→ 这是跨平台「技能编排 ≠ 确定性执行」的首次官方确认，直接冲击「用 skills 串多步含确认流程」的朴素假设，与 [[Confirmation UI 安全机制]] 及 [[XPIA 跨提示注入]] 的「确认点不可被编排顺序绕过」主张一致。
- **认证策略与已知缺陷（★6/10，安全相关）**：默认 entity **不需要认证**；敏感信息（如金融）须设 `authenticationPolicy`；单个属性可见性 `internal` 仅作用于 Siri 响应，结果含敏感信息的 intent 须在 **intent 级别** 也设策略。iOS & iPadOS 27.3 release notes 载 **known issue**：**即便定义了要求解锁的策略，Siri AI 仍可能在未解锁时显示该实体**——属 beta 期认证策略执行缺陷，内部测试建议暂不用真实数据。→ 与 [[Confirmation UI 安全机制]] 的 Apple 侧落地（EntityOwnership + authenticationPolicy 棘轮）互补，本次补充「beta 期策略未强制执行」的安全缺口。
- **接入面隔离（★5/10，安全相关但非新机制）**：开发者预览**仅在开发签名构建 + 内部 TestFlight** 生效，**外部测试者与 App Store 版本暂不可用**；预览期 customer availability 在「几个月后」、App Store 提交「春季」。→ 属发布节奏隔离，非新 OS 隔离机制，但降低了预览期爆炸半径。

### 去伪 / 丢弃（按口径）
- **Apple 新 `@AppIntent(schema:)` schema 域 / 新系统 Schema 类型**：不成立——本窗口为既有机制能力放大（tool/skills/任意实体索引），App Intents Updates 官方页仍 June 2026。
- **Android AppFunctions beta02 / alpha14**：不成立——官方仍 beta01（10-21）。
- **Android「开放开发工具给 Claude/Codex」= 消费者端侧意图框架进展**：不成立——属 AI 编程智能体 + 安卓 dev tooling（android signals / Android Bench 2.0），非 AppFunctions/Connected Apps 消费者框架，按「无 OS 级落地」丢弃。
- **Windows 新 OS 执行总线 API / XPIA 新 OS 机制**：不成立——MXC 为 10-07 GA reprised（dev.to 11 月 reprised 解读）；ESPC 11 月 M365 治理（Copilot in Excel SKILL.md / Purview DSPM）属 M365 层、非 Windows OS bus；EMBRACE（alongside.team，10-29）为 AI 编程工具内嵌浏览器 XPIA（Cursor/Copilot/Codex/VS Code/Claude Desktop 文件读取漏洞），属**工具层**非四平台 OS 执行总线，按「OS 级」口径丢弃。
- **HarmonyOS 新 Intents Kit / ArkAF API**：不成立——双十一营销 + 元服务教程，无窗口内变更。
- **BFCL 新端侧 Planner entry**：不成立——FunctionGemma 270M / qwen3-0.6b 仍不在榜。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
