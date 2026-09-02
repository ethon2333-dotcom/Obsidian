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

## 2026-08-09 增补：第④支——学习型防御 AgentAntibody + NowSecure iOS 27 攻击面（来源 [[AppIntent 每日情报 2026-08-09]]）

**① AgentAntibody（arXiv 2608.04053，2026-08-04 提交）—— 把「学习型防御」补进本库**
- 此前本库 XPIA 缓解只归为**静态三件套**：隔离（[[Agent Workspace 隔离执行]]）+ 确认（[[Confirmation UI 安全机制]]）+ 数据视图隔离（[[Dual View 智能体数据视图隔离]]）。AgentAntibody 是**第四支——学习型**：维护持久「抗体库」编码对用户**安全边界**的演化理解，运行时识别越界并启动免疫响应，跨遭遇进化。
- 直击最难的「意图歧义」场景：有害与合法动作都符合任务描述时，静态确认/过滤难分；它从每次遭遇**学习用户边界**应用到下次。
- 量化了安全-实用权衡：ablation 显示若匹配后**中止整个任务**，AgentDojo 的 SU-HM 从 72.0% → 24.2%——「低攻击成功率 ≠ 安全」，防注入要同盯任务完成率。完整机制/数字见 [[AgentAntibody 自适应免疫防御 2026]]。
- ⚠️ 预印本自报数字（AgentDojo ASR 3.8% / LBB 2.5%），未在独立榜复现。

**② NowSecure iOS 27 App Intents 攻击面（2026-08-05）—— 给「拐点①一次性注入」补一个可测清单**
- 移动 AppSec 厂商把「App Intents → agentic Siri → iOS 27」威胁落到 actionable 清单：盘 App Intents/schemas、测完整 workflow（非仅 UI）、监控数据流向哪些模型。与 Apple Session 347 威胁模型（间接 PI 经工具输出/日历/锁屏触发）一致。详见 [[Apple AppIntents Schema Protocol 2026#2026-08-09 增补]]。
- 对四平台防护对照表的意义：Apple 列的「系统级 Confirmation UI + EntityOwnership」现在有了具体的 AppSec 验证动作（锁屏 Siri intent 鉴权审计、App Attest），是从「设计」到「可测」的闭环。

**威胁模型四个拐点的当下状态**
① 一次性注入（基线）→ ② 文档型蠕虫自传播（[[文档型 XPIA 自传播蠕虫]]）→ ③ ADI 数据注入（[[Agent Data Injection 数据注入攻击]]）→ ④ 学习型防御（[[AgentAntibody 自适应免疫防御 2026]]，补防非补攻）。前三个是攻击演进，④是防御演进；**四平台 OS 层仍停留在①的静态防护，③的 ADI 与④的学习型防御均未被任何平台内建**。

## 深化补充

- **威胁模型的三个拐点（已立）**：① 一次性注入（本库基线）→ ② 文档型蠕虫自传播（[[文档型 XPIA 自传播蠕虫]]）→ ③ ADI 数据注入（[[Agent Data Injection 数据注入攻击]]）。三者是「注入会繁殖」「注入不靠指令」「注入伪造结构」的递进，四平台防护目前**均停留在拐点①**。
- **与确认机制的分层**：XPIA 的缓解需三层叠加——隔离（[[Agent Workspace 隔离执行]]）+ 确认（[[Confirmation UI 安全机制]]）+ 数据形态隔离（[[Dual View 智能体数据视图隔离]]）；且据 [[Confirmation UI 安全机制]] 2026-08-03 增补，确认本身需走「带外」第三档（AIMS：LLM MUST NOT hold credentials）才抗 ADI。
- **与 Agentic OS 的张力**：当 [[Agentic OS 意图调度内核]] 把调度单元升级为意图，意图本身成为新注入面，XPIA 防线需前移到意图注册 / 写回阶段。

- [ ] 四平台对「拐点③ ADI」是否已有任何官方类别级回应？截至 2026-08-04 均待补。
- [ ] XPIA 在「Proactive Agent 主动触发意图」场景下如何拦截？主动触发意味着 Agent 自己发起，确认点更难布（见 [[Agentic OS 意图调度内核]]）。
- [ ] 能否把 XPIA 防护纳入 OS 意图框架的「能力描述」环节（[[Intent Schema Protocol 意图模式规范]]），让声明即带防护属性？

## 2026-08-09晚 增补：Google 官方六层防御口径 + NCSC 的「混淆代理」定性（来源 [[AppIntent 每日情报 2026-08-09-晚]]）

### ① Google 对 Gemini 的分层防御——**官方支持页原文六层**（Google Workspace 管理员帮助，最后更新 **2026-03-17**）

此前本库对 Google 侧防护多为二手转述，本轮拿到**官方逐条口径**：

| 层 | 官方英文名 | 作用 |
|---|---|---|
| ① | **Prompt injection content classifiers** | 专有 ML 模型，在多种数据格式中检测恶意指令 |
| ② | **Security thought reinforcement** | 在提示内容周围**加装定向安全指令**，提醒 LLM 执行用户任务、忽略嵌入的对抗指令（业界俗称 **spotlighting**） |
| ③ | **Markdown sanitization + suspicious URL redaction** | 借 Safe Browsing 移除 / 遮蔽外部图片 URL 与可疑链接，**防 EchoLeak 式渲染外泄** |
| ④ | **User confirmation framework** | 对敏感操作（官方举例：**删除日历事件**）要求显式确认，HITL 兜底 |
| ⑤ | **End-user security mitigation notifications** | 检测 / 缓解后**告知用户**，形成协同治理 |
| ⑥ | **Model resilience** | 模型自身的对抗鲁棒性 |

**判读**：⑤「缓解后通知用户」是四平台里少见的一层——它把安全事件变成**用户可感知的信号**而非静默拦截。这条对 OS Agent 的 PRD 价值高于其技术含量：**用户需要知道「刚才有人试图操纵你的助手」**，这是建立长期信任的必要条件，也是 [[Confirmation UI 安全机制]] 之外的第二种「用户在环」形态（**事后知情** vs 事前确认）。

### ② 客户端层新增第⑤支防御形态：读 / 写边界隔离

本库既有防御谱系为：隔离执行 / 确认 / 数据视图隔离 / 学习型防御（AgentAntibody）。本轮补入第⑤支——**执行边界的读写分级**，代表实现见 [[Chrome Agent Origin Sets 与用户对齐评判器 2026]]。它与前四支正交：不判断内容是否恶意，只限制「读来的数据能流向哪里」。

### ③ 英国 NCSC：提示注入可能**永远无法被完全缓解**

据 Computerworld 转述，NCSC 将提示注入定性为 **"confused deputy"（混淆代理）** 类漏洞——**受信任的系统被诱骗代不受信任方行事**；其根因是 LLM 无法可靠区分「指令」与「数据」，因此建议组织**以设计管理风险**（限制访问与权限），而非期待技术修复消除问题。同期 Gartner 建议企业**封禁 AI 浏览器**。

> ⚠️ **口径标注**：NCSC 表态与 Gartner 建议均来自 Computerworld 二手转述，**原文链接与具体发布日期待补**。OWASP「73% 生产 AI 部署中存在提示注入（2024 评估）」一项同为该文转述，**未独立核实**。

**对本笔记结论的影响**：三个拐点之上再加一条**元判断**——若 NCSC 定性成立（这是**架构缺陷**而非**可修 bug**），则四平台的正确目标不是「防住注入」，而是**「假定注入必然发生，用权限与边界把爆炸半径压到可接受」**。这与 Chrome「bounds the threat vector」的措辞一致，也解释了为何工业界主流投入在**边界**（origin set / workspace 隔离）而非**检测**。

## 2026-08-15 增补：Windows Copilot Vision + 语义文件索引 = XPIA 读路径扩张

> 来源：[[AppIntent 每日情报 2026-08-15]]。

Windows Copilot Vision 通过**屏幕像素 + 语义文件索引**扩展读取路径——Agent 能读取的内容从「显式授予」扩张到「屏幕上可见 + 索引可检索」。这一读路径扩张发生在**应用层（app-layer）**，并非走 ODR 总线（OS-defined registry bus），属于**观察性能力（observation only）**。

含义：XPIA 防御需覆盖的读路径更长——不仅是工具调用参数注入，还包括视觉/索引侧的非预期数据摄入。这与本库既有「拐点③ ADI」同源：被读取的内容若是被污染的结构化数据，Agent 可能基于它自推错误结论。但 Copilot Vision 的读路径**不经过 ODR 受控发现**，是 OS Agent 读路径治理的一个新增缺口（详见 [[Agent Data Injection 数据注入攻击]]）。

## 关联

- 来源：[[AppIntent 跨平台情报简报 2026-07-30]] ｜ [[AppIntent 每日情报 2026-08-01]] ｜ [[AppIntent 每日情报 2026-08-09]] ｜ [[AppIntent 每日情报 2026-08-09-晚]]
- 第⑤支·读写边界：[[Chrome Agent Origin Sets 与用户对齐评判器 2026]]
- 写回风险：[[Agent 写回路径 XPIA 风险评估 SOP]] ｜ 蠕虫范式：[[文档型 XPIA 自传播蠕虫]]
- 隔离：[[Agent Workspace 隔离执行]] ｜ 确认：[[Confirmation UI 安全机制]] ｜ 数据视图隔离：[[Dual View 智能体数据视图隔离]]
- 数据注入（拐点③）：[[Agent Data Injection 数据注入攻击]] ｜ 学习型防御（拐点④）：[[AgentAntibody 自适应免疫防御 2026]]
- 平台：[[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ iOS 27 攻击面：[[Apple AppIntents Schema Protocol 2026]]

## 2026-08-26 增补：间接提示注入已成 web 级 operational 现象（CSA 数据 + Black Hat USA 2026，来源 [[AppIntent 每日情报 2026-08-26]]）

> 接续 08-09晚 的 NCSC「confused deputy / 架构缺陷非可修 bug」定性。本期补**量化证据**：间接提示注入从「demo」推为「web 级运营现象」，直接抬高 OS Agent 读路径治理优先级。

**① CSA（Cloud Security Alliance）研究笔记实测的 web 级规模**
- 引 Google 安全数据：每月爬取约 **20–30 亿页**，其中携带恶意注入指令的页面占比在 **2025-11 → 2026-02 相对 +32%**。
- 含义：注入不再是「针对性攻击」，而是 **SEO 垃圾式广撒网**——成本趋零、坐等任意 agent 来读；payload 已 seeding 到全网，不挑目标。
- 与库内 [[Agent Data Injection 数据注入攻击]] 的「ADI 伪造结构化元数据」同源：读路径越长（屏幕/Copilot Vision/索引/文档），被污染数据进入 Agent 上下文的概率越高。

**② Black Hat USA 2026：被分析的每一个 AI 浏览器都易受提示注入**
- 会议结论：**every browser analyzed proved vulnerable**——不是「多数」，是「每一个」。根因是 AI 浏览器助手「读页面内容（攻击者可控）+ 在已登录会话内代用户行动」这两件事本就合一，能力与漏洞同源。
- 与 08-09晚 NCSC「confused deputy」定性一致：**OWASP 仍称 prompt injection 驱动多数生产 AI 失败且 unsolved**；过滤/定界/分类器只降命中率，非参数化隔离。

**③ 对 OS Agent 的含义（落回本笔记结论）**
- 本笔记既有元判断「假定注入必然发生，用权限与边界压爆炸半径」获 operational 证据支撑——XPIA 防御重心应在**边界**（[[Chrome Agent Origin Sets 与用户对齐评判器 2026]] 的读写源集 / [[Agent Workspace 隔离执行]] 的隔离会话）而非**检测**。
- 回流动作：把 CSA「月 20–30 亿页 / +32%」作为量化论据，纳入 [[Agent 读入路径可信数据边界 SOP]] 的「为什么会读到污染数据」一节。
- ⚠️ 诚实标注：CSA/Black Hat 为安全研究口径（Safeguard.sh 转述 CSA + Black Hat 报告），具体页面样本与统计方法**待一手报告复核**。

#标签/XPIA #标签/安全 #标签/注入
