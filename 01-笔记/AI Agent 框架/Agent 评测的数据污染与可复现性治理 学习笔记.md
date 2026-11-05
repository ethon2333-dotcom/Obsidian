---
title: Agent 评测的数据污染与可复现性治理 学习笔记
tags: [benchmark-contamination, reproducibility, eval-governance, llm-eval, data-contamination, leaderboard-integrity, 广度种子]
created: 2026-10-27
source: 联网核实（WebSearch/WebFetch，2026-10-27；来源见文末清单）；刻意区别于 [[Agent 评测与基准 学习笔记]]（考卷本身）、[[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]]（评测 harness/裁判模型）、[[Agent 离线评估与偏好数据集 学习笔记]]（离线偏好集）
---

# Agent 评测的数据污染与可复现性治理

> [!note] 一句话心智模型
> 评测分数只有在「题没被背过、跑法能复现」两个前提下才是能力证据；数据污染让分数虚高，可复现性危机让分数无法复核——二者共同决定「你能不能信那个数字」。

本篇是 [[AI Agent 框架 MOC]] 下的**广度种子**，聚焦 Agent / LLM 评测的「污染与可复现性治理」这一相邻外辐射面。BREADTH > DEPTH：用表格铺广度，深度盲区留待解问题。

---

## 1. 定义

- **数据污染 / Data Contamination / Test-set Leakage**：基准的测试题、答案、解题步骤出现在模型训练数据中，使模型靠「回忆」而非「能力」拿分，分数被人为抬高（inflation）。可细分为直接（verbatim）、间接（语义近似）、时序（基准发布早于训练 cutoff）三类。
- **可复现性 / Reproducibility**：同一评测在另一时间/环境/配置下重跑，得到一致（或统计可比对）的结果。对 Agent 评测，因链式多次 LLM 调用 + 环境依赖，漂移被逐级放大。

## 2. 分类

### 2.1 污染类型（T1–T4，GEM 2026 综述四层 taxonomy）
| 层级 | 机制 | 代表证据 | 严重度 | 可检测性 |
|---|---|---|---|---|
| T1 Exact | 逐字/近似逐字题目混入训练语料 | MMLU 57% 选项猜中率（GPT-4 TS-Guessing，基线 25%） | 高 | 高 |
| T2 Syntactic | 表面变换后（改写/重排/重分词）仍存在 | MMLU-CF 词汇泄漏；改写微调复现 | 高 | 中 |
| T3 Semantic | 无词汇重叠的语义等价（翻译/复述） | 跨语言/复述膨胀 | 中 | 低 |
| T4 Task-level | 仅暴露题型/推理模式/领域知识 | 零样本题型污染、GSM1K 掉分 | 变 | 极低 |

### 2.2 检测手段（按模型访问权限：白盒→黑盒）
- **白盒**：N-gram overlap（8–13 gram）、embedding 相似度、DICE 层激活模式。
- **灰盒**：Perplexity、Min-K% / Min-K%++（Deng et al. 2024，基于异常 token 概率）、Membership Inference（CDD、ConStat）。
- **黑盒**：输出分布尖锐度、金丝雀串（canary）、Data Contamination Quiz（Golchin & Surdeanu 2024）、LLM 提示探测。

### 2.3 可复现失败点（2026 工程清单）
| 失败点 | 机制 | 治理手段 |
|---|---|---|
| Container drift | 镜像 tag（`:latest`）静默变更 | 按 digest（`sha256:…`）锁镜像 |
| 随机种子 | 未钉 `PYTHONHASHSEED`、temperature≠0 | temperature=0、top_p=1、显式 seed |
| 权重哈希 | 同名 checkpoint 不同权重分数差 | 记录权重 md5/sha |
| 工具版本 | 搜索 API/浏览器/代码 runner 版本漂移 | 锁定 tool 版本与 endpoint |
| 网络/日期 | 评测是否联网、系统当前日期 | 显式决定并钉死日期 |
| 静默重试 | 失败重试走到不同 endpoint 伪装成模型行为 | 只重试 5xx，失败即记 fail |

## 3. 主流方案与工具（广度表）

| 工具 / 方法 | 检测对象 / 作用 | 访问类型 | 成熟度 |
|---|---|---|---|
| N-gram overlap（8–13-gram） | 训练集↔测试集字面重叠 | 白盒（需语料） | 成熟，厂商标配 |
| Perplexity / Min-K% / Min-K%++ | 受污染样本异常低困惑度/概率 | 灰盒 | 成熟，常用 |
| Membership Inference（CDD、ConStat） | 样本/集合级是否在训练集 | 灰盒 | 研究中；实例级近随机 |
| Data Contamination Quiz (DCQ, 2024) | 黑盒探测记忆 | 黑盒 | 可用 |
| LLM Decontaminator (Yang et al. 2023) | embedding + GPT 语义去污 | 白/黑 | 研究中 |
| Canary strings / Watermarking（Sander et al. 2025, Meta FAIR） | 基准发布前水印，统计「放射性」pp-value | 发布侧 | 较新，预印本 |
| Clean-Eval / MMLU-CF (2024–2025) | 无污染基准重建（改写/私有集） | 基准设计 | 成熟/常用 |
| LiveBench / LiveCodeBench (2024–2025) | 滚动刷新、post-cutoff 新题 | 基准设计 | 成熟，常用 |
| JudgeBench / JudgeBiasBench / BabelJudge | LLM-as-judge 偏置审计（位置/长度/自我偏好） | 评测治理 | 2025–2026 活跃 |
| Contamination Transparency Card (CTC, GEM 2026) | 模型发布污染披露规范 | 治理提案 | 2026 提案 |

## 4. 2025–2026 进展（广度表）

| 进展 | 时间 | 要点 |
|---|---|---|
| 《The Leaderboard Illusion》(Singh/Cohere, arXiv 2504.20879) | 2025-04，NeurIPS 2025 D&B | 揭示 Chatbot Arena 私有测试+选择性披露操纵；Llama 4 事件（27 私有变体，仅最优上榜） |
| HuggingFace Open LLM Leaderboard 归档 | 2025-03 | 退场，劝用抗污染替代；v2 用 MMLU-Pro/GPQA 等更硬题 |
| HELM Capabilities 发布（prompt 级可复现） | 2025-03 | Stanford CRFM；HELM（2022 Liang et al.）衍生 HELM Lite/MedHELM/VHELM/HELM Safety |
| SWE-bench Verified 被 OpenAI 弃用 | 2026-02 | 审计 138 难题：59.4% 有测试/描述缺陷 + 前沿模型可逐字复述 gold patch（污染）；推 SWE-bench Pro |
| SWE-bench Pro 自身再被审计 | 2026-07（待核实） | Datacurve 审计称 ~30% 题目根本缺陷、评分器误判（Scale 未确认，待核实） |
| Reliable without Validity (arXiv 2606.19544) | 2026-06 | judge 可靠性（test-retest）与效度（kappa vs 真值）分离度量 |
| 55 篇污染检测系统综述 + CTC 框架 | 2026 (GEM) | 四层 taxonomy；inflation 估计约 6%–40%；指令微调/RL 后训练污染审计为盲区 |
| OTel gen_ai 语义约定 / eval-as-code | 2025–2026 | 可复现性工程底座：trace 可组合、reproducibility manifest、CI 门禁 |

## 5. 代表基准 / 排行榜治理

**抗污染基准设计范式**
- 时序隔离 / 滚动刷新：LiveBench、LiveCodeBench、LatestEval（题源自竞赛/arXiv/新闻，post-cutoff）。
- 私有/加密测试集：HLE（held-out）、SEAL（Scale AI，专家写新题永不公开）、SWE-bench Pro（私有仓库 + GPL 反污染）。
- 无污染重建：MMLU-CF、Clean-Eval、FrontierMath（未公开题）。
- 发布前水印（Sander et al. 2025）：可给「污染 pp-value」，作为分数旁的可信度标签。

**排行榜治理动作**
- HF Open LLM Leaderboard 退场（2025-03）：标志静态榜单饱和/易被 hill-climb，行业转向抗污染榜单。
- LMArena 改革：公开所有提交日志、要求 test 平台模型须限期公开可用（《Leaderboard Illusion》倒逼）。
- HELM 路线：方法/prompt/分项分全公开，作为「可信引用」基准。
- 披露规范：Contamination Transparency Card（CTC）主张每次发布披露「污染制度/clean 子集/Δ=Acc_cont−Acc_clean」。

**可复现性治理落地**
- 锁：Docker digest、PYTHONHASHSEED、model version + weight hash、tool 版本、当前日期。
- 写：eval-as-code（可执行而非散文）+ reproducibility manifest（dataset/model/framework/seed/temperature/env）。
- 报：置信区间而非单点；多次运行报方差；CI 门禁做回归告警。
- 追：OpenTelemetry `gen_ai.*` 语义约定统一 agent eval trace。

## 6. 关键挑战（点到为止）

- **无银弹**：无任何检测方法在 T1–T4 全层级、全访问权限、全训练阶段都可靠（GEM 2026）。
- **语义级污染逃避**：合成数据/蒸馏链路的「概念性模仿」无词汇重叠，token 级方法 F1 仅 0.17–0.49；分层检测可到 0.76（arXiv 2511.17602，2025-11）。
- **指令微调/RL 后训练污染审计**仍是盲区（已 contaminated 模型再 SFT/RL 难追）。
- **LLM-as-judge 自身偏见**：长度偏置（质量持平时偏长）、位置偏置（经典已改善但仍在）、自我偏好（同族 +26pt，2026 llm-judge-bench）；judge 漂移窗口 60–90 天需重校准。
- **排行榜可操纵性**：私有测试、选择性披露、数据不对称（Google 19.2%/OpenAI 20.4% arena 数据 vs 83 开放模型合计 29.7%）属结构性 Goodhart。

---

## 7. 深度盲区（待解问题）

- [ ] 待解问题：能否设计「同时抗 T3/T4 污染又不牺牲可比性」的基准——既能挡语义/任务级泄漏，又保持跨实验室可比、低成本复现？
- [ ] 待解问题：封闭前沿模型在黑盒条件下，是否存在假设自由的可靠污染检测（当前实例级 MIA 近随机，需 held-out 分布先验）？
- [ ] 待解问题：LLM-as-judge 的偏置校准漂移（60–90 天窗口）如何在 CI/监控中自动化告警与重校准？
- [ ] 待解问题：Contamination Transparency Card 能否从提案升级为顶会/厂商发布的强制披露规范，而非自愿？
- [ ] 待解问题：合成数据 / 蒸馏链路导致的「语义级」污染，如何在上游训练管线被阻断而非评测端补救？

---

## 8. 与库内笔记的关联

- 与 [[Agent 评测与基准 学习笔记]] 分工：**那篇讲「考卷本身」（基准地图与可信度危机概览），本篇讲「考卷有没有泄题 + 能不能复现」的治理面**。
- 与 [[Agent 评测自动化与 LLM-as-judge 工程 学习笔记]] 分工：**那篇讲评测 harness/工具链与裁判模型工程，本篇聚焦污染检测 + 可复现性 + 排行榜治理（含 judge 偏置治理）**。
- 与 [[Agent 离线评估与偏好数据集 学习笔记]] 分工：**那篇讲离线评测方法论与偏好数据集，本篇讲污染如何污染这些数据集与评测结论**。
- 与 [[AI Agent 评测的对抗鲁棒性持续监控 学习笔记]] 咬合：**那篇讲线上护栏漂移监控，本篇的 judge 漂移/污染审计可并入其「持续监控」门禁**。

#标签/AI Agent框架 #标签/评测治理 #标签/可复现性

---

## 附：来源清单（联网核实，2026-10-27）

1. Nourbakhsh et al. (2026). *Are LLM Benchmarks Already Contaminated? A Systematic Review of Contamination Detection Methods*. GEM 2026 (Outstanding Paper). ACL Anthology 2026.gem-main.50 — 四层 taxonomy、五检测族、CTC 框架、inflation 6%–40%。
2. Sander et al. (2025, Meta FAIR). *Detecting Benchmark Contamination Through Watermarking*. arXiv:2502.17259 — 水印 + 统计 pp-value。
3. Singh et al. / Cohere Labs (2025). *The Leaderboard Illusion*. arXiv:2504.20879（NeurIPS 2025 D&B）— Arena 操纵。
4. OpenAI (2026-02-23). *Why we no longer evaluate SWE-bench Verified* — 污染 + 59.4% 缺陷审计。
5. White et al. (2024). *LiveBench: A Challenging, Contamination-Free LLM Benchmark*. ICLR 2025.
6. Zhao et al. (2024/2025). *MMLU-CF: A Contamination-free MMLU Benchmark*. ACL 2025. arXiv:2412.15194.
7. Liang et al. (2022). *HELM: Holistic Evaluation of Language Models*. arXiv:2211.09110；HELM Capabilities (2025-03)。
8. Deng et al. (2024, NAACL). *Investigating Data Contamination in Modern Benchmarks*（TS-Guessing）；Golchin & Surdeanu (2024) *Data Contamination Quiz*.
9. Mehta (2025-11). *Hierarchical Contamination Detection for Synthetic Training Data*. arXiv:2511.17602 — 语义级污染逃避现有方法。
10. Spheron (2026) agent benchmarking guide / Cenpie *Agentic AI Field Manual* / PromptLayer / Authensor — 可复现性六失效点、reproducibility manifest、eval-as-code。
11. HuggingFace Open LLM Leaderboard 归档声明（2025-03）；LMArena 回应与改革（news.lmarena.ai）。
12. Reliability without Validity (2026-06, arXiv 2606.19544)；Judging the Judges (2026-04)；llm-judge-bench (2026-05) — judge 偏置与可靠性。

## ⚠️ 待核实清单

- ⚠️ **CLEAN-Bench 确切所指待核实**：联网未找到名为「CLEAN-Bench」、专指 Agent 评测污染的通用基准；已核实的近似物为 *Clean-Eval*（Zhu et al. 2023）与 *Clean Evaluations on Contaminated Visual Language Models*（Lu/Miao/Wai Lam，VLM 方向）。若你指某具体 CLEAN-Bench，请补充链接。
- ⚠️ **SWE-bench Pro 的 2026-07「~30% 缺陷」审计**来自 Datacurve，Scale AI 未确认，数字与归属待核实。
- ⚠️ HELM「进入维护模式（mid-2026）」说法来自二手 wiki，未在一手斯坦福 CRFM 公告中确认，待核实。
- ⚠️ **inflation 6%–40%** 为 GEM 2026 综述按基准/设定汇总的区间估计，非单一权威数字。
- ⚠️ 各排行榜分数、arena 数据占比（19.2%/20.4%/29.7%）来自《Leaderboard Illusion》原稿，LMArena 对部分数字有反驳，使用时注明争议。
- ⚠️ 部分 2026 预印本（arXiv 2606.19544 等）编号形如未来编号，来源为 WebSearch 聚合，正式发表信息待核实。
