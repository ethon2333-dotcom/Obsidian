---
date: 2026-10-08
tags: [AppIntent, 每日情报, Windows, Apple, MXC, iOS272, 执行安全]
source: "https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ ; https://www.it-connect.tech/microsoft-turns-windows-into-an-ai-agent-platform-with-mxc-local-models-and-rtx-spark-pcs ; https://tldrdailynews.com/news/technology/technology/apple-seeds-third-ios-272-beta-skipping-271-to-protect-iphone-duo-launch-pbr3qrkohk"
importance_score: "★★★★☆"
intent_category: "执行安全 / 系统级意图框架"
---

# AppIntent 每日情报 2026-10-08

> [!abstract] 30 秒速览
> 本窗口（2026-10-07 21:00 → 10-08 21:00）四大 OS 官方框架层中，**唯一 OS 级净新增 = Windows Microsoft Execution Containers (MXC) 于 2026-10-07 正式 GA**（preview → GA：开源沙箱、五档隔离、agent 身份分离、`/sandbox` 启用、GitHub Copilot+Defender 实测拦截）——是 09-13 IFA 预览以来的首个 GA 级增量。Apple 侧**事实收口**：Apple 跳过 iOS 27.1 beta、直发 iOS 27.2 beta 3（24B5099f），27.1 为 iPhone Duo 折叠屏专属预装版，常规线无新 `@AppIntent(schema:)` Schema。Android（alpha12 无 alpha13）、HarmonyOS（无新 API）、BFCL v4（端侧 Planner 无新入榜）均零净新增；OWASP 2026 重排 + ACS、llama.cpp/Langflow CVE 等非四平台 OS 框架，按口径丢弃。

## ① Schema 定义与语义路由（本窗口）

| 平台 | 本窗口 Schema/路由层净新增 | 重要性 | 处置 |
|---|---|---|---|
| Apple | 无（iOS 27.2 beta 3，build 24B5099f，无新 `@AppIntent(schema:)` / App Intents Domains API；27.1 为 Duo 专属、不开放 beta） | — | 已复核·无净新增（事实收口：跳过 27.1） |
| Android | 无（AppFunctions 守 `alpha12`，无 `alpha13`；无新 schema/routing API） | — | 已复核·无净新增 |
| HarmonyOS | 无（Intents Kit 官方页稳定；A2UI 守 alpha01；无新 API） | — | 已复核·无净新增 |
| 跨平台 BFCL | 无（端侧 Planner 无新入榜；Qwen3.7 Max 75.0% 居首快照稳定） | — | 已复核·无净新增 |

要点：
- **Apple 跳号事件**（★6/10，事实收口）：Apple 于 09-17 直发 iOS 27.2 beta 1、跳过 27.1；最新 27.2 beta 3（24B5099f）。媒体共识 = 防 Duo 代码经 27.1 beta 解包泄露；故常规 iPhone 用户在新 Schema 上**无新增**。下个观察点：10-23 Duo 首发随附的 iOS 27.1 正式版是否带来双屏场景新 intent/entity schema。
- Android / HarmonyOS / BFCL：均无路由/评测层净新增，延续「OS 框架不日更」。

## ② 系统安全与 UX（Confirmation / 隔离 / 反注入）

### 🔑 真增量①：Windows Microsoft Execution Containers (MXC) 正式 GA（★7-8/10，OS 框架 GA 级增量）
- **GA 时间/事件**：2026-10-07 旧金山「Hybrid Intelligence」活动（Satya Nadella + Pavan Davuluri + Jensen Huang）宣布 MXC 在 Windows 11 **正式 GA**（此前 preview）。来源：官方博文 <https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/> + it-connect.tech / pymnts / ainewsbank 多家 corroboration。
- **机制**：开源执行沙箱；组织运行时定义 agent 可访问的**文件与网络边界**并强制策略。隔离五档可调：**进程 / 会话 / WSL 容器（WSLc）/ 虚拟机 / Windows 365 for Agents**。
- **身份分离（第二支柱）**：每个动作归到 **agent 而非用户**；现场 GitHub Copilot 演示——agent 遵从网页恶意指令，**Defender 拦截动作并切断该 agent 对 SharePoint 的访问、不影响用户本人**——证实用户/agent 双身份。
- **启用与生态**：Copilot CLI `/sandbox`、GitHub Copilot app 按项目开启；默认 agent 写项目文件夹、系统其余只读/不可达；shell/本地 MCP/语言 server 隔离。已支持 OpenAI Codex / GitHub Copilot / OpenClaw / Replit / LM Studio / NVIDIA OpenShell / Unsloth AI；后续 Claude Code / Perplexity / Manus / Raycast 等；Meta **Muse for Windows** 即将接入。原生隔离：Windows=ProcessContainer / macOS=Seatbelt / Linux=bubblewrap。
- **沙箱外盲区（诚实标注）**：内置文件工具、远程 MCP server 不在 OS 级沙箱内，须叠加 [[确认机制]] + 流量级检测（Project Perception）。
- **归属**：关闭本笔记「MXC 何时 GA」待办；与 07 月独立账号+ACL、09-13 容器级、09-15 签名吊销构成**账号→文件夹→容器→连接器→身份**五层隔离/治理栈。详见 [[Windows Copilot Actions 与 Agent Workspace 2026]] 10-08 增补 + [[Agent Workspace 隔离执行]] 10-08 增补。

### 真增量②（事实收口，★6/10）：Apple 跳过 iOS 27.1 beta、iOS 27.2 beta 3 无新 Schema
- 详见 [[Apple AppIntents Schema Protocol 2026]] 10-08 增补；本窗口 Apple 侧无新 `@AppIntent(schema:)` API，框架稳定。

### 去伪/丢弃（按口径）
- **OWASP 2026 LLM Top 10 重排 + Agent Control Standard (ACS v0.1)**：属跨平台治理/标准文档，**非四平台 OS 框架执行总线 API**，按任务「聚焦 OS 级框架」丢弃（同此前 OWASP 处置）。
- **XPIA CVE（llama.cpp CVE-2026-107183 / Langflow CVE-2026-97676~97680 等）**：经核查为**工具链/应用层**漏洞（推理框架/低代码平台），**非四平台 OS 框架执行总线**，按口径丢弃（同 10-06 丢弃 GitLab AI Gateway、10-05 丢弃 MCP 工具链 CVE）。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
