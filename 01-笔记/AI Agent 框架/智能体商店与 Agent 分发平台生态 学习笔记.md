---
title: 智能体商店与 Agent 分发平台生态 学习笔记
tags: [智能体分发, agent-marketplace, agent-store, ai-agent, 平台经济, 广度种子]
created: 2026-09-25
source: 联网检索
---

# 智能体商店与 Agent 分发平台生态

> [!abstract] 一句话心智模型
> 智能体商店是 AI 能力的「应用商店」——把 Agent 从「自己从头造」变成「发现、评估、部署别人造好的」，**分发层**正在成为 Agent 生态的胜负手，其玩法类比移动时代的 App Store，但多了「能力/协议」这一分发维度。

---

## 1. 定义与分类（按分发模式）

智能体「商店 / 市场 / 分发平台」指：让开发者发布、用户发现与使用、平台撮合并（通常）结算的智能体（或智能体能力）集散地。按**分发模式**可分为四类：

| 分发模式 | 特征 | 代表 | 类比 |
|---|---|---|---|
| **平台内嵌市场** Platform-native | 宿主 App 内嵌，靠宿主流量驱动发现 | GPT Store、Claude Marketplace、Gemini Gems、Coze/豆包商店、腾讯元器 | App Store 内嵌于 iOS |
| **独立开放市场** Independent/Open | 跨宿主、开放分发，常由第三方运营 | Dify/Coze 市场、Skills 市场（Agensi/Agent37/ClawdHub）、Hugging Face Spaces | 独立应用商店 / 包管理器 |
| **企业私有市场** Enterprise Private | 私有化或企业内部分发，重治理与审计 | Salesforce AgentForce、Microsoft Copilot Studio、腾讯云智能体平台、火山 HiAgent、百度千帆 | 企业软件采购目录 |
| **协议化能力分发** Protocol-based | 不以「完整 Agent」为单位，而以「工具/技能」标准分发 | MCP Servers、Agent Skills（SKILL.md）、A2A | SDK / npm 包 |

> 关键洞察：当 Agent 可被「标准化能力」组合时，分发粒度从「整包应用」下沉到「可复用的工具/技能」，这与 [[Agent 协议生态 学习笔记]] 中的 MCP/A2A 直接咬合。

---

## 2. 主流方案对比表

| 平台 | 厂商 | 形态 | 端侧/云侧 | 创作者生态 | 审核机制 |
|---|---|---|---|---|---|
| GPT Store | OpenAI | 平台内嵌对话 Agent + 拟上线的 App Directory（基于 MCP） | 云侧 | 创作者经济（订阅分成，比例待核实） | 平台审核；自定义 GPT 指令可被提示注入提取（待核实） |
| Claude Marketplace / Agent Skills | Anthropic | 企业集成市场 + SKILL.md 开放格式 | 云侧（Claude Code 可端侧跑） | 第三方付费市场（Agensi 称 80% 创作者分成，待核实） | 开放格式 + 第三方安全审计（待核实） |
| Gemini Gems / Gemini Agent | Google | 平台内嵌 + Workspace 侧边栏（Gmail/Docs/Sheets…） | 云侧 | Workspace 团队共享 | 平台审核（细节待核实） |
| Coze 扣子 / 豆包智能体 | 字节 | 零代码平台 + 多渠道发布（豆包/飞书/抖音/微信） | 云侧 | 开发者 300 万+、插件 800–1 万+（待核实） | 平台审核（细节待核实） |
| 元器 | 腾讯 | 零代码 + 微信/QQ/公众号生态分发 | 云侧 | 微信生态内分发 | 平台审核（细节待核实） |
| 文心智能体 / 千帆 | 百度 | 全栈开发平台（零/低/原生代码）+ 搜索生态分发 | 云侧 | 开发者生态 | 平台审核（细节待核实） |
| 百宝箱 | 支付宝/阿里 | 低门槛 + 支付宝小程序/支小宝分发 | 云侧 | 商家/机构生态 | 平台审核（细节待核实） |
| 钉钉 AI Agent Store | 阿里钉钉 | 企业 IM 内应用市场 | 云侧 | 首批 200+ 助手（待核实） | 平台审核 |
| 通义 / 阿里云 | 阿里 | 模型 + Agent 一站式（百炼/百宝箱体系） | 云侧 | 开发者生态 | 平台审核 |
| AgentForce | Salesforce | 企业 CRM 内预置 Agent（销售/客服/教练） | 云侧 | ISV / 伙伴生态 | 企业治理 + 合规审核 |
| Copilot Studio | 微软 | M365 内建 Agent，接 Microsoft Graph | 云侧 | Power Platform 生态 | 企业治理 |
| Dify 市场 / Hugging Face Spaces | 开源/社区 | 开源 LLM 应用 + 社区托管运行 | 云侧（可私有化） | 开源社区 | 社区/自托管，弱中心审核 |

---

## 3. 2025–2026 进展（点到为止）

- **分发渠道碎片化**：Agent 分发裂为五类市场模型（平台内嵌 / 独立开放 / 企业私有 / 协议化能力 / 开源注册表），且各自买家旅程不同（分类口径待核实）。
- **GPT Store 拟走「两层模型」**：休闲 GPT（对话 Agent）+ 严肃 App（基于 MCP 的 ChatGPT App Directory，2025-12 起接受开发者提交，细节待核实）。
- **Claude Skills 市场已成形（2026-05 口径）**：目录追踪 4,200+ skills、770+ MCP servers、2,500+ marketplaces、12 万月访客；但碎片化明显（Agensi/Agent37/ClawdHub/SkillsMP/LobeHub 五强并立，无统一赢家，待核实）。
- **中国混战**：Coze 于 2025-07 开源 Coze Studio（Apache 2.0）；字节豆包 2025 Q1 上线智能体超 10 万（待核实）；腾讯元器、百度文心、支付宝百宝箱、钉钉 Agent Store 同期卡位。
- **商业化路径收敛**：托管访问（hosted-access，运行时+计费+迭代）显著优于一次性文件售卖；同类目头部 5–10 个 skill 拿走 60–80% 收入（赢家通吃，待核实）。
- **安全危机升温**：自定义 GPT 的系统提示/知识文件可被提示注入提取；平台加速安全扫描与下架机制（具体通过率/下架率待核实）。
- **端侧缺位**：当前主流商店均为云侧托管；手机/OS 级「端侧智能体」分发机制尚不成熟，参见 [[应用层 Agent 框架 vs 系统级意图框架 对照]]。

---

## 4. 深度盲区（留给 Ethon 补充）

- [ ] 各大平台**创作者分成比例与结算周期**具体如何？（GPT Store / Skills 市场 / Coze 星火计划 / 元器分成等）
- [ ] 智能体**审核通过率、下架率、内容安全红线**是什么？尤其国内平台口径很不透明。
- [ ] **端侧智能体**（手机/OS 级）的分发机制如何与云端商店耦合？与系统意图框架的边界在哪？
- [ ] **企业私有市场 vs 公有市场**的治理边界、审计责任、数据出境如何划分？
- [ ] 跨平台可移植性（Agent Skills / MCP）在真实商业场景的**落地率**如何？是否仍是「表面锁定」（Claude.ai ≠ API ≠ Claude Code 无同步）？
- [ ] 国内「拟人化 AI」相关办法对智能体商店的**身份/内容合规**要求如何具体落地？

---

## 5. 与库内笔记的关联

- 能力分发底层是协议：[[Agent 协议生态 学习笔记]]（MCP / A2A / Agent Skills 标准）。
- 多 agent 协作催生「可复用 agent 组件」需求：[[多智能体协作与编排 学习笔记]]。
- 行业纵深场景是商店里最易变现的类目：[[垂直行业 Agent 纵深入 学习笔记]]。
- 商店后端的模型接入与路由：[[模型服务化与 LLM 网关 学习笔记]]。
- 端侧分发的系统级接口：[[应用层 Agent 框架 vs 系统级意图框架 对照]]。

---

## 附：来源清单

1. https://blog.csdn.net/Ai_easygo/article/details/163247801 — 《2026年Agent商店生态全景：五大市场模型的竞争格局与商业化路径》
2. https://callsphere.ai/blog/ai-agent-marketplace-ecosystem-trends-2026 — AI Agent Marketplaces and the Emerging Agent Ecosystem in 2026
3. https://digitechbytes.com/?p=48793/ — The Skills Marketplace, Six Months Later（Claude Skills 2026-05 数据）
4. https://news.qq.com/rain/a/20250701A07QBY00 — 《巨头混战Agent》（字节豆包 / 腾讯元器）
5. https://www.ai-indeed.com/aboutNews/27531.html — 《2026中国智能体平台全景盘点》
6. https://learninggpt.ai/lessons/gemini/agents-overview — Gemini agents 2026 概览

---

## ⚠️ 待核实清单

- GPT Store 分成比例、App Directory 基于 MCP 并 2025-12 开放开发者提交的具体时间线与政策。
- Claude Skills 市场 4,200+ skills / 770+ MCP servers / 2500+ marketplaces / 12 万月访客，及 Agensi 80% 创作者分成——均来自 2026-05 第三方目录，需对照官方复核。
- 字节 Coze「300 万开发者、80 万日活」、豆包「10 万+ 智能体（2025 Q1）」等数字。
- 自定义 GPT 指令可被提示注入提取的普遍性与防御现状。
- 头部 skill 拿走 60–80% 收入的赢家通吃比例。
- 国内「拟人化 AI」办法对智能体商店身份/内容合规的具体落地要求与生效时间。
- Gemini Gems / Agent 的审核机制、是否开放公开「商店」式分发的细节。

#标签/AI-Agent框架 #标签/智能体分发 #标签/agent-marketplace
