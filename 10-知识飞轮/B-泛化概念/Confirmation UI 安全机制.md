---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, 安全, ConfirmationUI, 概念]
aliases: [确认机制]
---

# Confirmation UI 安全机制

## 一句话定义

**Confirmation UI（确认界面）/ Step-up Auth** 是系统在执行敏感意图（支付、发信、删除）前强制弹出的确认与授权层，确保「人类始终在环」，且沙盒化、声明式授权只响应 App 明确暴露且获许可的能力。

## 为什么重要

- 不经过确认层，AI 控制手机就得依赖「录屏 + 模拟点击」，隐私与误操作风险极大。
- 高危动作的系统级确认应是**平台强制层**，而非交给开发者各自实现（否则会漏）。

## 适用边界

- 区分「可逆/低频动作」（可静默）与「不可逆/高危动作」（必须确认）。
- 与隔离执行互补：确认解决「是否执行」，隔离解决「执行域泄漏」（见 [[Agent Workspace 隔离执行]]）。

## 证据与例子（四平台对照）

| 平台 | 机制 |
|------|------|
| Apple | `OwnershipProvidingEntity`（EntityOwnership `.shared`/`.public`/`.unknown`）差异化提示；高危 Intent 系统级拦截 |
| Windows | Agent Workspace 隔离会话 + 低权限账号 + ACL/审计/吊销；敏感步骤显式同意；连接器 OAuth |
| HarmonyOS | 可信设备能力协商；上下文充足时免二次确认；跨设备安全通道 |
| Android | UI Automation 对购买等敏感动作「执行前预警」；用户可经通知/live view 接管 |

## 2026-07-31 增补：两种新形态（来源 [[AppIntent 每日情报 2026-07-31]]）

**形态一：系统中介的一次性数据授权（Android 17，2026-06-16）**

把敏感授权从「App 申请长期权限」升级为「**系统代持、单次、字段级**的确认 UI」——这是 Agent 时代 Confirmation UI 的正确形态，因为 Agent 不该长期持有权限：

| 新机制 | 替代的旧权限 | 授权粒度 |
|---|---|---|
| `ACTION_PICK_CONTACTS` | `READ_CONTACTS` | 用户选定的**特定字段**（如仅邮箱），临时 |
| 系统渲染的位置信息按钮 | 精确位置权限 | **仅当前会话** |
| `ACTION_OPEN_EYE_DROPPER` | 屏幕捕获 / MediaProjection | 单次取色 |

配套时间维度的防护：短信 OTP **延迟投递**（域名不匹配 3 小时 / SDK 37+ 标准短信 3 秒），直接针对「Agent 或恶意 App 抢读验证码」这一新攻击面。

**形态二：支付/履约边界由被调用方保留（国内实践，2026-07）**

- WAIC 演示（Amoo × 美团跑腿）：系统 Agent 完成地址推断与订单填写，**进入付款环节任务停在美团页面等待用户确认**。
- 支付宝 **AHA** × OPPO 小布（7-15）：小布理解需求、阿宝调用支付宝近 200 项生活服务，**关键授权与支付仍由用户确认**。
- 华为小艺「帮帮忙」（7-31 南都实测）可 GUI 操作支付宝/淘宝/拼多多，**微信提示「尚未接入」**。
- **三分边界成型**：**系统理解意图 / App 保留履约与支付 / 用户保留最终决定权**。确认权不再只是「弹窗与否」，而是「**在谁的界面上弹**」——落在被调用 App 的原生页面，才同时满足可审计与可追责（见 [[端侧执行通道 GUI 与 MCP 路线之争]]）。

**治理侧**：中国网络空间安全协会（2026-07-31）提出对手机助手/终端智能管家建立 **终端分级标识、可信开源代码安全** 体系；智能体**审计与交易**国家标准正在补齐（见 [[智能体互联国家标准与 AIP]]）。

## 可复用启发

- OS Agent 设计 Checklist：高危动作 = 系统级 Confirmation UI + 沙盒授权 + 可中断。
- **授权应是「系统代持 + 单次 + 字段级」**，而非把长期权限交给 Agent；能用系统选择器代替权限申请的，一律用选择器。
- **高危确认要落在被调用方的原生界面**（支付停在支付 App），这样责任链清晰、可审计。
- 归属判定（EntityOwnership）让确认提示更精准，减少误确认。

## 2026-08-01 增补：形态三——「可逆」补全四维安全（来源 [[AppIntent 每日情报 2026-08-01]]）

**阶跃 Step AOS 四维安全框架**：可信 / 可见 / 可控 / **可逆**，为本库补上此前缺失的维度。

- **新增「可逆」维度**：操作出错支持**一键撤回 + 任务中止**。时间轴补全为——**Confirmation UI 管「执行前」、隔离管「执行中」、Undo 管「执行后」**。Word 文档型 XPIA 蠕虫（见 [[文档型 XPIA 自传播蠕虫]]）恰恰证明「执行后才发现」是常态，因此「可逆」不是锦上添花，而是 Execution 闭环的必要一环。
- **「可控」的具体化**：Step AOS 的「**权限按需授予，任务结束自动回收**」，与 [[XPIA 跨提示注入]] 中记录的 Android 17「系统代持 + 单次 + 字段级」授权是同一思路的两种实现——Agent 不该长期持有权限。
- **治理侧互文**：这与「确认权应落在被调用方原生界面（支付停在支付 App）」的二分边界一致（见 2026-07-31 增补「形态二」），共同指向「系统理解意图 / App 保留履约与支付 / 用户保留最终决定权」。

## 2026-08-03 增补：路线分歧 + 第四维「确认内容完整性」（来源 [[AppIntent 每日情报 2026-08-03]]）

**A. 路线分歧坐实（Android 侧补一格）**：Android AppFunctions 官方指引把破坏性动作的确认**下放给 App 自己实现**（`While the agent might invoke them, your app should include its own confirmation step... add more than one confirmation step`），与 Apple 的**系统级 Confirmation UI + entity ownership** 是两条不同路线——Apple 体验一致但 App 灵活低；Android 灵活但一致性与可审计性全靠开发者自觉，且把安全成本转嫁给用户多次点击。这填补了本库四平台确认机制对比表此前缺的 Android 一格。

**B. 第四维升级：确认内容的完整性来自哪里？**（叠加 AIMS 的反向论点）

- 带外防御研究（arXiv 2606.26479）提出 **AIMS**：**「LLM MUST NOT hold credentials」，授权应由授权服务器完成，而非本地 UI 确认**。若 Agent 已被 ADI/IPI 污染，它呈现给用户的确认文案本身就是被操纵的产物——**用户确认的是攻击者写好的话，本地点击 ≠ 授权**。
- 确认机制三档判据（四平台目前都在 1–2 档）：
  1. **最弱**：Agent 自组织确认文案 → ADI 一破全破；
  2. **中等**：系统据结构化元数据渲染确认（Apple entity ownership 路线）→ 但元数据若可伪造仍不安全；
  3. **最强**：确认/授权走**带外**通道，由不可被模型影响的组件（[[Agent 身份与硬件级审批]]）完成。

## 2026-08-09晚 增补：Chrome 的「确认触发器由谁判定」——三档触发器分类法（来源 [[AppIntent 每日情报 2026-08-09-晚]]）

本笔记此前的三档判据讨论的是**确认内容从哪来**（Agent 自组织 / 系统元数据 / 带外）。Chrome 架构（**2025-12-08**，[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]）补上了一个正交且此前缺失的维度：**确认由什么触发**。

| Chrome 的确认触发点 | 触发判定方式 | 本库判读 |
|---|---|---|
| 导航到银行 / 医疗等敏感站点 | **确定性清单比对** | 高后果场景**不赌分类器准确率** |
| 用 Google Password Manager 登录 | **确定性**（且模型**无凭证访问权**） | 直接落实 AIMS「LLM MUST NOT hold credentials」 |
| 支付 / 发消息等后果性动作 | 确定性 + 模型混合（官方自陈"try to pause"、分类器仍在调准确率） | 语义类动作只能混合，**是承认的弱点** |

**新增判据（触发器三档，与既有「内容三档」正交，可组成 3×3 矩阵）**：

1. **最弱**：由**规划模型自己**决定何时该问用户 → 被污染的模型可以选择不问；
2. **中等**：由**独立分类器 / 评判模型**决定 → 好于①，但准确率有边界（Chrome 自陈 `"cannot flag everything"`）；
3. **最强**：由**确定性规则**决定（清单、动作类型、资产敏感度）→ 不可被内容影响。

**这条对 OS 意图框架的直接含义**：四平台目前在「确认内容」上普遍处于 1–2 档，而在「确认触发器」上更弱——Android 把确认**整体下放给 App**（见上方 08-03 增补 A），意味着**触发时机也由 App 自定**，系统无法保证「危险动作一定会弹窗」。**Chrome 的做法反过来说明：触发器应当由系统按动作类型确定性判定，而不是交给可被影响的一方。** 落到 Registry 设计上，即 intent 声明中应带**系统可读的后果性标记**（不可逆 / 涉资金 / 涉凭证），由系统而非 App 决定是否强制确认。

**另一条正交形态：事后知情**。Google 官方六层防御中的 **End-user security mitigation notifications**（见 [[XPIA 跨提示注入]] 2026-08-09晚 增补）与 Chrome Enterprise 在 **Chrome History 中把 agent 导航页面显式标记为 agent actions**，共同构成「确认」之外的第二类用户在环形态——**事前确认管授权，事后标记管追溯**。后者成本远低，且是可追溯性合规的低成本抓手，四大 OS 意图框架**均无对应物**。

## 2026-08-15 增补：Trust Insights 作为 coerced-intent 互补信号

> 来源：[[AppIntent 每日情报 2026-08-15]]。

Trust Insights（WWDC26 Session 379）检测的是「用户是否正被社会工程胁迫而发出**非自愿**意图」，与 Confirmation UI 的「用户主动授权」**正交**——前者是**执行前意图真实性检查**（coerced intent authenticity），后者是**执行前授权确认**。二者叠加构成「双重闸门」：即便用户点了确认，若意图被判定为受胁迫，仍可拦截。

注意：Trust Insights 是 **App 集成能力**（通过 `com.apple.developer.trustinsights.base` entitlement 接入），**不是 OS 总线级强制**；其落地依赖开发者接入 `InsightEvaluator` / `IsLikelyBeingCoachedInsight`，因此与本笔记既有判据「确认应是系统级强制层而非交给开发者」形成张力——它补的是「意图真实性」这一确认机制此前完全缺失的维度，但落点仍在 App 侧。详见 [[Trust Insights 意图 coercion 检测框架 2026]]。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]] ｜ [[AppIntent 每日情报 2026-08-09-晚]]
- 触发器分类法来源：[[Chrome Agent Origin Sets 与用户对齐评判器 2026]] ｜ 确定性原则：[[带外防御与确定性门控]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入：[[XPIA 跨提示注入]] ｜ 蠕虫：[[文档型 XPIA 自传播蠕虫]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[Agentic OS 意图调度内核]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入防护：[[XPIA 跨提示注入]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]

## 2026-08-16 增补：Session 347 副作用轴 = 触发器三档里的「确定性规则」实例（来源 [[AppIntent 每日情报 2026-08-16]]）

> 接续本笔记 2026-08-09晚 的「触发器三档分类法」。Apple Session 347 的**风险元数据（副作用轴）驱动确认**是「第 3 档·确定性规则触发」在 OS 意图框架里的首个官方实例。

- Session 347：系统用**静态风险元数据（基于意图副作用）+ 动态系统状态**做风险评估，高风险（destructive / exfiltration / shared-content update）**更可能触发确认**；确认触发由**系统按动作类型确定性判定**，不交给 App 或模型自决。
- 这直接坐实本笔记 08-09晚 的结论：「**确认触发器应由系统按动作类型确定性判定，而非交给可被影响的一方**」。Apple 用「副作用分类」落实了这一点；对照 Android 把确认整体下放 App（本笔记 08-03 增补 A），两平台在「触发器归属」上仍处对立路线。
- 与新建 [[意图风险元数据与鉴权策略棘轮 2026]] 互补：该节点记副作用轴分类与鉴权棘轮机制，本节点记「它属于哪种确认触发器档位」。

## 2026-08-17 增补：Apple 硬件级确认锚点——Secure Enclave「Secure intent」（来源 [[AppIntent 每日情报 2026-08-17]]）

> 接续本笔记 08-09晚「触发器三档」与 08-16「副作用轴 = 第 3 档确定性规则」。本期补一个**硬件层**确认锚点，是「最强档（带外/不可被模型影响）」在 Apple 平台的既有实例。

- **Secure intent（Apple Platform Security）**：一条**物理链路**——从物理按键（Face ID 双击 / Touch ID 指纹）直连 **Secure Enclave**，**完全绕过操作系统与 Application Processor**。即使拥有 root 权限或内核级软件也**无法伪造**用户意图确认。
- 当前用途：Apple Pay 交易确认、Magic Keyboard with Touch ID 与 Mac 配对终结。支持 iPhone X+ / Apple Watch S1+ / iPad Pro 全系 / iPad Air(2020) / Apple silicon Mac（T2 机型有等价机制）。
- **对确认机制分层的位置**：它把本笔记「三档触发器 / 三档内容」里的**最强档（带外、物理、不可被模型影响）**落到了硬件——与 AIMS「LLM MUST NOT hold credentials」、[[Agent 身份与硬件级审批]] 同构。App Intents 的**软件层风险元数据确认**（08-16 副作用轴）是「第 3 档确定性规则」，而 Secure intent 是「第 3 档的硬件根」——两者互补：软件层管「动作多危险要确认」，硬件层管「这次确认本身是不是真人按的」。

⚠️ 口径：Secure intent 是 Apple Platform Security 既有机制（非 2026 新发布），本次作为「确认机制硬件锚点」补入本库；它**不接入 App Intents 总线**，目前仅用于支付/配对等高敏场景，是否扩展到 agentic intent 确认待官方。

#标签/安全 #标签/ConfirmationUI #标签/StepUpAuth
