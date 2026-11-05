---
title: 端侧模型推理的可解释性 UX 落地
tags:
  - broadth-seed
  - 端侧可解释性
  - AIUX
  - saliency
  - 归因可视化
  - 端侧AI
created: 2026-10-16
source: WebSearch + WebFetch 核实（2025–2026 公开资料：厂商新闻室、学术/arXiv、XAI UX 模式库、行业博客）
---

> **一句话心智模型**：端侧模型的「可解释性」落到手机上，不是给工程师看 saliency 图，而是把「模型为什么给出这个结果」翻译成用户可读、可纠、可信赖的微交互（归因高亮 / 置信度 / 自然语言理由 / 反事实）。

## 广度覆盖

| 维度 | 要点（点到为止） |
|---|---|
| **定义** | 端侧模型推理可解释性 UX = 把手机本地跑的小/大模型「为何得出此输出」以**用户可读**形式呈现（归因高亮、特征重要性、置信度、自然语言理由、反事实），区别于工程师侧的算法可解释性。 |
| **分类（按呈现形态）** | ① 归因高亮（saliency / segmentation mask / attention 区域）② 特征重要性（条形图 / 表单着色）③ 自然语言理由 NLE ④ 反事实（"若 X 不同，结果会是 Y"）⑤ 置信度 / 分级提示 ⑥ 持续 AI 标识 + 可纠正（"Was this helpful?"） |
| **主流方案（算法层）** | LIME、SHAP、Integrated Gradients、Attention maps、LRP、XRAI、TCAV；移动端专用 saliency 如 SAM-mobile（Aalto，针对移动 UI 数据集校准）。 |
| **主流方案（UX 层）** | Progressive disclosure（简单默认→高级按需）、confidence tiers（高/中/低一档式提示而非裸概率）、counterfactual toggles、attribution highlight、持续而非一次性的 AI 披露标识。 |
| **2025–2026 进展** | EU AI Act 推动金融/医疗场景 SHAP 可视化合规（银行信用评分面板）；移动 XAI 框架/SDK 开始内置可解释性；counterfactual 交互在移动场景被验证提升理解（Georgia Tech 2025，媒体口径）；UX 模式库成型（置信度 / 归因 / 反事实 / 注意力高亮四类被 GitHub 2026 模式库收录）。 |
| **代表产品** | Samsung Galaxy S25 媒体浏览器：自然语言搜照片 + 自动剪辑（零样本标签 3× 扩增，官方新闻室）；医学影像注意力图（Google Health / IBM Watson，云端为主）；Spotify "Made for You" 理由文案；金融 App 信用评分 SHAP 面板（云端为主）；计算摄影抠图/主体分割 mask 可视为一种「归因可视化」端侧落点。 |

## 关键张力（PM 视角）

- **端侧约束 vs 解释成本**：SHAP 等全局归因在端侧开销大（有资料称 SHAP 增加 5–10× 推理时间，靠云边混合缓解）——端侧优先「轻量归因」（mask / 区域 / NLE），重归因走云。
- **透明度 ≠ 全量技术细节**：认知过载会反噬信任；移动端要"对的事在对的时机透出一点"，而非 dump 张量流。
- **用户想要被「告知 AI 在做事」**：68% / 72% 类调查数字（IBM / Accenture 2025，媒体口径）指向"持续、情境化 AI 标识"需求，而非一次性 splash 弹窗。

## BREADTH > DEPTH：深度盲区（待解问题）

- [ ] 真正把**像素级 saliency 热力图直接呈现给终端消费者**的旗舰手机 AI 功能，目前公开案例是否真的存在？（多数消费端仍用分割 mask / 高亮框 / 文字理由，而非 gradcam 热力图）——待核实
- [ ] 端侧 SLM 上跑 LIME/SHAP 的**实测开销账本**：在 Snapdragon 8 Gen 3 等 NPU 上的 ms / 内存代价，是否有公开 benchmark？
- [ ] 计算摄影（HDR 融合 / 夜景降噪 / 人像虚化）的"AI 做了什么"是否算**广义归因可视化**，行业有无统一 UX 范式？
- [ ] 反事实交互在**中文 / 国内安卓生态**的可用性研究与本土化案例。
- [ ] 端侧可解释性与隐私/模型保护如何平衡（全透明可能暴露模型或招对抗）——具体落地护栏。
- [ ] EU AI Act 对"面向用户 AI 决策解释"的**强制粒度**到底到哪一层（仅高影响决策 vs 全部）。

## 防信息孤岛（库内连接）

- 与 PM 决策侧 [[AI 产品的可解释性 UX 与归因展示 学习笔记]] 互补：那篇从 PM 决策/归因展示整体视角，本篇聚焦**端侧推理这一落地场景**的 UX 模式。
- 与算法层 [[端侧模型推理可解释性与 saliency 可视化 学习笔记]] 互补：那篇讲端侧"怎么算归因"（梯度/注意力/LIME-SHAP/TCAV/显著性图），本篇讲"算出来怎么给用户看"。

## 附：来源清单

1. Samsung Newsroom（TW）— Galaxy S25 媒体浏览器自然语言搜照片 + 自动剪辑，零样本标签扩增。官方新闻室，可信度较高。
2. arXiv 2204.02448 — *Predicting and Explaining Mobile UI Tappability with Vision Modeling and Saliency Analysis*（XRAI 归因 + 对比样例，设计师侧可解释性）。
3. Aalto University *Understanding Visual Saliency in Mobile User Interfaces* / SAM-mobile（移动 UI 专用 saliency 模型）。
4. Mobile Product Studio — *AI in Mobile UX: 68% User Frustration in 2026* / *Mobile UI AI Trust: 2025 IBM Study*（contextual feature importance、counterfactual、NLE、置信度 UX 模式；含调查数字，媒体口径）。
5. Brandon Travis — *Explainable AI Strategies in User-Facing Products*（LIME/SHAP/attention maps/counterfactual、EU AI Act 驱动 SHAP 可视化、progressive disclosure）。
6. GitHub `vasilyu1983/AI-Agents-public` — *AI & Automation UX Patterns (2025-2026)*（置信度/归因/反事实/注意力高亮/渐进自主模式库，2026-08 更新）。
7. models.news — *Beyond Accuracy: Designing Model-Centric UX for Consumer Devices in 2026*（edge-first、multi-tier confidence、degradable UX）。
8. johal.in / LinkedIn Office Matters — 端侧 XAI 技术栈（LIME/SHAP/Integrated Gradients/LRP）与移动部署约束（二次来源）。

## ⚠️ 待核实清单

- [ ] **68% / 72% 调查数字**（IBM 2025、Accenture 2025）为博客转述，原始研究未直接核验，记为媒体口径、待核实。
- [ ] **Georgia Tech 2025 counterfactual 研究**"显著提升移动场景理解"为博客引用，原始论文未核验，待核实。
- [ ] **22% 互动提升 / 35% 信任提升 / 70% 企业 App 2026 集成 XAI** 等量化结论均来自厂商/咨询博客自有数据，待核实。
- [ ] **EU AI Act 强制 SHAP 信用评分可视化**为二级来源表述，法规原文强制粒度待核实。
- [ ] **消费者端像素级 saliency 热力图**是否真有旗舰落地，公开资料稀缺，待核实（疑似目前多为 mask/框/理由而非热力图）。
- [ ] **端侧 SHAP 5–10× 推理开销**数字来自单篇博客，缺多源交叉验证，待核实。

#标签/端侧可解释性 #标签/AIUX #标签/saliency #标签/归因可视化
