---
title: AI 辅助竞品情报与行业扫描 学习笔记
tags: [竞品情报, 行业扫描, PM工具, AI, 广度种子]
created: 2026-09-16
source: WebSearch/WebFetch 核实（Crayon/AlphaSense/Kompyte/Similarweb AI/秘塔 等 2025-2026 公开资料）
---

# AI 辅助竞品情报与行业扫描 学习笔记

> **心智模型**：竞品情报的本质是「用公开信号持续降低对手的不确定性」，AI 把"人盯人"升级为"机器盯全网 + 人做判断"，但判断权永远留在 PM 手里。

⚠️ **合规红线（先写死）**：本笔记所有内容只基于**公开渠道**（官网/新闻/社媒/招聘/专利/应用商店评论/财报），**不碰任何 NDA 资料、不写竞品内部机密**。AI 也不能监控非公开来源（客户对话、分析师闭门会、员工私域）。竞品情报只用公开资料，机密一律不碰。

## 1. 定义
**AI 辅助竞品情报（AI-assisted CI）**：用 AI 持续采集竞品与行业的公开信号（产品页/定价/招聘/新闻/专利/评论/财报），自动过滤噪声、摘要、结构化（SWOT、对比矩阵），并推送预警与周报。区别于一次性研究，强调**持续监测 + 可分发**。

## 2. 情报类型分类（BREADTH）
| 类型 | 关注什么 | 典型数据源 |
|---|---|---|
| 产品动态 | 功能发布、定价变更、页面改版 | 官网变更、发布说明、应用商店更新 |
| 行业趋势 | 技术方向、监管、资本流向 | 新闻、研报、融资公告、专利 |
| 人才动向 | 战略转向前兆 | 招聘（LinkedIn/Indeed）、高管变动 |
| 用户口碑 | 竞品真实体验与痛点 | G2/Capterra/应用商店评论、社媒 |

## 3. 主流方案横向对比
> 点到为止。价格多为媒体口径/第三方估算，标「待核实」；未实测。

| 厂商 | 定位 | 核心数据源 | 亮点 | 备注 |
|---|---|---|---|---|
| Crayon | 企业级 CI 监测 | 网站/定价/招聘/专利/新闻/社媒，100+ 数据类型 | Sparks AI 自动生成 battlecard；2025 加 MCP server；接入 Salesforce/Slack | 偏销售赋能，年费约 $15k–50k（**待核实**） |
| AlphaSense | 市场/金融情报 | 5亿+ 商业文档、财报、专家访谈(Tegus)、新闻 | Deep Research agent（2025.6）、AI Agent Interviewer；2026 Gartner CI 平台 MQ 领导者 | 90% S&P100 在用；2025.10 ARR 破 $500M（公开稿）；偏金融/战略，价高 |
| Kompyte | 自动化 CI + battlecard | 网页变更、广告、评论、招聘、社媒 | AI 每日摘要，约 1 小时/周；现并入 Semrush（**待核实**，据 2025 文章） | Gartner 点评两极（AI 摘要不稳、数据源偏浅） |
| Similarweb AI | 数字市场与流量情报 | 网站/APP 流量、关键词、AI 搜索可见度 | 2025 推 AI Search Intelligence（AI Brand Visibility/Traffic Tracker）、MCP server、AI Agents | 流量为建模估算，高 stakes 决策需一手佐证 |
| 秘塔 AI（Metaso） | 中文 AI 搜索/行业研究 | 全网/文库/学术（1.2亿篇文献） | 工作流式研究、可出思维导图/报告；中文语境强 | 月度 MAU 约 6500万（**待核实**，二手源）；适合中文行业扫描 |
| Perplexity / ChatGPT / Gemini 深度研究 | 一次性 cited 研究 | 公开网页、上传文件 | 临时竞品调研、SWOT/对比表生成，带引用 | 非持续监测；需人工复核防幻觉 |
| Perimeter | 竞品情报工具（**待核实**） | — | — | 检索显示「Perimeter（原 ProcessBolt）」实为**供应商风险管理**工具，是否仍为 CI 工具**待核实** |
| 腾研 | 国内竞情/研究工具（**待核实**） | — | — | 具体产品与定位未核实，标「待核实」 |
| 特工宇宙 | 国内 AI Agent 平台（**待核实**） | — | 含行业研究员/创投情报类专家 Agent，可编排竞品追踪 | 作为 CI 工作流载体**待核实**，未实测 |

## 4. 2025–2026 进展（速览）
- **从"搜索"到"agent 化"**：Crayon 加 MCP、AlphaSense 推 Deep Research/Workflow Agents、Similarweb 发 AI Agents——情报从"查"走向"持续运行 + 自动分发"。
- **AEO/AI 可见度成为新战场**：品牌在 ChatGPT/Perplexity/Gemini 的被推荐度成为竞品新指标（Similarweb AI Brand Visibility）。
- **AI 摘要普遍化但需人审**：几乎所有工具都上 AI 摘要/自动 SWOT，但媒体与 Gartner 点评均强调**幻觉与浅分析风险**，仍需 PM 复核。
- **国产工具补位中文场景**：秘塔、纳米、特工宇宙等在中文学术/行业研究、Agent 编排上快速迭代。

## 5. 代表产品（PM 视角）
- 重型持续监测：Crayon、AlphaSense、Kompyte（Semrush）、Similarweb
- 轻量/临时研究：Perplexity、ChatGPT Deep Research、秘塔 AI
- 自搭自动化：n8n/Zapier 定时抓取 + Claude/GPT 显著性分析 → Slack 推送（开发者 1–2 天可搭）

## 深度盲区（留给 Ethon 后续深挖）
- [ ] **待解问题**：Android OS PM 场景下，哪些"公开信号"能最提前预示竞品（如鸿蒙/Windows）的系统级 Agent 动作？确定优先级清单。
- [ ] **待解问题**：battlecard / SWOT 自动生成的质量阈值——什么置信度才敢进销售/决策材料？
- [ ] **待解问题**：AEO（AI 引擎可见度）如何纳入自家产品与竞品的对比框架？有无可量化指标？
- [ ] **待解问题**：中文情报源（应用商店评论、社交、招聘）的自动化抓取工具链，国内有哪些可用且合规？
- [ ] **待解问题**：情报"预警噪声"治理——如何设 alert 规则避免被 500M 数据源淹没？
- [ ] **待解问题**：与 [[数据飞轮与 AI 产品度量 学习笔记]] 的边界——自家度量 vs 外部竞情如何不串味？

## 关联笔记
- 用户研究侧的 AI 工具链 → [[AI 用户研究与产品洞察工具链 学习笔记]]（访谈分析，非竞品）
- 自家产品度量 → [[数据飞轮与 AI 产品度量 学习笔记]]（自家长北极星/采纳率，非竞品）
- 平台与生态博弈视角 → [[意图框架开发者生态与平台经济 学习笔记]]
- 搜索与 RAG 生态（AEO 相关）→ [[AI 搜索与 RAG 问答产品生态 学习笔记]]
- 上层索引 → [[竞品情报 MOC]] / [[PM决策层 MOC]]

---

## 附：来源清单
1. Crayon 官网 / Sparks Live Tiles 博客 / StayModern & TeachUsTechnology 评测（2025–2026）
2. AlphaSense 官网、$500M ARR 新闻稿（2025-10-07）、Sacra 收入估算（2026）、Gartner MQ 2026
3. Kompyte 官网、Gartner Reviews（2025-10 更新）、Battlecard 2025 工具盘点（提并入 Semrush）
4. Similarweb 2025 Year-in-Review、AI Search Intelligence / AEO 工具文（2026-07）
5. 秘塔 AI（metaso.cn）、人人都是产品经理/AI产品库 评测（2025）
6. MarqOps《10 AI Competitive Intelligence Tools & Agents (2026)》、SkyCrumbs、AI Business Weekly、Meltwater 2026 买家指南

## ⚠️ 待核实清单
1. **Perimeter**：检索显示其为供应商风险管理工具（原 ProcessBolt），是否仍是竞品情报工具**待核实**。
2. **腾研**：具体产品与定位未核实，标「待核实」。
3. **特工宇宙**：作为 CI 工作流载体的能力与实测**待核实**。
4. **Kompyte 并入 Semrush**：据 2025 第三方文章，时间线与范围**待核实**。
5. **Crayon 年费 $15k–50k**：第三方估算/媒体口径，**待核实**，无公开标价。
6. **秘塔月活约 6500 万**：来自二手行业文，**待核实**。
7. 各工具 AI 摘要准确率、battlecard 采纳率等**效果数字均来自厂商稿/媒体，未独立验证，切勿当评测结论引用**。

#标签/竞品情报 #标签/行业扫描 #标签/PM工具
