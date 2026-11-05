---
title: AI 产品的渐进式披露与可纠正性 UX 学习笔记
tags: [PM, 交互设计, UX, AI产品, AgenticUX]
created: 2026-10-11
source: "WebSearch 核实：progressive disclosure / undoable AI actions / HIG 2025-2026"
---

> 心智模型：把 AI 当成"会犯错且会自己动手的实习生"——先小步试水建立信任（渐进式披露），每一步都留好撤回绳（可纠正性），比"弹窗问你确定吗"更保护用户也更能保留效率。

# 广度覆盖

## 1. 这是什么：两个互补的概念

| 维度 | 渐进式披露 (Progressive Disclosure) | 可纠正性 / 可撤销 (Undoable & Reversible) |
|---|---|---|
| 核心问题 | 何时、向谁暴露 AI 的能力与推理 | 用户/AI 的改动如何安全回退 |
| 作用方向 | 信息"由浅入深"按需展开 | 操作"由做→可撤"留后路 |
| 关键手段 | 折叠面板 / Inspect reasoning / 置信度 / "了解更多" | Undo、版本快照、Action Log、补偿动作 |
| 信任机制 | 降低认知负荷 + 建立"它懂我" | 降低试错成本 + 建立"我能掌控" |

两者常被一起讨论：能力披露越克制，越需要靠"可撤"兜底；反之若动作可一键回退，就能更大胆地让 AI 自动执行。

## 2. 主流方案与模式（速查表）

| 模式 | 一句话 | 代表产品 / 来源 | 适用场景 |
|---|---|---|---|
| 渐进式披露 XAI | 先给结论+关键依据，"了解更多"再展开完整推理链 | Apple HIG、Smashing Mag 2025 "Goldilocks Zone" | 深度推理 Agent、可解释性 |
| 影响/可逆矩阵 | 高利害×不可逆→Intent Preview；高利害×可逆→Action Audit+Undo | JAR Digital 框架（待核实） | Agent 决策点分级 |
| Undo / Redo 栈 | AI 改动作为可逆操作入账，Cmd-Z 即可回退 | Cursor checkpoints、Notion AI、Claude Code git-undo（待核实） | 创作/代码工具 |
| 版本快照 (Snapshot) | 批量运行前拍"前照"，事后 diff + 回滚 | Figma 版本历史、Lovable 迭代前快照（待核实） | 批量/多页改动 |
| Action / Audit Log | 每条 AI 动作记 prompt、输出、来源、触发者 | Perplexity 引用、Anthropic Console transcript（待核实） | 企业/合规 |
| 草稿 vs 提交 (Draft-Commit) | AI 产出先落"草稿区"，用户确认才生效 | Office/Gmail 类比（待核实） | 高风险文案/发送 |
| 延迟发送 / 撤回窗 | 动作后留数秒~数十秒窗口可反悔 | Gmail "Undo Send" 类比（待核实） | 发送/触达类动作 |

## 3. 2025–2026 进展（已核实要点）

- **Apple HIG 原则**："优先用 Undo 而非确认弹窗；破坏性操作应尽可能可逆"——Undo 几乎总是优于"Are you sure?"（表述源自 HIG 镜像，待核实官方原文）。
- **Figma AI Agent（2026）**：Cmd/Ctrl+Z 只覆盖手动编辑；Agent 改动需点聊天里的 Undo 按钮（每轮后短暂出现），无选择性回退，可让 Agent 在对话里"撤销刚才做的"；版本历史可整体回滚（Figma 官方论坛，2026-06）。
- **Notion AI**：当前会话内撤销 + 逐页版本历史可回滚；但**无工作区级改动日志**，数据库 schema 改动不受页历史保护，删除页依赖约 30 天回收站（restora.cc 复盘，待核实）。
- **Human-in-the-loop 2026 指南**：把 AI 列为 undo 栈的"一等公民"；多步操作合并成单条 undo 项；破坏性动作用"补偿动作"而非"时间倒流"；高利害域跨会话持久化 undo 历史（AYDesign，待核实）。

## 4. 代表产品对比

| 产品 | 可纠正机制 | 注意点 |
|---|---|---|
| Figma | 聊天 Undo 按钮 + 版本历史 | Agent 改动 ≠ 手动 Undo，需单独入口 |
| Notion | 会话撤销 + 逐页版本历史 | 缺工作区级 diff，批量改动需先快照 |
| Office / Copilot | 标准 Cmd-Z 栈 | 文档场景天然可逆 |
| Cursor / Claude Code | 会话 checkpoint / 频繁 git commit | 面向开发者，回退粒度粗但稳 |
| Gmail | 延迟发送撤回窗 | 类比：Agent 触达类动作可借"撤回窗" |

## 5. 一句话 PM 决策点

- 先按「影响 × 可逆」给每个 AI 决策点分级：可逆的用 Undo/Log，不可逆的才用确认闸门（与 [[Confirmation UI 分级与产品责任边界]] 联动）。
- 让 AI 改动进入统一 Undo 栈，别让用户记两套快捷键。
- 批量/多页 Agent 动作前强制"快照"，否则事后无法 diff。
- 与 [[Agentic UX 交互设计模式 学习笔记]]、[[AI 产品的用户反馈回路与纠错机制 学习笔记]]、[[智能体身份与信任 学习笔记]] 互补。

# 深度盲区（待 Ethon 补充）
- [ ] 渐进式披露在「主动服务 Agent」里的触发阈值如何量化（信任额度耗尽前披露到哪一层）？
- [ ] 多步 Agent 动作合并 undo 的"自然边界"怎么定（按工具调用 / 按轮次 / 按子目标）？
- [ ] 快照成本 vs 回滚价值：多大批量才值得强制快照？端侧怎么存快照？
- [ ] "补偿动作"在安卓系统级 Agent（如发短信/扣费）怎么产品化且不让用户困惑？
- [ ] 同一动作对 A 用户可逆、对 B 不可逆（如已读/已发送）时 UI 怎么表达？

附：来源清单
- Apple HIG – Undo and redo (developer.apple.com/design/human-interface-guidelines/undo-and-redo)
- JAR Digital — Designing Agentic AI Requires a Deliberate Approach to Transparency (jardigital.net)
- Smashing Magazine 2025-12 — Beyond The Black Box: Practical XAI For UX Practitioners
- Figma Forum 2026-06 — Does Figma AI Agent support Undo?
- restora.cc — Notion AI Changed 50 Pages. Which Ones?
- AYDesign — Human-in-the-loop AI design guide for 2026 (aydesign.ai)
- 2026-10-11

⚠️ 待核实清单
- Apple HIG 关于 "undo over confirmation dialogs" 的具体原文与章节（当前来自 HIG 镜像站点）。
- JAR Digital 影响/可逆矩阵是否为业界通用框架，还是单篇方法论。
- AYDesign 指南中 Cursor/Lovable/Linear 的具体 undo 实现细节（博客转述）。
- Figma Agent 的 GA 时间与积分政策（mantlr 2026 博客，版本可能变动）。
- Gmail "Undo Send" 用于 Agent 触达类动作的「撤回窗」时长最佳实践尚无统一标准。

#标签/PM决策层/AI产品/交互设计
