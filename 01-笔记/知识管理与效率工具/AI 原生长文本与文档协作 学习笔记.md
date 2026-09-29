---
title: AI 原生长文本与文档协作 学习笔记
tags: [效率工具, AI写作, 文档协作, 办公, 学习笔记]
created: 2026-09-18
source: WebSearch/WebFetch 核实（见文末来源清单）
---

# AI 原生长文本与文档协作 学习笔记

> 一句话心智模型：AI 原生长文本 = 让 AI 从聊天框走进文档本身，成为写作、改写、协作工作流里的常驻能力，而非独立对话。

## 广度覆盖（BREADTH > DEPTH，点到为止）

### 定义与范畴

「AI 原生长文本」指 AI 能力被深度嵌入文档/写作/协作工作流，而不是以独立聊天机器人形态存在——写作、续写、改写、摘要、引用核查都在文档原地发生，AI 是"常驻协作者"而非"需要复制粘贴的中转站"。它与「AI 搜索/问答」的区别在于：后者回答"问题"，前者产出"成稿/成稿中的改动"；与「聊天机器人/IM 入口」的区别在于：前者对话的上下文是整篇文档与工作流，后者是会话窗口。2025-2026 的关键演化是从"生成一段文字"走到"代你在文档内执行多步操作"（文档智能体）。

### 分类 / 产品形态（表格）

| 维度 | 形态 | 代表产品 | 备注 |
| --- | --- | --- | --- |
| 嵌入位置 | 办公套件内嵌（在 Word/Docs/飞书文档里直接改） | Microsoft 365 Copilot、Gemini in Docs、飞书豆包工作伙伴·文档、WPS 灵犀、腾讯文档 | 最符合"原生"定义；改动留痕、格式保留 |
| 嵌入位置 | 块/页面级知识库内嵌 | Notion AI（含 Custom Agents）、Confluence/Atlas Rovo | 文档即数据库，AI 可读写结构 |
| 产品定位 | 独立写作助手（外挂式） | QuillBot、Jasper、Grammarly、Sudowrite | 改写/营销长文/校对，常做插件或网页 |
| 产出形态 | AI 演示/文档生成器 | Gamma、飞书/PPT 智能生成 | 一句话出结构化 deck |
| 架构形态 | 文档智能体框架（doc agent / multi-agent RAG） | Notion Custom Agents、Copilot Cowork、Samsung DeepDive、SlideAgent/ORCA | 多步规划、代查代改、跨文档 |
| 部署 | 本地优先文档 RAG（个人知识库 AI 化） | Obsidian + Smart Connections/Copilot + Ollama、AnythingLLM | 数据不出本机，详见 [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]] |

### 核心能力维度

| 能力维度 | 是什么 | 当前成熟度（2025-2026） |
| --- | --- | --- |
| 长文生成与续写 | 从空白页/提纲到成稿，或接着已有段落写 | 套件级标配（Gemini "Help me create"、Copilot 整篇起草、WPS 灵犀端内生成） |
| 改写润色 | 重写/缩短/扩写/调语气/统一风格 | 最成熟，QuillBot 七模式、Gemini "Match writing style"、Copilot 选段改写 |
| 摘要 | 长文/多文档压成要点 | 普遍；NotebookLM 式"源受限"、飞书评论式迭代 |
| 引用与事实核查 | 标注出处、基于文档内来源写作、防幻觉 | 起步期：Gemini 源受限写作（2025-10）、Copilot 引文、Grammarly Authorship 标注人机撰写部分 |
| 多人协作中的 AI | 实时建议、按评论改稿、冲突消解 | 飞书"评论迭代"、Copilot 按评论执行修改（2026-06）、Gemini 评论工作流（2026-07） |
| 文档智能体（doc agent） | 代查资料、代改文档、跨文档多步执行 | 2026 主线：Notion Custom Agents、Copilot Cowork、飞书豆包工作伙伴主动跟进 |

### 2025-2026 进展

- **Notion：从"会回答的 AI"到"会干活的 AI 同事"**。2026-02 发布 **Custom Agents**（3.3），常驻、按日程/事件触发、跨数百页运行；2026-04（3.4）加 AI 自动填表、技能（Skills）、Slack 私频道接入；2026-07（3.6）引入 **External Agents**（Claude、Cursor 可纳入同一看板）、可读写 PPTX/XLSX/DOCX/PDF、Outlook 接管。2026-05 起改 **Notion Credits** 按量计费（待核实具体单价）。
- **Microsoft 365 Copilot：Agentic 编辑 GA**。2026-04-22 Word/Excel/PowerPoint 的"agentic 多步编辑"正式可用（GA），Copilot 直接在文档内执行结构化改动；**Copilot Cowork**（长时多步、跨文件，基于 Anthropic 技术）2026-06-16 GA；**Work IQ** 把邮件/会议/聊天/关系当上下文；2026-06 起支持"按评论执行修改"与 PowerPoint 品牌套件/Brand Kit。
- **Google Gemini in Docs：Workspace Intelligence 重做写作体验**。2026-04-22 重新设计 Gemini 体验——"Help me create" 跨 Drive/Gmail/Chat 生成首稿、"Match writing style / Match doc format" 统一文风与版式；**Workspace Intelligence** 让 Gemini 实时理解跨 Workspace 上下文（Gmail/Chat/Calendar/Drive）；2026 加音频摘要、文内图片生成、评论工作流、自定义持久指令。默认模型 Gemini 3 Flash（待核实版本号）。
- **国内办公套件集体"智能体化"**：飞书 **aily 更名为豆包工作伙伴**（2026-08-13），深度嵌入文档/多维表格/会议，支持全域上下文、评论迭代、风险披露模式；腾讯文档 **"人机双写"**（2026-06，行业首发说法待核实），WorkBuddy 内核，人与 AI 同文档同权限实时协同；**WPS 灵犀专业版** 2026-07-15 发布（原"WPS 灵犀 claw"更名）、2026-08-03 收费，主打记忆系统 + 文档专家 + 专业数据源 + 技能生态。
- **独立写作助手重塑定位**：QuillBot 2026-05 末全品牌重塑为"创造力平台"（改写/翻译/摘要/页内 AI Cursor 合一）；Jasper 转为"营销操作系统"，2026-01 推 **Optimization Agent**（面向 GEO/被 AI 引用）；Grammarly 公司更名为 **Superhuman**（待核实）并推 proactive agent。
- **文档智能体 / Agentic RAG 成为底层范式**：2025-2026 学术与产业界出现多智能体文档框架（SlideAgent 三级、ORCA 模态专家池、SPD-RAG 一文档一 agent、Samsung DeepDive 报告代写），核心是"规划—检索—多步执行—带引文产出"；与个人知识库 RAG 同源（见 [[AI 搜索与 RAG 问答产品生态 学习笔记]]）。

### 代表产品（表格对比）

| 产品 | 定位 | 核心 AI 能力 | 备注 |
| --- | --- | --- | --- |
| **Notion AI** | 知识库 + 常驻 AI 同事 | Custom Agents（定时/事件触发）、Skills、跨文件读写、External Agents | 2026 重心从写作转向自动化工作流；计费改 Credits |
| **Microsoft 365 Copilot** | Office 套件原生协作副驾 | Word/Excel/PPT agentic 编辑、Copilot Cowork 长时多步、Work IQ 上下文、按评论改稿 | 多模型（OpenAI + Claude，Claude 在 Excel/PPT 曾为默认，待核实）；企业权限/ sensitivity label 继承 |
| **Gemini in Google Docs** | Workspace 原生写作伙伴 | Help me create、Match 文风/版式、源受限写作、音频/图片生成、评论工作流 | Workspace Intelligence 跨应用上下文；数据不用于训练/广告（官方承诺） |
| **飞书 豆包工作伙伴·文档**（原 aily） | 飞书内原生 AI 同事 | 全域上下文写作、评论迭代改稿、风险披露模式、主动跟进周报 | 权限与本人一致、操作可追溯；2026-08 更名 |
| **腾讯文档 / WorkBuddy** | 微信生态协同文档 | "人机双写"同文档实时协同、本地 Office 文件内修改 | 2026-06 首发说法待核实；"人人/人机/机机"多端同步 |
| **WPS 灵犀专业版** | 国产 Office 原生智能体 | 端内对话→成品、长文转 PPT、PDF 语义拆分/翻译、记忆系统、技能生态 | 2026-07-15 发布、08-03 收费；接入豆包/火山引擎 |
| **QuillBot** | 改写/摘要/学术助手 | 七模式改写、语法、摘要、引用生成、Co-Writer | 2026-05 重塑为创造力平台；免费档有限 |
| **Jasper** | 营销长文/品牌声量平台 | 长文 Editor、Brand Voice、Campaigns、Optimization Agent（GEO） | 面向营销团队；无免费档，价格待核实 |
| **Gamma** | AI 演示生成器 | 主题/大纲→排版配图 deck（约 60 秒） | 全球用户量最大之一（待核实） |

## 与库内笔记的关联

- [[AI 在即时通讯与办公协作入口 学习笔记]]：本文聚焦"文档/长文写作"场景里的原生 AI，后者聚焦聊天/IM 常驻入口（豆包/元宝/微信内 AI）；两者是"办公 AI 化的两个切面"——一个在文档里、一个在对话流里，边界正在因"人机双写""智能伙伴"而融合。
- [[本地优先 AI 与个人 LLM 桌面应用生态 学习笔记]]：本文云侧文档 AI 的"本地镜像"是 Obsidian + Ollama 那套——同样做"在文档里问答/续写"，只是数据不出本机；前者打便利与协作，后者打隐私与离线。
- [[AI 原生浏览器与 Agent 浏览器 学习笔记]]：浏览器 Agent（Comet/Opera Neon）"代操作网页"，文档智能体"代操作文档"——同一股 agentic 浪潮落在不同载体；前者动 DOM，后者动段落与版式。
- [[PKM 方法论与 Obsidian 生态 学习笔记]]：Obsidian 到 2026 仍无原生 AI，文档 AI 能力全部外挂插件；本文的"云文档原生 AI"正是 PKM 笔记在"个人知识库 AI 化"上的另一端参照（见 [[AI 搜索与 RAG 问答产品生态 学习笔记]]）。
- [[AI 搜索与 RAG 问答产品生态 学习笔记]]：文档智能体的"代查代改"本质建立在 RAG/GraphRAG 之上；Notion/飞书/WPS 的"全域上下文"就是企业版 RAG，本文是它向"写作工作流"的延伸。

## 深度盲区（留给 Ethon 后续补充）

- [ ] 文档智能体（doc agent）在多人实时协作下的**权限与冲突模型**？当 AI 代改的段落正被人类编辑，谁优先、如何 merge、如何回滚？
- [ ] "按评论执行修改"（Copilot/飞书）的**可靠性边界**在哪？复杂法律/财务文档的多步编辑错误率有无第三方实测（待补）？
- [ ] 云文档 AI 的"全域上下文"与"个人知识库 AI 化"的**护城河差异**？企业数据 vs 个人 vault，迁移成本与隐私取舍如何决定选型？
- [ ] 写作助手"人机撰写标注"（Grammarly Authorship）会否成为**合规刚需**？AI 生成文档的署名/披露规范会怎么演化？
- [ ] 作为 Android OS PM：系统级"文档智能体"（如端侧长文摘要/改写）与这些云端 App 的**分工边界**？端侧能否做"离线可改的轻量 doc agent"？

## 附：来源清单

1. Notion 官方 Release Notes（notion.com/releases，2026-04-14 / 2026-07-01 "3.6"）— Custom Agents、Skills、External Agents、计费改 Credits
2. Microsoft 365 Blog《Copilot's agentic capabilities… generally available》(2026-04-22) 与《Powering Frontier Transformation with Copilot and agents》(2026-03-09) — Cowork、Work IQ、agentic 编辑 GA
3. Microsoft Tech Community《What's New in Microsoft 365 Copilot | June 2026》— 按评论执行修改、PowerPoint Brand Kit、Skills
4. Google Workspace Updates（workspaceupdates.googleblog.com，2026-04-22 / 2026-07-28）— Gemini in Docs 重做、Workspace Intelligence、评论工作流、图片生成
5. buildfastwithai.com《Gemini in Google Workspace: Every AI Feature Explained (2026)》— Workspace 集成概览（第三方综述）
6. 飞书官网/帮助中心（feishu.cn，helpdesk.feishu.cn，2026-08-13 更名公告）— 豆包工作伙伴·文档能力
7. 腾讯文档/今日头条《大厂整合潮下的 AI 办公变局 2026》— "人机双写"、WPS 灵犀、飞书 aily 定位（第三方综述）
8. WPS 官方社区（bbs.wps.cn，2026-06-09 / 2026-07-15）— WPS 灵犀专业版内测与发布
9. redeepseek.io《AI Writing Tools in 2026》— QuillBot/Jasper/Grammarly 重塑（第三方综述，含待核实更名与定价）
10. emergentmind.com《Document Agent Frameworks》与 Samsung Tech Blog《DeepDive》— doc agent / Agentic RAG 架构（论文/企业实践综述）

## ⚠️ 待核实清单

- Notion 文中出现的远期模型版本名（GPT-5.4 Mini & Nano、Haiku 4.5、MiniMax M2.5、Opus 4.8、Grok 4.3、GLM 5.2）来自 Notion 发布说明，版本命名疑似超前，需查官方确认。
- Notion Credits 具体单价（$10/1000 等来自第三方博客）与"2026-05-04 起计费"的落地细节，需查 Notion 官方定价页。
- Microsoft 自报的 Copilot 参与度/留存/满意度增幅（+52% / +11% / +21% 等，2026-04-22）为厂商口径，未经第三方复现，标记待核实。
- "Claude 在 Excel/PowerPoint 早期成默认引擎、Word 夏季跟进"的多模型切换细节，需查 Microsoft 官方公告。
- Gemini 默认模型"Gemini 3 Flash / 3 Pro"的版本与默认范围，需查 Google 官方说明。
- 飞书文档 AI 实测数据（周报 35 秒/份、节省 76%、专业度 4.3/5）来自第三方 wiki 实测，样本与方法未独立验证，标记待核实。
- 腾讯文档"人机双写 2026-06 行业首发"的"首发"定性来自第三方文章，需查腾讯文档官方公告。
- WPS 灵犀专业版实测（万字报告 52 分钟 vs 4 小时）来自官方社区/第三方案例，标记待核实。
- QuillBot / Jasper / Grammarly 的定价、功能与"Grammarly 更名 Superhuman"均来自第三方对比站与综述，具体数字与更名事实需回各厂商官网确认。
- Gamma"全球用户量最大之一"等定性/数字为第三方口径，未核实。
- 各产品的"MAU/用户数/节省工时"等量化指标，凡非官方一手财报/公告的，一律视为待核实，不得直接用于对外材料。

#标签/效率工具/AI写作/文档协作
