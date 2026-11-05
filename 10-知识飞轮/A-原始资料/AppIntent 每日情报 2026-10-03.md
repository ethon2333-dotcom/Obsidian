---
date: 2026-10-03
tags: [情报, AppIntents, 系统级意图框架, 端侧Agent, 执行安全, XPIA, Apple, 权限治理]
source:
  - https://developer.apple.com/news?id=p6zjojqw
  - https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/
  - https://www.theverge.com/tech/1004295/apple-limit-mac-disk-access-ai-agents
  - https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/
  - https://news.future-shock.ai/the-signal-october-3-2026
  - https://k.sina.com.cn/article_1826017320_6cd6d02802001xeaw.html
  - https://developer.apple.com/documentation/updates/appintents
  - https://developer.android.google.cn/jetpack/androidx/releases/appfunctions
importance_score: "★★★★☆"
intent_category: 执行安全 / OS 权限治理 / 确认机制
---

# AppIntent 每日情报 2026-10-03（系统级 Agent 与 OS 意图框架前沿）

> [!abstract] 30 秒速览
> - **核心突破**：本窗口（2026-10-02 21:01 → 10-03 21:01）**四大 OS 官方框架层仍零净新增 API**（iOS 27.1 无新 `@AppIntent(schema:)` Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 无新 Registry API）。唯一 OS 级真增量 = **Apple 于 2026-10-02 在 Developer News 发布「Updates to Full Disk Access in macOS」**——宣布将 Full Disk Access（FDA，macOS 最宽泛的文件权限）改为「仅能以非常明确的用户操作授予」，并**首次把 AI 智能体的自主能力增长作为该权限 redesign 的官方理由**（★7/10）。
> - **关键指标**：Apple 原文逐句——「As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially.」FDA 暴露文件 / 邮件 / 信息 / 浏览历史；macOS 27 路径 `System Preferences > Privacy & Security > Full Disk Access`。Apple **未公布版本 / 时间 / 形态**（forward-looking 政策信号，非同日生效的 API 变更）。
> - **OS Agent 执行安全**：Apple 加入 Windows（Agent Workspace 低权账号 + ODR 三档 consent）/ Android（`EXECUTE_APP_FUNCTIONS` 门控 + `setAppFunctionsPolicy`/`APP_FUNCTIONS_DISABLED`）/ Microsoft Digital Defense Report 2026（agent 身份 / 权限 / prompt injection / revoke）的「**agent 执行边界 = OS 权限 / 隔离 / 确认边界**」收敛。直接对应 [[确认机制]] / [[隔离执行]] / [[XPIA 跨提示注入]]。

## ① Schema 定义与语义路由机制（四大 OS 框架层）

**Apple（AppIntents 无净新增；macOS 权限层有治理信号）**：`developer.apple.com/documentation/updates/appintents` 最新条目仍为 **June 2026**（App schema domains / `IndexedEntityQuery` / `OwnershipProvidingEntity` / `EntityCollection` 等），**无 October 新 Schema API**。iOS 27.1 首个 beta **仍未放出**，无新 `@AppIntent(schema:)` Schema。但本窗口 Apple 在**桌面 OS 权限层**（非 AppIntents Schema 层）发出新治理信号——macOS Full Disk Access 收紧（见②），属执行安全 / 权限模型范畴，与 AppIntents Schema 正交。延续「OS 框架不日更」。

**Android（无净新增）**：`developer.android.google.cn/jetpack/androidx/releases/appfunctions` 最新仍为 **`1.0.0-alpha12`（2026-09-23）**；本窗口检索（含官方 release notes 与 alpha-channel）**无 alpha13 信号**。`a2ui` 守 `1.0.0-alpha01`。无新 Registry/权限/scope API。

**HarmonyOS（无净新增）**：HC2026（9-17~21）内容已覆盖；本窗口检索命中的均为 HDC2026 / HarmonyOS 7 Beta1 / 7.0 Beta1 旧文，**无新框架/API**。Intents Kit（Want）/ 元服务（installationFree）/ ArkAF 2.0（意图/Skills/A2A 三层）/ A2UI 不变。

**Windows（无净新增）**：26H2 已 GA（09-29），本窗口**无新 Registry API**。ODR / Agent Workspace / Copilot Actions / Copilot Vision 四支柱维持 09-30 状态。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**★7/10 真增量：Apple macOS Full Disk Access 收紧（2026-10-02，Apple Developer News）**。Apple 发布「Updates to Full Disk Access in macOS」，要点（原文逐句）：

- FDA「largely sidesteps」macOS 为保护用户数据设置的常规控制，原用于让备份应用正常工作。
- 部分开发者以可能危及用户安全的方式使用该权限——授权后应用可访问系统中的**文件、邮件、信息，甚至浏览历史**；通讯类应用还会**危及用户通讯对象的隐私**。
- 「Going forward, we will introduce additional controls to ensure that users who genuinely wish to grant an app this extraordinary level of access can only do so with **very explicit user action**.」
- 「**As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially.**」
- Apple 强调要让用户在授权前「clearly understand these risks」。

**为什么是执行安全增量（OS PM 视角）**：FDA 是 macOS TCC 的**例外权限**——它绕过了 Mail / Messages / Safari 历史等逐项隐私提示，让一个 app 看到本需显式同意才能访问的一切。传统 app 拿 FDA 做固定工作（备份文件夹）；而 **agent 会读看起来与任务相关的任何内容、可能被网页/文档中隐藏的指令引导、并可能把内容发往远端模型**——文章本身点明：授予 agent 同一 blanket 权限后，**单次 prompt injection 即可暴露多年消息**。Apple 把「显式用户动作」作为新门控，等于把 agent 执行边界收口到 OS 权限/确认边界，与四平台其他三家的方向同构（见下）。

**语境（非 Apple 裁定）**：TechCrunch / The Verge 把时机与两起事件关联——① Inc. 专栏作者 Jason Aten 称 Meta 的 Muse agent 读了其私信；Meta 反驳称 Muse 仅在用户**同时开启 FDA 与 Muse 的 Messages connector** 时才能读 Messages，且可随时撤销；② 既往 Wired 报道的 ChatGPT Mac 客户端漏洞。两起均未被独立证实，是「agent 时代风险」的语境，非 Apple 裁定结论。

**跨平台收敛（本笔记核心结论）**：四平台在「agent 执行边界 = OS 权限/隔离/确认边界」上收敛——
- **Windows**：Agent Workspace 独立会话 + 低权限账号 + ACL + Agent ID 审计；ODR 三档 consent（Ask every time / Allow always / Never allow）。
- **Android**：`EXECUTE_APP_FUNCTIONS` 仅限可信 caller（如 Gemini）；`setAppFunctionsPolicy` + `APP_FUNCTIONS_DISABLED` 可经 MDM 全局禁用 AppFunctions 数据给 on-device agents。
- **Apple（本窗口新增）**：macOS FDA 改为「仅非常明确的用户动作」可授予，首次把 agent 自主性列为理由。
- **Microsoft（跨窗口权威，2026-10-01 Digital Defense Report 2026）**：专章「securing AI agents」——agent 身份、权限、prompt injection、revoke access 四件套，报告称攻击者已用 AI 做侦察/钓鱼/恶意软件/漏洞编写。
- 含义：从「应用权限」到「agent 权限」的范式迁移正在四平台同步发生；差异只在**门控颗粒度**（Apple=显式动作 / Windows=低权账号+consent 时长 / Android=caller 白名单+MDM 开关 / Microsoft=身份+revoke）。

**性质判定**：非新 OS API（是 Apple 对 FDA 权限模型的 forward-looking 政策信号，未给版本/时间/形态），但属 **Apple 桌面 OS 首次将权限边界与 agent 风险显式绑定**，达 ★7/10 收录阈值；是四平台收敛叙事的关键拼图。→ 新建 B 节点 [[Apple 桌面 Agent 权限治理 macOS Full Disk Access 2026]]。

**去伪/无新增（已复核）**：BFCL v4 仍 Llama 3.1 405B **88.5%** 居首（benchlm.ai 10-02 更新、anotherwrapper 10-03 更新一致）；端侧 MiniCPM5-2B 66.6 / LFM2.5-8B-A1B 49.7 / Needle2 42.6 / FunctionGemma-270m 27.03 **无新端侧 Planner 入榜**；Qwen3-0.6B tool-router BFCL v4 54.08（think）/ 29.17（no-think）为既有数据（LittleLamb ONNX 卡，非本窗口新）。XPIA 本窗口无新 CVE / 研究突破（RAMPART / agentmelt / Zylos 等维持既有状态）。

## 诚实标注 / 待办

- Apple **未公布** FDA 新管控的具体形式 / 版本 / 上线时间；是政策信号，非同日生效的 API 变更——「very explicit user action」究竟是多一步对话框还是更细的 per-folder 粒度，待 beta 落地后逐字复核。
- Meta Muse 读私信指控**未被独立证实**；Wired ChatGPT Mac 漏洞为既往报道；二者均非 Apple 裁定，仅作语境。
- 看哪个 macOS beta 落地、是否进 WWDC session；与 App Store 审核收紧（policy notice 后通常跟进）联动待观察；FDA 收紧是否影响依赖它的工具（Alfred / PopClip / Hazel / Setapp 套件）待开发商反馈。
- 沿用在跑待办：iOS 27.1 beta / 公开版（10-19~23 第三方预期）是否带新 Schema；Per-Intent Privacy Manifest 官方逐字；AppFunctions alpha13 / A2UI alpha02；Watch OS 26；高通 NPU exact specs；Berkeley 官方 BFCL v4 博客；多智能体注入一手论文 / 自复制注入 OpenAI 原文。

> [!note] 概念节点双链
> - [[Intent Schema Protocol 意图模式规范]]
> - [[Intent Router 语义路由]]
> - [[Function Calling 端侧工具调用]]
> - [[Confirmation UI 安全机制]]
> - [[Atomic Service 元服务]]
> - [[Agent Workspace 隔离执行]]
> - [[A2A 端侧智能体协议]]
> - [[XPIA 跨提示注入]]
