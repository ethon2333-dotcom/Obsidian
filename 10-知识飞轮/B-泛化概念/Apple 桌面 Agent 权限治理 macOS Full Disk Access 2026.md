---
type: concept
status: draft
derived_from: "[[AppIntent 每日情报 2026-10-03]]"
tags: [权限治理, 执行安全, Apple, macOS, FullDiskAccess, 确认机制, 隔离执行]
---

# Apple 桌面 Agent 权限治理（macOS Full Disk Access，2026）

## 一句话定义
Apple 在 macOS 上把最宽泛的文件权限 **Full Disk Access（FDA）** 改为「仅能以非常明确的用户操作授予」，并**首次把 AI 智能体的自主能力增长作为该权限 redesign 的官方理由**——标志 Apple 桌面 OS 将「权限边界」与「agent 风险」显式绑定。

## 为什么重要
- **范式迁移信号**：从「应用权限」到「agent 权限」。FDA 是 macOS TCC 的例外权限，绕过 Mail / Messages / Safari 历史等逐项隐私提示，让一个 app 看到本需显式同意才能访问的一切。传统 app 拿 FDA 做固定工作（备份文件夹）；而 **agent 会读任务相关的任何内容、可能被网页/文档中隐藏的指令引导、并可能把内容发往远端模型**——授予 agent 同一 blanket 权限后，**单次 prompt injection 即可暴露多年消息**。
- **四平台收敛拼图**：Apple 加入 Windows（Agent Workspace 低权账号 + ODR 三档 consent）/ Android（`EXECUTE_APP_FUNCTIONS` 仅限可信 caller + `setAppFunctionsPolicy`/`APP_FUNCTIONS_DISABLED`）/ Microsoft（Digital Defense Report 2026：agent 身份 / 权限 / prompt injection / revoke）的「**agent 执行边界 = OS 权限 / 隔离 / 确认边界**」叙事，补齐此前 Apple 桌面侧在该收敛上的空白。
- **OS PM 启示**：桌面 agent 的「可达性」应默认走**最小化、scoped、显式确认**的 OS 权限，而非 blanket 例外权限；这与移动端 AppIntents / AppFunctions 的「能力注册 + 调用方鉴权」同源。

## 适用边界
- **范围**：macOS 桌面；FDA 是 TCC 例外权限（原用于备份应用）。**iOS / iPadOS 默认数据隔离**，app 间数据互不可见，不受 FDA 逻辑影响——Apple 原文也点明「iPhone/iPad 默认隔离，Mac 的 FDA 是 deliberate exception」。
- **状态**：Apple **未公布**新管控的具体形式 / 版本 / 上线时间；是 **forward-looking 政策信号**，非同日生效的 API 变更。「very explicit user action」究竟是「多一步对话框」还是「per-folder 细粒度」，待 beta 落地后逐字复核。
- **不推翻**：与 AppIntents Schema Protocol 正交（FDA 是桌面 OS 权限层，非意图 Schema 层）；与「意图 Registry 来源/provenance 轴四平台全空白」结论无关（见 [[四平台意图 Registry 来源轴与权限模型对比 2026]]）。

## 证据与例子
- **一手（Apple Developer News，2026-10-02，「Updates to Full Disk Access in macOS」）**：
  - 「Full Disk Access largely sidesteps these controls in order to allow backup apps to function properly on the Mac.」
  - 「some developers are using Full Disk Access in ways that could put users at risk, exposing everything on their systems—including files, mail, messages, and even browsing history—without users' full knowledge and understanding.」
  - 「users who genuinely wish to grant an app this extraordinary level of access can only do so with **very explicit user action**.」
  - 「**As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially.**」
- **语境（非 Apple 裁定）**：TechCrunch / The Verge 关联两起事件——① Meta Muse agent 被称读了用户私信（Meta 反驳：需同时开 FDA + Muse Messages connector，可撤销）；② 既往 Wired 报道的 ChatGPT Mac 客户端漏洞。均未被独立证实。
- **现状路径**：macOS 27 中 FDA 位于 `System Preferences > Privacy & Security > Full Disk Access`，列出所有请求过该权限的 app，逐项开关可随时撤销。

## 可复用启发
- **桌面 agent 构建者**：不要把 FDA 当默认；只申请功能真正需要的文件夹/数据类型，用 Apple scoped file picker，显式解释为何需要访问，并**记录 agent 读了什么、敏感内容尽量留端**——与 Apple 信号方向一致。
- **确认机制设计**：OS 级「显式用户动作」是 agent 可达性门控的最外层兜底；它应与 [[确认机制]]（sensitive/destructive 操作的 step-up 确认）、[[隔离执行]]（scoped access vs blanket）配合使用，而非替代。
- **跨平台对照模板**：评估任一平台的 agent 执行安全时，按四维度打分——① 调用方身份/白名单（Android EXECUTE_APP_FUNCTIONS caller）② 隔离账号/容器（Windows Agent Workspace）③ 确认/consent 颗粒度与持久化（ODR 三档 / Apple 显式动作）④ revoke 能力（Microsoft 身份+revoke）。

## 关联
- 来源：[[AppIntent 每日情报 2026-10-03]]
- 方法/概念：[[确认机制]]（显式用户动作即确认 UI 的 OS 级前置）、[[隔离执行]]（scoped access vs blanket FDA）、[[XPIA 跨提示注入]]（单次注入暴露多年消息）、[[Confirmation UI 安全机制]]
- 跨平台对照：[[Windows Copilot Actions 与 Agent Workspace 2026]]（Agent Workspace 低权账号 + ODR consent）、[[Android AppFunctions 设备侧意图 2026]]（EXECUTE_APP_FUNCTIONS 门控 + setAppFunctionsPolicy）、[[四平台意图 Registry 来源轴与权限模型对比 2026]]（权限模型收敛）、[[Agent 身份与硬件级审批]]
- 待正交澄清：与 [[Apple AppIntents Schema Protocol 2026]] 不同层（FDA=桌面 OS 权限；AppIntents=iOS 意图 Schema），不可混为一谈。
