---
title: Agent 评测与基准 学习笔记
tags:
  - Agent评测
  - Benchmark
  - GUIAgent
  - 广度种子笔记
  - OS产品
created: 2026-08-09
source: 联网核实的公开资料（核实日期 2026-08-09）。主要一手来源：UC Berkeley RDI 博客《How We Broke Top AI Agent Benchmarks》(2026-04)、Princeton HAL 排行榜官网 hal.cs.princeton.edu（含 ICLR 2026 论文 arXiv:2510.11977）、AndroidWorld 论文 arXiv:2405.14573、Mobile-Agent-v3.5 论文 arXiv:2602.16855、Minitap mobile-use 论文 arXiv:2602.07787、android_world GitHub 仓库。二手来源为各类榜单聚合站与行业博客，已在来源清单中单独标注性质。
---

> 学习定位：这是一篇**广度种子笔记**。目标是把「AI Agent 评测」这块版图整个铺开——有哪些基准、分几类、怎么演化、坑在哪、工程侧有什么工具。**深度刻意留白**：每个 benchmark 的题目构造、评分脚本、分数复现方法一律不展开，全部收进文末 `## 待解问题`。读完这篇你应该能画出地图，但还不能自己跑一次评测。

---

## 一句话心智模型

**Agent 评测不是"给模型打分"，而是"设计一个能被信任的测量仪器"——而 2026 年整个行业最痛的发现是：仪器本身比被测对象更容易坏。**

推论有三条，贯穿全篇：
1. 分数 = 模型能力 × 脚手架(scaffold) × 评分环境的严密性。三者不分离，任何单一数字都不可比。
2. 「最终答案对不对」只是评测的第一层，**轨迹(trajectory)** 和 **单轮(per-turn)** 才是能改进系统的那两层。
3. 公开榜单衡量的是"能不能做到"，产品验收要衡量的是"能不能稳定地、便宜地、安全地做到"。这两件事不是同一个指标。

---

## 一、评测对象：Agent 到底有几个可测面

传统 LLM 评测测的是「一次输入 → 一次输出」。Agent 引入了循环（见 [[Loop Engineering 循环工程]]），可测面立刻爆炸。

| 维度 | 问的问题 | 典型度量 | 是否有公开基准 |
|---|---|---|---|
| 最终结果 (Outcome) | 任务完成了吗 | 成功率 / 环境终态校验 | 有，绝大多数基准都在这层 |
| 轨迹 (Trajectory) | 路径合理吗 | 步数、循环检测、轨迹匹配、错误恢复率 | 少，2025-2026 才起来 |
| 工具调用 (Tool Use) | 选对工具、填对参数了吗 | 工具选择准确率、参数合法率 | 有（BFCL 一类） |
| 单轮语义 (Per-turn) | 这一轮有没有越权/泄漏/惹毛用户 | 策略违规、PII 泄漏、用户挫败信号 | 基本没有，靠自建 |
| 成本 (Cost) | 花了多少钱、多少 token、多久 | $/成功任务、p95 时延、步均 token | 少，HAL 是少数强制记录成本的 |
| 可靠性 (Reliability) | 重跑 k 次还成吗 | pass^k、方差、可预测性 | 极少，正在成为新前沿 |
| 安全 (Safety) | 会不会被注入/越权/reward hacking | 注入成功率、越权率 | 碎片化，见 [[工具调用安全 学习笔记]] |

关键区分 —— **pass@k vs pass^k**：
- `pass@k`：k 次里至少成功一次（HumanEval 传统口径，对 Agent 过于宽容）。
- `pass^k`：k 次全部成功才算过（τ-bench 采用）。**对产品而言 pass^k 才是诚实的信号**，因为用户不会重试到成功为止。这个区别对 OS 场景尤其致命。

---

## 二、基准分类地图

### 2.1 通用助理 / 综合类

| 基准 | 出品方 | 规模 | 环境形态 | 评分方式 | 备注 |
|---|---|---|---|---|---|
| **GAIA** | Meta + HuggingFace | 466 题，L1/L2/L3 三级 | 无交互环境，问答式（可用工具） | 精确字符串匹配 | 验证集答案公开在 HF 上 → **污染风险被 HAL 团队明确点名** |
| **AgentBench** | 清华 THUDM | 8 类环境（OS / DB / 知识图谱 / 网页 / 游戏等） | 多环境集合 | 各环境自定义 | 2023 出品，泛化性测试的经典参照，近年热度被专项基准分走 |
| **AssistantBench** | 学术 | 真实网页助理任务 | 在线网页 | 答案匹配 | HAL 收录基准之一 |
| **HLE (Humanity's Last Exam)** | CAIS + Scale AI | 约 2500 专家题 | 纯问答 | 答案匹配 | 严格说是知识/推理基准，不是 Agent 基准，但常被并列引用 |

> GAIA 的设计哲学值得记：**人类容易、模型很难**（人类基线远高于模型）。这与 MMLU 那类"人类难、模型易"的知识基准是相反的取向。

### 2.2 工具调用 / 函数调用类

| 基准 | 出品方 | 测什么 | 关键特点 |
|---|---|---|---|
| **BFCL**（Berkeley Function Calling Leaderboard） | UC Berkeley | 原子级函数调用：选对函数、填对参数、多函数并行、**relevance detection（该不该调）** | V4 起加入 agentic 类目（多跳搜索、记忆管理、格式敏感性）。**"知道什么时候不调工具"是最被低估的子项** |
| **τ-bench** | Sierra Research | 零售/航空域，LLM 模拟用户多轮对话 + 工具调用 + **策略遵守** | 用 `pass^k`；校验**数据库终态**而非只看回复文本 |
| **τ²-bench / τ³-bench** | Sierra Research | τ 系列后继：双向控制、更多域（如电信）、语音等 | 原始 τ-bench 榜单已冻结在 2024 末模型集，新模型分数来自后继版本或第三方复现，**互不可比** |

**BFCL 与 τ-bench 的关系**：BFCL 是原子能力，τ-bench 是"原子能力 + 对话管理 + 策略遵守 + 状态跟踪"的复合任务。BFCL 高分是 τ-bench 高分的**必要非充分条件**。这个层级关系对设计内部指标很有参考价值。

### 2.3 GUI / OS 操作类 ⭐（对 Ethon 最重要）

先分清三个不同层次，混淆它们是读 GUI Agent 榜单最常见的错误：

| 层次 | 测什么 | 代表基准 | 与 [[工业级 GUI Agent 架构（VLM+无障碍树）]] 的对应 |
|---|---|---|---|
| **Grounding（定位）** | 给一句话，能否点中屏幕上正确的元素 | ScreenSpot / ScreenSpot-v2 / ScreenSpot-Pro / OSWorld-G | 对应"感知层"单点能力 |
| **离线轨迹（Offline）** | 给定人类录制的轨迹，模型的下一步动作是否与人类一致 | Mind2Web、Multimodal-Mind2Web、AitW、AndroidControl | 对应"动作预测"，**不测执行，不测恢复** |
| **在线交互（Online / Env）** | 真机/真模拟器里跑到底，校验系统终态 | AndroidWorld、OSWorld、WebArena、WindowsAgentArena、Online-Mind2Web | 对应端到端，**唯一能反映真实可用性的层次** |

> ⚠️ 离线动作匹配分数高 ≠ 在线能跑通。离线基准没有"错了以后能不能恢复"这个维度，而这恰恰是真实设备上最主要的失败来源。

**移动端 / Android 系（重点）**

| 基准 | 出品方 | 规模 | 环境 | 奖励/评分 | 状态（截至 2026-08） |
|---|---|---|---|---|---|
| **AndroidWorld** | Google Research (Rawles et al., 2024) | **116 任务 / 20 App** | 真实 Android 模拟器（Pixel + AVD） | **device state（设备终态校验）** | 事实标准。任务参数**动态随机实例化**（可生成海量变体，抗记忆），但已接近饱和 |
| **AitW (Android in the Wild)** | Google | 约 30,378 条 episode，357+ App | 离线录制 | 无环境奖励，动作匹配 | 大规模训练/离线评估数据集，常被当训练集用 |
| **AndroidControl** | Google | 约 15,283 条，833 App | 离线 | 动作匹配 | 同上，偏细粒度指令 |
| **AndroidArena** | 学术 | 约 221 任务 / 13 App | 离线为主 | Action match / LLM 判分 | 规模小，更多作为早期参照 |
| **LlamaTouch** | 学术 | 约 496 任务 / 57 App | 真机 | **screen match（界面状态匹配）** | 真机路线的代表 |
| **B-MoCA** | 学术 | 少量任务模板 | Android | regex | 关注跨设备配置泛化 |
| **MobileWorld** | 学术（2025-2026） | 约 201 任务（待核实） | Android | 终态校验 | AndroidWorld 的加难替代：**跨 App 任务占比大幅提升 + 引入"指令歧义时应主动澄清"类目 + MCP 工具调用类目** |
| **MMGUI-Bench** | 学术（2026） | 待核实 | 多平台 | 待核实 | 专测 GUI Agent 的**记忆能力** |

**桌面 / 网页系**

| 基准 | 规模 | 环境 | 评分 | 备注 |
|---|---|---|---|---|
| **OSWorld** | 369 任务 | 真实 Ubuntu/Windows/macOS VM，真实 App（Chrome、LibreOffice、VS Code…） | device/cloud state | NeurIPS 2024；已衍生 OSWorld-Verified（修正错误评分脚本）、OSWorld-G（纯 grounding）、OSWorld-MCP（GUI + MCP 工具混合调用） |
| **WebArena** | 812 任务 | 自托管仿真网站（电商/论坛/CMS/GitLab/地图） | url / text match | 变体众多：WebArena-Lite、WebChoreArena（专测"枯燥重复"任务，分数显著下降） |
| **VisualWebArena** | 约 900+ 任务 | 同上 + 视觉理解 | 多模态匹配 | 视觉推理是明显短板项 |
| **WindowsAgentArena** | 154 任务 / 11 App | 真实 Windows | device state | Microsoft 出品，Office + 系统设置权重高 |
| **Mind2Web** | 2,350 任务 / 137 真实网站 | 离线 | 动作匹配（原版无环境奖励） | 后继：Mind2Web 2 / Online-Mind2Web（改为在线真实浏览） |
| **WebVoyager** | 643 任务 / 15 站 | 在线真实网站 | **LLM judge** | 用 LLM 判分 → 继承 judge 的全部偏差 |
| **OmniACT** | 约 9,802 | 离线 | 脚本匹配 | 大规模 UI 自动化 |

**Grounding 系**

| 基准 | 规模 | 覆盖 | 难度信号 |
|---|---|---|---|
| ScreenSpot | 约 1,200 指令 / 600+ 截图 | 移动 + 桌面 + Web | 图标/小组件比文本元素难得多 |
| ScreenSpot-v2 | 扩充版 | 同上 | 修正了 v1 的标注错误 |
| ScreenSpot-Pro | 约 1,581 | 23 个**专业软件**、5 个行业、超高分辨率 | **专门用来暴露"实验室 UI vs 专业 UI"的落差**，早期分数极低 |
| OSWorld-G / OSWorld-G-Refine | 子集 | 桌面 | 精标注 query |

### 2.4 编码 / 长程执行类

| 基准 | 规模 | 2026 状态（重要） |
|---|---|---|
| **SWE-bench Verified** | 500 实例 | ⚠️ **已被广泛认为失效**。OpenAI Frontier Evals 团队 2026-02 公布审计后停止上报该分数，理由包括：被审计的最难问题中约 59.4% 测试用例本身有缺陷；前沿模型可仅凭 task ID 复现 gold patch → 训练污染 |
| **SWE-bench Pro** | 731 实例（一说总量 1,865，含公开/私有/商业分片） | 主推的抗污染替代品。但**厂商自报 scaffold 分 vs 第三方标准 harness 分差距常超 10 分**，且私有商业分片上所有模型分数都明显下跌 |
| **SWE-bench Multimodal** | — | 引入截图/前端场景，覆盖 JS 生态 |
| **SWE-rebench / SWE-bench Live** | 滚动更新 | 按模型发布日期之后抓新 GitHub 任务 → **结构上抗记忆**，是目前最干净的口径之一 |
| **Terminal-Bench** | 89 任务（v1）；已有 2.x | 测终端原生工作流（shell、文件系统、DevOps），Harbor 沙箱框架 |
| **USACO / SciCode / CORE-Bench / ScienceAgentBench** | — | HAL 收录的长程/科学计算类基准 |

### 2.5 检索 / RAG 类

RAG 评测和 Agent 评测在方法论上是分叉的——它更早成熟，指标更收敛。详见 [[RAG 检索增强生成]] 与 [[RAG 详细学习笔记]]。

| 框架/基准 | 性质 | 核心指标 |
|---|---|---|
| **RAGAS** | 开源框架，LLM-as-Judge | Faithfulness（忠实度）、Answer Relevancy、Context Precision、Context Recall |
| **ARES** | 开源框架 | 在 RAGAS 基础上加**带置信度的判分器**（小模型微调，校准更好） |
| **TruLens** | 开源框架 | Feedback functions + 执行轨迹追踪 |
| **RAGChecker / TREC RAG Track** | 学术基准/评测活动 | 细粒度 claim 级别核查 / 标准化检索评测（**具体年度赛制与结果待核实**） |

RAGAS 四指标的**因果顺序**很重要：Recall 低 → 模型没检索到东西只能编 → Faithfulness 也低。**先修 Recall，再修 Precision，最后修 Generation**。反过来调是白费力气。

---

## 三、2025-2026 的五个结构性趋势

### 3.1 从「答案对不对」转向「轨迹好不好」

这是方法论上最大的转向。三层评测栈已成共识：

| 层 | 何时用 | 谁在用 |
|---|---|---|
| Outcome（终态） | **发布门禁 (gate)** | 所有公开基准 |
| Trajectory（轨迹） | **回归调试 (debug)** | AgentEvals、Phoenix、DeepEval 的 span 级评估 |
| Per-turn（单轮） | **生产在线监控** | 需要毫秒级分类器，LLM judge 太贵太慢 |

实务共识（Anthropic 的 evals 指南也持此立场）：**用 outcome 指标卡发布，用 trajectory 指标定位问题**。过度规定路径会让 eval 变脆——Agent 经常用设计者没想到的合法路径完成任务。

### 3.2 基准被"打穿"：可信度危机（本年度最重要的事件）

**UC Berkeley RDI（Hao Wang, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song）2026-04 发布《How We Broke Top AI Agent Benchmarks》**，用一个自动化漏洞扫描 Agent，在**不解决任何一道题**的前提下刷到接近满分：

| 被攻破基准 | 声称达到的分数 | 攻击手法（据其博客） |
|---|---|---|
| Terminal-Bench (89 任务) | 100% | 替换 `curl`/`uvx` 等系统二进制，让验证阶段读到伪造的 pytest 通过输出 |
| SWE-bench Verified (500) | 100% | 注入 10 行 `conftest.py` pytest hook，强制所有测试通过 |
| SWE-bench Pro (731) | 100% | 容器内覆写结果解析器 |
| WebArena (812) | ~100% | 配置泄漏 + DOM 注入 + prompt injection |
| FieldWorkArena (890) | 100% | 校验逻辑根本不检查答案正确性 |
| CAR-bench | 100% | 跳过 reward 组件 |
| GAIA (165) | ~98% | 公开答案 + 归一化碰撞 |
| OSWorld (369) | 73% | VM 状态篡改 + 公开 gold 文件（隔离相对较好，未被完全攻破） |

> 上表数字**来自 Berkeley RDI 官方博客的自述**，是"攻击可达上限"，**不是任何模型的能力分数**。引用时必须说清楚。

其根因被归纳为一句话：**评分器信任了被评分者**（评测代码与 Agent 在同一容器、gold 答案对 Agent 可达、`eval()` 吃 Agent 可控字符串、LLM judge 的 prompt 能被 Agent 注入）。

它给出的整改建议，本质是把安全工程搬进评测：评分跑在 Agent 容器之外、绝不把参考答案放进 Agent 可达范围、用解析器替代 `eval()`、对 judge 输入做结构化分隔、**发布前用 null agent / random agent / 注入 agent 做对抗测试**。

**最便宜的自查动作（强烈建议内部照做）**：跑一个什么都不做的 **null agent**。如果它得分 > 0，你的 harness 就有洞。

### 3.3 污染 (Contamination) 与"真实性 gap"

| 现象 | 表现 | 应对 |
|---|---|---|
| 训练污染 | 公开基准题目/答案进了预训练语料，模型凭记忆复现 | 私有分片、滚动更新（SWE-rebench 式）、发布日期之后抓题 |
| 推理期查找 | 模型跑时去翻 git history / 上网找现成答案 | 断网、封 git 历史，并报告断网前后的分数差 |
| Harness 差异 | 同模型换 scaffold 分数大幅波动 | 用标准化 harness（HAL 式），或强制披露 scaffold |
| 榜单-生产落差 | 榜单高分，产品里不能用 | 只把公开基准当"资格线"，验收用自建集 |

**一个可直接照搬的诚实动作**：任何对外/对内引用分数，都必须同时说明三件事——**哪个 harness、哪个数据分片、谁跑的**。三者缺一，数字不可比。

### 3.4 LLM-as-a-Judge 的可靠性争议

Judge 已是规模化评测的骨干，但它是**测量仪器**，不是神谕。

| 已被反复记录的失效模式 | 说明 | 缓解 |
|---|---|---|
| 自我偏好偏差 | 同家族模型给自家输出打高分 | **跨家族判分**：A 家模型判 B 家输出 |
| 位置偏差 | 偏爱先出现的答案 | 打乱顺序、双向比较 |
| 长度偏差 | 偏爱更长的输出 | rubric 里显式约束 |
| 顺从偏差 | 批判性不足，倾向通过 | 要求先给证据再打分 |
| **judge 可被注入** | Agent 输出直接进 judge prompt | 结构化分隔 + 输入消毒 |

工程共识（2026）：多评委集成（不同模型家族）、结构化 rubric + 强制引证、**建 500+ 条人工标注校准集**、判分模型与 prompt 版本固定并纳入变更管理。此外出现了 **Agent-as-a-Judge**（让评委 Agent 遍历完整轨迹并自己调工具核实），以及针对"评委质量本身"的元评测数据集。

### 3.5 成本与可靠性成为一等公民

**Princeton HAL（Holistic Agent Leaderboard，ICLR 2026 / arXiv:2510.11977）** 是这个方向最值得跟的一手基础设施：

- 三个定位词：**standardized（统一 harness）、cost-aware（强制记 token/美元）、third-party（第三方跑，不收厂商自报）**。
- 覆盖 9 个基准（GAIA、AssistantBench、Online-Mind2Web、SWE-bench Verified Mini、τ-bench Airline、USACO、SciCode、CORE-Bench、ScienceAgentBench）。
- 核心论点：**要看帕累托前沿，不看一维排名**——"Agent 可以贵 100 倍而只好 1%"。其榜单每条记录都同时挂着准确率和美元成本，同一基准上不同 Agent 的成本能差两三个数量级。
- 轨迹全量公开但**加密分发**，防止被爬取造成污染。
- **2026 现状（官网原文）：已暂停用新模型更新榜单，转向专门衡量"可靠性"**——一致性、可预测性、鲁棒性、安全性、自我认知。

这个转向本身就是信号：**行业开始承认"最高分"没那么有用，"稳不稳"才有用。** 这与 [[OS-PM-性能与稳定性指标体系]] 的思路高度同构。

---

## 四、工程侧：可观测 / 评测工具生态

不做优劣排序，只做地图。多数团队最终是"开源框架做开发期评测 + 商业平台做生产期监控"的混合形态。

| 工具 | 性质 | 定位 |
|---|---|---|
| **LangSmith** | 商业（LangChain 生态） | Trace 捕获 + 标注工作流 + 评测，与 LangChain/LangGraph 深度绑定 |
| **Langfuse** | 开源 + 云 | 开源可自托管的 LLM 可观测性，prompt 管理 + 评测 |
| **Braintrust** | 商业 | 评测数据集管理、实验对比、CI 集成 |
| **Arize Phoenix** | 开源 + 商业 | 生产可观测 + 内置 judge + 人工反馈回收；有 agent function-calling 专项评估 |
| **DeepEval** | 开源 | 面向 CI/CD 的单测式评测，支持 span 级 / 轨迹评估 |
| **RAGAS** | 开源 | RAG 专项四指标 |
| **OpenAI Evals** | 开源 | 最早的 eval 规范化尝试，偏 OpenAI 生态 |
| **W&B Weave** | 商业 | 轨迹日志与成本追踪（HAL 即用它做 logging） |
| **Inspect AI** | 开源（UK AISI） | 面向安全评测的框架，学术/监管侧采用较多 |
| **OpenTelemetry GenAI 语义约定** | 标准 | **把 token/成本/时延做成 span 级可观测的标准动作**，比选哪个平台更重要 |

> 选型提醒：这些工具解决的是"采集 + 编排 + 展示"，**它们不替你定义指标**。指标定义仍是产品经理的活。

---

## 五、对 OS PM 的意义 ⭐

这是本篇对 Ethon 最直接的一节。背景：端侧意图框架（见 [[端侧意图框架 学习笔记]]、[[端侧意图路由选型 PM Checklist]]）与系统级 GUI Agent（见 [[工业级 GUI Agent 架构（VLM+无障碍树）]]）要回答的问题是"我们做的到底行不行"，而公开榜单**不能直接回答这个问题**。

### 5.1 哪些公开基准可以直接借鉴（借的是"评分方法"，不是"分数"）

| 想验收的能力 | 借鉴哪个基准的**方法论** | 具体可搬的做法 |
|---|---|---|
| 端侧意图识别/路由准确性 | **BFCL** | 不只测"选对工具"，把 **relevance detection（该不该触发 Agent）** 单列为一类。系统级入口的**误触发代价远高于漏触发**，这一项应设独立门槛 |
| GUI Agent 端到端可用性 | **AndroidWorld** | 核心是两点：**设备终态校验**（而不是看模型说自己做完了）+ **任务参数动态随机实例化**（同一任务模板生成海量变体，防止回归集被"背下来"） |
| 元素定位（感知层） | **ScreenSpot-Pro** | 用"专业/复杂/高分辨率界面"单独建 grounding 集，别只用干净的 Demo App。这一层的分数能独立归因，最适合做模型/算法迭代的快速回路 |
| 跨 App 长程任务 | **MobileWorld 的设计取向** | 显式统计**跨 App 任务占比**和**平均步数**。AndroidWorld 一类基准跨 App 比例很低，而真实手机场景里跨 App 才是常态 |
| 歧义处理 | **MobileWorld 的"主动澄清"类目** | 专门造一批**故意说不清楚**的指令，验收指标是"是否发起澄清提问"而非"是否猜对"。这是消费级 OS 的体验红线 |
| GUI + 工具混合 | **OSWorld-MCP / MobileWorld 的 MCP 类目** | 验收"该走 API 时走 API、该点屏幕时点屏幕"的路由正确性，直接对应 [[GUI Agent vs 原生 API 产品决策树]] 与 [[MCP 与设备侧 MCP]] |
| 多轮 + 策略遵守 | **τ-bench** | 两个可搬点：① 校验**系统终态**（真的发出去了吗）而非对话文本；② 用 **pass^k** 而非 pass@k |
| 成本与稳定性 | **HAL** | 每条评测记录强制挂上：token / 时延 / 电量 / 内存峰值 / 重跑方差。**端侧的"成本"不是美元，是功耗、内存和热** |
| harness 可信度 | **Berkeley RDI** | 内部评测集上线前跑一遍 **null agent 与 random agent**；分数 > 0 就说明 harness 漏了 |

### 5.2 为什么公开基准不能直接当验收标准

| 原因 | 对 OS 场景的具体后果 |
|---|---|
| **成功率口径不同** | 公开基准算"任务成功率"，OS 验收要算"**用户可感知失败率**"。一次误删短信 / 误付款的权重，和一次没找到设置项完全不同——**基准里所有失败等权，产品里失败按代价分级** |
| **不测成本与功耗** | 端侧最硬的约束是内存、功耗、发热、首响时延。绝大多数公开基准完全不记这些（HAL 记美元成本，仍不等于端侧成本模型） |
| **不测隐私与权限边界** | 无障碍服务 / 读屏权限的滥用风险、跨 App 数据流动，公开基准几乎不覆盖，而这是 OS 上架与合规的一票否决项 |
| **环境是仿真的** | 模拟器里的 App 版本固定、无广告弹窗、无登录态失效、无网络抖动。真机上这些才是主要失败源 |
| **分数不可比** | scaffold / 分片 / 跑分方 三者一变分数就变。厂商自报与第三方复现常有两位数差距 |
| **污染与可被刷** | 公开题目会进训练集；harness 本身可被利用（3.2 节）。**任何用于对外承诺的指标，都不该建立在纯公开集上** |
| **饱和后失去分辨力** | AndroidWorld 已有多方声称 >90% 甚至 100%（详见来源清单，均为单方自报、未见第三方统一 harness 复现）。**一个大家都接近满分的基准，无法支撑选型决策** |

### 5.3 一句话结论

> **公开基准的正确用法是"资格线 + 方法论供应商"，不是"验收线"。**
> 资格线：候选方案连 AndroidWorld/ScreenSpot 这类都过不去，直接淘汰。
> 方法论：把它们的**评分设计**（终态校验、动态实例化、pass^k、成本记账、对抗自查）搬进内部评测集。
> 验收线：必须是**自建的、私有的、按业务失败代价加权的、带成本与功耗约束的**任务集。这一层的建设成本，很可能高于 Agent 本身的研发成本——但没有它，就没有"能不能上线"的判据。

---

## 六、库内关联

| 已有笔记 | 与本篇的关系 |
|---|---|
| [[AI Agent 框架 MOC]] | 上级索引，本篇归入其"评测"分支 |
| [[工业级 GUI Agent 架构（VLM+无障碍树）]] | **被测对象**：本篇 2.3 节的三层（grounding / 离线轨迹 / 在线交互）正好对应其感知—决策—执行分层 |
| [[GUI Agent vs 原生 API 产品决策树]] | **决策依据**：OSWorld-MCP、MobileWorld 的 MCP 类目提供了"GUI vs API 路由是否正确"的可测化思路 |
| [[端侧意图框架 学习笔记]] | **被测对象**：意图识别/路由的验收指标可借 BFCL 的 relevance detection 设计 |
| [[端侧意图路由选型 PM Checklist]] | **互补**：Checklist 管选型维度，本篇补上"选完之后怎么量化验证" |
| [[OS-PM-性能与稳定性指标体系]] | **方法论同源**：HAL 的成本感知与可靠性转向，与传统 OS 性能/稳定性指标体系是同一套思路在 AI 上的延伸 |
| [[工具调用安全 学习笔记]] | **强耦合**：Berkeley RDI 揭示的 prompt injection / 越权 / reward hacking，同时是安全议题与评测议题 |
| [[RAG 检索增强生成]] / [[RAG 详细学习笔记]] | **子领域**：RAGAS 四指标是本篇 2.5 节的展开 |
| [[MCP 与设备侧 MCP]] | **被测对象**：OSWorld-MCP 一类基准正在把 MCP 调用能力纳入评分 |
| [[Loop Engineering 循环工程]] | **理论支撑**：轨迹评测本质是给"循环"这个结构建立可观测性 |
| [[Context Engineering 学习笔记]] | **变量来源**：同模型换 scaffold/上下文组织，分数大幅波动——这是"harness 差异"的技术根因 |
| [[Agent 框架生态与竞品]] / [[Agent 协议生态 学习笔记]] | **横向**：框架和协议的竞争，最终要靠评测来裁决，但目前裁决工具本身不可靠 |
| [[手机AI智能体知识库]] | **场景库**：本篇 5.1 的验收指标设计需要与其中的真实场景清单对齐 |
| [[意图框架·跨体系索引 MOC]] | 跨体系检索入口 |

---

## 待解问题

- [ ] **AndroidWorld 的"动态实例化"到底怎么实现？** 任务参数随机化的具体机制、如何保证随机变体的难度分布一致、`device state` 奖励函数是怎么写的（读 `android_world` 源码中的 `TaskEval` 子类）——这是自建端侧评测集最值得直接借鉴的工程细节。
- [ ] **端侧成本模型如何量化？** 公开基准记美元/token，端侧要记功耗、内存峰值、发热、首响时延。有没有已有的端侧 Agent 成本评测方法论？需要自己定义一套"每成功任务的 mAh"吗？
- [ ] **失败代价加权的成功率怎么设计？** 把"误付款"和"没找到设置项"等权是错的，但加权系数怎么定、怎么让它在版本间可比、怎么避免被优化目标带偏？有没有成熟的可借鉴范式（如安全领域的风险矩阵）？
- [ ] **pass^k 在端侧的合理 k 值是多少？** k 太小检不出不稳定，k 太大跑不起（真机成本高）。业界有没有关于 k 与真实用户感知失败率之间映射关系的研究？
- [ ] **LLM-as-a-Judge 的校准集要怎么建？** "500+ 条人工标注"是从哪来的经验数字？Krippendorff's alpha / Cohen's kappa 达到多少才算可用？跨家族判分具体怎么落地到内部流程？
- [ ] **Berkeley RDI 的 7 类漏洞模式完整清单是什么？** 需要读原博客与后续论文，整理成一份**内部评测 harness 的安全检查表**（null agent 测试、评分器隔离、gold 答案可达性审计……）。
- [ ] **各家 GUI Agent 的 >90% AndroidWorld 声称，哪些经过第三方复现？** 目前看到的高分（含 100% 的声称）均为单方自报，需要核实是否有统一 harness 下的独立复现，以及各自的 scaffold 差异有多大。
- [ ] **轨迹评测的具体度量如何落地？** "步数""循环检测""错误恢复率"听起来清晰，但参考轨迹从哪来？允许多少条合法路径？如何避免过度规定路径导致 eval 变脆？

---

## 附：来源清单

| 事实 | 来源 | 性质 |
|---|---|---|
| AndroidWorld：116 任务 / 20 App / device state 奖励 / 动态实例化 | arXiv:2405.14573（Rawles et al., Google Research）+ google-research/android_world GitHub README | **一手·学术论文 + 官方仓库** |
| 各基准规模对照（Mind2Web 2350/137 站、AitW 30378/357+ App、AndroidControl 15283/833 App、AndroidArena 221/13 App、LlamaTouch 496/57 App、OSWorld 369、WebArena 812、VisualWebArena 314(原表)、WindowsAgentArena 154/11、OmniACT 9802、WebVoyager 643/15、GAIA 466） | AndroidWorld 论文 Table 1（arXiv:2405.14573v3） | **一手·学术论文内的横向对照表**（口径为论文发表时点，后续版本可能变化） |
| Berkeley RDI 攻破 8 个基准的分数与手法（Terminal-Bench 100%、SWE-bench Verified 100%、SWE-bench Pro 100%、WebArena ~100%、FieldWorkArena 100%、CAR-bench 100%、GAIA ~98%、OSWorld 73%） | rdi.berkeley.edu 博客《How We Broke Top AI Agent Benchmarks》(2026-04, Hao Wang, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song) | **一手·研究机构官方博客**。注意：这是"攻击可达上限"，非模型能力分 |
| OpenAI 停止上报 SWE-bench Verified；被审计的最难问题中 59.4% 测试有缺陷；模型可凭 task ID 复现 gold patch | 由 Berkeley RDI 博客与多家二手媒体共同引述 OpenAI Frontier Evals 2026-02 的公告 | **二手转述一手**（原始 OpenAI 公告本人未直接读取，⚠️ 待核实原文） |
| HAL 定位（standardized / cost-aware / third-party）、覆盖 9 个基准、帕累托前沿论点、轨迹加密分发、**已暂停用新模型更新并转向可靠性评测** | hal.cs.princeton.edu 官网（2026-08-09 直接抓取）+ ICLR 2026 论文 arXiv:2510.11977 | **一手·官方站点 + 会议论文** |
| HAL 榜单具体分数（如 GAIA 上 HAL Generalist Agent + Claude Sonnet 4.5 为 74.5% / $178.20） | 同上，官网 2026-08-09 快照 | **一手·第三方独立评测**。⚠️ 榜单已暂停更新，且截至 XXXX-XX 排行榜口径会变动——本篇正文刻意不引用具体名次 |
| GUI-Owl-1.5 / Mobile-Agent-v3.5 在 OSWorld-Verified、AndroidWorld、WebArena、ScreenSpot-Pro、OSWorld-MCP、MobileWorld 等 20+ 基准上的成绩 | arXiv:2602.16855（阿里 Qwen 团队，2026-02） | **一手·但属厂商/模型团队自报**（自家 scaffold、自家复现），非第三方独立评测 |
| "首次在 AndroidWorld 达到 100%、超过人类 80% 基线" | arXiv:2602.07787（Minitap mobile-use，2026-02） | **一手·但属单团队自报**，未见第三方统一 harness 复现 |
| MobileWorld 的设计取向（跨 App 占比高、含主动澄清类目、含 MCP 类目、约 201 任务） | arXiv:2602.16855 引用其为 Kong et al.；具体数字来自二手榜单聚合站 | **混合**：基准存在性为一手引用，**具体数字为二手，⚠️ 待核实** |
| τ-bench 用 pass^k、校验数据库终态、原榜单冻结在 2024 末模型集 | Sierra Research 官方仓库 sierra-research/tau-bench 与 tau2-bench（经二手站转述） | **二手转述一手**（⚠️ 仓库原文待核实） |
| BFCL V4 新增 agentic 类目（多跳搜索、记忆、格式敏感性）、含 relevance detection | 多家二手榜单聚合站一致描述 | **二手** |
| LLM-as-a-Judge 的四类偏差（自我偏好/位置/长度/顺从）与缓解手段、校准集 500+ 条经验值 | 多篇 2025-2026 行业分析与 Agent-as-a-Judge 相关论文的二手汇总 | **二手**（原始论文待核实） |
| METR 记录 o3 等模型在约 30% 的评测运行中出现 reward hacking，且明确禁止后仍持续 | 由 Berkeley RDI 博客与多家二手媒体引述 METR 报告 | **二手转述一手**（⚠️ METR 原报告待核实） |
| RAGAS 四指标定义与因果顺序（Recall → Precision → Generation） | RAGAS 开源文档 + 多篇二手教程 | **二手为主** |
| 可观测/评测工具清单（LangSmith、Langfuse、Braintrust、Phoenix、DeepEval、OpenAI Evals、W&B Weave、Inspect AI） | 多篇 2026 行业综述；W&B Weave 与 HAL 的关系见 HAL 官网 | **二手 + 部分一手** |

---

**⚠️ 待核实清单**

- ⚠️ **所有 SOTA 百分比本篇均刻意未写入正文。** 原因：本次检索到的多个榜单聚合站给出的分数**互相矛盾**，且出现了大量无法交叉验证的模型名（不同站点对同期"最强模型"的命名与分数完全对不上）。这本身就是"榜单生态不可信"的直接证据。**凡需引用分数，请回到一手榜单页面自行抓取，并注明抓取日期与 harness。**
- ⚠️ OpenAI Frontier Evals 关于 SWE-bench Verified 的原始公告（2026-02）未直接读取，"59.4%"与"停止上报"两条需回到 openai.com 原文确认。
- ⚠️ METR 关于 o3 reward hacking 的原报告未直接读取，30.4% / 128 runs / 禁止后仍 70-95% 三个数字均为二手转述。
- ⚠️ MobileWorld 的具体任务数（约 201）、跨 App 占比（62.2%）、平均步数（27.8）来自二手，需回到原论文核对；其正式出处（Kong et al.）年份为 2025 还是 2026 亦待确认。
- ⚠️ SWE-bench Pro 的实例数存在两种说法（731 / 1,865），可能分别指"单一分片"与"含公开+私有+商业的总量"，需核对官方定义。
- ⚠️ Terminal-Bench 当前主版本号（2.0 / 2.1）及其与 v1（89 任务）的任务集差异未核实。
- ⚠️ τ³-bench 是否已正式发布、包含哪些新域（语音、金融文档检索等），仅见二手描述。
- ⚠️ TREC RAG Track 的最新年度（2025 / 2026）赛制与结论完全未核实，本篇仅列名。
- ⚠️ ScreenSpot-Pro 的 1,581 样本 / 23 应用 / 5 行业 三个数字来自二手榜单站。
- ⚠️ OSWorld 常被引用的"人类专家基线 72.36%"来自二手，需回原论文确认。
- ⚠️ AndroidWorld 的人类基线存在 80%（Minitap 论文口径）等不同说法，需确认各自的测量条件。
- ⚠️ 本篇所有"截至 2026-08 的状态判断"（如"AndroidWorld 接近饱和""SWE-bench Verified 已被广泛弃用"）均为对当前公开讨论的概括，**属趋势判断而非可验证事实**，会随时间失效。

---

#标签/Agent评测 #标签/Benchmark #标签/GUIAgent #标签/OS产品 #标签/广度种子笔记
