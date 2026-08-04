# Figma 学习笔记

> 边学边记。目标：能用 Figma 做 Android 系统功能的可点原型（Prototype），用于演示 OS 级 Agent 交互。

## 当前在学 / 待补
- [ ] Figma 基础：Frame / Auto Layout / Component / Variant
- [ ] Prototype 模式：连线交互、Overlay（弹窗/确认卡）、Smart Animate
- [ ] 安卓组件库：Material 3 / 或自建系统 UI 组件（状态栏、通知、设置）
- [ ] 变量（Variables）与模式（Modes）：做深色/浅色、或不同确认强度态
- [ ] 适合做「系统级 Agent」演示的插件（待补）

## 技巧积累
- _（学到一条记一条）_
- Overlay 适合做 Confirmation UI 的 L1/L2 弹窗，能直接演示「确认→执行」流。
- 用 Component + Variant 表达一个意图的多种状态（待确认 / 执行中 / 完成 / 失败）。

## 关联
- 规格模板 → [[安卓系统功能原型规格模板]]
- 功能设想来源 → [[手机AI智能体知识库]]

## 深化补充

### 一句话心智模型

> **Figma 不是画图工具，是「有状态的 UI 数据库」——你在建的是一张组件表，Variant 是行，Property 是列，Prototype 只是这张表的一个查询视图。**

我一开始把 Figma 当 PPT 用（画一张张静态图），学不进去的原因就在这。转念一想：作为 PM 我本来就习惯写状态机和字段表，那 Figma 的正确打开方式就是**先定义状态维度，再让 UI 从状态里长出来**。这个视角一换，Variant / Variable / Conditional 三件套立刻就都说得通了。

对我这种 OS PM 尤其关键的一点：**系统级功能的本质就是状态机**（权限态、执行态、降级态），Figma 恰好是少数能把状态机可视化演示出来的工具。这比在 PRD 里写十行「若…则…」有用得多。

### 学习路径重排（按"对我最有用"排序，不按官方教程排）

原来的清单是按 Figma 功能顺序列的，我重排成**按我的产出目标倒推**：

| 优先级 | 学什么 | 为了做出什么 | 大概认知负担 |
|---|---|---|---|
| **P0** | Auto Layout（含 grid flow） | 任何能自适应的列表/卡片 | 低，1 小时能上手 |
| **P0** | Component + Variant + Property | 一个意图卡的 4 种状态 | 中，概念要绕一下 |
| **P1** | Overlay + Smart Animate | 确认弹窗「弹出→执行→消失」 | 低 |
| **P1** | **Variables + Modes** | 一套稿子切「宽松/严格确认策略」 | 中高，最值钱 |
| **P2** | **Conditionals + Expressions** | 真·分支流程（授权通过 vs 拒绝） | 高，但能省掉几十个 Frame |
| **P2** | Dev Mode / Code Connect | 交付给开发看规格 | 低，主要是交付侧 |
| **P3** | Slots | 复杂组件的插槽化 | 高，先不碰 |

**我的判断：P1 的 Variables + Modes 是这里投入产出比最高的一格。** 因为它对应的是我真正想演示的东西——同一个 Agent 流程，在"高信任模式"和"高风险模式"下确认强度不同。用 Mode 切换，一套稿子讲两个故事，而不是画两套。

### 具体例子：用 Figma 演示一次「Agent 执行确认」

这是我想做出来的第一个原型，拆成 Figma 语言：

**① 定义状态维度（Component Property）**

一个「意图执行卡」组件，开三个属性：
- `state`（Variant）：`待确认` / `执行中` / `已完成` / `失败`
- `risk`（Variant）：`低` / `中` / `高` —— 决定卡片色带和按钮文案
- `title`（Text property）：意图描述文字，可换

4 × 3 = 12 个 Variant。听起来多，但 Auto Layout 做好后大部分是改颜色和文案。

**② 定义策略变量（Variables + Modes）**

建一个 Variable Collection 叫 `确认策略`，两个 Mode：

| 变量 | Mode: 宽松 | Mode: 严格 |
|---|---|---|
| `需二次确认` | false | true |
| `确认按钮文案` | "好" | "确认支付 ¥xx" |
| `倒计时秒数` | 0 | 3 |

演示时切一下 Mode，整套原型的确认强度就变了——**这就是我在 [[Confirmation UI 安全机制]] 里想表达的"分层确认"，用嘴说不清楚，一切 Mode 就懂了。**

**③ 接流程（Prototype + Conditional）**

用 conditional 判断 `risk == 高` → 走 Overlay 二次确认；否则直接跳「执行中」。这样**一条连线覆盖两种路径**，不用画两条流程。

**④ 加时间感**

「执行中」→「已完成」用 After delay 触发 + Smart Animate，让评审的人真的感觉到"Agent 在干活"。静态图永远传达不出**等待焦虑**，而等待焦虑恰恰是端侧 Agent 最大的体验风险（见 [[OS-PM-性能与稳定性指标体系]] 里的时延讨论）。

### 三个我踩过/预判会踩的坑

1. **Variant 数量爆炸**：维度一多就是笛卡尔积。经验法则——**超过 3 个维度就该拆组件**，或者把某个维度改用 Variable 而非 Variant 表达（颜色、文案这类适合 Variable）。
2. **把 Prototype 当演示，而不当规格**：原型跑通了不等于规格写清了。原型讲"看起来怎样"，[[安卓系统功能原型规格模板]] 讲"边界条件是什么"。**两者必须配对交付**，只给原型开发会来问一百个问题。
3. **过度追求高保真**：我的目标是"讲清系统级 Agent 交互"，不是"做出能上架的 UI"。灰模 + 正确的状态流转 > 精致的圆角和阴影。**别在像素上耗时间。**

### 关联

- 交付配对 → [[安卓系统功能原型规格模板]] ｜ [[PRD写作SOP]]
- 原型要演示的机制本体 → [[Confirmation UI 安全机制]] ｜ [[Agent 身份与硬件级审批]]
- 状态机来源（画什么） → [[OS 系统级 Agent PRD 范例]] ｜ [[Agentic OS 意图调度内核]]
- 竞品交互参考（抄谁的流程） → [[HarmonyOS 意图框架竞品观察]] ｜ [[Windows Copilot Actions 竞品观察]]
- 降级态怎么画 → [[OS-PM-AI Runtime动态调度与降级策略]]

### 待解问题

- [ ] Figma 的 conditional / expression 能力，够不够表达一个**真实的多步 Agent 任务 DAG**（比如鸿蒙图推理引擎那种并行子任务）？还是说超过 3 步就该换工具（FigJam 画流程 + Figma 画界面）？
- [ ] Dev Mode / Code Connect 对**系统 UI（非 App UI）**交付有多大意义？系统 UI 的实现方在 framework 层，他们真的会看 Figma 吗？还是我该直接产出规格文档更实际？—— 这个得找实现同学问一次。
- [ ] 我做原型的**真实受众**是谁？如果是评审决策层，保真度可以低但故事要顺；如果是交互设计师，那我做的是需求输入不是设计稿。**受众没想清楚之前，别开始画。**
- [ ] 有没有必要学 Figma 的 Variables 与真实 design token 打通（Code Connect）？还是说这属于设计师职责，我了解概念即可？

#标签/Figma #标签/学习
