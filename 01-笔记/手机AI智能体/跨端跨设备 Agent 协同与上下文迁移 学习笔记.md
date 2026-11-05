---
title: 跨端跨设备 Agent 协同与上下文迁移
tags: [cross-device, agent-orchestration, continuity, context-migration, 端侧, 超级终端, 分布式, 手机AI智能体]
created: 2026-10-27
source: 厂商官方文档(Apple/Google/华为开发者联盟/Samsung/Microsoft)+ 权威媒体(Applemagazine/AppleInsider/新华网/自由时报3C/EEWorld 等)。具体年份与数字以「待核实」标注处需二次核验。
---

# 跨端跨设备 Agent 协同与上下文迁移

> **心智模型：** 跨端协同的本质不是"把 App 搬到另一块屏幕"，而是把**用户意图、会话上下文与任务进度**作为一等公民，在手机/PC/车机/手表/家居/眼镜之间做**无感续接**——这是 Apple Continuity 的"动作接力"在 AI 时代的升维：从"搬运活动"到"搬运意图"。

---

## 一、定义（广度）

**跨端跨设备 Agent 协同**：在异构设备形态（手机、PC、平板、车机、手表、智能家居、AR/VR 眼镜、可穿戴）之间，Agent 以统一身份协作，将**会话/上下文/用户状态/任务进度**跨端迁移与续接，使"任务先行、设备随后"，而非"先想清楚用哪台设备"。

它与单设备内跨应用编排的差异见 [[OS 级系统 Agent 与跨应用自动化 学习笔记]]（那篇聚焦"一台设备内"的 App 编排）；与端侧个性化/联邦隐私的差异见 [[端侧模型的个性化隐私联邦边界 学习笔记]]（那篇聚焦"个性化与隐私联邦"，本篇聚焦"跨设备协同与上下文迁移"）。鸿蒙侧的落地形态可串接 [[HarmonyOS 元服务 学习笔记]]。

---

## 二、分类（按协同粒度 / 迁移对象分层）

**按协同粒度（从底到顶）**
| 层级 | 职责 | 代表技术 |
|---|---|---|
| 1. 设备发现与配对 | 无感发现、双向认证、信任建立 | Apple 近场+Apple Account；华为 Hichain；Matter 配码 |
| 2. 连接/传输 | 异构网络自动组网、低时延链路 | 分布式软总线、蓝牙/Wi-Fi/UWB 抽象层 |
| 3. 会话/上下文迁移 | 对话历史、屏幕状态、意图重建 | iCloud 同步 Siri 对话、Cross-device Sessions |
| 4. 任务/能力编排 | 谁执行、算力/硬件池化、进度续接 | 超级终端、HMAF、Cross-Device Resume |
| 5. 统一身份与权限 | 跨端身份、授权、隐私边界 | Apple Account、三星账号、Matter 多 Admin |

**按迁移对象**
- 会话/对话历史（Siri AI 跨设备同步、Copilot 跨端续写）
- 应用状态/任务进度（Handoff、应用流转、Cross-Device Resume）
- 用户上下文（位置/健康/日程/情境，随设备传感器变化）
- 媒体/文件（Universal Clipboard、一碰传、拖放）
- 硬件/算力能力（分布式摄像头、GPU 池化、Nearby 算力调用）

---

## 三、主流方案（广度表格）

| 厂商/阵营 | 协议/框架 | 核心能力 | 状态 |
|---|---|---|---|
| Apple | Continuity / Handoff + Apple Intelligence | Handoff、通用剪贴板、iPhone 镜像、跨设备 Siri 对话同步、Spatial Preview | 已商用（iOS/macOS/watchOS/visionOS）；部分 AI 能力 2026 beta，**版本命名与可用性待核实** |
| Google | Cross-device SDK + Adaptive Android / Android XR | 设备发现/安全连接/多设备会话（Sessions API）、自适应多形态 UI | Cross-device SDK 仍处 **Developer Preview，生产可用性待核实** |
| Samsung | SmartThings + One UI Seamless（"One Samsung"） | 应用程序流转、多重控制（Multi Control）、Galaxy Buds 自动切换、健康同步 | 已商用（One UI 7.0+） |
| Huawei | 分布式软总线 + 超级终端 + HMAF（鸿蒙智能体框架） | 一碰传/碰一碰、任务接续、硬件虚拟化池化、小艺+智能体协同 | 已商用（HarmonyOS 5/6） |
| Microsoft | Phone Link / Link to Windows / Cross-Device Resume | 通知/短信/照片/文件/应用投屏/跨设备续接（Spotify、Office、WhatsApp、Copilot 文件） | 已商用（Windows 11）；累计下载 5 亿+（**截至 2025 末，待核实**） |
| CSA / 跨品牌 | Matter 1.4 / 1.5 + Thread 1.4 | 跨品牌智能家居互操作、本地控制、多 Admin | 标准已发布；**相机类 Matter 1.5 各平台落地时间待核实** |

---

## 四、2025-2026 进展（时间线表格）

| 时间 | 事件 | 来源口径 |
|---|---|---|
| 2024 | macOS Sequoia 推出 iPhone Mirroring，扩展 Continuity | Apple 官方新闻稿 |
| 2025（Google I/O） | Adaptive Android 覆盖 5 亿+ 活跃设备；Android 16 桌面窗口化；Android XR；Compose Adaptive Layouts / Jetpack Navigation 3；Gemini Nano ML Kit GenAI API | Android Developers 官方博客 |
| 2025.05 | Microsoft 推出 Cross-Device Resume（手机→PC 续接） | 媒体/Grokipedia 汇总 |
| 2025.06 | 华为 HDC：HarmonyOS 6 发布，引入 HMAF 鸿蒙智能体框架；宣称跨终端协同时延 < 80ms | 新华网报道（**具体时延数字待核实**） |
| 2025.09 | Phone Link 联系人同步至 Microsoft Teams（不含中国大陆） | 媒体汇总 |
| 2025 末 | Matter 1.5 + Thread 1.4 发布，统一摄像头等品类标准 | EEWorld / CSA 口径 |
| 2026.01 | Microsoft 扩展 Cross-Device Resume（更多 App、更多 OEM） | 媒体汇总 |
| 2026（WWDC26） | 媒体报道 iOS 27/macOS 27 等系统引入 Siri AI 独立 App、跨设备对话同步、Spatial Preview（Mac→Vision Pro） | **AppleMagazine / 自由时报3C 等二次媒体，版本号与功能清单待核实** |

---

## 五、代表产品（点到为止）

- **Apple Continuity / Handoff**：动作接力标杆，AI 时代升级为"意图接力"（Siri 上下文跨设备）。
- **华为超级终端 / 一碰传**：分布式软总线把多设备虚拟成一"超级终端"，任务/服务自由流转。
- **Samsung SmartThings + 应用流转 / 多重控制**：Galaxy 全家桶无感接续与跨设备拖放。
- **Microsoft Phone Link / Cross-Device Resume**：Windows 侧"类 Handoff"，开放兼容 Android 多 OEM。
- **Matter + Thread**：智能家居跨品牌"管道"统一后，竞争转向"AI 大脑"（Gemini for Home / Alexa+ / Apple Intelligence+HomeKit）。

---

## 六、关键挑战

1. **上下文一致性**：跨端状态需序列化/重建，弱网或并发修改下如何保证最终一致（冲突合并）。
2. **统一身份与权限**：跨厂商非同一账号体系时，授权与信任如何建立（生态围墙）。
3. **隐私暴露面**：上下文跨端流动扩大攻击面，需端到端加密 + 最小权限（如 Matter Setup Code、Hichain 双向认证）。
4. **延迟与可靠性**：异构网络（Wi-Fi/蓝牙/UWB）自动切换、弱网降级策略。
5. **碎片化**：同能力不同厂商实现割裂，缺乏类似 MCP 的开放"跨端上下文迁移"标准。

---

## 七、深度盲区（留给 Ethon 补充）

- [ ] 跨端上下文迁移是否会出现类似 [[MCP 与设备侧 MCP]] 的**开放标准协议**（区别于单设备 MCP）？目前各厂商私有，互操作缺位。
- [ ] 当 Agent 跨设备续接时，[[端侧模型的个性化隐私联邦边界 学习笔记]] 中的个性化记忆如何随上下文**安全迁移而不泄漏**？
- [ ] 弱网/离线场景下跨端任务接续的**最终一致性与冲突合并**方案（CRDT / 操作日志）孰优？
- [ ] 除 Matter 外，是否有面向 **Agent 级的跨厂商互操作协议**能突破生态围墙？
- [ ] "超级终端"式硬件池化（分布式 GPU/摄像头）在 Agent 编排下的**资源调度与计费模型**如何设计？

---

## 八、附：来源清单（实际查阅）

- Apple 官方新闻稿：macOS Sequoia / iPhone Mirroring（apple.com/newsroom/2024/06）
- AppleMagazine：WWDC26 生态智能转向（applemagazine.com，二次媒体）
- AppleInsider：Continuity 跨设备 Siri 对话同步与 Spatial Preview 使用指南（二次媒体）
- 自由时报 3C：WWDC 2026 Siri AI 跨设备聊天（3c.ltn.com.tw，二次媒体，**版本号待核实**）
- Android Developers：Cross-device SDK 概览；Google I/O 2025 自适应 Android（developer.android.com）
- Samsung 官网：Galaxy 生态系统/应用流转/多重控制（samsung.com）
- 华为开发者联盟：分布式软总线架构；HarmonyOS Connect（developer.huawei.com / devicepartner.huawei.com）
- 新华网：华为开发者大会 2025（HarmonyOS 6 / HMAF）（news.cn）
- Microsoft 相关：Phone Link / Cross-Device Resume 汇总（Grokipedia、MakeUseOf、WindowsForum，二次媒体）
- EEWorld / CSA 口径：Matter 1.5 + Thread 1.4 智能家居前瞻（eeworld.com.cn）

## ⚠️ 待核实清单

- Apple WWDC26 具体系统版本号（iOS 27 / macOS 27 等）、Siri AI 独立 App 与 Spatial Preview 的确切功能与上市时间（仅二次媒体报道）。
- Google Cross-device SDK 是否在 2026 进入生产可用（官方仍标 Developer Preview）。
- 华为"跨终端协同时延 < 80ms"的具体测试条件与口径。
- Microsoft Phone Link"累计下载 5 亿+"的时点与统计口径。
- Matter 1.5 摄像头支持在 Apple / Google / Amazon 各平台的具体落地时间。
- 三星"应用流转"在 One UI 7.0+ 的精确支持设备清单与区域限制。

---

#标签/手机AI智能体 #标签/跨端协同 #标签/Agent编排
