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

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入：[[XPIA 跨提示注入]] ｜ 蠕虫：[[文档型 XPIA 自传播蠕虫]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]] ｜ [[Agentic OS 意图调度内核]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 注入防护：[[XPIA 跨提示注入]]
- 平台：[[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[Android AppFunctions 设备侧意图 2026]]

#标签/安全 #标签/ConfirmationUI #标签/StepUpAuth
