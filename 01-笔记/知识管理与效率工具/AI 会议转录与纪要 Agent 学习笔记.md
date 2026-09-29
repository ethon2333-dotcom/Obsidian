---
title: AI 会议转录与纪要 Agent 学习笔记
tags: [ai-agent, 效率工具, 会议-agent, 语音转录, 纪要生成, 知识管理]
created: 2026-09-15
source: 官方文档 + 行业报道 + 第三方横向测评（信息截止 2026-07/09）
---

# AI 会议转录与纪要 Agent 学习笔记

**一句话心智模型：** AI 会议 Agent 不是"录音笔"，而是把你开过的每一场会，自动变成"可检索的对话记忆 + 可执行的待办闭环"——它抢的是会议结束后那 30–60 分钟的人工整理时间。

> ⚠️ 定位说明：本文聚焦**会议 / 通话场景**的自动化转录与纪要生成，与库内"用户研究访谈分析"类笔记刻意不重叠（后者偏研究洞察而非会议流转）；也不展开通用 PKM 方法论（见 [[PKM 方法论与 Obsidian 生态 学习笔记]]）。

## 1. 定义

AI 会议转录与纪要 Agent = 自动加入/捕获会议 → ASR 转写 → LLM 提炼摘要/决策/行动项 → 分发到日历、CRM、任务系统的Agent化工具链。核心交付物：可搜索转写稿 + 结构化纪要 + 行动项（owner + 截止时间）。

## 2. 分类

| 类型 | 说明 | 代表 |
|---|---|---|
| 实时转录 | 会议进行中边说边出文字，常带说话人标注、实时字幕 | Otter、通义听悟、飞书妙记 |
| 异步转录 | 上传录音/录像文件，云端转写并总结 | 通义听悟（文件）、讯飞听见、Sonix |
| 会议纪要生成 | 在转写基础上做摘要、章节、决策提取 | 飞书妙记智能纪要、Fireflies 总结、Zoom AI Companion |
| 行动项提取 | 自动识别"谁要在何时做什么"，并推送到任务/CRM | Fireflies、Zoom Tasks、Circleback、Notion AI |

> 多数产品是"实时转录 + 纪要生成 + 行动项"的组合，边界已模糊。

## 3. 主流方案与代表产品

- **欧美云端派**：Fireflies.ai、Otter.ai、Fathom、Granola、tl;dv、Read AI、Tactiq、Zoom AI Companion、Notion AI Meeting、Microsoft Teams Recap
- **中国生态派**：通义听悟（阿里云）、飞书妙记（字节）、钉钉 AI 听记、讯飞听见（科大讯飞）、腾讯会议 AI 纪要、腾讯元宝录音笔
- **端侧/隐私派**：Granola（Mac 本地捕获，无 bot）、Jamie（欧盟托管、ISO 27001）、Meetily / Caven（端侧转写）

## 4. 2025-2026 进展（广度点到为止）

- **实时多说话人分离（Diarization）成熟**：说话人自动标注从"说话人1/2"进化到按声纹匹配姓名（飞书妙记 2025 新增声纹识别；Fireflies/Otter 多人识别）。
- **与日历 / CRM 打通成标配**：Fireflies 100+ 集成、Otter 2026-04 宣布 knowledge engine 并向 Jira 推送、Zoom AI Companion 把行动项变成 Zoom Tasks。
- **本地端侧隐私转录升温**：受隐私质疑推动（Washington Post 2026-07 报道、企业 IT 封堵自动入会 bot），端侧 ASR 准确率已逼近云端，Granola/Jamie/Meetily 主打"音频不出设备"。
- **Agentic 自动建待办**：从"给摘要"到"自动落到 tracker"——Zoom Tasks、Circleback、Granola 通过 MCP / Zapier 把行动项写进 Linear/Notion/CRM；Notion AI 用后台 agent 配置化生成任务。
- **会议即"工作记忆层"**：新叙事从"转录"转向"跨会议记忆引擎"（如 Otter knowledge engine、Tana 把会议更新进单一记录），可跨时间追问"我们上次对预算怎么定的"。
- **平台内置化**：Zoom / Teams / Google Meet 原生 AI 摘要免费或随订阅附送，独立工具价值向"跨平台 + 深度 CRM + 端侧隐私"收缩。Microsoft Teams 计划 2026-07 推出 Recap 应用作统一会议回溯中枢。

## 5. 代表产品对比表

| 产品 | 定位 | 实时/异步 | 说话人分离 | 行动项 | 隐私端侧 | 价格档（待核实厂商口径） |
|---|---|---|---|---|---|---|
| Fireflies.ai | 团队/销售自动化工作流 | 实时+异步 | ✅ 多人 | ✅ 分发第三方 | 云端；承诺任何套餐都不用你的数据训练 | 免费无限转写 / Pro $10·Business $19·Enterprise $39（月/人，年付） |
| Otter.ai | 英语实时转录先行者 | 实时为主 | ✅（英文强） | ✅（向 Jira 等） | 云端；默认用去标识数据训练 | 免费 300min/月 / Pro $16.99·Business $30（月/人） |
| Fathom | 最慷慨免费档 | 实时 | ✅ | ✅（付费同步 Slack/CRM） | 云端；botless 录制 beta | 免费无限录制转写 / Premium $15·Team $19 |
| Granola | Mac 本地、bot-free | 实时（本地捕获） | 依赖手动笔记补全 | 付费经 MCP/Zapier | ✅ 端侧捕获，音频不出设备 | 试用后 $14/月 |
| Zoom AI Companion | Zoom 原生 | 实时+会后 | ✅ | ✅→Zoom Tasks | 云端；随付费 Zoom 附送 | 含于付费 Zoom 计划（高级需 Custom add-on） |
| Notion AI Meeting | Notion 内的纪要 | 实时（桌面端） | ✅ | ✅（agent 配置） | 云端 | Notion AI 附加 $10/月 |
| tl;dv | 免费跨平台录制 | 实时 | ✅ | ✅（CRM/跟进） | 云端；端到端加密 | 免费无限录制 |
| 通义听悟 | 中文/企业会议 | 实时+异步 | ✅ 发言人标签 | 标记（无直连任务系统） | 云端；企业版支持本地化部署 | 新用户 90 天试用 / 按量计费 |
| 飞书妙记 | 飞书会议原生 | 实时+异步 | ✅ 2025 声纹识别 | ✅ 同步飞书任务 | 云端；依赖飞书生态 | 基础版含额度 / 超额按 AI 用量 |
| 讯飞听见 | 中文高精度+方言 | 实时+异步 | ✅ 5–10 人声纹 | 提取（无直连任务） | 云端；离在线双模 | 会员约 ¥30/月起 / 精转 ¥1.34/分钟 |

> 价格与"准确率百分比"多来自厂商官方口径或第三方测评，实际受口音/噪音/术语影响，**标「待核实」**。

## 6. 与库内笔记的关联

- 会议纪要是 PKM 的"输入源"之一：转写稿如何回流到个人知识库，是 [[PKM 方法论与 Obsidian 生态 学习笔记]] 的待解命题（见下方深度盲区）。
- 这类工具本质是"寄生在会议平台上的 Agent"，与 [[AI 原生浏览器与 Agent 浏览器 学习笔记]] 同属"Agent 作为工作流载体"的谱系。
- 行动项自动建待办、对接 CRM，与 [[低代码无代码 Agent 搭建平台 学习笔记]] 讲的 agent 编排 / MCP 集成是同一套能力。

## 7. 深度盲区（留给 Ethon 补充）

- [ ] 本地端侧转录（Granola / 讯飞离线模式）在中文多人抢话场景的**真实准确率**到底怎样？是否值得为隐私牺牲召回？
- [ ] 转写稿 / 纪要与 **Obsidian vault 双向同步**的最佳路径是什么（插件？API？手动归档？），能否自动生成带 wikilink 的笔记？
- [ ] 企业数据合规：涉密/客户会议能否用云端 bot？ consent（告知同意）与数据主权（跨境）的红线在哪？
- [ ] 自动 action item 的**可靠度**——漏提、错提责任人的概率有多少，是否反而制造"虚假跟进"？
- [ ] 国内生态（飞书/钉钉/腾讯/通义）与国际工具（Fireflies/Fathom）在**跨平台会议**（如中外团队混用 Zoom+飞书）下如何衔接？

## 附：来源清单

- Fireflies.ai 官方博客：Fireflies vs Otter 对比（2026）、What Is AI Transcription（2026）—— fireflies.ai/blog
- Otter.ai 官方定价页 —— otter.ai/pricing
- 飞书官网：智能会议 / 飞书妙记介绍 —— feishu.cn
- 第三方横向测评（2026-07 截止，含钉钉/飞书/通义/讯飞/腾讯/Otter/Fireflies 规格表）—— 来自社区实测汇总
- AI Jet：10 Best AI Meeting Notes Tools in 2026 —— aijet.cc
- Atlas Workspace：Best Meeting Notes App 2026（62 小时实测） —— atlasworkspace.ai
- Tana Blog：7 AI meeting tools that turn talk into action（2026） —— tana.inc
- The AI Rankings：Best AI for Meeting Notes in 2026 —— theairankings.com
- AI in Asia：AI Meeting Notes That Write Themselves（2026） —— aiinasia.com
- Briefarc：AI Meeting Recorders privacy risk（引 Washington Post 2026-07-09） —— briefarc.com
- Yaps.ai / Kiolo：本地端侧转录与隐私对比（2026） —— yaps.ai、kiolo.com
- 搜狐科技：Microsoft Teams Recap 应用将于 2026-07 推出 —— sohu.com（2026-06-27）

## ⚠️ 待核实清单

- [ ] Fireflies "99% 英文 / 95% 其他语言"、Otter "~95% 英文" 等**准确率数字**为厂商营销口径，真实场景待实测。
- [ ] 各产品**具体价格档**（尤其 Fireflies/Otter/Fathom 月付与年付差异）可能随策略调整，以官网最新为准。
- [ ] Otter 涉及的"集体诉讼 / 可能 $50–150M 和解"估算来自第三方分析师（UC Today），**未经司法确认**。
- [ ] 国内产品（通义听悟/飞书妙记/钉钉/讯飞/腾讯会议）的**中文识别准确率、方言支持、免费额度**官方多未公布具体数字，表中为功能定性，非量化指标。
- [ ] Microsoft Teams Recap 的**正式上线时间与功能分层**（Audio/Video Recap 需 Copilot 许可）依 2026-06 报道，可能变动。
- [ ] "端侧 ASR 准确率已逼近云端"为 2026 行业报道结论，具体差距因设备/场景而异，待独立评测。

#标签/AI会议Agent #标签/效率工具 #标签/Agent
