---
title: AI 工作流自动化与编排 学习笔记
tags: [知识拓展, 效率工具, 工作流自动化, AI编排, iPaaS, AgenticWorkflow, 自动化编排]
created: 2026-09-19
source: "WebSearch 综合（Zapier / n8n / Make / Relay.app / 飞书·Coze / Dify 官网与第三方评测）"
---

# AI 工作流自动化与编排 学习笔记

> **心智模型：工作流自动化与编排 = 把"触发→判断→动作"这条流水线从代码里搬到可视化画布上，再用 AI 节点把"条件分支"升级成"语义判断"，让机器替你跑可重复的业务动作——它卖的是「编排」能力，不是「造一个 Agent」。**

## 1. 定义与边界

- **工作流自动化（Workflow Automation）**：用可视化 DAG（有向无环图）把多个 app 的步骤串成一条可重复执行的管线。核心是 *triggers（触发器）* + *actions（动作）* + *branches（条件分支/循环/合并）*。
- **AI 编排（AI Orchestration）**：在上述管线里嵌入 LLM 节点（摘要、抽取、分类、生成、调用工具），让"判断是否走某分支"由模型而非死规则决定。
- **与传统 iPaaS 的区别**：老牌 iPaaS（如传统 ETL/集成总线）强调"系统间数据同步"；新一代 AI 工作流平台把"AI 推理步骤"作为一等公民节点，并叠加 *human-in-the-loop*、*MCP 工具调用*、*agent 子流程*。
- **与"低代码搭 Agent 平台"的差异（本篇重点边界）**：[[低代码无代码 Agent 搭建平台 学习笔记]] 聚焦"造一个能对话的 Agent 应用"（Coze/Dify/元器 的 bot/agent 形态）；本篇聚焦"把多个系统按 DAG 编排成自动化流水线"——前者是**产物形态**，后者是**运行/编排范式**。两者重叠区：Coze 工作流、Dify Workflow 既是搭 Agent 也能做编排。

## 2. 分类（触发-动作 / DAG 编排 / Agentic workflow）

| 范式 | 心智 | 代表 | AI 介入程度 |
|---|---|---|---|
| **触发-动作型（Zap 式）** | If-this-then-that，线性串联 | Zapier（基础 Zaps）、飞书多维表格自动化、钉钉宜搭自动化 | 低，AI 多为单个「AI 步骤」贴花 |
| **DAG 可视化编排型** | 画布上分支/循环/合并，复杂数据路由 | Make（原 Integromat）、n8n、Relay.app | 中，AI 节点可参与分支判断 |
| **Agentic Workflow 型** | 工作流里嵌「能调用工具、自我循环的 Agent 子流程」 | n8n AI Agent 节点、Zapier Agents、Coze 工作流、Dify Workflow | 高，LLM 主导决策与多步规划 |

## 3. 主流方案对比（产品 - 定位 - AI 能力）

| 产品 | 定位 | AI 能力 | 自托管 | 计费口径 |
|---|---|---|---|---|
| **Zapier** | 最易上手的 SaaS 自动化，应用目录最广 | AI by Zapier（GPT 类步骤）、Zapier Agents（自主后台 Agent）、MCP 连接 Claude/ChatGPT、Copilot 自然语言建流 | ❌ 纯云 | 按 task/step 计费 |
| **Make** | 可视化强、性价比高的 DAG 编排 | OpenAI/Claude/Vertex 模块、条件分支接 AI 输出 | ❌ 纯云（EU 数据驻留） | 按 operation 计费 |
| **n8n** | 开发者向、可自托管的 AI-native 编排 | LangChain 节点、AI Agent 节点（ReAct/function-calling）、向量库、MCP Client 节点、Guardrails、HITL | ✅ 自托管 + 云 | 按 execution 计费 |
| **Relay.app** | 强调 human-in-the-loop 的现代编排 | 内建 AI 抽取/摘要/分类、多模型（GPT-4o/Claude/Gemini）、人工审批节点、可建 MCP server | ❌ 纯云 | 按 step + 信用点 |
| **飞书多维表格自动化** | 国内协作套件内的"表驱动"自动化 | 公式引擎 + 自动化触发 + 外接 Coze/大模型节点（见下） | ❌（飞书云） | 包含在飞书订阅 |
| **钉钉宜搭 AI** | 低代码表单/流程引擎 + AI 组件 | AI 填表、AI 审批助手、流程智能 | ❌（钉钉云） | 包含在钉钉 |
| **Coze 工作流** | 字节扣子的"工作流"编排能力（非 bot 本体） | 文档解析/OCR、代码节点、大模型节点、条件分支、计划任务触发 | ❌（云） | 平台内 |
| **Dify Workflow** | LLM 应用平台的编排画布 | 数据集/RAG 节点、Agent 节点、本地部署可选 | ✅ 可自托管 | 平台内 |

> 国内实践常是「Coze 工作流 + 飞书多维表格」组合：Coze 负责抓取/抽取/调用大模型，飞书负责数据存储、视图看板与群触达（如"盯 100 个博主爆款监控系统"案例）。

## 4. 2025–2026 进展（WebSearch 核实，媒体口径见「待核实」）

- **Zapier Agents 从 beta 转 GA 并重做**：2025-05-22 起从"聊天"转向"自动化"，引入 *Pods*（按职能分组 Agent）、*Activity dashboard*（审计/需人工介入过滤）、agent-to-agent 调用；2025-11 指南强调"自动化处理可预测工作、AI 处理复杂努力"的编排心智。来源：zapier.com 博客与帮助文档。
- **n8n 全面 AI 化**：AI Agent 节点（包 LangChain，支持 ReAct/记忆/向量库）、MCP Client 节点（2025-11）、Human-in-the-loop 节点（第三方称 2026-01）、Guardrails 节点；2025-08 改纯 execution 计费。来源：n8n.io + 第三方评测（具体日期**待核实**）。
- **Relay.app 把 human-in-the-loop 作为差异化卖点**，并新增原生 Tables、可对外建 MCP server。
- **原生入口 AI 自动化**：Gmail/Slack 等通过 Zapier MCP、各平台 AI 步骤把"AI 动作"下沉到日常 app（"原生 AI 自动化"趋势，细节**待核实**具体产品版本）。
- **工作流 Agent（agentic workflow）兴起**：把"能自我循环、调工具的 Agent"作为工作流的一个节点，而非独立聊天机器人——这与 [[多智能体协作与编排 学习笔记]] 的"编排"主线直接交汇。
- **国内**：飞书 + Coze 工作流、钉钉宜搭 AI、企业微信 WorkBuddy 等把"自动化编排"下沉到协作/办公入口（媒体口径，见来源清单）。

## 5. 代表产品速查

- 海外 SaaS：Zapier、Make、Relay.app、Tray.io（企业 iPaaS，**待核实**当前 AI 能力）
- 开发者/自托管：n8n、Hugging Face `smolagents` 流、LangGraph（偏代码而非画布，见 [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]）
- 国内：飞书多维表格自动化、钉钉宜搭 AI、企业微信（WorkBuddy）、Coze 工作流、Dify Workflow、腾讯云/阿里云相关流编排

## 6. 待解问题（留给 Ethon 深补）

- [ ] **编排 vs 搭建的边界到底在哪？** Coze 工作流/ Dify Workflow 同时是"搭 Agent"和"编排"，如何在本库两篇笔记间划清归类口径？
- [ ] **Agentic workflow 与传统 DAG 的本质区别**是"动态决策"还是"可自愈重试"？值得单独写一篇对比。
- [ ] **n8n 自托管的真实成本**（VPS + 运维时间）与 Zapier 规模化账单的折线交叉点在哪？需要量化建模。
- [ ] **MCP 作为"编排总线"** 是否正在取代各平台的私有 connector？对 Android 端侧/移动自动化有何启示？
- [ ] **human-in-the-loop 在 PM 工作流**（需求评审、发布审批）里怎么落地成可复用模板？

## 7. 关联笔记

- 差异化对照：[[低代码无代码 Agent 搭建平台 学习笔记]]（本篇是"编排范式"，那边是"Agent 产物"）
- 范式交汇：[[多智能体协作与编排 学习笔记]]（agentic workflow 的 Agent 层）
- 工具链旁支：[[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]（LangGraph 等代码态编排）
- 场景入口：[[AI 会议转录与纪要 Agent 学习笔记]]（会议 action item 可由工作流编排回流）

---

## 附：来源清单

1. Zapier 官网 / Agents 博客与帮助文档（2025-05、2025-11）— https://zapier.com/blog/zapier-agents-pods-dashboards/ ｜ https://help.zapier.com/hc/en-us/articles/36713413544845-Big-changes-to-Zapier-Agents-and-planned-maintenance
2. n8n 官网 — https://n8n.io
3. n8n AI 能力与定价第三方评测 — https://theplanettools.ai/tools/n8n ｜ https://automationatlas.io/answers/can-you-build-ai-agents-in-n8n
4. Make vs n8n vs Zapier 对比（2025）— https://mohasoftware.com/blog/n8n-vs-zapier-vs-make-which-automation-platform-wins-in-2025 ｜ https://www.artificial-intelligence-wiki.com/ai-automation/ai-workflow-orchestration-tools/make-vs-n8n-vs-zapier
5. Relay.app 官网与指南 — https://www.relay.app ｜ https://artificial-intelligence-wiki.com/ai-automation/ai-workflow-orchestration-tools/relay-app-guide
6. 飞书 + Coze 工作流实践（国内案例）— https://www.feishu.cn/content/article/7647059037481094382 ｜ https://devpress.csdn.net/v1/article/detail/154872859

## ⚠️ 待核实清单

- **n8n MCP Client 节点（2025-11）、HITL 节点（2026-01）具体发布日期**：来自第三方评测博客，非 n8n 官方发布页，需以官网 changelog 复核。
- **n8n 被 SAP 以 $5.2B 估值入股（2026-05）**：来自第三方 AI 工具站（howaiworks.ai），估值数字与交易细节需以 SAP/n8n 官方新闻稿核实，本文未采纳该数字进正文。
- **Zapier "450K+ Agents、9,000+ 集成、3.39M+ MCP 调用"等宣传数字**：属厂商官网口径，未独立核实，正文已转为定性描述。
- **"Gmail/Slack 原生 AI 自动化"具体产品版本与上线时间**：泛指行业趋势，具体原生能力以 Google/Slack 官方更新核实。
- **各平台应用数量（Zapier 6,000+ / Make 1,000+ / n8n 400+~1,900+）口径不一**：不同来源差异大，正文用区间或定性表述，精确数待核实。
- **钉钉宜搭 AI、企业微信 WorkBuddy 的具体 AI 编排能力**：媒体/厂商口径，功能边界待以官方文档核实。

#标签/效率工具/工作流自动化 #标签/AI编排 #标签/iPaaS #标签/AgenticWorkflow
