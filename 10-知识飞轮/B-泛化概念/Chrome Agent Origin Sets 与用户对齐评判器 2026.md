---
date: 2026-08-09
captured: 2026-08-09
tags: [概念蒸馏, 执行安全, XPIA, 确定性门控, 读写分级, Chrome, 意图路由]
source: "https://security.googleblog.com/ （Nathan Parker, Chrome security team, 2025-12-08）· https://techcrunch.com/2025/12/08/google-details-security-measures-for-chromes-agentic-features/"
importance_score: "★★★★☆（8/10）"
intent_category: "执行安全 / 读写分级 / 确定性门控 / 跨源数据外泄防护"
aliases: [Agent Origin Sets, User Alignment Critic, 用户对齐评判器, 代理源集合]
---

# Chrome Agent Origin Sets 与用户对齐评判器 2026

> [!abstract] 30 秒速览
> **核心突破**：Google Chrome 把「同源策略 / Site Isolation」这套浏览器二十年的确定性安全原语，**扩展成了 Agent 执行边界**——每个任务会话维护 **read-only origins** 与 **read-writeable origins** 两个集合，由**不暴露给不可信内容的确定性门控函数（gating function）**决定；同时用一个**只看动作元数据、不看网页正文**的隔离 Gemini 模型（User Alignment Critic）否决偏离用户目标的动作。
> **关键指标**：VRP agentic 类别赏金最高 **$20,000**；首版实现为简化版（**仅跟踪 read-writeable 集合**，官方自陈）。
> **OS Agent 场景**：这是本库迄今看到的**第一个把「读 / 写分级」产品化到客户端、并且明确把 tool call（非 web 内容）也纳入 read-vs-write 划分**的一手官方架构——**可直接迁移到 OS 意图层**（App Intents / AppFunctions / Intents Kit 的意图调用本质就是 tool call）。

> ⚠️ **日期与层级双重校准（重要）**
> - **真实发布日期 = 2025-12-08**（作者 Nathan Parker，Chrome security team，原载 security.googleblog.com），**非本情报窗口内新闻**，属**库内空白补漏**。
> - **层级 = 浏览器 / 客户端层，不是 Android OS 层**。切勿写成「Android 已支持来源分级」——这正是 [[Agent Data Injection 数据注入攻击]] 在 2026-08-04 记下的层级误判教训。
> - 本笔记全文经**转载站全文 + TechCrunch 一手引述 + Computerworld 独立报道**三源交叉；`blog.chromium.org` 与 `support.apple.com` 直取均失败，**官方 URL 逐字复核仍待补**。

## 一句话定义

**Agent Origin Sets** 是把浏览器同源策略扩展到 AI Agent 的执行边界机制：按任务会话把数据源切成「可读」与「可读写」两个白名单集合，由确定性门控函数把关；**User Alignment Critic** 是与之配套的隔离评判模型，只审查提议动作的元数据、不接触网页正文，因此无法被页面内容直接毒化。

## 为什么重要

1. **它是「读入路径分级」第一次以产品形态出现在客户端**。此前本库记录的两个答案都不在这一层：CaMeL / Dual View 在**研究层**（[[带外防御与确定性门控]]、[[Dual View 智能体数据视图隔离]]），微软 AGT 在**治理层**（[[数据溯源分级与单调棘轮]]）。Chrome 把它做进了三十亿用户的客户端。
2. **它给出了「确定性 vs 模型」的工业分工样本**——不是非此即彼，而是**分工**（见下方对照表）。这对 [[带外防御与确定性门控]] 的「门不能是模型」原则是一次现实校验：Chrome 的**门控函数是确定性的**，但**判断相关性的 critic 是模型**——靠「隔离」而非「确定性」保证它不被污染。这是一个折中变体，而非对原则的否定。
3. **tool call 也被划成 read / write**——这一句是全文对 OS 意图框架**最可迁移**的部分。App Intents / AppFunctions 暴露的每个 intent 本质就是一次 tool call，Chrome 已经在问「这次调用相对本任务是读还是写、合不合适」，而四大 OS 的意图 Registry **都还没有这一列**。

## 适用边界

- **不适用**：Agent 需要跨大量不可预知域名自由探索的开放式任务——origin gating 会带来摩擦，Google 自陈首版「会调优以减少不必要的摩擦」。
- **不解决**：**同源内的注入**。若恶意内容就在任务相关的可读 origin 内（如商品页的用户评论），origin set 不拦截，只能靠 PI classifier + critic。这正是 [[Agent Data Injection 数据注入攻击]] 场景一的形态。
- **不等于**：来源**可信度分级**。origin set 是**可见性 / 可写性**的白名单（binary），不是 `public → restricted` 的**密级棘轮**（[[数据溯源分级与单调棘轮]]）。两者正交，可叠加。
- **critic 的残余风险**：它看到的元数据仍由被污染的 planner 生成——若攻击者能让 planner 编造一个「看起来对齐」的动作描述，critic 无从分辨。官方未讨论此自指风险，**待补**。

## 证据与例子（官方口径，本库未复现）

### 四层防线

| 层 | 机制 | 性质 | 关键设计 |
|---|---|---|---|
| ① 动作审查 | **User Alignment Critic**（独立 Gemini） | 模型（但隔离） | 只见动作**元数据**，不见未过滤网页内容 → "cannot be poisoned directly from the web"；否决后要求 planner 重新规划或交还用户 |
| ② 边界隔离 | **Agent Origin Sets** | **确定性门控** | read-only / read-writeable 双集合；门控函数同样不暴露给不可信内容；planner 无法自行加 origin |
| ③ 用户在环 | 分级确认 + work log | 确定性清单 + 模型 | 敏感站点走**确定性清单**；密码管理器登录、支付、发消息前暂停 |
| ④ 攻击检测 | 提示注入分类器 | 模型 | 与 planner 推理**并行**运行，配合 Safe Browsing + 端侧诈骗检测 |

### 「确定性 vs 模型」分工表（本库提炼，最具 PRD 价值）

| 判断 | Chrome 用什么 | 为什么这么分 |
|---|---|---|
| 这个 origin 能不能加入集合 | **确定性门控函数** | 门必须不可被内容影响 |
| 这个 origin 是否与任务相关 | 模型（critic 变体） | 相关性是语义问题，只能模型判 |
| 模型生成的 URL 能不能导航 | **确定性检查（限已知公开 URL）** | 防模型编 URL 做数据外泄 |
| 这是不是银行 / 医疗站点 | **确定性清单** | 高后果场景不赌模型准确率 |
| 这段内容是不是注入 | 模型（分类器） | 官方自陈"cannot flag everything" |

### 其他事实

- **iframe**：与任务无关 origin 的 iframe **完全不呈现给模型**；点击 / 输入只允许在授权 iframe。
- **导航**：planner 想去新 origin → 由 critic 变体判定相关性后才加入；页面自行跳转 → 同样过 critic。
- **tool call**：`"the planning model may ingest other non-web content such as from tool calls, so we also delineate those into read-vs-write calls and similarly check that those calls are appropriate for the task."`
- **首版简化**：`"We've initially implemented a simpler version of origin gating that just tracks the read-writeable set."` —— **read-only 集合的完整实现尚未落地**。
- **血统**：官方明示灵感部分来自 **dual-LLM pattern**（Simon Willison, 2023）与 **CaMeL**（Google DeepMind, arXiv 2503.18813）。
- **红队**：自动化生成恶意沙箱站点，优先覆盖 UGC 与广告投放两类广触达向量，以及金融交易 / 凭证泄露两类持久伤害。
- **VRP**：agentic 能力类别最高 **$20,000**。
- **企业侧延伸**（Chrome Enterprise "Future Mode Part 2"，ChromeOSphere，**日期待补**）：Chrome Enterprise Premium 把 DLP 引入 agent 数据流；**Chrome History 中被 agent 导航的后台页面显式标记为 agent actions** —— 这是一条**审计标记**设计，四大 OS 意图框架均无对应物。

## 可复用启发

1. **做 OS 意图 Registry 时，给每个 intent 加一列「读 / 写」**。这是 Chrome 全文最便宜、最可抄的一条：不需要密级体系，只需要声明「此 intent 是消费数据还是产生副作用」，就能让系统在编排时把「读」的结果不自动喂给「写」。**四平台目前都没有这一列**。
2. **门控函数与评判模型要分开设计，且用不同手段保护**：门控函数靠**确定性**（不可被内容影响），评判模型靠**隔离**（只喂元数据）。把两者混成一个「安全大模型」是最常见的错误。
3. **高后果判断不要交给分类器**。Chrome 对「是不是银行站」用确定性清单而非模型——**后果越不可逆，越要用确定性判据**。这与 [[带外防御与确定性门控]] 的动作分层矩阵同构。
4. **"首版只做了一半" 值得抄的是节奏**：先上 read-writeable 集合（防写 = 防不可逆损害），read-only 集合（防读 = 防外泄）后续再补。做端侧 Agent 权限时同样应**优先关住写路径**。
5. **审计标记（agent actions 标签）应进 OS 层**：用户事后要能回答「这一步是我点的还是 Agent 点的」。这条比任何事前确认都更容易落地，且是 EU AI Act 可追溯性的低成本抓手（见 [[数据溯源分级与单调棘轮]] 中 Article 10 勾稽）。

## 未决问题

- [ ] **官方 URL 逐字复核**：security.googleblog.com 原文（本轮 `blog.chromium.org` 直取 404，依赖转载 + TechCrunch 引述）。
- [ ] critic 只看 planner 生成的元数据 —— **被污染的 planner 能否编造「看起来对齐」的元数据骗过 critic**？（critic 机制的自指漏洞，官方未讨论）
- [ ] read-only 集合完整实现的时间表？
- [ ] tool call 的 read-vs-write 判定是**声明式**（工具自报）还是**推断式**（模型判）？若是自报，则回到「元数据可否伪造」的 ADI 老问题。
- [ ] Chrome Enterprise "Future Mode Part 2" 的发布日期与 Gemini Spark 集成时间线。

## 关联

- **索引**：[[意图框架·跨体系索引 MOC]]
- **主题枢纽**：[[语义路由]] ｜ [[确认机制]] ｜ [[隔离执行]] ｜ [[XPIA 跨提示注入]]
- **来源**：[[AppIntent 每日情报 2026-08-09-晚]]
- **同层防线**：[[带外防御与确定性门控]]（确定性门原则的现实校验）｜ [[Dual View 智能体数据视图隔离]] ｜ [[数据溯源分级与单调棘轮]] ｜ [[Agent Workspace 隔离执行]] ｜ [[Confirmation UI 安全机制]]
- **攻击面**：[[Agent Data Injection 数据注入攻击]] ｜ [[XPIA 跨提示注入]] ｜ [[文档型 XPIA 自传播蠕虫]]
- **平台对照**：[[Android AppFunctions 设备侧意图 2026]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Intent Routing Stack 六方意图路由分层对照 2026]]
- **方法**：[[Agent 读入路径可信数据边界 SOP]] ｜ [[Agent 写回路径 XPIA 风险评估 SOP]]

#标签/安全 #标签/XPIA #标签/确定性门控 #标签/读写分级 #标签/Chrome
