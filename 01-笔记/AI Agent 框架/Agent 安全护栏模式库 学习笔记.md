---
title: Agent 安全护栏模式库 学习笔记
tags: [AI Agent, 安全护栏, Guardrail, 策略即代码, 输入护栏, 输出护栏, 广度种子]
created: 2026-10-13
source: WebSearch 核实（Guardrails AI / NVIDIA NeMo Guardrails / LiteLLM / Microsoft Azure AI Content Safety / Meta Purple Llama / Google ShieldGemma / Anthropic / OWASP LLM Top 10 2025 / GuardBench），2026-10-13
---

# Agent 安全护栏模式库 学习笔记

> 一句话心智模型：**护栏模式库 = 在 LLM 调用边界（输入 / 输出 / 工具 / 检索 / 对话流）以"确定性代码 + 轻量分类器"编织的一套可复用安全拦截设计模式**；它区别于 [[工具调用安全 学习笔记]]（鉴权）、[[AI Agent 沙箱与安全执行环境 学习笔记]]（隔离）、[[AI 评测红队与对齐 学习笔记]]（模型红队）、[[智能体身份与信任 学习笔记]]（身份/授权）这些相邻层——护栏管的是"内容/行为该怎么被允许、拦截、改写"，而非"谁有权、跑在哪、模型本身安不安全"。

## 广度覆盖

### 1. 定义与心智模型

"Guardrail（护栏）"在 AI Agent 语境里指**部署在模型调用路径上的、可编程的安全控制点**，对请求/响应做检测、拦截、改写或升级。它通常是一个**中间件（middleware）/ 网关（gateway）/ 代理（proxy）**，在模型外层运行，因此**无需重训模型即可热更新策略**。

与相邻主题的分工（刻意不重复立题）：
- 鉴权/授权 → [[工具调用安全 学习笔记]]、[[智能体身份与信任 学习笔记]]、[[AI Agent 的权限与可撤销委托 学习笔记]]
- 隔离/沙箱 → [[AI Agent 沙箱与安全执行环境 学习笔记]]
- 模型红队/注入攻防 → [[AI 评测红队与对齐 学习笔记]]、[[AI 评测红队 Agent 链路注入 学习笔记]]
- 投毒/供应链 → [[AI 模型供应链安全与开源投毒防护 学习笔记]]
- **本笔记专属**：护栏*设计模式本身* + 如何编排编排（policy-as-code / DSL / 分层编排）

### 2. 护栏模式分类（按触发位置与职责）

| 模式 | 触发位置 | 典型检查 | 典型动作 | 代表实现 |
|---|---|---|---|---|
| 输入护栏 Input Guard | 用户/工具响应进入模型前 | prompt injection、越狱、敏感词、格式/长度校验、PII 脱敏 | 拦截 / 改写 / 打标 | NeMo input rails、Azure Prompt Shields、Llama Prompt Guard |
| 输出护栏 Output Guard | 模型响应返回前 | 毒性、PII 泄漏、事实一致性、格式 schema | 拦截 / 改写 / 降级 / 人工升级 | Guardrails AI、Llama Guard、ShieldGemma |
| 检索护栏 Retrieval Guard | RAG 文档入库/出库 | 投毒文档、越权检索、间接注入 | 过滤 / 权限裁剪 | NeMo retrieval rails、OWASP LLM08 |
| 执行/工具护栏 Execution Guard | 工具调用发起前 | 危险操作、越权 scope、非幂等调用次数 | 拦截 / 限流 / HITL 闸门 | LiteLLM、OWASP LLM06 |
| 对话/主题护栏 Topic/Dialogue Guard | 多轮流程中 | 跑题、违规话题、对话状态机越界 | 重定向 / 拒答 | NeMo Colang、topical rails |
| 内容审核分级 Content Moderation | 输入+输出 | 仇恨/暴力/色情/自伤等危害分类 | 分级处置 | Azure Content Safety、Llama Guard、ShieldGemma |
| 语义防火墙 Semantic Firewall | 全链路（结构化隔离） | 把"不可信数据"与"指令"在结构上分离 | 结构包裹 / 标记化 | LlamaFirewall、Spotlighting |
| 人审闸门 HITL Gate | 不可逆动作前 | 高风险/高代价动作 | 人工确认（UI 呈现见 [[Confirmation UI 分级与产品责任边界]]） | 各框架 human-in-the-loop 钩子 |

### 3. 主流护栏框架 / 产品对比

| 框架 | 形态 | 护栏语言/机制 | 强项 | 定位 |
|---|---|---|---|---|
| **Guardrails AI** | 开源（Py/JS） | RAIL（XML 声明式 schema）+ 自定义 Validator | 结构化输出校验、自动 re-ask 纠正、Guardrails Hub 预置校验器 | "LLM 的类型系统"：输出质量/结构强制 |
| **NVIDIA NeMo Guardrails** | 开源 | Colang（对话流 DSL）+ rails 配置 | 对话流/话题/检索/执行护栏、IORails 并行降低延迟 | "对话策略编排层" |
| **LiteLLM Guardrails** | 开源网关 | YAML 配置 pre/post/during_call 钩子 + 多 callback | 非侵入式、跨 100+ 模型、PII/密钥/注入/内容多引擎 | "网关层护栏承载" |
| **Microsoft Azure AI Content Safety / Prompt Shields** | 云服务 | 统一 API（直/间接注入检测 + Spotlighting + 内容过滤） | 实时、企业级、Defender for Cloud 集成、Foundry 控制面 | "托管内容安全 + 注入防护" |
| **Meta Purple Llama** | 开源 | Llama Guard（分类器）+ Prompt Guard + Code Shield + LlamaFirewall | 端到端 safeguard + CyberSec Eval 红蓝基准 | "开源 safeguard 全家桶" |
| **Google ShieldGemma** | 开源 | 基于 Gemma 的安全分类器（文本/图像） | 多模态（ShieldGemma 2 图像）、Responsible Generative AI Toolkit | "开放小模型分类器" |
| **Anthropic（护栏实践）** | 模型内 + 运营 | Constitutional AI + Constitutional Classifier + 实时 classifier + ASL/RSP 治理 | 内在对齐 + 运行时分类器 + 能力分级治理 | "对齐即护栏 + 治理闸门" |

### 4. 2025–2026 进展（已联网核实）

- **OWASP LLM Top 10 2025** 已发布（2023 初版，2025 更新）：**LLM01 Prompt Injection 仍居榜首**，并明确"仅靠系统提示不足以防注入，需在请求边界/检索路径/输出路径做结构性强制"（LLM05 Improper Output Handling、LLM06 Excessive Agency 也与护栏强相关）。
- **NVIDIA NeMo Guardrails** 进入 Colang 2.0 时代（2025，带形式语义的多轮状态机），最新发布 **0.22.0（2026-05-22，第三方源）**；新增 IORails 并行执行引擎以压低叠加护栏的延迟。
- **Meta Purple Llama** 2025-04-29 一次性更新：**Llama Guard 4（12B，原生多模态）**、**Prompt Guard 2（86M/22M，BERT 式注入/越狱检测）**、**LlamaFirewall（面向 Agent 的护栏框架 = PromptGuard 2 + AlignmentCheck + CodeShield）**、**CyberSec Eval 4**。
- **Microsoft** 将 Azure AI Content Safety 整合进 **Foundry Control Plane**；Prompt Shields 在 **Build 2025** 推出 **Spotlighting**（区分可信/不可信输入，专防间接注入 XPIA）；并与 **Defender for Cloud** 集成做运行时威胁告警。
- **Google** 推 **ShieldGemma 2（基于 Gemma 3 的 4B 图像安全分类器，2025-03）**，扩展自文本版 ShieldGemma，纳入 Responsible Generative AI Toolkit。
- **Anthropic** 2025 引入 **Constitutional Classifier**（辅助模型实时拦截越狱/越界输出）；并以 **Responsible Scaling Policy（RSP）/ AI Safety Level（ASL）** 做能力分级治理闸门（Claude Opus 4 启用 ASL-3）。
- **护栏基准 GuardBench**（欧盟 JRC，EMNLP 2024）：覆盖 40 个数据集、提供公开排行榜；2025-10-09 又新增 4 个数据集。IBM **Granite Guardian** 在榜单领先（多家第三方评测）。
- **趋势共识**：① 护栏必须在模型**之外**的结构层运行（否则会被注入本身绕过）；② 分层/纵深防御（确定性规则 + 分类器互补）；③ 护栏也需被评测（GuardBench 类基准兴起）；④ 网关化（LiteLLM/AI Gateway 非侵入承载）成为主流架构。

### 5. 代表产品与玩家

- 开源阵营：Guardrails AI、NVIDIA NeMo Guardrails、Meta Purple Llama（Llama Guard / Prompt Guard / Code Shield / LlamaFirewall）、Google ShieldGemma、IBM Granite Guardian、Protect AI LLM Guard。
- 云/平台阵营：Microsoft Azure AI Foundry（Content Safety + Prompt Shields）、AWS Bedrock Guardrails（可被 LiteLLM 调用）、Google Vertex AI / Gemini 安全分类器、Anthropic 内置 classifier + Bedrock/Vertex 渠道治理。
- 网关/编排阵营：LiteLLM、各类 LLM Gateway（把护栏作为 pre/post_call 钩子非侵入挂载）。

## 与相邻主题分工（再强调，避免立题重叠）

- 本文聚焦"**有哪些护栏模式 + 怎么编排**"——把护栏当**可复用设计模式**收口。
- 鉴权/授权/身份/委托 → 见 [[工具调用安全 学习笔记]]、[[智能体身份与信任 学习笔记]]、[[AI Agent 的权限与可撤销委托 学习笔记]]。
- 隔离/沙箱（执行环境层）→ 见 [[AI Agent 沙箱与安全执行环境 学习笔记]]。
- 红队/注入攻防（攻击面视角）→ 见 [[AI 评测红队与对齐 学习笔记]]、[[AI 评测红队 Agent 链路注入 学习笔记]]。
- 高风险动作的人审 UI 长相 → 见 [[Confirmation UI 分级与产品责任边界]]。
- 投毒/供应链 → 见 [[AI 模型供应链安全与开源投毒防护 学习笔记]]。

## 待解问题（留给 Ethon）

- [ ] 对于一个"端侧 OS Agent"，护栏应该跑在端上（隐私/延迟友好）还是云侧网关？端侧能否承载 Llama Guard 级别的分类器？
- [ ] "语义防火墙"把不可信数据与指令结构上分离——在 Android 的 App Intents / 工具调用栈里，这个边界具体落在哪一层工程实现上？
- [ ] 护栏叠加（确定性规则 + 多个分类器）的**延迟预算**怎么定？是否应该像 NeMo IORails 那样强制并行？
- [ ] HITL 闸门与护栏如何配合：哪些护栏失败应"硬拦截"，哪些应"升级人工"（见 [[Confirmation UI 分级与产品责任边界]]），产品责任边界如何划？
- [ ] 护栏策略该不该像代码一样进 Git、做 code review、跑 CI（policy-as-code）？PM 如何参与护栏策略的验收指标定义？
- [ ] GuardBench 这类基准能否直接复用到"产品级护栏验收"，还是只适合模型级评测？

## 附：来源清单

1. NeMo Guardrails 概述与 Colang：https://www.hivebook.wiki/wiki/nemo-guardrails-nvidia-s-programmable-rails-for-llm-apps
2. NeMo Guardrails 实战（FinBot 分层护栏，2026-08）：https://lumienai.com/news/nemo-guardrails-enterprise-ai-safety-developer-guide
3. Guardrails AI RAIL 规范：https://deepwiki.com/guardrails-ai/guardrails/3.2-rail-specifications
4. AI Guardrails 对比 2025（Guardrails AI / NeMo / Llama Guard 哲学差异）：https://www.artificial-intelligence-wiki.com/ai-security/model-safety-and-alignment/guardrails-comparison-2025
5. LiteLLM Guardrails 与网关钩子：https://deepwiki.com/wikiw2025/BerriAIlitellm6915/5.6-guardrails-and-enterprise-features
6. Microsoft Azure Prompt Shields / Content Safety（含 Spotlighting, Build 2025）：https://azure.microsoft.com/en-us/blog/enhance-ai-security-with-azure-prompt-shields-and-azure-ai-content-safety/
7. Microsoft 间接提示注入纵深防御（2025-07）：https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks
8. Meta Purple Llama 组件表（Llama Guard 4 / Prompt Guard 2 / LlamaFirewall / CyberSec Eval 4）：https://aiwiki.ai/wiki/purple_llama
9. Google ShieldGemma 2（图像安全分类器, 2025-03）：https://ai.google.dev/gemma/docs/shieldgemma/model_card_2
10. OWASP LLM Top 10 2025 与护栏映射：https://aisecurityplatform.com/guides/owasp-llm-top-10-explained
11. GuardBench（EU JRC, EMNLP 2024, 40 数据集, 排行榜）：https://code.europa.eu/llm-safety/guardbench
12. IBM Granite Guardian 登顶 GuardBench：https://research.ibm.com/blog/granite-guardian-tops-guardbench
13. Anthropic 护栏实践（Constitutional Classifier / ASL / RSP，第三方梳理）：https://delatorre.ai/claude-ai/

## ⚠️ 待核实清单

- ⚠️ NeMo Guardrails **0.22.0（2026-05-22）** 版本号来自第三方 wiki，非 NVIDIA 官方发布页，需以 PyPI/GitHub release 为准复核。
- ⚠️ Anthropic **Constitutional Classifier 拦截 95% 越狱 vs 未增强 14%** 的数字来自第三方博客（IntuitionLabs），为单源、内部测试口径，未找到 Anthropic 官方一手报告交叉验证，标"待核实"。
- ⚠️ GuardBench 排行榜具体分数（Granite Guardian 86%/85%、NVIDIA/Meta 82%/80%/78%/76%）来自 IBM Research 文章，属厂商自述，需以公开排行榜实时数据复核。
- ⚠️ Google 是否另有"文本版 ShieldGemma 持续更新到 2026"的明确官方口径未逐条核实，本笔记仅确认 ShieldGemma（文本, Gemma 2）与 ShieldGemma 2（图像, Gemma 3, 2025-03）存在。
- ⚠️ OWASP LLM Top 10 2025 与 Agentic AI Top 10（2025-12 发布）为两份清单，本笔记护栏映射主要基于 LLM Top 10 2025，Agentic 专项未展开，待补。

#标签/AIAgent框架 #标签/AI安全 #标签/护栏Guardrail
