---
title: "AI 原生浏览器与 Agent 浏览器 学习笔记"
tags: [广度种子, AI浏览器, Agent浏览器, 效率工具]
created: 2026-09-02
source: "WebSearch/WebFetch 核实（见文末来源清单）"
---

**AI 原生浏览器 = 把 AI Agent 焊进浏览器内核（能替你点、填、订、发），而不只是给普通浏览器加一个「AI 侧边栏插件」——区别在于 Agent 拥有对页面与跨标签页的"操作权"，而非仅"解释权"。**

> 心智模型展开：普通浏览器 + 插件 = 你操作、AI 旁观并总结；AI 原生浏览器 = AI 成为"副驾驶/代驾"，直接读取页面 DOM、跨标签页推理、执行多步任务。它与 [[AI 搜索与 RAG 问答产品生态 学习笔记]]（独立搜索产品，Q&A 层）是上下游关系——浏览器是 AI 搜索/操作的**入口载体**；与 [[PKM 方法论与 Obsidian 生态 学习笔记]]（个人知识管理方法论）则完全不在一层——本篇谈"信息如何被获取与操作"，后者谈"信息如何被内化与连接"。

## 一、产品形态分类

| 形态 | 特征 | 代表 |
|---|---|---|
| **内置 Agent 的独立浏览器** | 从零以 AI 为先设计，Agent 是内核公民，可跨标签页操作 | Comet、Dia、Opera Neon、ChatGPT Atlas |
| **传统浏览器 + AI 层（插件式/缝合式）** | 在既有浏览器上叠加 Gemini/Copilot/Leo 侧边栏与少量 Agent 能力 | Chrome + Gemini Auto Browse、Edge Copilot、Brave Leo、Arc（已转向 Dia） |
| **浏览器原生自动化平台** | 不做"浏览"，专做"代你自动化网页操作"，常要求交出密码/历史 | Aside（候补）、Jatter |

关键分野：**Agent 是否在页面上拥有"操作权"**（点击/填表/提交），而非仅"解释权"（摘要/问答）。拥有操作权的，才称得上 Agent 浏览器。

## 二、玩家格局速查表（广度，点到为止）

| 产品 | 出品方 | 核心能力(Agent代操作/搜索/总结) | 形态 | 进展状态 |
|---|---|---|---|---|
| **Comet** | Perplexity | 代搜索/跨标签页总结/填表订票/发邮件日历/语音 | 独立浏览器(Chromium) | 2025-07 发布(Max $200/月) → 2025-10 全免费 → 2026 全平台(iOS/Android/Win/Mac)免费 |
| **Dia** | The Browser Company（2025-10 被 Atlassian 收购，约 $610M *待核实*） | 跨工作应用上下文(Slack/Notion/Gmail/日历)、Skills 可复用工作流 | 独立浏览器(Chromium，Arc 团队) | 2025-06 beta → 2025-10 开放 macOS；Dia Pro $20/月 |
| **Opera Neon** | Opera | Neon Do(代操作标签页/填表)、Make(生成网站/游戏/报告)、ODRA(深度研究)、**暴露 MCP 端点** | 独立浏览器(订阅 $19.9/月) | 2025-05 公布 → 2025-09/12 公测；2026-03 MCP 连接器 |
| **ChatGPT Atlas** | OpenAI | 侧边栏总结/重写、Agent Mode 代规划执行、与 ChatGPT/Codex 融合 | 独立浏览器(macOS 起) | 2025-10-21 发布 macOS；2026-03 与 ChatGPT/Codex 统一为桌面应用 |
| **Chrome + Gemini** | Google | Auto Browse(多步任务)、Gemini 常驻侧边栏、Personal Intelligence | 传统浏览器+AI 层 | 2026-01-29 大更新(Gemini 3 驱动) |
| **Aside** *(未 GA)* | YC 背书 | 浏览器内原生自动化(代填表/管数据)，"交出密码与浏览历史" | 独立自动化平台 | 候补名单，未正式发布 |
| **Jatter** | Jatter | 页面级问答/个性化推荐/内置笔记 | 独立浏览器(免费+$10/月) | 2025-06 发布 |

## 三、2025–2026 进展（核心叙事）

- **十个月四连发**：2025-07 至 2026-03，Comet / Dia / Opera Neon / Atlas 四款"Agent 浏览器"先后达到可用/免费层级。浏览器这一"十五年无像样新进入者"的品类，被 Agent 浪潮强行激活。
- **免费化是主旋律**：Comet 从 $200/月 → 90 天内全免费，倒逼 Dia（免费档 + $20 Pro）、Atlas（绑定 ChatGPT 订阅不单卖）。信号一致：**浏览器不是变现单元，是 AI 订阅/搜索广告/企业捆绑的获客渠道**（对标 Chrome 作为 Google 搜索 loss leader）。
- **架构并未收敛**：四家对"Agent 该站在哪"下注不同——Comet 重搜索与跨标签页；Dia 重工作应用上下文；Opera Neon 重"动作优先"+ 开放 MCP；Atlas 重把用户锁在 ChatGPT 内。
- **巨头缝合**：Chrome 在 2026-01 才补齐 Auto Browse，AI 能力仍落后于专用 challenger，但凭 ~72% 份额（*待核实*）仍是默认入口。

## 四、与 Agent 框架 / AI 搜索的关系

- **与 [[AI 搜索与 RAG 问答产品生态 学习笔记]]**：Comet 本质就是 Perplexity 答案引擎的"浏览器壳"——AI 搜索是内核，浏览器是分发层。浏览器 Agent 化 = AI 搜索从"问答"走向"代办"。二者是同一赛道的两端，不是竞品。
- **与 Agent 框架**：Opera Neon 暴露 **MCP 端点**，允许 Claude/ChatGPT 把你的标签页、会话、已登录页面当上下文——浏览器正在变成 Agent 的"环境/工具供给层"，与 [[低代码无代码 Agent 搭建平台 学习笔记]] 中"Agent 需要可操作环境"的逻辑同源。
- **与工作流自动化**：Aside/Jatter 的"交出密码代操作"，与 RPA / 低代码 Agent 平台能力高度重叠，只是把执行现场从"后端 API"搬到"前端浏览器 DOM"。

## 五、隐私与数据归属问题（重点张力）

- **浏览器即监控**：Dia "观察你访问过的每个网站与每个登录态"；Aside 直白要求"交出密码、历史、上下文"。Agent 的操作权 = 对你数字生活的读取权。
- **提示注入（Prompt Injection）真实存在**：Comet 被独立安全研究者披露过 "CometJacking" 等漏洞（恶意网页内嵌指令可静默抽取邮件/日历/凭据），时间跨度 2025-10 至 2026-03。Agent 在不可信网页上"自动点击"是结构性风险。
- **商业模式矛盾**：Perplexity CEO 曾公开表示 Comet 部分目的是收集浏览数据用于未来广告定向（与 Google 用 Chrome 的逻辑一致）。"免费"的代价是数据。
- **合规边界模糊**：同事实体（已登录银行/邮箱）被 Agent 操作时，责任归属、审计、撤销机制均不成熟。

## 六、待解问题（留给 Ethon 自行补充）

- [ ] 浏览器 Agent 的**权限与安全边界**应如何设计？（沙箱？人类在环确认？可撤销委托？）
- [ ] 当 Chrome（~72% 份额）把 Gemini 焊进内核，专用 Agent 浏览器靠什么**留存**而非只做"尝鲜入口"？
- [ ] 它与**端侧意图框架/OS 级 Agent**（如手机系统级智能体）是互补还是入口竞争？见 [[手机AI智能体知识库]]（若存在）
- [ ] Agent 浏览器作为"个人数据的超级聚合点"，**数据主权/本地优先**是否可能成为差异化卖点（对比隐私浏览器 Brave/DuckDuckGo）？
- [ ] 与 [[低代码无代码 Agent 搭建平台 学习笔记]] 的边界会否融合——未来"搭一个浏览器 Agent 工作流"是否就是低代码平台的自然延伸？

## 附：来源清单

1. AgentMarketCap — *Four Agent Browsers in Ten Months*（2026-04-16）`agentmarketcap.ai`
2. getaibriefs.com — *What Is an AI Browser? Atlas, Comet, and the Browser War of 2026*
3. newscadence.com — *The browser wars aren't about search anymore*
4. thebestaitools.co — *Perplexity Comet Review*
5. agentmarketcap.ai/agents/perplexity-comet — Comet 数据页
6. myaiguide.co / theplanettools.ai / recatools.com — Comet 功能与定价综述
7. tokenfeed.ai — *The Browser Is Now an Agent*

> ⚠️ 说明：上述来源混有独立媒体与 AI 生成内容农场的综述，时间线事实（发布/免费日期）多源一致可采信；**具体数字与远期模型版本名为单源/推测，已在下文标注待核实**。

## ⚠️ 待核实清单

- [ ] The Browser Company 被 Atlassian 以 **$610M** 收购的具体金额与日期（仅单源）。
- [ ] Chrome 全球份额 **~72%**、Comet **~18M MAU / 480M 查询每月 / $310M ARR** 等量化指标（单源 agentmarketcap，无其他佐证）。
- [ ] 文中出现的 **Claude Opus 4.6 / GPT-5.4 / Gemini 3.1 Pro** 等远期模型版本名（疑似推测，非官方确认）。
- [ ] Opera Neon **MCP 端点**对外开放细节与可用性（仅厂商/单篇综述提及）。
- [ ] Atlas 与 ChatGPT/Codex **"统一为单一桌面应用"** 的最终形态（2026-03 公告，落地细节待查）。

#标签/广度种子/AI浏览器 #标签/效率工具/Agent
