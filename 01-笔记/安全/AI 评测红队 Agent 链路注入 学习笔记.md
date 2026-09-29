---
title: AI 评测红队 Agent 链路注入 学习笔记
tags: [安全, AI安全, red-teaming, Agent安全, 提示注入, 间接提示注入, 工具投毒, 多智能体]
created: 2026-09-20
source: 主要来自 WebSearch 核实的公开资料（AgentDojo/InjecAgent/ToolEmu 论文、OWASP Agentic Top 10、Gray Swan AI 红队竞赛报道、Lakera/Protect AI 官网等），2026-09-20 核实。
---

> 心智模型一句话：把"单模型越狱"升级为"在 Agent 多步链路里，攻击者通过检索内容、工具返回、外部网页等间接渠道注入指令，劫持规划与工具调用"。

## 1. 这是什么（广度定位）

一句话区分：[[AI 评测红队与对齐 学习笔记]] 关注模型层越狱/对齐；本篇关注 **Agent 拿到工具后、在规划-调用多步链路里被间接注入劫持**。与 [[工具调用安全 学习笔记]]（鉴权/授权）互补：本篇是"授权无误但语义被劫持"；与 [[AI Agent 沙箱与安全执行环境 学习笔记]]（隔离技术）互补：本篇是"要防什么攻击"，沙箱是"最后一道隔离"。

## 2. 攻击面分类（表格）

| 类别 | 定义 | 典型载体 | 代表案例/基准 |
|---|---|---|---|
| 直接注入 | 对手直接在 prompt 里覆盖指令 | 聊天输入、system override | 越狱；竞赛中直接注入 ASR 仅 5.7% |
| 间接注入 (IPI) | 恶意指令藏在 Agent 会读取的数据里 | 网页/RAG/邮件/PDF/工具返回 | Greshake et al. 2023 "Not what you've signed up for"；EchoLeak CVE-2025-32711 |
| 工具投毒 (Tool Poisoning) | 工具/MCP 描述字段藏指令，Agent 信任即执行 | 恶意 MCP server、被篡改 tool schema | OWASP ASI04；2025-09 首例 npm 恶意 MCP |
| 多 Agent 传播 | 注入在 Agent 间消息/共享记忆里横向扩散 | A2A 协议、共享上下文、记忆中毒 | OWASP ASI06/ASI07/ASI08；Morris-II 自复制 |

## 3. 主流研究 / 基准（表格）

| 基准 | 机构/年份 | 规模/要点 | 关键结论 |
|---|---|---|---|
| AgentDojo | ETH Zurich + Invariant, NeurIPS'24 | 97 任务 / 629 安全用例 / 4 套件(Banking/Slack/Travel/Workspace) | 指标 BU / UA / ASR；Claude 3.7 Sonnet ASR≈8.5%（inspect 实现，待核实具体版本） |
| InjecAgent | UIUC, 2024 | 1054 用例 / 17 用户工具 + 62 攻击者工具 | ReAct-GPT-4 基线 24% 脆弱，增强后≈47% |
| ToolEmu | ICLR'24 | 36 工具包/311 工具/144 用例，LM 仿真沙箱 | 68.8% 失败经人工确认为真实风险 |
| OfficeBench | 2024 | 300 多应用办公任务（能力基准，含注入面） | 最强 GPT-4o 仅 47% 通过，人 93.3% |
| Agent-SafetyBench | 2024 | 349 环境 / 2000 用例 / 10 失败模式 | 综合 agent 安全覆盖 |
| WASP / MCP-SafetyBench | 2025 | 网页 agent / MCP 协议专测 | 部分 ASR 高达 86%；MCP 主机侧 >80% |

## 4. 代表防御方案（表格）

| 方向 | 思路 | 代表 |
|---|---|---|
| 输入隔离 | 结构化查询 / delimiter + spotlighting，区分可信与不可信内容 | StruQ(USENIX'25)、SecAlign(CCS'25)、Azure Prompt Shields+Spotlighting |
| 权限最小化 | 工具作用域、短效凭证、默认只读 | OWASP ASI03；Agent 沙箱（见 [[AI Agent 沙箱与安全执行环境 学习笔记]]） |
| 工具沙箱 | 隔离执行、受限网络出口 | 见 [[AI Agent 沙箱与安全执行环境 学习笔记]] |
| 人类确认 | L1/L2 分级确认高风险动作 | 见 [[Confirmation UI 分级与产品责任边界]]（库内） |
| 输出校验 | 动作级策略校验、形式化验证 | Bedrock Automated Reasoning(GA 2025-08，待核实准确率口径) |
| 提示护栏 | 实时 PI 检测/拦截（I/O 双端） | Lakera / Protect AI / Prompt Guard 2 / NeMo Guardrails |

## 5. 2025-2026 进展（点到为止）

- **红队竞赛实证**：Gray Swan AI + 英国 AISI（2025-03~04）约 2000 人 / 180 万次攻击，22 模型 44 场景，**100% 至少失败一次**，均 ASR≈12.7%；间接注入 27.1% vs 直接 5.7%；演化出 ART 基准（~4700 攻击提示）。（媒体口径，待核实原始论文数字）
- **OWASP Agentic Top 10（ASI01-ASI10）** 于 2025-12 发布，首份 agent 风险基线；ASI01 目标劫持/ASI04 供应链/ASI05 意外代码执行直接相关。
- **真实漏洞**：EchoLeak(CVE-2025-32711) 零点击 Copilot 渗出；首例恶意 MCP(npm, 2025-09)；Anthropic MCP SDK 设计缺陷(2026-04，待核实补丁状态)。
- **态势判断**：前沿实验室合成测试号称 sub-1% ASR，但人类红队仍可通过间接注入稳定突破（ThreatPrompt 2025 年终）——"合成鲁棒 ≠ 真实安全"。

## 6. 代表性产品 / 框架（表格）

| 类别 | 代表 | 说明 |
|---|---|---|
| 扫描/防护 | Lakera（2025 被 Check Point 收购）、Protect AI、Cisco AI Defense | 实时 PI 检测 + 数据泄漏防护；Lakera 宣称 >98% 检测、<50ms（厂商口径，待核实） |
| 红队框架 | PyRIT(Microsoft)、Garak(NVIDIA)、ART 基准 | 自动化对抗生成→执行→评分闭环 |
| 框架护栏 | LangChain/LangGraph guardrails 集成、NeMo Guardrails | 框架内置 I/O 护栏（具体集成形态/年份待核实） |
| 沙箱 | E2B / Modal / Daytona / Firecracker / gVisor | 执行隔离，见 [[AI Agent 沙箱与安全执行环境 学习笔记]] |

## 7. 待解问题（深度盲区，留给 Ethon 补）

- [ ] AgentDojo 各模型最新 ASR 排行与趋势（2026 版待核实）
- [ ] 间接注入在 Android 端侧 agent（on-device tool use）的特殊性？
- [ ] MCP 投毒（ASI04）在 PM 视角的供应链责任归属如何落地？
- [ ] "权限最小化 + 人类确认" 与 UX 流畅度的权衡边界在哪？
- [ ] 多 Agent 传播有没有可量化的"感染率"基准？

## 附：来源清单（实际查阅）

- AgentDojo 官网/论文：https://agentdojo.spylab.ai/ ；arXiv:2406.13352
- InjecAgent：arXiv:2403.02691（UIUC Kang Lab）
- ToolEmu：Ruan et al., ICLR 2024
- "Not what you've signed up for"（IPI 奠基）：arXiv:2302.12173（Greshake/Abdelnabi et al., AISec 2023）
- OfficeBench / Agent-SafetyBench：arXiv:2412.14470
- Gray Swan AI 红队竞赛报道：the-decoder.com（2025-04）
- OWASP Agentic Top 10 (ASI01-ASI10)：owasp.org（2025-12）
- Lakera：https://lakera.ai/ ；Check Point 收购公告
- Azure Prompt Shields / Bedrock Guardrails / Google Model Armor（厂商文档）
- ThreatPrompt 2025 年终综述

## ⚠️ 待核实清单

- AgentDojo 中 Claude 3.7 Sonnet 8.5% ASR 的具体版本与 inspect 实现口径。
- Gray Swan 竞赛数字（2000 人/180 万次/ASR 12.7%/间接 27.1%）为媒体二次报道，待查原始论文。
- Lakera "98% 检测 / <50ms / 0.01% FP" 为厂商口径，未独立验证。
- LangChain/LangGraph guardrails 集成的具体形态与年份。
- Bedrock Automated Reasoning "99% 准确率" 为广告口径。
- Anthropic MCP SDK 设计缺陷(2026-04)的官方补丁状态。
- Lasso Security 产品细节未单独核实（与 Lakera/Protect AI 同列为防护类，具体差异待查）。

#标签/安全 #标签/AI安全 #标签/red-teaming #标签/Agent安全
