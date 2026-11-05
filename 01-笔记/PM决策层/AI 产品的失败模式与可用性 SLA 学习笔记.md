---
title: AI 产品的失败模式与可用性 SLA 学习笔记
tags: [PM, 产品可靠性, SLA, 优雅降级, AI失败模式, 错误预算]
created: 2026-10-15
source: [WebSearch 2026-10-15 ×5：LLM 失败模式分类 / failover·fallback / status page / confidence threshold / 可用性监控 等核实]
---

**AI 功能不像传统功能可定死 SLA：失败模式多样且不可完全消除，产品经理必须用「降级体验 + 可用性承诺 + 错误预算」把不确定性框进可控边界。**

> 心智模型一句话：传统功能「要么工作要么挂」，AI 功能「可能部分错、可能自信地错、可能慢死、可能只在某些区域挂」——所以产品工程的关键是**设计失败时的样子**，而不是假设它不失败。

## 广度覆盖：失败模式 × 可用性 SLA（点到为止）

| 失败模式 | 定义 | 失效机理 | 主流应对方案与代表实践 | 2025-2026 进展 | 关键玩家 |
|---|---|---|---|---|---|
| **幻觉 Hallucination** | 生成看似合理但虚假的事实/引用/数据 | LLM 统计式生成、缺乏真值锚定；罕见事实错误率有理论下界（Kalai et al. 2025，把幻觉建模为二分类误差） | 来源引用（Perplexity 内联编号引用）、RAG 检索校验、claim-level attribution、输出结构化校验 | 顶级模型在 grounded summarization 上幻觉率约 0.7–1.5%（2025，较 2024 的 1–3% 下降，**待核实**）；复杂推理/开放域仍 >33% | OpenAI / Anthropic / Google / Perplexity |
| **拒答 Abstention** | 该答时拒、或不该拒时乱编 | 「I don't know」电路误触发（Anthropic 2025-03 circuit-tracing study：识别到名字但了解甚少时，已知实体特征抑制拒绝、推向编造）；评测奖励猜测而非承认不确定 | 置信度门槛、明确「我不知道」分支、human handoff | 把幻觉拆成 ≥9 类子失败（fabrication/confabulation/omission/retrieval…），工程上按类施策 | Anthropic（可解释性）/ OpenAI |
| **过度自信 Overconfidence** | 高置信地给出错误答案 | 语言自信 ≠ 认知置信；token 概率 ≠ 事实正确（Guo 2017 校准问题；GPT-4 技术报告称后训练反而降低部分基准校准） | 置信度校准（Platt scaling / 直方图分箱映射到真实正确率）、**定性**置信表达（高/中/低，而非「73%」假精度） | 2026 主流实践确立「自主→人在环→ abstain」三态降级范式（OpenAI/Anthropic/Google 部署） | 各前沿实验室 + Twig（阈值校准） |
| **格式崩坏 Format/Schema Drift** | JSON/CSV/Markdown 列错位、schema 不匹配、指令不遵循 | format-dependent reasoning failure：prompt 格式微调即可切换内部子电路（如 Llama-3.1-8B 因格式改变误判 9.11>9.8） | schema 锁定、输出校验、fail-if-mismatch 只重印无效行、provider-specific prompt adapter | 基准审计显示格式/措辞微调可导致 20–40pp 准确率摆动（**待核实**），推动 format-normalization 与自适应格式选择 | LiteLLM / 各网关 |
| **超时 / 长尾延迟 Timeout** | P99 远高于 P50，长请求易超时 | 大模型输出长度差异大，P99 通常是 P50 的 5–20 倍 | 分层延迟 SLA（按输出长度分档）、hedged requests（双发取快）、circuit breaker（连败 2–3 次快速失败） | 推理 SLA 设计从「uptime 百分比」转向「首字延迟 + 生成速率 + 分位延迟」三维监控 | Portkey / LiteLLM / Requesty |
| **服务降级 Degradation** | 「部分可用」：短请求正常、长请求超时；区域性 degraded | GPU 显存不足时非全或无；模型更新时神秘降级；限流峰值 | 优雅降级（返回更短合理响应+「已截断」提示）、多副本冗余、startupProbe 防冷启动流量、语义健康检查（HTTP 200 但空响应也判失败） | 多层告警（P1 错误率突增/P99 超 3× / P2 趋势 / P3 日报）成为标准实践 | 七牛云 / 各推理平台 |
| **地域不可用 Regional Outage** | 单一厂商/区域整体不可达或区域性 degraded | 基础设施事件、部署回滚、算力中心故障 | 多厂商 failover（primary/secondary/tertiary 路由）、多区域/多云、本地开源模型作最后兜底 | 2025-06 多厂商近同时宕机（ChatGPT/Claude/Grok 重叠时段中断，**待核实具体根因**）；IsDown 2025-12 报告显示 Anthropic 20 起 / OpenAI 22 起事件（**第三方监测，待核实**） | OpenAI / Anthropic / Google / Groq / DeepSeek |
| **横切：可用性 SLA / 错误预算** | 给 AI 能力承诺「可用性边界」并量化容错 | 多数 LLM 厂商**不提供** SLA 级 uptime 担保，条款通常排除服务中断责任 | 错误预算（可容忍 downtime 折算）、status page + 事故 webhook 实时告警、写进服务合同的 SLA 边界（统计窗口/排除项/降级如何计可用性） | 共识：单厂商架构不算生产级；多供应商 fallback 成架构刚需；按 70/20/10 预算分摊 primary/secondary/local | 各云平台 + 监控商（IsDown/dataku） |

## 深度盲区（留给 Ethon 自行补充）

- [ ] AI 功能 SLA 到底该不该向用户**承诺准确率**？承诺哪些维度（可用性 / 响应延迟 / 幻觉率上限）才不会变成法律陷阱？
- [ ] **降级体验的信任代价**：频繁触发 fallback/human handoff 会不会让用户觉得「这 AI 不行」、反而比一次错误更伤信任？（需结合 [[AI 产品的信任建立与破灭周期 学习笔记]] 的信任动力学验证）
- [ ] **移动端弱网下的 AI 可用性**：Android 端离线/弱网时 AI 功能如何优雅降级？端侧小模型兜底的质量落差用户能否接受？
- [ ] 错误预算怎么在「AI 功能」上落地？传统 SRE 错误预算是 binary 可用性，AI 的「部分错」如何折算进预算？
- [ ] 置信度门槛的**校准成本**谁来付？小团队没有 holdout 数据做 Platt scaling，阈值设多少是拍脑袋？
- [ ] 跨厂商 fallback 时**输出一致性**如何保证（同一 prompt 不同模型答案微妙不同）？结构化 JSON 抽取类任务尤其脆弱——产品上怎么兜底？

## 与库内笔记的连接（防信息孤岛）

- [[数据飞轮与 AI 产品度量 学习笔记]] —— 失败模式需要度量支撑：幻觉率、采纳率、信任衰减、降级触发率都应是度量体系指标，本文补「失败分类」这一层。
- [[负责任 AI 与 AI 产品伦理落地 学习笔记]] —— 安全拒答、红队发布闸门、过度自信的合规风险，是 RAI 框架在「失败」维度的落地。
- [[AI 产品的信任建立与破灭周期 学习笔记]] —— 降级/handoff 体验直接改写信任曲线；本文的「错误预算/降级代价」是其工程化补充。
- [[AI 产品的用户反馈回路与纠错机制 学习笔记]] —— 失败收集、👎/自然语言纠错是「失败 → 改进」闭环的关键输入。
- [[AI 产品的渐进式披露与可纠正性 UX 学习笔记]] —— 降级时「能力由浅入深 + 可撤销/可纠正」是避免死路的 UX 底座。
- [[AI 产品的可解释性 UX 与归因展示 学习笔记]] —— 置信度表达、来源引用范式是「过度自信/幻觉」的前端呈现解。

## 附：来源清单

1. Writingmate.ai《Can AI Chatbots Make Mistakes? How to Avoid them in 2025?》—— 失败模式清单（幻觉/上下文丢失/指令不遵循/逻辑错误等）。
2. dev.to Victor Amit《Why LLMs Fall for Manipulation?》—— Kalai et al. 2025（幻觉=分类误差、错误率下界）、Anthropic 2025-03 电路研究（「我不知道」误触发）、Guo 2017 校准、置信度≠准确率。
3. EmergentMind「Format-Dependent Reasoning Failure」—— 格式依赖推理失败、prompt 格式切换子电路。
4. techwalker《Patronus AI TRAIL 评估体系》（148 案例错误分类：推理/系统执行/规划协调）—— 89% 错误率数字**待核实**。
5. PitchAvatar《Why AI makes mistakes》—— 引用 BBC/EBU 2025（约 45% 新闻查询出错）、Columbia（引用新闻 >60% 自信错误），数字**待核实**。
6. TheNeuralBase「Uptime and reliability history」（2026-04 校验）—— 多数 LLM 厂商无 SLA 级 uptime 担保、多厂商 fallback 刚需。
7. AI/TLDR《LLM Provider Outages: Fallbacks and Multi-Provider Failover》—— LiteLLM/Portkey/Requesty 工具、typed fallback、hedged requests、语义健康检查。
8. 七牛云博客《破局高可用：大模型服务 SLA 保障与多模型无缝切换架构实践》—— 统一网关、智能路由、降级。
9. CSDN《大模型推理服务的 SLA 设计》—— P99=P50 的 5–20 倍、三层告警、SLA 写进合同。
10. HuggingFace 事故响应片段 —— 10 分钟决策阈值、provider status page 滞后、质量漂移检测。
11. IsDown《LLM Providers Status Report – December 2025》(2026-01-22) —— Anthropic 20 / OpenAI 22 起事件统计，**第三方监测，待核实**。
12. dataku.ai《AI API uptime in H1 2025》—— 15 家厂商 uptime 排名（Anthropic 99.72% 等），**第三方监测，待核实**。
13. China Daily HK《Major US AI platforms hit by near-simultaneous outages》(2025-01) —— 2025-06 ChatGPT/Claude/Grok 近同时宕机事件。
14. Clearly Design《Designing for AI failures》(2026) —— Confidence Cascade、优雅降级层级、失败态 UI 模式。
15. Twig《How to Set a Confidence Threshold》—— 分主题阈值、阈值校准、优雅升级到人工。
16. Imversion《AI Fallback Strategies 2026》—— 规则/重试/拒绝+人工/handoff/降级 选型与排序。
17. Horizon Labs / TheNeuralBase「Quality UX for imperfect AI」—— 三态降级范式、confidence≠accuracy、EU AI Act 可解释日志要求。

## ⚠️ 待核实清单

- [ ] Patronus TRAIL 报告的「AI 代理错误率高达 89%」—— 单一研究、任务分布未知，未交叉验证。
- [ ] BBC/EBU 2025「约 45% AI 新闻查询出错」、Columbia「引用新闻 >60% 自信错误」—— 媒体口径，样本与定义未公开。
- [ ] 各厂商 uptime 百分比（Anthropic 99.72% / OpenAI 99.31% / Google 99.14% 等）—— 来自 dataku 第三方 5 分钟轮询，非官方 SLA，且监测口径可能偏差。
- [ ] IsDown 2025-12 事件计数（Anthropic 20 起 / OpenAI 22 起）—— 第三方聚合，厂商自报口径不一。
- [ ] 2025-06 多厂商近同时宕机的**共同根因**—— 公开信息未确认 ChatGPT/Claude/Grok 是否同源。
- [ ] 「顶级模型 grounded summarization 幻觉率 0.7–1.5%（2025）」趋势数字 —— 来自博客汇总，缺原始基准出处。
- [ ] 格式微调导致「20–40pp 准确率摆动」—— 来自基准审计研究，需看具体基准与模型。

#标签/PM #标签/产品可靠性 #标签/SLA
