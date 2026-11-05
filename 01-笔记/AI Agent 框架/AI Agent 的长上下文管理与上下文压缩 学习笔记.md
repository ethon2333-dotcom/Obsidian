---
title: AI Agent 的长上下文管理与上下文压缩
tags: [Agent, 上下文工程, 长上下文, 上下文压缩, KV cache, prompt caching, compaction, 记忆]
created: 2026-11-02
source: WebSearch 公开资料（Zylos context engineering 研究 2026、Prime Intellect RLM、AgentNative compaction pattern、LangGraph memory docs、LLMLingua/AutoCompressor 论文与综述、Anthropic/Claude Code compaction 与 prompt caching 文档、Gemini 长上下文报道）；详见文末来源清单
---

# AI Agent 的长上下文管理与上下文压缩

> [!note] 心智模型（一句话）
> Agent 跑多步任务时上下文会无限膨胀，等到撑爆窗口或把成本/延迟拉爆之前，必须**裁掉旧的、压缩冗余的、按需检索该取的**，让有限的窗口里始终装着"此刻最该被模型看到"的内容——本质是「窗口内的信息取舍工程」，而非把历史全部塞进去。

本篇聚焦 Agent 长上下文的**管理与压缩工程面**，区别于 [[Context Engineering 学习笔记]]（上下文组装的概念层）；也刻意区别于 [[AI Agent 的持久化与状态管理 学习笔记]]（那是运行态落盘/恢复，本篇讲窗口内的压缩与裁剪）。与 [[Agent 记忆系统 学习笔记]]（长期记忆分层）和 [[Agent 推理成本优化 学习笔记]]（成本/KV cache 复用）强咬合。

## 1. 定义与分类（广度全景）

| 类别 | 一句话 | 典型手段 |
|---|---|---|
| 截断 Truncation | 粗暴丢最早的 token/消息 | 滑动窗口 sliding window、trim 保留最近 N |
| 摘要压缩 Compaction | 把旧历史压成结构化摘要再回灌 | 分层摘要、server-side compaction、状态累积文档 |
| 检索压缩 Retrieval-based（RAG 减负） | 不进窗口，按需检索才进 | selective retrieval、rerank、过滤进窗口的文档 |
| 结构化上下文 Structured | 把信息改成紧凑结构而非自然语言流水 | state document、决策/约束清单 |
| 重要性筛选 Importance-based | 按注意力/重要性打分丢低价值块 | 困惑度打分、SnapKV/PyramidKV 选 KV |
| KV cache 管理 | 复用/裁剪 key-value 缓存降本提速 | prompt caching、KV 裁剪、prefix sharing |
| 分层记忆 Layered memory | 工作记忆 ↔ 外部冷库 换入换出（类虚拟内存） | MemGPT / MemoryOS swap-in/out |

## 2. 主流方案 / 技术

| 技术 / 方案 | 思路 | 适用场景 | 备注 |
|---|---|---|---|
| Claude 提示缓存 Prompt Caching | 标记 `cache_control` 缓存静态前缀，命中计费约 0.1x | 系统提示/工具 schema/共享文档每轮重复 | 写缓存约 1.25x（5 分钟档）/2x（1 小时档）；前缀须逐字节一致 |
| Gemini / 长上下文模型（200K+，Gemini 2.5/3.x 达 1M–2M） | 直接喂大窗口，省去 RAG | 单会话深工作、中等规模代码库 | "容量≠能力"，lost-in-the-middle 在 1M 仍存在 |
| LangGraph 消息修剪 trim | `trim_messages(strategy="last")` 每轮裁到预算内；`SummarizationNode` 摘要 | 多轮会话防溢出 | pre_model_hook 在 LLM 前跑 |
| LLMLingua / LLMLingua-2（微软） | 小模型按困惑度删低信息 token（hard prompt 压缩） | 黑盒 API 也能用，紧 token 预算 | 压缩率数字见待核实清单；缺多步交互结构理解 |
| AutoCompressor / ICAE / Gist Tokens（软提示压缩） | 把长文本压成 embedding/summary tokens | 需改模型内部或训练 | **闭源 API 不可用**（白盒方法） |
| MemGPT / MemoryOS（分层记忆） | 工作记忆 ↔ 外部记忆 换入换出，类 OS 虚拟内存 | 超长会话、跨会话态 | 与 [[Agent 记忆系统 学习笔记]] 同主题不同侧重 |
| RAG 减负 | 检索只取相关片段，不过量进窗口 | 知识库问答、长文档 | 与上下文压缩正交、可叠加 |
| KV cache 复用 / 裁剪 | 复用前缀 KV、按注意力选重要 KV | 多轮、长上下文推理降本 | SnapKV/PyramidKV 属推理层裁剪 |

## 3. 2025–2026 进展（点到为止）

- **长上下文模型普及**：Claude 1M token、Gemini 2.5/3.x 1M–2M 成为主流卖点；但研究反复指出"窗口大 ≠ 用得好"，lost-in-the-middle 在大窗口依旧存在。
- **Prompt cache 成标配**：Anthropic / OpenAI / Gemini 均提供 prompt caching，闭源 API 下的首选降本手段（先缓存静态前缀，再压缩动态部分）。
- **Compaction 自动化**：Claude Code / Anthropic Compaction API 自动压缩（默认累计输入越过约 15 万 token 触发，可下探到 5 万；Claude Code 约在 200K 窗口 95% 处自动压缩并回灌最近文件）；OpenAI 侧也有类似 compaction 思路。
- **上下文窗口 vs 压缩的权衡**：工程共识是"用大窗口做单会话深工作 + 外部持久记忆做跨会话连续性"，而非无脑堆窗口；压缩的隐藏成本（压缩本身要重读全文再总结）与缓存失效（改中间 token 会让后面整个缓存作废）成为新坑。

## 4. 代表产品 / 框架

- **Coding Agent 类**：Claude Code（自动 compaction + 最近文件回灌）、OpenAI Codex、Cognition（自训压缩模型处理长工程轨迹）。
- **框架层**：LangGraph（`trim_messages` / `SummarizationNode` / checkpointer）、LangChain（`langmem` 短期记忆）、Letta（前 MemGPT，记忆管理）。
- **压缩工具**：Microsoft LLMLingua 系列、LongLLMLingua（问题感知压缩）、Selectively Context、RECOMP。
- **推理层**：SnapKV、PyramidKV（KV cache 裁剪，需接入 vLLM/SGLang 等引擎，存在工程兼容成本）。

## 5. 深度盲区（待解问题）

- [ ] ACON / 自学习上下文保留：agent 如何从自身"上下文导致的失败"中学习该留什么？（[[Agent 记忆系统 学习笔记]] 如何与这类在线学习打通？）
- [ ] 压缩导致的"关键事实静默丢失"如何评测？有没有标准回归 eval（replay 轨迹比 completion rate）？
- [ ] Compaction 与 prompt cache 的耦合：自动压缩会不会悄悄击穿前缀缓存命中率、把 prefill 成本拉爆？
- [ ] 软提示压缩（AutoCompressor/ICAE）在闭源 API 下完全不可用，那"高质量无损压缩"在 API-only 场景的落地边界在哪？
- [ ] 多智能体间交接（inter-agent seam）的上下文压缩标准是什么？什么该传、什么该只传指针？（关联 [[AI Agent 工具调用的幂等性与副作用管理 学习笔记]] 的副作用边界）
- [ ] "上下文预算 budgeting" 在端侧/手机 Agent 上如何分配系统提示、工具定义、历史、检索文档的 token 配额？（关联 [[Agent 推理成本优化 学习笔记]]）

---

## 附：来源清单

1. Zylos — Context Engineering for AI Agents: From Craft to Production Discipline (2026-06) — 压缩三模式、分层记忆、五层 Zylos 记忆模型、token 削减 80% 口径、Claude 1M / Gemini 2.5 2M。
2. Prime Intellect — Recursive Language Models / Context-Folding (2026-01) — context folding、RLM (arXiv 2512.24601)、AgentFold 等。
3. AgentNative — Context Compaction Pattern for Long-Running Agents (2026) — compaction schema、ACON 26–54% 数字、缓存友好重建。
4. LangGraph 官方 memory 文档 — `trim_messages` / `SummarizationNode` / checkpointer / pre_model_hook。
5. ML4Devs — Prompt Caching and Compression — Anthropic prompt caching 计费口径、LLMLingua 说明。
6. PointFive — Prompt Compression Tools (2026) — 方法分类（缓存≠压缩）、各工具风险。
7. arXiv 2405.11299 — CAP Principle for LLM Serving：长上下文服务综述，LLMLingua/ICAE/AutoCompressor 黑白盒分类、Agent Memory。
8. AGI Daily — 四项研究改进上下文压缩 — Hard/Soft/KV 三类路线、ACON。
9. o-mega.ai — Context Engineering: 4 Techniques (2026) — Claude Code compaction 阈值、KV cache 经济账、append-only 压缩。
10. Anthropic 官方文档 / Claude Code — Prompt Caching、Compaction API 阈值（公开文档口径）。

## ⚠️ 待核实清单

- 🔸 LLMLingua "最高 20x 压缩、98.5% 准确率保留"、LongLLMLingua "+17.1% @ 4x"、Zylos "削减 token 至多 80%"、ACON "26–54% 峰值 token 削减 @ ~95% 精度"——均为来源方/论文口径，具体数字与你在用的模型/任务未必一致，落地前需自行复测。
- 🔸 Claude Compaction API "默认 15 万 token 触发、可下探 5 万"、Claude Code "约 200K 窗口 95% 处压缩"——来自厂商文档与博客，阈值随版本变动，以官方最新文档为准。
- 🔸 Gemini 3.1 Pro "1M 上下文、SWE-bench 80.6%、750M 用户"——媒体/厂商口径，未逐一交叉核实。
- 🔸 各源对"上下文窗口多大开始性能衰减"说法不一（有说 32K 起、有说 50–70% 填充起），属经验区间而非硬边界。

#标签/Agent #标签/上下文工程 #标签/长上下文 #标签/上下文压缩
