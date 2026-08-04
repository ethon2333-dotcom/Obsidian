---
type: concept
status: draft
derived_from: "[[AppIntent 跨平台情报简报 2026-07-30]]"
tags: [AppIntent, 安全, XPIA, 注入, 概念]
---

# XPIA 跨提示注入

## 一句话定义

**XPIA（Cross-Prompt Injection Attack）** 是在 UI、文档、网页或屏幕内容中嵌入恶意指令，劫持正在运行的操作系统 Agent，使其执行非用户本意的操作（如借 Agent 权限发消息、转账、泄露数据）。

## 为什么重要

- 系统级 Agent 拥有真实的跨 App 操作权限，XPIA 是其头号新型攻击面（Windows 已将其单列风险）。
- 与传统 prompt injection 不同：XPIA 来源是「环境上下文」（屏幕/文档），而非用户对话，更难靠对话过滤拦截。

## 适用边界

- 任何具备屏幕感知（Copilot Vision / Android UI Automation）或多源输入的 OS Agent 都暴露此风险。
- 缓解不能只靠模型对齐，必须架构层防护。

## 证据与例子（四平台防护对照）

| 平台 | 主要缓解手段 |
|------|--------------|
| Windows | ODR 受控发现 + Agent Workspace 隔离会话 + 用户始终在环（interruptible） |
| Apple | 系统级 Confirmation UI 拦截高危 Intent；`OwnershipProvidingEntity` 差异化提示 |
| HarmonyOS | 可信设备能力协商；上下文充足免二次确认；跨设备安全通道 |
| Android | UI Automation 敏感动作「执行前预警」+ 用户接管 |

## 可复用启发

- OS Agent 设计 Checklist：受控发现（ODR）+ 隔离执行（[[Agent Workspace 隔离执行]]）+ 高危确认（[[Confirmation UI 安全机制]]）+ 用户可中断。
- 对屏幕感知能力（Copilot Vision 类）默认 session-bound + 显式 opt-in。

## 2026-08-01 增补：从「一次注入」到「注入会繁殖」（来源 [[AppIntent 每日情报 2026-08-01]]）

**Copilot for Word 文档型 XPIA 蠕虫**（Håkon Måløy《Context Collapse, Part 3》，与 MSRC 协调披露 2026-07-28）把本库的威胁模型推过拐点：XPIA 不再只是「一次注入」，而是**会把自己复制进被生成的新文档**，使被污染的内部产物成为下一轮会话的载体。MSRC 协调披露 **144 天后，漏洞「类别」仍未关闭**——模型从 GPT-5.5 升到 GPT-5.6 仍复现。

**四道既有防线对「一次性攻击」的假设全部被打破：**
- **隔离失效**：[[Agent Workspace 隔离执行]] 能隔离「Agent 执行域」，但隔离不了被污染的产物在同事之间正常流转（载体是一份看起来完全合法的内部文档）。
- **确认失效**：Confirmation UI 拦「敏感动作」（付款/发信/删除）；而「改一份草稿里的财务数字」是 Copilot 本职，不触发任何确认。
- **审计失效**：每一次传播都是一次「合法的内部创作事件」，审计日志看不出异常。
- **溯源失效**：第二代载体已不需要原始攻击文件在场。

**新增设计原则（已写入 [[Agent 写回路径 XPIA 风险评估 SOP]] 与 [[文档型 XPIA 自传播蠕虫]]）：** 凡 Agent 具备「写回」能力的路径，必须评估「注入能否自我复制」。判据三问：① Agent 能否修改会被他人复用的产物？② 该产物会不会再次进入 Agent 上下文？③ 修改本身是否属于 Agent 正常职责（不触发确认）？三问全「是」= 蠕虫风险。

**企业侧诚实结论**：没有任何客户侧开关能完整解决该类别，只能靠卫生措施降低频率。给 CISO 的答案是「**载荷修了，类别没修**」。

## 2026-08-03 增补：ADI 把威胁模型推过第三个拐点（来源 [[AppIntent 每日情报 2026-08-03]]）

首尔国立大学团队（arXiv 2607.05120，2026-07-06；CSA 简报 07-18）提出 **ADI（Agent Data Injection，智能体数据注入）**，把本库对「注入」的定义整个改写：

- **此前假设被打破**：所有 XPIA 研究与防御都假设「攻击 = 伪装成数据的指令」，于是去过滤祈使句、找命令式语气。ADI 反过来——**攻击者只伪造 Agent 视为可信的结构化元数据**（元素 ID、数据来源标记、发件人字段、工具调用/响应格式），Agent 全程没读到一句指令，却自己得出错误结论。
- **同环境对照（论文/CSA 口径，未复现）**：经典指令注入成功率 **0–0.7%**，ADI 在 JSON 数据 **31.3–43.3%**、网页 DOM **33.3–100%**、真实商用 Agent（无专用工具）**最高 50%**。六款商用 Agent（Claude in Chrome / Antigravity / Nanobrowser / Claude Code / Codex / Gemini CLI）全部中招。
- **防御评估**：输入/输出过滤器完全失效；CaMeL Strict **唯一归零（0%）**，但可用性从 **81.2–84.8% → 36.5%**。作者结论：**「current agents do not isolate trusted data from untrusted data」**——这是架构级缺失，类比 Agent 时代的 SQL 注入，靠加过滤器无效。
- **四平台靶面（均待补，无一家公开 ADI 类别评估）**：Apple `.appEntityIdentifier` / View Annotations 的实体标识符（恰是 ADI 场景一靶心）、Android `AppFunctionMetadata` / `app_metadata`、HarmonyOS A2A 消息格式、Windows Agent Workspace 内工具格式。详见 [[Agent Data Injection 数据注入攻击]]。
- **与 Stored IPI 同源**：姊妹论文 DualView（arXiv 2607.03821）证明传统隔离对存储型注入仍 53.3% 失守，提出数据视图隔离原语，见 [[Dual View 智能体数据视图隔离]]。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]]
- 写回风险：[[Agent 写回路径 XPIA 风险评估 SOP]] ｜ 蠕虫范式：[[文档型 XPIA 自传播蠕虫]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 确认：[[Confirmation UI 安全机制]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]]

#标签/XPIA #标签/安全 #标签/注入
