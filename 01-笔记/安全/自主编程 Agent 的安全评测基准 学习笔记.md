---
title: 自主编程 Agent 的安全评测基准 学习笔记
tags: [安全, AI编程安全, 安全评测基准, 代码安全, 广度种子]
created: 2026-10-07
source: WebSearch/WebFetch 核实（Meta CyberSecEval 系列、Frontier AI Cybersecurity Observatory、SecureAgentBench、SUSVIBES/Agent Security League、MITRE ATLAS、ART/Gray Swan、AIShellJack 等，2025-2026）
---

# 自主编程 Agent 的安全评测基准 学习笔记

> 心智模型：当 AI 从"补全一行代码"升级为"自主改多文件、跑命令、发 PR"，**评测焦点从"模型会不会写漏洞"转向"Agent 在真实工作流里会不会产出可被利用的、含新漏洞的代码，以及是否被注入劫持"**——基准 = 给这一风险面一把可比较的尺。

本文刻意区别于 [[AI 编程助手的代码安全责任 学习笔记]]（责任归属维度：责任边界 / 生成代码漏洞 / 侵权 / 护栏审查），本文只谈**评测基准与方法学**。相关执行侧见 [[AI Agent 沙箱与安全执行环境 学习笔记]]，红队方法学见 [[AI 评测红队与对齐 学习笔记]] 与 [[AI 评测红队 Agent 链路注入 学习笔记]]，工具鉴权见 [[工具调用安全 学习笔记]]。

## 一、广度覆盖：核心表格

### 1.1 定义与边界
| 维度 | 说明 |
| --- | --- |
| 安全评测基准（benchmark） | 用固定任务集 + 评分器（oracle）量化"AI/代码是否不安全"的可复现测量工具；oracle 可为静态扫描(Bandit/CodeQL)、动态执行(PoC exploit)、LLM-judge |
| 自主编程 Agent | LLM 驱动的、可自主生成/编辑/执行代码并交互工具（terminal、git、PR）的系统，如 SWE-agent / OpenHands / Aider / Cursor / Claude Code |
| 区别于"责任"与"执行隔离" | 责任讲谁背锅（见 [[AI 编程助手的代码安全责任 学习笔记]]），隔离讲代码在哪跑（见 [[AI Agent 沙箱与安全执行环境 学习笔记]]）；本文只测"安不安全、怎么测" |
| 关键演化轴 | 任务来源(手搓CWE→真实CVE仓库) · 生成单元(片段→函数→整应用→仓库) · 交互(单次补全→多轮→自主Agent) · oracle(静态→动态exploit→LLM-judge) |

### 1.2 评测分类（按"被测对象 / 风险面"）
| 类别 | 测什么 | 代表基准 |
| --- | --- | --- |
| 不安全代码生成（Secure Code Gen） | 模型/ Agent 产出代码是否含已知 CWE | SecurityEval、LLMSecEval、CyberSecEval、CodeSecEval、CWEval、SafeGenBench、SecRepoBench |
| 仓库级 / Agent 安全生成 | 多文件编辑、真实漏洞引入点、是否引入新漏洞 | SecureAgentBench、SUSVIBES、BaxBench、DualGauge、SEC-bench、A.S.E |
| 漏洞检测 / 修复能力 | 模型能否发现/修补真实 CVE | PrimeVul、VulnLLMEval、AutoPatchBench(CyberSecEval4)、CVE-Bench、VulnRepairEval |
| 自主攻击能力（offensive uplift） | 模型能否助长真实攻击（钓鱼/CTF/勒索） | CyberSecEval 3、CyBench、NYU CTF Bench、RedCode |
| Agent 红队 / 注入劫持 | 提示注入、工具投毒、越权命令、数据泄露 | AgentDojo、AgentHarm、ART、AIShellJack、WAInjectBench |
| 安全门禁 / CI 卡点（方法论，非基准） | 把评测落到发布闸门：pre-commit→pre-merge→pre-deploy | AI-SDLC Safety Framework、Cisco Project CodeGuard、NIST SSDF SP 800-218 |

### 1.3 主流评测基准与工具（精选）
| 基准 / 工具 | 机构 | 形态 | 关键设计 |
| --- | --- | --- | --- |
| **CyberSecEval 1/2/3/4** | Meta (Purple Llama) | 开源套件 | C3 评 8 类风险；C4 新增 AutoPatchBench(自动补洞)、CyberSOCEval(威胁情报推理)；配套 Code Shield/ Prompt Guard |
| **SecurityEval** | 2022 | 数据集 | 121 条 prompt，覆盖 75 类 Python 漏洞 |
| **LLMSecEval** | 2023 | 数据集 | 150 条 prompt，映射 Top-25 CWE，配 CodeQL 评分 |
| **CodeSecEval** | 2024 (arXiv:2407.02395) | Harness | 同时给安全/不安全参考实现 + 测试预言，发现"功能过但安全不过" |
| **SecCodePLT** | 2024 (arXiv:2410.11096) | 平台 | 统一评代码 GenAI 风险，27 个 CWE，含 5 步攻击任务 |
| **CWEval** | 2025 (arXiv:2501.08200) | Harness | 动态预言，同时评功能与安全 |
| **SecRepoBench** | 2025 (arXiv:2504.21205) | 数据集 | 27 个真实仓库级安全编码任务 |
| **SafeGenBench** | 2025 (arXiv:2506.05692) | 数据集 | 字节跳动，558 道安全敏感题，覆盖漏洞分类法 |
| **SecureAgentBench** | 2025 (arXiv:2509.22097) | 环境 | 105 任务，真实漏洞引入点(VIC)，功能测试+PoC+静态；测 SWE-agent/OpenHands/Aider |
| **SUSVIBES / Agent Security League** | Endor Labs 等 | 基准+报告 | FuncPass/SecPass 双指标；Agent 只看"功能对且安全对"的解 |
| **AgentDojo** | ICLR 2025 | 基准 | 629 条安全用例，工具输出注入；银行/工作流套件 |
| **AgentHarm** | ICLR 2025 | 基准 | 110 条恶意 Agent 任务，评"越狱后是否仍能干坏事" |
| **ART (Agent Red Teaming)** | Gray Swan + UK AISI | 竞赛→基准 | 4700 条高质量攻击 prompt 持久榜 |
| **AIShellJack** | 2025 (arXiv:2509.22040) | 攻击框架 | 314 条 payload、70 个 MITRE ATT&CK 技术，测 Cursor/Copilot 注入执行命令 |

### 1.4 2025-2026 进展（要点，媒体数字见文末待核实清单）
| 进展 | 要点 |
| --- | --- |
| "13 把尺、没有一把能对齐" | 综述(The Weather Report, 2025)指出 2022-2026 至少 13 个安全代码生成基准，因任务源/单元/交互/oracle 各不相同，分数不可比、不可纵向追踪；呼吁"连续可比基准" |
| Agent 比补全更危险 | 多项研究发现：自主 Agent 生成的完整应用/补丁"功能正确但含漏洞"比例显著高于补全工具；SUSVIBES/Agent Security League 报告"功能正确的解里 >80% 仍含漏洞" **待核实（厂商报告口径）** |
| 简单安全提示无效 | SecureAgentBench：给 Agent 显式安全指令并未显著提升"正确且安全"率，有时反而拉低功能正确性 |
| MITRE ATLAS 纳入 Agent | 2025-10 新增 14 个 agentic 技术（如 AI Agent 工具调用外泄、RAG DB 注入、记忆篡改、Agent 上下文投毒）；v5.1.0(2025-11) 达 16 战术/84 技术 |
| 红队实测普遍失守 | ART 竞赛(2025-03~04)：近 2000 人 / 180 万次攻击 / 6.2 万次成功，22 个模型"每个至少失败一次"；间接注入(27.1%)远强于直接(5.7%) **待核实（竞赛口径，非独立复现）** |
| 编码编辑器被远程劫持 | "Your AI, My Shell"(arXiv:2509.22040)：污染外部开发资源即可让 Cursor/Copilot 执行恶意命令，ASR 最高 84% **待核实（单一研究，未跨全版本复现）** |

### 1.5 代表研究 / 产品实践
| 实践 | 要点 |
| --- | --- |
| **AI-SDLC Safety Framework (ASSF)** | 把 AI 代码当"低信任输入"：分级信任(T1未验证/T2已扫/T3人工背书) + 强制验证闸门(pre-commit 静态/密钥/依赖 → pre-merge SAST/DAST → pre-deploy 集成/回归/SBOM) + 溯源追踪 + 回滚 |
| **Cisco Project CodeGuard (2025)** | 开源，基于 OWASP/CWE 的 AI 代码安全规则，给 Cursor/Windsurf/Copilot 用 |
| **NIST SSDF SP 800-218** | 软件供应链安全实践基线，可落地为 AI 代码策略即代码(policy-as-code)闸门 |
| **CI 安全门禁范式** | 在 PR 流水线跑 SAST( Semgrep/CodeQL )+ 密钥扫描(Gitleaks)+ 依赖扫描(Snyk/SCA)，失败即阻断合并；IDE 实时扫描(ASCA)收紧反馈环 |
| **OpenSSF / Sigstore** | 模型签名与 AI 代码来源(attestation)规范，属"闸门"的上游溯源 |

## 二、BREADTH > DEPTH：点到为止的留白

- 评测本质是"oracle 决定 secure 的定义"：静态扫描只认模式，exploit 只认真崩，LLM-judge 认语义——同一代码三种结论可并存。
- "功能正确且安全"才是发布标准；仅功能过 ≠ 可发布（见 SUSVIBES 的 SecPass 远低于 FuncPass）。
- 安全门禁 = 把评测落到**发布阻塞点**；基准分数属"选型阶段"，扫描输出属"发布闸门"，二者不可互替。
- Agent 红队要映射到 MITRE ATLAS 技术 ID，产出才可被合规/整改直接消费。

### 待解问题（留给 Ethon 补充）
- [ ] 库内是否需要一个"连续可比"的 AI 代码安全追踪面板（而非一次性基准）？与 PM 决策如何挂钩？
- [ ] SecPass 这类"正确且安全"率，作为 Android OS 发布卡点 SLA 的阈值该设多少（参考行业但需自定）？
- [ ] AIShellJack 证明编辑器可被远程劫持——Android 开发机/CI  runner 的等效威胁面与现有 [[AI Agent 沙箱与安全执行环境 学习笔记]] 覆盖是否够？
- [ ] 间接提示注入致代码泄露（arXiv:2506.01055 银行 Agent 15-50% 效用降）在"代码 Agent 泄露密钥/源码"场景是否已有对应基准？
- [ ] 国产模型/工具（如文心/通义/腾讯工蜂）在 CyberSecEval / SecureAgentBench 上的表现是否有公开数据？
- [ ] 护栏有效性如何评测：Code Shield / Prompt Guard 类过滤器的误拦率(false positive)对研发流速的影响量化？

## 附：来源清单
- Meta, *CyberSecEval 3* (arXiv:2408.01605) + Purple Llama / CyberSecEval 4（GitHub: meta-llama/PurpleLlama）
- He et al., *SecurityEval* (arXiv:2210.09263, 2022)
- Tony et al., *LLMSecEval / Instruct Prime / Reflexion* (arXiv 2511.03898)
- Wang et al., *CodeSecEval* (arXiv:2407.02395, 2024)
- Yang et al., *SecCodePLT* (arXiv:2410.11096)
- Peng et al., *CWEval* (arXiv:2501.08200, 2025)
- Dilgren et al., *SecRepoBench* (arXiv:2504.21205, 2025)
- ByteDance, *SafeGenBench* (arXiv:2506.05692, 2025)
- Chen et al., *SecureAgentBench* (arXiv:2509.22097, 2025)
- Endor Labs, *Agent Security League / SUSVIBES* 报告（2025-12 初版）
- Debenedetti et al., *AgentDojo* (ICLR 2025)；Zou et al., *AgentHarm* (ICLR 2025)
- Gray Swan AI + UK AISI, *ART benchmark*（2025 红队竞赛）
- Liu et al., *"Your AI, My Shell" / AIShellJack* (arXiv:2509.22040, 2025)
- Alizadeh et al., *Simple Prompt Injection Attacks Can Leak Personal Data* (arXiv:2506.01055, 2025)
- MITRE ATLAS v5.1.0（2025-11）；AI Security in Practice 威胁建模综述
- The Weather Report, *Thirteen Yardsticks, No Ruler*（2025，基准可比性综述）
- NIST SP 800-218 (SSDF)；Cisco Project CodeGuard (2025)；OpenSSF/Sigstore

## ⚠️ 待核实清单
- [ ] "Google 约 75% 新代码由 AI 生成""Copilot 不安全率 40%→17%(2021-2025)"——媒体/综述口径，非本库独立复现。
- [ ] SUSVIBES "功能正确的解里 >80% 仍含漏洞"、FuncPass 最高 61% / SecPass 最高 12.5%——Endor Labs 厂商报告口径，待跨团队复现。
- [ ] ART 竞赛"180 万次攻击 / 6.2 万次成功 / 100% 模型至少失败一次 / 平均 ASR 12.7%"——竞赛口径，数字随参与方与版本漂移。
- [ ] AIShellJack "Cursor/Copilot 恶意命令执行 ASR 最高 84%"——单一研究、未覆盖所有版本，待核实。
- [ ] "仅 12% 组织对 AI 代码采用与传统代码同等安全标准"——vendor 博客口径，待核实。
- [ ] Gartner "Predicts 2026" 提出的 context-deficient defects 类别——商业报告口径，待核实。
- [ ] 各基准具体数字均基于发布时模型版本，存在版本漂移，不可当作当前模型定论。

#标签/安全 #标签/AI编程安全 #标签/安全评测基准 #标签/代码安全
