---
title: AI 编程助手的代码安全评测基准 学习笔记
tags: [code-security, eval-benchmark, ai-coding, copilot, breadth-seed, cybersecurity, llm-security]
created: 2026-10-27
source: 联网核实（WebSearch / WebFetch，2026-10-27），详见文末「附：来源清单」；媒体口径与未定数字均标「待核实」
---

# AI 编程助手的代码安全评测基准 学习笔记

> [!abstract] 一句话心智模型
> 代码安全评测基准 = 给 AI 编程助手/Copilot 类工具出"安全考卷"，量化它们**生成含漏洞代码的比例、修复漏洞的准确率、被代码内提示注入劫持的概率、以及许可证合规风险**——但 2022-2026 年已诞生 13+ 套基准，彼此**不可比**，所以"AI 代码是否更安全了"至今没有统一答案。

> 本篇聚焦「**怎么测 / 有哪些基准**」，与 [[AI 编程助手的代码安全责任 学习笔记]]（聚焦「**谁负责 / 责任归属**」）刻意互补；并交接 [[自主编程 Agent 的安全评测基准 学习笔记]]（agent 自主执行视角）与 [[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]（工具谱系）。

---

## 一、定义与心智边界

**代码安全评测基准（Code Security Evaluation Benchmark）**：一套标准化的任务集 + 评分 oracle，用于衡量代码生成式 LLM / Copilot / 自主 coding agent 在安全维度的表现。

- 考"生成安全代码的能力"（defensive）：少生成漏洞、能修漏洞。
- 考"被滥用的风险"（adversarial）：会不会被诱导写恶意代码、被提示注入劫持。
- 关键区分：**不安全代码补全率（insecure output rate）** ≠ **功能正确率**。同一份代码可以编译通过、单测全绿，却仍可一键被注入（Veracode 2025/2026 反复验证）。

---

## 二、分类（广度扫览）

### 2.1 按评测对象（生成单元）

| 生成单元 | 说明 | 代表基准 |
|---|---|---|
| 代码片段 / 函数体 | 单轮补全或 text-to-code | SecurityEval、LLMSecEval、SALLM、CodeSecEval |
| 整应用 / 仓库 | agent 从规格搭出完整后端 | BaxBench、SecRepoBench、SusViBes、RealSec-bench(2026) |
| 多轮 / agentic | 多步交互、工具调用 | MT-Sec、DualGauge、SecureAgentBench |

### 2.2 按评测维度（核心指标）

| 维度 | 含义 | 代表基准 / 研究 |
|---|---|---|
| **不安全代码补全率** Insecure code completion rate | 生成代码含 ≥1 个可利用漏洞（映射到 CWE/OWASP）的比例 | CyberSecEval 全系、SecurityEval、SALLM |
| **漏洞修复准确率** Vulnerability repair | 能否正确修复已知漏洞且不引入回归 | AutoPatchBench(CyberSecEval4)、PatchEval(2025)、`VulnFix-bench`（名称/状态待核实） |
| **代码中的提示注入** Prompt-injection-in-code | 通过文档/依赖/PR 内容注入指令劫持 coding agent | CyberSecEval 2+（26%–41% 成功率） |
| **许可证合规** License compliance | 生成代码是否携带 copyleft/受限许可或逐字复现训练数据 | LicoEval（相似度，非纯合规，专门基准名称待核实） |
| **包幻觉** Package hallucination | 推荐不存在的依赖（slopsquatting） | Spracklen et al. USENIX Security 2025（19.7% 推荐包不存在） |
| **代码克隆/重复** | 生成克隆放大已知缺陷 | GitClear 2025/2026（克隆 +8x / +81%） |

### 2.3 按评分 oracle

- **静态扫描**（Bandit / CodeQL / Semgrep 规则）：快但误报/漏报，难抓逻辑级漏洞。
- **动态执行 + 安全测试 / 真实 exploit**：更精确（SecCodePLT、BaxBench 用 CVE-patch exploit）。
- **LLM-as-judge**：抓静态漏掉的逻辑问题，但依赖裁判模型能力（CyberSecEval 2+ 用 judge LLM）。
- 现实结论：**传统 pattern-based SAST 仅抓到 AI agent 漏洞的 ~12%，contextual 工具 ~88%**（DryRun Security 2026 实测）——这是深度盲区。

---

## 三、主流基准速查表

| 基准 | 发布方 | 评测内容 | 年份 |
|---|---|---|---|
| **CyberSecEval**（v1→v4） | Meta（Purple Llama，开源 MIT） | 不安全代码补全 + 网络攻击协助 + 提示注入 + 代码解释器滥用 +（v4）自动补丁 AutoPatchBench | 2023–2025 |
| **SecurityEval** | 学术（arXiv:2210.09263） | 121 条 Python prompt，覆盖 69 个 CWE | 2022 |
| **LLMSecEval** | MSR 2023（arXiv 待核实编号） | 150 条自然语言需求→安全代码，安全单测+功能单测双判 | 2023 |
| **SALLM** | ASEW'24（arXiv:2311.00889） | 100 条安全相关 Python prompt，首创 `vulnerable@k`/`secure@k` 指标 | 2024 |
| **SVEN** | ICSE 2024（arXiv:2302.05319） | C/Python 的 CodeQL 标注 vuln/safe 最小差异配对，安全加固与对抗测试 | 2024 |
| **CodeSecEval** | 学术（arXiv:2407.02395） | 基于 CWE 的安全代码生成评测 harness | 2024 |
| **SecCodePLT** | UCSB/VirtueAI（arXiv:2410.11096；NeurIPS 2025） | >5.9k 样本、44 个 CWE 类、Python/C/C++/Java，动态可执行评测（含端到端攻击） | 2024（v1）/ 2025 正式 |
| **BaxBench** | ETH Zurich（arXiv:2502.11844） | 392 个后端任务，端到端功能+exploit 验证 | 2025 |
| **CWEval** | 学术（arXiv:2501.08200） | 结果驱动的"功能+安全"联合评测 | 2025 |
| **SecRepoBench** | 学术（arXiv:2504.21205） | 仓库级安全编码，318 任务 / 27 仓库 | 2025 |
| **RealSec-bench** | 学术 | 仓库级，静态+LLM-vote 功能判分 | 2026（待核实细节） |
| **Veracode GenAI Code Security Report** | Veracode（行业基准，非学术） | 80 安全任务×100+ LLM，OWASP Top 10 失败率 | 2025 / 2026 |

> 完整 13 套基准脉络见 *The Weather Report*「Thirteen Yardsticks, No Ruler」(2026) 的横向对比表（2022–2026）。

---

## 四、2025-2026 进展速查表

| 时间 | 事件 / 数字 | 含义 |
|---|---|---|
| 2025-07 | Veracode 2025：100+ 模型、45% 样本失败 OWASP 检查；Java 72%、XSS 防御失败 86%、日志注入 88% | 功能准确率大涨，安全没跟上 |
| 2025-02 | BaxBench：当时最佳模型 62% 方案"错误或含漏洞"（非纯不安全） | 常被误传为"62% 有漏洞" |
| 2025-04 | CyberSecEval 4（随 Llama 4）：新增 AutoPatchBench，测 C/C++ 自动修漏洞 | 基准从"会不会作恶"转向"能不能修" |
| 2025 | SecCodePLT 收编进 NeurIPS 38；USENIX Security 2025 包幻觉 19.7% | 动态评测、供应链风险成主线 |
| 2026-07 | Veracode 2026：仍 44% 失败；最佳模型通过率 68%，多数 50–53%；XSS 通过率仅 15% | 更大更新的模型**并未**更安全 |
| 2026-03 | DryRun Security：Claude Code / Codex / Gemini 搭的 30 个 PR 中 87% 含 ≥1 漏洞；传统 SAST 仅抓 12% | agent 引入新型逻辑级漏洞 |
| 2026 | RealSec-bench 等仓库级基准出现；Cloud Security Alliance：74 个 CVE 归因 AI 编码工具（下限值，待核实） | 视角从 snippet 升到 repo/产品级 |

---

## 五、代表研究与工具（点到为止）

- **奠基性学术测量**：Pearce et al.（IEEE S&P 2022）Copilot 1698 程序 ~40% 含漏洞；Perry et al.（CCS 2023）有 AI 助手者写出的代码更不安全且更自信（SQL 注入 36% vs 7%）。
- **行业红队/实测**：Veracode 年报、GitClear（克隆/可维护性）、Apiiro（Fortune 50 遥测：AI 提交 3–4x、安全发现 10x）、OWASP AISVS Appendix C。
- **评测/护栏工具**：Meta Code Shield（推理时过滤不安全代码，MIT）、GitHub CodeQL/Code Review、Semgrep Multimodal(2026)、DryRun Security、Endor Labs、Aegis（AI 代码专用）。
- **基准聚合**：Hugging Face `FrontierAICybersecurity` 网络安全排行榜（含 CyberSecEval-3、SecCodePLT、RedCode 等横向数据）。

---

## 六、关键挑战（广度，不展开）

1. **基准不可比（核心痛点）**：13 套基准在任务来源、生成单元、交互模式、oracle 上彼此错位，分数"既不能比、也不连续"——无法回答"AI 代码是否逐年更安全"（The Weather Report 2026）。
2. **基准滞后于真实漏洞**：任务多来自历史 CWE/手工 prompt，真实 0-day 与新型 agent 逻辑漏洞（broken access control、OAuth 缺陷）难覆盖。
3. **语言/场景覆盖不均**：早期偏 Python；Java/C/C++/多语言与"整应用/仓库级"覆盖仍薄弱。
4. **oracle 决定"安全"定义**：静态扫描、exploit、LLM-judge 对同一段代码可给出相反结论。
5. **"规模 vs 质量"权衡**：手工高质量但不可扩展，自动生成则引入不相关样本（SecCodePLT 用"专家种子+LLM 变异+验证"试图平衡）。

---

## 七、深度盲区（本篇未展开，待解）

- [ ] 待解问题：是否存在**跨年份、跨模型、方法学对齐**的连续基准，能真正追踪"AI 代码安全性随时间的变化"？（目前只有一次性快照）
- [ ] 待解问题：**许可证合规（license compliance）** 是否有与代码安全同等严谨的专门基准？目前多为合规评分卡/相似度（LicoEval），缺可执行判定（待核实）。
- [ ] 待解问题：agent 引入的**逻辑级 / 业务级漏洞**（非 CWE 模式匹配类）如何用自动化 oracle 稳定检测？传统 SAST 仅 12% 覆盖率。
- [ ] 待解问题：**包幻觉 / slopsquatting**（19.7% 推荐包不存在）应否纳入代码安全评测的强制维度？目前是独立研究方向。
- [ ] 待解问题：`VulnFix-bench`、`Project SEED` 等是否为已发布独立基准，还是内部/未公开数据集？（本文未能核实，标待核实）

---

## 八、库内关联

- 责任归属互补：[[AI 编程助手的代码安全责任 学习笔记]]
- 自主 Agent 评测视角：[[自主编程 Agent 的安全评测基准 学习笔记]]
- 工具谱系背景：[[AI 编程助手与 Agentic Coding 工具生态 学习笔记]]
- 评价工程化落地（Eval-as-Code / CI 门禁）可交接：[[开发者态 Agent 评测与 CI 集成 学习笔记]]

---

## 附：来源清单

1. Meta Purple Llama CyberSecEval 系列（v1 2023-12 / v2 2024-04 / v3 arXiv:2408.01605 / v4 2025-04）+ Code Shield — https://github.com/meta-llama/PurpleLlama
2. CyberSecEval 2 论文 arXiv:2404.13161；CyberSecEval 3 arXiv:2408.01605
3. SecurityEval arXiv:2210.09263；LLMSecEval（MSR 2023）；SALLM arXiv:2311.00889（ASEW'24）
4. SVEN arXiv:2302.05319（ICSE 2024）；CodeSecEval arXiv:2407.02395
5. SecCodePLT arXiv:2410.11096（NeurIPS 2025）；仓库 https://github.com/ucsb-mlsec/SecCodePLT
6. BaxBench arXiv:2502.11844（ETH Zurich, 2025）；CWEval arXiv:2501.08200；SecRepoBench arXiv:2504.21205
7. Veracode《2025 / 2026 GenAI Code Security Report》（07-2025 / 07-2026）
8. Pearce et al. "Asleep at the Keyboard?" IEEE S&P 2022；Perry et al. CCS 2023
9. Spracklen et al. "We Have a Package for You!" USENIX Security 2025（包幻觉 19.7%）
10. GitClear "AI Copilot Code Quality" 2025 / "The Maintainability Gap" 2026
11. Apiiro "4x Velocity, 10x Vulnerabilities" 2025；DryRun Security AI Coding Agent 测试 2026-03
12. OWASP AISVS Appendix C: AI-Assisted Secure Coding — https://github.com/owasp/aisvs
13. The Weather Report "Thirteen Yardsticks, No Ruler" 2026（13 套基准横向对比）
14. Awesome-AI-Security-Benchmarks（GitHub 汇总列表）；Hugging Face FrontierAICybersecurity 排行榜
15. Cloud Security Alliance "Vibe Coding's Security Debt" 2026-04（74 AI 归因 CVE，下限值）

---

## ⚠️ 待核实清单

- `VulnFix-bench`、`Project SEED` 是否为已公开发布的独立基准（未能核实，疑似内部/未公开数据集）。
- **许可证合规**维度的专门基准名称与年份（现有公开资料多为合规评分卡/相似度研究，未找到与代码安全同严谨度的可执行基准）。
- `RealSec-bench`(2026)、`SusViBes`(2025)、`DualGauge`(2025) 的具体任务规模与评分方法（仅见汇总表，未逐篇核实原文）。
- Cloud Security Alliance 所列 74 个 AI 归因 CVE 为**下限值**（研究者自陈检测盲点，非比例）。
- 各厂商/模型的精确不安全率数字随测试集、oracle、年份剧烈波动，引用时务必标注来源与口径，勿跨基准直接比较。

#标签/效率工具 #标签/代码安全 #标签/评测基准
