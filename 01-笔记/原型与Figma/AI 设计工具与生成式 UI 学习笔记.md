---
title: AI 设计工具与生成式 UI 学习笔记
tags: #Figma #AI设计 #生成式UI #设计工具 #原型 #横向图谱
created: 2026-09-14
source: 联网核实（WebSearch / WebFetch，2026-09-14）
---

> **一句话心智模型**：AI 设计工具把「描述（文字 / 草图 / 截图 / 代码）」直接变成「可编辑的 UI 或代码」——设计稿不再是画出来的，而是「生成 + 精修」出来的。

这是一份**广度种子笔记**：只画地图、不挖深井。Ethon 在学 [[Figma 学习笔记]]，本篇帮他看清「AI 生成 UI」这个生态有哪些玩家、按什么能力分类，深度（保真度、与 Figma 工作流衔接、Android 规范遵循等）留白给他补。

## 广度覆盖

### 按「能力」分类的工具图谱

| 能力分类 | 是什么 | 代表产品 | 2025–2026 进展 |
|---|---|---|---|
| **文生 UI**（text → UI 屏 / 线框） | 输入一句描述，生成整屏布局或可编辑稿 | Figma First Draft、Galileo AI（已并入 Google → Stitch）、Uizard Autodesigner、Canva Magic Design、Motiff 文生设计 | First Draft 2024 上线、2025–2026 大幅扩展；Galileo 被 Google 收购后改名 Stitch（Google Labs） |
| **图生可编辑稿**（草图 / 截图 → 可编辑设计） | 手绘草图、截图、参考图转成数字可编辑 UI | Uizard（手绘→线框）、v0 by Vercel（截图 / Figma 导入）、Stitch（sketch-to-design）、Midjourney（概念图 → 进 Figma 精修） | Uizard 主打「完整设计集」而非单屏；v0 支持 Figma 文件直转组件 |
| **design-to-code**（设计稿 → 生产代码） | 生成可直接用的前端 / 原生代码 | v0 by Vercel（→ React/Tailwind/shadcn）、Figma Code-to-Canvas（反向：代码→设计）、Claude/ChatGPT（→ Jetpack Compose / SwiftUI） | v0 于 2025-05 推 OpenAI 兼容 API、2025-06 推 Design Mode；「Generative UI」范式（LLM 流式吐 React 组件）走热 |
| **AI 辅助排版 / 增强**（编辑器内 AI） | 不生成整屏，而是自动布局、改名、给建议、做可访问性审计 | Figma AI（Auto Layout AI、图层重命名、设计建议）、Motiff（AI 布局 / 设计批评）、Canva Magic Edit、UX Pilot（注意力热力图 + WCAG 审计） | Figma AI 建议被形容「像资深设计师实时 review」；UX Pilot 把「生成 + UX 验证」合一个工具 |

### 主流方案速查（点到为止）

- **Figma AI（Make / First Draft / Code-to-Canvas）** — 在 Ethon 已用的 Figma 文件内原生生成，零工作流切换。First Draft 生成可编辑线框；Figma Make 生成含导航/状态/交互的多屏原型；Code-to-Canvas 粘贴代码得可编辑设计。**局限**：不能用你自己的设计系统生成（官方说「hope to make available soon」）；手动改过后无法再用提示词迭代 First Draft。
- **v0 by Vercel** — 不是设计工具，是「设计→代码加速层」。输出真实 React + Tailwind + shadcn/ui 代码，一键部署 Vercel。适合「设计决策已定、要快速落地代码」的后期阶段。
- **Galileo AI → Stitch（Google）** — 文生高保真单屏，导出 Figma 为可编辑组件；质量普遍认为高于 Uizard，但不生成完整流程 / 交互逻辑。
- **Uizard** — 文生 / 草图生 / 截图生，主打「完整设计集」+ 手绘草图转数字线框；有 Figma 插件；免费版导出限 5 屏。
- **Motiff** — 中国团队 2024 年推出的 AI-native 设计平台，界面像 Figma，内置 AI 组件生成 / 设计系统生成（号称可识别至多 7,000 图层）/ 设计批评；定价显著低于 Figma（来源口径不一，待核实）。
- **Canva Magic Studio** — 面向「所有人」的营销 / 社媒 / 演示场景（Magic Design、Magic Write、Magic Media、Magic Switch 改尺寸），非专业产品 UI 工具。
- **Midjourney / Designer** — MJ 定位概念图 / moodboard，导出进 Figma 或 PS 精修，不是 UI 工具本身；「Designer」具体指代待核实（见下方清单）。

### 范式层面的两点

- **Generative UI（生成式 UI）**：Vercel 的说法——你描述组件，系统流式返回 React（RSC）组件，而非截图。代表「描述即界面」的方向。
- **Android 侧关联**：已有实践用 Claude / ChatGPT 把设计稿转 **Jetpack Compose + Material 3** 代码（单组件首轮准确率有博主称 ~80%，待核实）；行业预测 Apple / Google 会把「提示词生布局」原生集成进 Xcode / Android Studio。对 Ethon（Android OS PM）最相关的切口是：**prompt → 系统 UI 可点原型 / Material 3 代码**。

## 深度盲区 · 待 Ethon 补充

- [ ] **可编辑性与 fidelity**：AI 生成的稿子在 Figma 里图层结构有多「干净」？自动布局 / 组件化是否到位，还是只是一堆打平的形状，难以继续迭代？
- [ ] **与 Figma 工作流衔接**：First Draft / 导入的 Galileo / v0 稿，怎么接进 Ethon 已有的 [[Figma 学习笔记]] 组件 + Variant + Variables 体系？能复用设计系统吗（官方说暂不能）？
- [ ] **Android 设计规范遵循**：生成式 UI 工具大多是 Web / iOS 范式训练，生成物对 **Material 3 / 系统级 UI（状态栏、通知、设置）** 的遵循度如何？需要后处理多少？
- [ ] **系统级 Agent 演示场景**：Figma Make 生成的多屏原型，够不够演示「Agent 执行确认流」（参考 [[安卓系统功能原型规格模板]] 的确认点）？还是只能做普通 App 界面？
- [ ] **design-to-code 的落地价值**：作为 PM，v0 / Compose 代码生成对我「验证交互」有多大用？还是说保真灰模 + 正确状态流转（Figma 原生）更划算？
- [ ] **选型边界**：当「要快速给评审看一个故事」vs「要交付开发可消费的稿」，该分别用哪类工具？成本（积分 / 订阅）怎么算？

## 关联

- 已在学的工具与方法 → [[Figma 学习笔记]]
- 开工前先填的规格（确认点 / 状态）→ [[安卓系统功能原型规格模板]]

## 附：来源清单

1. Figma 官方帮助：Use First Draft with Figma AI — https://help.figma.com/hc/en-us/articles/23955143044247-Use-First-Draft-with-Figma-AI
2. Figma AI 2026 深度评测（similarlabs，含 Make / Code-to-Canvas / 定价 / 模型口径）— https://similarlabs.com/zh/blog/figma-ai-review
3. Figma State of the Designer 2026（72% 设计师用生成式 AI、91% 认为提升质量）— https://geekvibes.agency/blog/figma-make-state-of-designer-2026
4. v0 by Vercel 概览与定价 / Design Mode / API — https://www.toolmage.com/en/tool/v0/ ｜ https://heyorai.com?p=19790/
5. Galileo AI → Stitch、Uizard、Motiff、Canva 对比 — https://merge.rocks/blog/top-ai-design-tools-for-ux-ui-designers-in-2025 ｜ https://nightwatcherai.com/blog/figma-ai-plugins-alternatives
6. Canva Magic Studio 2025 指南 — https://artificial-intelligence-wiki.com/ai-tools/ai-productivity-tools/canva-magic-design-guide
7. Generative UI 范式 & Android / Jetpack Compose 代码生成 — https://www.techswill.com/tag/galileo/ ｜ https://www.pragmaticcoders.com/?p=17280/

## ⚠️ 待核实清单

- Figma AI 底层模型口径「Gemini 3.0 Pro + OpenAI GPT Image」仅单来源（similarlabs），待多源核实。
- Galileo AI 改名 Stitch（Google 收购）的时间线与当前产品名（Galileo / Stitch 混用），建议以 Google Labs 官方页为准。
- v0「100M+ 用户交互」「Vercel 估值 $3.25B / $250M 新资金」来自单一商业博客，待核实。
- Canva Pro 定价口径不一（$12.99 / $15 月），Motiff 定价口径不一（Dev Mode $1 / Pro $6），需以官网为准。
- 设计稿→Jetpack Compose 的「首轮 ~80% 准确率」来自单一博客，样本与模型版本未明，待核实。
- 「Midjourney Designer」具体指代不明（MJ 本体是概念图工具，无明确「Designer」产品线），本笔记未将其作为独立方案立论。
- Figma「agent 新入口（2026-05-20 起逐步灰度）」来自官方帮助文档，可信度高，但 beta 范围与最终形态仍可能变动。

#标签/Figma #标签/AI设计 #标签/生成式UI #标签/设计工具 #标签/原型
