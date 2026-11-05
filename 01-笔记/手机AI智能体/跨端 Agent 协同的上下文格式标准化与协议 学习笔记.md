---
title: 跨端 Agent 协同的上下文格式标准化与协议
tags: [agent, context, cross-device, 端侧, context-protocol, 互操作, 序列化, 手机AI智能体]
created: 2026-10-28
source: 厂商/基金会官方博客与文档（modelcontextprotocol.io、Google Open Source Blog、Agentic AI Foundation、AIP 开放原子社区、aip.openatom.tech）+ 学术/开源（SSRN Engram、GitHub UCIP）+ 科技媒体（Android Authority、IT之家、中新网、经济参考报）。年份与具体数字以「待核实」标注处需二次核验；部分分析师口径数字已显式标出。
---

# 跨端 Agent 协同的上下文格式标准化与协议

> **心智模型：** 跨端 Agent 上下文标准化的本质，是把"用户上下文（对话/画像/设备态/意图）"从各厂商的**私有二进制**升格为一种**可序列化、可携带、可跨运行时互操作的"通用货币"**——不解决格式与协议，跨端协同就永远卡在生态围墙里。本文聚焦"怎么序列化、什么 schema、如何互通"这一层，区别于 [[跨端跨设备 Agent 协同与上下文迁移 学习笔记]]（那篇讲协同机制 / Continuity 式体验）。

---

## 一、定义（广度）

**上下文格式标准化与协议**：规定"一个 Agent 的上下文（对话历史、用户画像、设备状态、意图、记忆）"在被**序列化、存储、跨设备/跨厂商迁移或跨 Agent 共享**时所使用的**数据格式（schema）、传输协议与互操作契约**。它回答的不是"任务怎么接力"（那是 [[跨端跨设备 Agent 协同与上下文迁移 学习笔记]] 的范畴），而是"上下文以什么形状流转、对方能否读懂"。

与单设备内上下文工程的差异见 [[Context Engineering 学习笔记]]（那篇聚焦"如何为单个 Agent 组装上下文"）；与意图作为上下文核心要素的差异见 [[端侧意图框架 学习笔记]]。

---

## 二、分类（按协议层 / 序列化方式）

**按协议层（从上下文"内部表示"到"跨厂商互通"）**

| 层级 | 职责 | 代表格式/协议 | 序列化 |
|---|---|---|---|
| L0 上下文内部表示 | 记忆/画像/意图的本地结构化表示 | Engram、UCIP、个人记忆库 | JSON / Protobuf |
| L1 Agent↔工具上下文 | 单个 Agent 连接工具/数据时的上下文注入 | **MCP** | JSON-RPC |
| L2 Agent↔Agent 上下文交换 | 跨框架/跨厂商 Agent 间发现与任务/上下文委派 | **A2A**、AIP、Agent Communication Protocol | JSON-RPC 2.0 / Protobuf |
| L3 厂商跨端同步 | 生态内设备间会话/状态/上下文续接 | Apple Continuity/Handoff、华为分布式软总线+HMAF、Google Cross-device SDK/Handoff、Samsung App Continuity | 各厂商私有 |
| L4 跨品牌管道 | 智能家居等跨品牌"管道"互操作（非 Agent 上下文专属） | Matter / Thread | 私有/标准化二进制 |

**按序列化方式**

| 序列化 | 特点 | 采用者 |
|---|---|---|
| JSON / JSON-RPC | 可读、易调试、LLM 友好；体积与解析开销较大 | MCP、A2A（传输层）、Engram、UCIP（导出） |
| Protocol Buffers | 二进制、体积小（UCIP 标称 3–10× 小于 JSON）、解析快，适合端侧/弱网 | UCIP v1.1 核心、A2A 规范真源 `a2a.proto` |
| 厂商私有封包 | 不公开 schema，跨生态不可读 | Apple/华为/三星/Google 端侧同步 |

---

## 三、主流方案与代表（Google / Apple / Huawei / MCP 等）

| 阵营 / 协议 | 定位 | 核心 schema / 格式 | 互操作现状 |
|---|---|---|---|
| **MCP**（Anthropic→Linux Foundation Agentic AI Foundation） | Agent↔工具/数据上下文注入，"AI 的 USB-C" | JSON-RPC（stdio / Streamable HTTP）；MCP Apps 扩展可返回 UI；官方扩展已 Production | 开放标准；2025-12 捐入 Linux Foundation；OpenAI/Google DeepMind/Microsoft/AWS 已采用；**月 SDK 下载量与 server 数等规模数字来源为分析师口径，待核实** |
| **A2A**（Google→Linux Foundation，2025-04-09 发布，2025-06-23 捐入） | Agent↔Agent 跨厂商发现与协作 | Agent Card（JSON，发布于 `/.well-known/agent-card.json`）；规范真源 `a2a.proto`（Protobuf）；任务/消息/部件/产物模型 | v1.0 于 2026-03 发布；IBM Agent Communication Protocol 2025-08 并入；与 MCP 互补（MCP 纵向连工具、A2A 横向连 Agent） |
| **Engram**（SSRN 2026-06，学术开源） | 可携带、受治理的 AI 记忆协议，"AI 记忆的 OAuth" | 五对象 JSON 信封（IDENTITY / BELIEFS / CONSTRAINTS / CORRECTIONS / EVOLUTION）；7 端点 API；Ed25519 签名；CC-BY 4.0 | 参考实现 OpenClaw、Hermes；号称首个跨运行时 AI 记忆互操作案例；**学术提出，产业落地待观察** |
| **UCIP**（User Context Interchange Protocol，开源） | 多设备连续 AI 体验的"用户数字孪生"上下文 | v1.0 JSON → v1.1 改用 Protobuf（核心）；JSON 导出兼容 LLM；声明兼容 MCP（取数）+ A2A（Agent 间共享） | 开源协议/schema，非产品；**社区项目，成熟度待核实** |
| **AIP 智能体互联协议**（中国，开放原子基金会 AtomGit） | 国标驱动的智能体互联互通 | 符合《人工智能 智能体互联》系列国家标准（可信注册/身份/描述/交互/发现/工具调用）；代码 2025-10-27 首版开源 | 北邮 + 中国电子技术标准化研究院研发；华为/蚂蚁/小米/阿里/快手等 100+ 企业参与共建，50+ 试点；**2026-06-26 国家市场监督管理总局批准发布 7 项国标，待核实落地广度** |
| **Apple Continuity / Handoff** | 生态内会话/任务跨设备续接 | 私有（iCloud 同步 Siri 对话、跨设备上下文）；无公开 schema | 已商用；**开放协议缺位，跨厂商不可读** |
| **华为 分布式软总线 + HMAF** | 超级终端式多设备上下文/任务流转 | 私有（鸿蒙分布式能力）；HMAF 智能体框架 | 已商用（HarmonyOS 5/6）；鸿蒙 6 起宣称支持与苹果设备系统级互联 |
| **Google Cross-device SDK / Handoff（开发中）** | 安卓多设备会话/任务/通知同步 | 私有；Cross-device SDK 的 Sessions API；Handoff 字符串见于 Play Services v25.25.31 beta | **Cross-device SDK 仍为 Developer Preview；安卓 Handoff 在 APK 拆解阶段、上线时间待核实** |
| **Samsung App Continuity / Multi Control** | Galaxy 全家桶应用接续/跨设备拖放 | 私有 | 已商用（One UI 7.0+） |
| **Matter / Thread** | 跨品牌智能家居"管道" | 标准化（非 Agent 上下文专属） | 标准已发布（Matter 1.5 / Thread 1.4）；**摄像头等品类各平台落地时间待核实** |

---

## 四、2025-2026 进展（时间线）

| 时间 | 事件 | 来源口径 |
|---|---|---|
| 2024-11 | Anthropic 发布 MCP | 官方 |
| 2025-04-09 | Google 发布 A2A | Google 官方博客 |
| 2025-06-23 | A2A 捐入 Linux Foundation（AWS/Cisco/Microsoft/Salesforce/SAP/ServiceNow 等创始） | 官方 |
| 2025-08 | IBM Agent Communication Protocol 并入 A2A | 官方/媒体 |
| 2025-10-27 | AIP 智能体互联协议族首版代码开源（开放原子 AtomGit） | 经济参考报/社区官方 |
| 2025-12 | MCP 捐入 Linux Foundation Agentic AI Foundation | 官方/媒体（**具体月份待核实**） |
| 2026-03 | A2A v1.0 稳定版（Signed Agent Cards、多租户、多协议绑定）；MCP Apps 官方扩展 Production | 官方 |
| 2026-04 | A2A 一周年：150+ 支持组织、22000+ GitHub stars（**规模数字来自 Linux Foundation 口径，建议二次核验**） | Google Open Source Blog / Linux Foundation |
| 2026-06 | Engram 论文（SSRN）发布 v0.1 | 学术 |
| 2026-06-26 | 国家市场监督管理总局批准发布《人工智能 智能体互联》7 项国家标准 | 百度百科/国标口径（**具体标准号与发布形式待核实**） |
| 2025-2026 | Google 安卓 Handoff / Task Continuity 在 Play Services 代码中出现；Pixel 10（Android 16）Quick Share 兼容 AirDrop | Android Authority / IT之家（**功能上线时间待核实**） |

---

## 五、代表产品 / 项目（点到为止）

- **MCP 生态**：Claude / ChatGPT / VS Code / Cursor 等已支持；Clipto MCP 把本地多模态记忆封装为可调用上下文（Product Hunt 2026-08 月榜第一，**榜单口径待核实**）；mobile-mcp 把 MCP 工具链伸进真机（无障碍树优先）。
- **A2A 生态**：Google Cloud ADK / Agent Engine、Azure AI Foundry、AWS Bedrock AgentCore 均已支持 A2A 端点；A2Family 衍生 AP2（Agent Payment）、A2UI、UCP。
- **Engram / UCIP**：学术与社区层面的"可携带上下文/记忆"开放 schema 探索。
- **AIP**：国标 + 开源双轨的中国智能体互联方案，与厂商生态（华为/小米/阿里等）强绑定。
- **厂商私有**：Apple Continuity、华为超级终端、Samsung App Continuity、Google Cross-device SDK——体验成熟但**无开放 schema**。

---

## 六、关键观察（本篇相较协同机制篇的差异）

1. **开放标准正快速成型，但与"跨端设备迁移"仍错位**：MCP/A2A 解决的是"Agent↔工具"和"Agent↔Agent"的文本/服务层互通，而"手机→车机→手表"的**端侧上下文（含设备态、传感器、隐私记忆）序列化与续接**尚无对等开放协议——各厂商仍用私有封包。
2. **序列化之争：JSON 可读 vs Protobuf 紧凑**：端侧/弱网场景倾向 Protobuf（UCIP、A2A 规范真源），但 LLM 注入与调试更友好 JSON——两者并存，靠"Protobuf 传输 + JSON 导出"折中（UCIP）。
3. **身份与签名成为互操作前置**：A2A Signed Agent Cards、Engram Ed25519、AIP 可信注册，说明"谁能读我的上下文"已上升为协议的一等公民（呼应 [[端侧模型的个性化隐私联邦边界 学习笔记]]）。
4. **国标路线（AIP）与开源基金会路线（MCP/A2A）可能分叉**：中国市场走"国家标准 + 开源社区"双轨，全球走 Linux Foundation 治理，二者 schema 是否互通是 unknowns。

---

## 七、深度盲区（留给 Ethon 补充）

- [ ] 跨端**端侧上下文（设备态/传感器/隐私记忆）**是否存在类似 MCP 的开放序列化协议？目前 L3 全为厂商私有。
- [ ] 当 Agent 跨设备续接时，[[端侧模型的个性化隐私联邦边界 学习笔记]] 中的个性化记忆如何随上下文**安全迁移而不泄漏**？schema 层是否要内建"最小权限导出"字段？
- [ ] JSON vs Protobuf 在端侧上下文（尤其包含多模态/向量记忆）的**体积与延迟边界**到底在哪？有无实测账本？
- [ ] AIP（国标）与 MCP/A2A（Linux Foundation）的 schema 是否/如何**互映射**？中国厂商出海时是否双栈？
- [ ] 跨厂商非同一账号体系时，上下文互操作的**信任与授权模型**（参照 Matter Setup Code / Hichain）如何下沉到 Agent 层？
- [ ] 弱网/离线跨端上下文续接的**最终一致性与冲突合并**（CRDT / 操作日志）在协议层应放在哪一层？
- [ ] 厂商"兼容苹果"（安卓/鸿蒙系统级 AirDrop/Handoff 兼容，2025 热词）是否意味着**跨生态上下文格式**出现事实标准萌芽？

---

## 八、附：来源清单（实际查阅）

- Model Context Protocol 官方：modelcontextprotocol.io（定义/架构/MCP Apps 扩展）
- Google Open Source Blog：A2A 一周年与捐赠 Linux Foundation（opensource.googleblog.com/2026/04）
- Agentic AI Foundation / enterpriseaiworld.com：A2A 加入 AAIF，与 MCP 互补的层级说明（aaif.io）
- Superkind / Agentica Wiki / Luby：A2A 机制、Agent Card、a2a.proto、v1.0 时间线（二次/百科口径）
- SSRN：Engram — An Open Protocol for Portable, Governed AI Memory（papers.ssrn.com，2026-06）
- GitHub：UCIP User Context Interchange Protocol（agi-2026/UCIP，开源 schema）
- AIP 智能体互联社区：aip.openatom.tech（首版代码 2025-10-27 开源、国标、试点）
- 经济参考报 / 人民网 / 中国商报：AIP 协议代码发布与试点（jjckb.xinhuanet.com、finance.people.com.cn、zgswcn.com）
- Android Authority：安卓 Handoff / Task Continuity APK 拆解（2025-06/07）
- IT之家 / 网易 / udn：谷歌"任务连续性"/安卓 Handoff 报道（2025-09）
- 中新网天津：Clipto MCP 登 Product Hunt 2026-08 月榜（tj.chinanews.com.cn，二次媒体）
- clawpk.net：mobile-mcp 把 MCP 伸进真机（二次技术媒体）
- 百度百科：AIP 智能体互联协议条目（含 2026-06-26 国标发布，待核实）

## ⚠️ 待核实清单

- MCP 月 SDK 下载量（传闻 97M，2026-03）、public server 数（10,000+）、集成成本降幅（60–70%）等规模数字来自分析师（Clarion/Luby）口径，**非官方一手，待核实**。
- A2A"150+ 支持组织、220,000+ GitHub stars"来自 Linux Foundation 2026-04 口径，建议二次核验。
- MCP 捐入 Linux Foundation Agentic AI Foundation 的具体月份（本文记 2025-12，待核实）。
- A2A 不同报道对版本号不一致（v1.0 / v1.2 均有），以官方 `a2a.proto` 与 release notes 为准。
- Google 安卓 Handoff / Task Continuity 正式上线时间与是否全 Android 设备（非仅 Pixel）待核实；Cross-device SDK 是否 2026 进入生产可用待核实。
- 华为"跨终端协同时延 < 80ms"具体测试条件待核实（见 [[跨端跨设备 Agent 协同与上下文迁移 学习笔记]]）。
- AIP《人工智能 智能体互联》7 项国家标准的具体标准号、发布形式（指导性技术文件）与落地广度待核实。
- Clipto MCP 的 Product Hunt 2026-08 月榜第一为媒体口径，待核实。
- 厂商"兼容苹果"系统级功能的区域限制（如国行无 GMS 设备能否获得）与精确支持设备清单待核实。

---

#标签/手机AI智能体 #标签/跨端协同 #标签/上下文工程
