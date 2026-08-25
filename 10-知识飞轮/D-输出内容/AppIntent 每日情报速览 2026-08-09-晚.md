---
date: 2026-08-09
tags: [输出复盘, AppIntent, 情报速览, 执行安全, 读写分级]
source: "https://security.googleblog.com/ （Nathan Parker, 2025-12-08）· https://techcrunch.com/2025/12/08/google-details-security-measures-for-chromes-agentic-features/ · https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini"
importance_score: "★★★★☆（8/10）"
intent_category: "执行安全 / 读写分级 / 确定性门控 / 意图 Registry 字段设计"
---

# AppIntent 每日情报速览 2026-08-09-晚

> [!abstract] 30 秒速览
> **核心突破**：挂了 6 天的最高优先待办「四平台是否对意图元数据做来源分级」取得**第二次实质进展**。答案不在 OS 层，而在**浏览器层**——Chrome 已把「同源策略」扩展成 Agent 执行边界：**read-only / read-writeable 双 origin 集合 + 确定性门控函数 + 只看元数据的隔离评判模型**。
> **关键指标**：VRP agentic 赏金 **$20,000**；Chrome 首版**仅实现 read-writeable 集合**；Google 官方防御口径确认为**六层**（此前本库仅有二手转述）。
> **OS Agent 场景**：Chrome 明确把 **tool call 也划成 read-vs-write**。App Intents / AppFunctions / Intents Kit 暴露的每个 intent 本质就是一次 tool call——**这是当前四平台意图 Registry 最低成本、最可抄的一条补丁**。

## 目标

在同日 21:00 完整跑之后做增补跑，不重复检索，把全部预算投给连续 6 日未解的最高优先待办，并执行 08-03 就定下、连续多轮未跑完的「改查官方安全文档」路径。

## 正文

### ① Schema 定义与语义路由机制

本轮对**意图 Schema 该长什么样**给出了一条此前没有的、极低成本的字段建议。

四平台意图 Registry（Apple `@AppIntent(schema:)`、Android `@AppFunction` + `app_metadata.xml`、HarmonyOS Skills、Windows ODR / Agent Launchers）目前描述的都是**「这个能力是什么」**——名称、参数、KDoc 描述、实体类型。**没有任何一家描述「这个能力在数据流中是读还是写」**。

Chrome 的做法反过来证明这一列有用：它按任务会话维护两个集合，**读来的数据只能流向可写集合内的目标**，从而在架构上切断「读到的恶意内容 → 直接驱动写动作」这条链路。而且官方明确把非 web 的 **tool call 也纳入同样的读 / 写划分**。

于是本库把此前给出的「防 ADI 最小字段提案」（六类来源枚举 + 四级密级 + 单调棘轮，来自 [[数据溯源分级与单调棘轮]]）**降级出一个最低版本**：

> **只加一个 `readOrWrite` 声明位。** 不需要密级体系，就能让系统拒绝把「读」的产物自动喂进「写」的动作。

这条对语义路由的意义是：Planner 在选 intent 时，除了「哪个 intent 语义最匹配」，还多了一个**确定性可判**的约束——本次任务的写目标是否在授权集合内。语义匹配交给模型，边界判定交给规则，分工清晰。相关枢纽见 [[Intent Schema Protocol 意图模式规范]] 与 [[Intent Router 语义路由]]。

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

本轮在安全侧产出三条可复用判据：

**（a）「隔离门」——确定性门与模型门之外的第三条路线。** 本库原则是「门不能是模型」（[[带外防御与确定性门控]]）。Chrome 的实现是**混合**：门控函数、模型生成 URL 白名单、敏感站点清单**全部确定性**；但「origin 是否与任务相关」「动作是否对齐用户目标」**由模型判**，靠**只喂动作元数据、不喂网页正文**的架构隔离来防污染。这提炼出第三档：**裁决者可以是模型，前提是它的输入面被收窄到攻击者不可写入的部分**。代价是风险转移——被污染的上游 planner 若能伪造「看起来对齐」的元数据，隔离门无从分辨。

**（b）确认「触发器」三档，与「确认内容」三档正交。** 本库此前只讨论确认文案从哪来。Chrome 补上了「谁决定要不要弹窗」：①规划模型自决（最弱，被污染就不弹）②分类器判定（有准确率边界）③**确定性规则**（清单 / 动作类型 / 资产敏感度，最强）。**Android 把确认整体下放给 App，意味着触发时机也由 App 自定，系统无法保证危险动作一定弹窗**——这是四平台里触发器最弱的一格。详见 [[Confirmation UI 安全机制]]。

**（c）「事后知情」是被忽视的第二类用户在环。** Google 官方六层里的 **end-user security mitigation notifications**（缓解后告知用户），加上 Chrome Enterprise 在浏览历史中**把 agent 导航的页面显式标记为 agent actions**，共同构成事前确认之外的形态：**事前确认管授权，事后标记管追溯**。后者成本低得多，且是可追溯性合规的现成抓手，**四大 OS 意图框架均无对应物**。

另需记录一条元判断：英国 NCSC 把提示注入定性为 **"confused deputy"** 类漏洞并称其**可能永远无法被完全缓解**（Computerworld 转述，原文待补）。若成立，则四平台的正确目标不是「防住注入」，而是**假定注入必然发生、用边界压小爆炸半径**——这正好解释了工业界为何主流投入在边界（origin set、[[Agent Workspace 隔离执行]]）而非检测。

## 方法

- 判读第一步仍是**分类「新事实 vs 口径变化 vs 层级误判」**。本轮最关键的动作是**层级校准**：Chrome 是浏览器，Origin Sets **没有**下沉为 Android AppFunctions 能力，同一家公司两条产品线的成熟度不可互相代入。若省掉这一步，就会错误地把待办标记为「已关闭」。
- 检索路径纠偏：常规 WebSearch 对「意图元数据来源分级」已连续多轮无效，本轮改走**官方安全文档 + 一手博客转载交叉**才拿到结果。Apple 侧 `support.apple.com` 网页直取失败，**下轮改走 PDF 全文**。

## 复盘

- **收获**：待办连续 6 日「无进展」的真正原因是**找错了层**——一直在 OS 文档里找，而答案在客户端产品里。**跨层找参照物**应固化为待办攻坚的常规动作。
- **仍未解**：Apple 一格依旧空白（连续第 7 日）。本轮 Apple 官方源直取失败，是唯一未推进的平台。
- **诚实标注**：Chrome 原文为**转载站全文 + TechCrunch 一手引述 + Computerworld** 三源交叉，`blog.chromium.org` 直取 404，**官方 URL 逐字复核待补**；NCSC / Gartner / OWASP 三组表述均为二手转述；Chrome Enterprise 后续文章日期待补。

> [!note] 概念节点
> [[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]

**索引与原子笔记**：[[意图框架·跨体系索引 MOC]] ｜ [[AppIntent 每日情报 2026-08-09-晚]] ｜ [[Chrome Agent Origin Sets 与用户对齐评判器 2026]] ｜ [[Agent Data Injection 数据注入攻击]] ｜ [[带外防御与确定性门控]] ｜ [[Confirmation UI 安全机制]] ｜ [[数据溯源分级与单调棘轮]] ｜ [[Dual View 智能体数据视图隔离]] ｜ [[Intent Routing Stack 六方意图路由分层对照 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[Agent 读入路径可信数据边界 SOP]]
