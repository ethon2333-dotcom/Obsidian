---
type: raw
status: inbox
date: 2026-08-02
captured: 2026-08-02
importance_score: ★★★★☆
intent_category: 系统级意图框架 / 端侧 Planner 意图路由 / 跨应用 Intent 工作流 / 执行安全（XPIA / 合规）
source:
  - "https://developer.android.com/ai/appfunctions （AppFunctions 官方文档：已发布 Agent Skill，四步生命周期）"
  - "https://developer.android.google.cn/blog/posts/android-17-is-here （Android 17 正式发布博文：AppFunctions + Agent Skill）"
  - "https://china.qianlong.com/2026/0801/8706085.shtml （HDD 西安站聚焦 HarmonyOS 7 新特性，2026-08-01）"
  - "https://developer.apple.com/cn/videos/play/wwdc2026/343/ （WWDC26 Session 343：探索适用于 Siri 和 Apple 智能的 App Intents 高级功能）"
  - "https://artificialintelligenceact.eu/article/15/ （EU AI Act Article 15: Accuracy, Robustness and Cybersecurity，entry into force 2026-08-02）"
  - "https://www.techtimes.com/articles/318005/20260608/wwdc-2026-app-intents-replaces-sirikit-gemini-siri-migration-clock-starts.htm （App Intents 2.0 streaming/multi-turn 报道）"
  - "https://dev.to/akaranjkar08/apple-wwdc-2026-rebuilt-siri-the-extensions-api-and-what-claude-on-14-billion-iphones-means-for-1c1l （App Intents 2.0 + Extensions 隐私架构）"
tags: [AppIntent, OS-Agent, 端侧Planner, 执行安全, XPIA, 合规, 每日情报, 跨平台2026]
---

# AppIntent 每日情报（2026-08-02）

> [!abstract] 30 秒速览
> **核心变化**：本日（2026-08-02）是 **EU AI Act Article 15（准确性 / 鲁棒性 / 网络安全）正式生效日**，这是 OS 级 Agent 执行安全第一次被写进**强制性法规**——第 15(5) 条明确把「提示注入（prompt injection）、对抗样本、模型投毒」列为高风险 AI 系统必须抵御的攻击面。四平台的「执行安全」从此不再是产品选择，而是合规底线。
> **窗口内真增量**：① **HarmonyOS 7（HDD 西安站 08-01）**：小艺升为基于 **Agentic 自演进架构**的系统级智慧大脑，小艺开放平台 **A2A 支持端侧 / 云侧双模**——头部银行 App 经端侧 A2A 覆盖 **1000+ 意图、多步执行、隐私数据不出端**；O2O App 经云侧 A2A 走完「问答→选座→购票→支付」端到端闭环；② **EU AI Act Article 15 今日生效**（执行安全合规地板）。
> **库内空白补漏**：③ **Apple WWDC26 Session 343 深入**（此前只覆盖 Session 345）：View Annotations（`.siriAnnotation` / `.appEntityIdentifier` / 选择类型标识 / 集合标注）解决「屏幕上的第三项」；`IntentValueQuery` 做结构化搜索；**Confirmations and entity ownership**（声明实体归属以差异化确认）；**App Intents 2.0** 新增 streaming responses / 更富实体类型 / conversational follow-ups（多轮）；④ **Android AppFunctions 官方 Agent Skill** 四步生命周期经官方文档验证（发现 / 实现配置 / KDoc 优化 / 测试调试）。
> **被本次排除**：M365 Copilot Agentic 模式扩大可用（08-01）属**应用 / M365 层**，非 OS 级执行总线，按过滤规则排除（见「边界判定」）。

## 检索与口径说明（诚实标注）

- **窗口**：按记忆文件建议，本日**正式切换为 7 日滚动窗口（2026-07-26 → 2026-08-02）**，保留「首次进入本库」判定做去重。严格 7 日窗口内命中两类：EU AI Act Article 15（08-02）、HarmonyOS HDD 西安站（08-01）。
- **补漏**：Apple Session 343（2026-06，WWDC26）、Android AppFunctions Agent Skill（Android 17 同期，库内 08-01 已提及高层、本次补验证细节）属**库内空白/已述待补**，逐条标真实日期，不冒充当日新闻。
- **信息源**：Horizon MCP 仍全部 disconnected，改用 WebSearch/WebFetch 直取官方源（developer.android.com、developer.apple.com、artificialintelligenceact.eu、华为 HDD 西安站官方通稿转载）。合成由本 Agent 完成，未消耗外部分析额度。
- **厂商/媒体自述数据一律标注口径**，未独立核验的名次与分数标「待补」。

---

## 原始内容

### 一、窗口内真增量（2026-07-26 → 2026-08-02）

#### 1. EU AI Act Article 15 今日（2026-08-02）正式生效：执行安全第一次成为法规地板 ★★★★★

**这是本期对 OS Agent 执行安全影响最深远的一条——它把「XPIA 防护」从产品特性变成了法律义务。**

- **生效事实**：EU AI Act **Article 15（Accuracy, Robustness and Cybersecurity）** 的 **entry into force = 2026-08-02**（依据 Article 113 实施时间线）。高风险 AI 系统（Annex III 八类：生物识别、关键基础设施、教育、就业/用工管理、必要服务获取/信用评分、执法、移民边境、司法民主）自此须满足准确性、鲁棒性、网络安全三性，且**全生命周期一致**。
- **与执行安全直接相关的关键条款**：
  - **第 15(5) 条（网络安全）** 明确列举须防护的 AI 特有漏洞：**训练数据投毒（data poisoning）/ 预训练组件投毒（model poisoning）/ 诱导模型出错的输入（adversarial examples 或 model evasion）/ 机密性攻击 / 模型缺陷**。换言之，**提示注入被监管文本明确点名**为高风险系统必须抵御的攻击面。
  - **第 15(4) 条（鲁棒性）** 要求对「系统或运行环境中出现的错误、故障、不一致（尤其因与自然人或其他系统交互而产生）」具备尽可能强的韧性；对**持续学习的系统**须消除/降低有偏输出进入后续输入的反馈回路风险。
  - **第 15(2)/(3) 条**：准确性须在技术文档（Annex IV）中**声明可测量的指标**，并鼓励制定基准与测量方法。
- **罚则**：高风险义务违规罚则上限 **€15M 或全球年营业额 3%**（Article 99）；禁止类实践另计更高档。合规基础设施缺口被广泛认为「几乎不存在」（多家合规机构 2026 上半年预警）。
- **对 OS Agent 的直接含义**（本库视角）：四平台的「系统级 Agent 执行总线」若部署于 EU 且落入高风险范畴，须证明 **prompt-injection 韧性、动作层（tool-use / API 调用）网络安全、自动不可篡改日志（Article 12）、人类监督（Article 14）**。这恰好对应本库已建的 [[XPIA 跨提示注入]]、[[Agent Workspace 隔离执行]]、[[Confirmation UI 安全机制]] 三条防线——**现在它们有了监管驱动力**，而非仅由产品 judgment 驱动。
- ⚠️ **口径与冲突（必须标注）**：EU 委员会 2025-11 提出 **Digital Omnibus** 一揽子修订，拟把 Annex III 独立系统的合规期限从 2026-08-02 推迟到 **2027-12-02**（嵌入式系统推到 2028-08-02）。但该文本**截至 2026-08-02 尚未正式通过生效**（仅「临时政治协议」），**原 08-02 日期仍是现行有效合规日**。任何以「会推迟」为由暂缓准备的团队，都是在押注一部尚不存在的法律——多家律所（Gibson Dunn / White & Case）明确如此提示。本库按「现行有效日」记录。

#### 2. HarmonyOS 7（HDD 西安站 2026-08-01）：小艺升为 Agentic 自演进系统级大脑，A2A 端侧/云侧双模 ★★★★☆

- **小艺定位升级**：HarmonyOS 7 将小艺升级为基于 **Agentic 自演进架构**的**系统级智慧大脑**；作为系统级智能体，具备意图理解与服务分发能力，可与操作系统、第三方智能体、应用、元服务、Skill 无缝协作；用户说一句话，小艺理解、调度、交付。
- **🔑 A2A 端侧 / 云侧双模（本期最高价值技术点）**：小艺开放平台提供 Agent、Skill 多种接入模式，**A2A 接入支持端侧 A2A 与云侧 A2A 双模对接**：
  - **端侧 A2A**：保障**低时延本地响应 + 数据高安全性**；
  - **云侧 A2A**：支撑**复杂任务深度推理**；
  - 开发者按业务场景灵活选择最优接入方式。
- **落地实证（这是双模从概念到落地的关键证据）**：
  - **国内头部银行 App** 经**端侧 A2A** 接入，实现覆盖 **1000+ 意图**、多步任务执行、**隐私数据不出端**；
  - **主流线上 O2O App** 经**云侧 A2A** 对接小艺，从**问答 → 选座 → 购票 → 支付**走完端到端任务闭环。
- **开发者实证（接入门槛）**：「奇妙工具箱」团队上线一年获 **120 万+ 用户 / 7 万+ 五星好评**；一周完成 Agent 接入（编排工作流 → 接入插件 → 开发卡片）；以「我想看一下金价」为例：意图分类节点 → 大模型节点语义理解 → 知识库节点检索 → 端侧插件拉起界面 → 卡片推送，完成「用户说一句 → 服务送到眼前」闭环。
- ⚠️ 口径：银行「1000+ 意图」「O2O 端到端闭环」为华为现场披露口径，**具体 App 名称、意图清单、成功率未独立核验（待补）**；HDD 西安站稿件为官方通稿转载，技术细节与 HDC 2026 表述一致（小艺 1.8 亿 DAU、日均唤醒 30 亿+、2100+ 系统能力 Skill 化、500+ 伙伴精选 Skill、2000+ 鸿蒙智能体），延续 [[HarmonyOS Intents Kit 与 ArkAF 2026]] 既有记录。

---

### 二、库内空白补漏（非 7 日窗口，已标真实日期）

#### 3. Apple WWDC26 Session 343 深入：View Annotations / IntentValueQuery / Confirmations + 实体归属（2026-06，此前未覆盖）★★★★☆

> 库内 08-01 已覆盖 Session 345（代码级 API 表）。本次补齐 **Session 343** 的章节结构与「屏幕感知 / 结构化搜索 / 确认与实体归属」三大机制。⚠️ Session 343 属 **WWDC26（2026-06）**，超出 7 日窗口，作为库内空白补漏补齐（与 08-01 补 Session 345 同口径）。

- **官方章节清单（developer.apple.com 视频页确认）**：
  1. 自定 Siri 的响应方式（Customize how Siri responds）
  2. 视觉响应（Visual responses）
  3. 互动上报（Interaction donations）
  4. **确认和实体所有权（Confirmations and entity ownership）**
  5. 使用 IndexedEntity 创建语义索引（Semantic index with IndexedEntity）
  6. **使用 IntentValueQuery 进行结构化搜索（Structured search with IntentValueQuery）**
  7. App 内搜索（In-app search）
  8. **屏幕感知（Onscreen awareness）**
  9. 利用现有整合（Leverage existing integrations：UserNotifications / NowPlaying / AlarmKit 等实体标注）
- **View Annotations（屏幕感知核心 API，解决「屏幕上的第三项」）**：
  - `.siriAnnotation` —— 把一个视图标记为 Siri 可理解的情境；
  - `.appEntityIdentifier` —— 把视图关联到某个 AppEntity；
  - `appEntityIdentifier(forSelectionType:)` —— 让用户选区（如列表里选中的项）映射到实体；
  - **集合标注（Collection annotation）** —— 一块区域整体标注为一组成实体。
  - 价值：Siri 不再只靠「屏幕上的第三项」这种脆弱猜测，而是拿到 App 主动暴露的语义锚点（与 [[Apple Intelligence 与 App Intents]] 中「App 界面私有内容不会自动向系统开放」一致——需开发者用标注主动开放）。
- **IntentValueQuery（结构化搜索）**：让 App 把自身的结构化查询能力暴露给 Siri/Spotlight，Siri 可在 App 数据模型上做「意图级」检索，而非字符串匹配。与 IndexedEntity 语义索引互补。
- **Confirmations and entity ownership（确认与实体归属）**：Session 资源明确有「Declare entity ownership for confirmations」小节——App 声明实体的归属（OwnershipProvidingEntity：`shared` / `public` / `unknown`），**Confirmation UI 据此差异化提示**（如「这是别人的相册，确定删除？」vs「确定删除你自己的？」）。这是库内既有 [[Confirmation UI 安全机制]] 在 Apple 侧的官方落地补强。
- **App Intents 2.0（与 Session 343 同期发布，多源交叉确认）**：在 v1 基础上新增三件修复主要痛点的能力：
  1. **Streaming responses（流式响应）**：App 边算边把部分结果回传给 Siri，不再等完整结果才渲染——对搜索类意图感知延迟改善明显；
  2. **更富实体类型（Richer entity types）**：Siri 从「关键词匹配」升级为「在 App 数据模型上做意图理解」；
  3. **Conversational follow-ups（多轮对话追问）**：单次 Siri 调用内可多轮细化（如搜索会后说「只看周二的会议」），成为一等公民模式（v1 需大量复杂度才勉强可行）。
  - ⚠️ 迁移为**增量式**：旧 App Intents 继续工作，按意图 opt-in streaming / 富实体 / 多轮。
- **隐私治理侧（Extension 模式）**：Apple 把 Claude / GPT / Gemini 作为 **Extensions** 直连 Siri，切换对用户透明；但**任何 AI 提供商建 Extension 都需经 App Review + App Store 分发**（dev.to 交叉确认）。这把「多模型路由」纳入了 Apple 的审查与分发治理——属执行安全/治理层信号，与本库 [[Confirmation UI 安全机制]]、[[Agent Workspace 隔离执行]] 的「受控发现 + 审批」思路同构。
- ⚠️ **未独立确认项（诚实标注）**：所谓「**Per-Intent Privacy Manifest**（IntentPrivacyManifest：dataAccessed / purpose / dataSentExternally / retentionPolicy）」作为**独立 API 名称**，本次一手检索**未能从 Apple 官方文档独立确认**（Apple 确有 PrivacyInfo.xcprivacy 隐私清单机制，但是否有「按意图粒度」的专用清单 API 待官方文档确认）。本库不把它作为已确认 API 记录，仅标注为「可能方向」。

#### 4. Android AppFunctions 官方 Agent Skill 四步生命周期（Android 17 同期，已验证）★★★☆☆

> 库内 08-01 已在 Android B-note 高层提及「官方 Agent Skill 分析关键工作流生成 Kotlin、优化 KDoc、给 ADB 调试命令」。本次用官方文档**验证四步生命周期全貌并补源链接**。

- **官方来源确认（developer.android.com/ai/appfunctions + Android 17 博文）**：Google 明确「We released an agent skill for AppFunctions」，技能仓位于 AppFunctions skill repository（github.com/android/skills 下的 device-ai/appfunctions）。
- **四步生命周期（官方原文）**：
  1. **Discovery（发现）**：分析代码库，识别并推荐**高价值、适合 AI 编排**的功能；
  2. **Implementation & Configuration（实现与配置）**：生成 Kotlin 实现，配置系统元数据与 build 依赖；
  3. **KDoc Refinement（KDoc 优化）**：为 AI 智能体与 Android MCP **优化函数与属性的文档**，提升 Agent 工具调用准确率（呼应本库「Schema 越规范，Planner 越小」论断）；
  4. **Testing & Debugging（测试与调试）**：提供 ADB 命令在设备端本地评估与调试；另可装 **AppFunctions 测试代理 App** 完整体验端到端工作流。
- **与设备侧 MCP 的关系（官方澄清，高价值）**：AppFunctions 是 **Android 专属、OS 级、本地执行的 hook**；标准 MCP server 是**平台无关、依赖云端执行 + 网络往返**的方案。开发 AppFunctions 可直接用设备上的**现有 App 状态**，无需在 App 外维护服务——这是对「设备侧 MCP」范式最清晰的官方定义（见 [[Android AppFunctions 设备侧意图 2026]]、[[DeviceSideMCP 设备侧MCP]]）。
- **状态**：AppFunctions 仍为**实验性 feature**，仅有限 App 与系统智能体可走完整 pipeline；EAP（goo.gle/eap-af）开放抢先体验；验证命令 `adb shell cmd app_function list-app-functions`。⚠️ 具体发布日期官方未单独给出，随 Android 17（2026-06-16 GA）文档在线，本库记为「Android 17 同期（日期待补）」。

---

### 三、边界判定（已评估后排除，展示过滤纪律）

#### 5. M365 Copilot Agentic 模式扩大可用（2026-08-01）—— 应用层，非 OS 级，排除

- 观察到多家媒体称 Microsoft 365 Copilot 的 Agentic 模式在 08-01 前后扩大可用、Classic Outlook 接入 Copilot（2026-08）。
- **排除理由**：本情报任务聚焦**系统级执行总线**（OS 内核/系统服务层把 App 能力注册为可被系统 Agent 编排的工具）。M365 Copilot 属**办公应用 / SaaS 层智能体**，不构成 OS 级意图框架/Registry/权限模型变化，**低于 ≥6/10 的 OS 级相关性阈值**，按过滤规则排除。
- 仅作记录：若未来其「Agent 在 Windows 桌面级获得系统调用权」则重新纳入。

---

## 正文拆解

### ① Schema 定义与语义路由机制

**A. 「端侧 / 云侧 A2A 双模」是 HarmonyOS 对「跨 Agent 编排该放哪」给出的最清晰答案。**

此前的 [[A2A 端侧智能体协议]] 只抽象了「端侧直连优先、跨设备走安全通道」。HarmonyOS 7 把它落地为**显式双模**：端侧 A2A 吃「低时延 + 数据不出端」（银行 1000+ 意图案例），云侧 A2A 吃「复杂深度推理」（O2O 端到端闭环）。这等于承认——**不是所有 Agent 协作都该在端侧**，端侧与云侧的分工应按「时延/隐私」vs「推理深度」划界。对做 OS 级 A2A 的 PM 而言，这是比单纯「端侧优先」更可执行的路由判据。

**B. Apple 用 View Annotations 把「屏幕感知」从猜测变成「App 主动声明」。**

Siri 过去的 on-screen awareness 常被诟病为「猜屏幕上的第三项」。Session 343 的 `.siriAnnotation` / `.appEntityIdentifier` / 选区映射 / 集合标注，本质是让 App **用 Schema 主动把屏幕语义锚点喂给系统**——再次印证本库长期主张：[[意图模式规范]] 的质量决定端侧路由上限。值得注意的是，这与「App 界面私有内容不自动开放」的边界声明完全一致：**语义开放是开发者显式 opt-in 的，不是系统扒屏**。

**C. IntentValueQuery + IndexedEntity + Streaming + 多轮，构成 Apple 2.0 的「可发现—可检索—可对话」闭环。**

把 Session 343 的 IntentValueQuery（结构化搜索）、IndexedEntity（语义索引）、2.0 的 streaming（流式）、conversational follow-ups（多轮）放到一起看：Apple 的 Schema Protocol 已从「单次意图执行」演进为「**持续对话中的结构化能力供给**」。这抬高了与其他三平台的代差——但也再次暴露 Schema 描述质量的杠杆作用（KDoc 写得好不好，直接决定 2.0 体验）。

**D. Android 的 Agent Skill 把「Schema 质量」变成可自动化产出的东西。**

AppFunctions Agent Skill 的 KDoc Refinement 步，本质是用 AI 把「给人看的注释」改写成「给 Agent 看的工具描述」——这恰好补上了 B 节里「Schema 写得含糊，再大模型也救不回」的短板。Android 的打法是用工具链把开发者从「写 Schema」的苦活里解放出来（与 Apple 的 VibeCoding/生成式 A2UI 思路遥相呼应）。

---

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入 / 合规）

**A. EU AI Act Article 15 把「XPIA 防护」从产品选择变成法律义务——这是执行安全叙事的第二个分水岭。**

本库 08-01 记录过第一个分水岭：Copilot for Word 文档型 XPIA 蠕虫把威胁模型从「一次注入」升级为「注入会自我复制」。今天 Article 15 生效是**第二个分水岭**：它把 prompt-injection 韧性、动作层网络安全、不可篡改日志、人类监督**写进高风险 AI 系统的强制合规**，罚则 €15M/3%。对四平台 OS Agent 而言含义明确：

- **Apple**：Extensions（Claude/GPT/Gemini）已纳入 App Review 分发治理；App Intents 2.0 的 Confirmations + entity ownership 直接对应「人类监督 + 差异化确认」。
- **Android**：AppFunctions 的系统代持一次性授权（[[Confirmation UI 安全机制]]）、ODR 式受控发现（EAP 仅限可信测试者）天然契合「受控发现 + 动作层安全」。
- **HarmonyOS**：小艺的「源头可控 / 记忆安全 / 理解可控 / 计算闭环」四支柱 + 芯片级可信根 + HPIC 增强级隐私测评，是最接近「端到端可举证」的架构。
- **Windows**：[[Agent Workspace 隔离执行]]（隔离会话 + 低权限账号 + ACL + 签名）是「动作层隔离」标杆；Article 15 现在给这套设计加了监管驱动力。

> 一句话：**此前四平台做 XPIA 防护是「想不想」，现在是「敢不敢不」**。

**B. 「端侧 A2A + 隐私不出端」是合规视角下的最优解，但带来新的攻击面问题。**

银行案例「1000+ 意图、多步执行、隐私数据不出端」在 Article 15 下极具说服力——端侧 A2A 天然满足「数据高安全性」。但本库 08-01 留下的未答问题在此更尖锐：**当多个端侧 Agent 通过 A2A 直接互写、互调，且载体是「看起来合法的内部产物」时，蠕虫式 XPIA 是否能在端侧 A2A 链里繁殖？** 四平台（含 HarmonyOS 端侧 A2A）目前**均无公开的类别级评估**（待补）。

**C. 用户体验侧补丁延续：Confirmations + entity ownership 把「确认」做细。**

Session 343 的「声明实体归属以差异化确认」是把 Confirmation UI 从「动作级」细化到「实体归属级」——删别人的相册 vs 删自己的，提示文案与风险权重不同。这是本库 [[Confirmation UI 安全机制]] 在 Apple 侧的官方补强，值得回填进该 B-note。

---

## 值得保留的点

1. **「AI Act Article 15 把 XPIA 防护从产品选择变成法律义务」** —— OS Agent 执行安全的第二个分水岭（继 Word 蠕虫之后）。罚则 €15M/3%，第 15(5) 条点名 prompt injection。
2. **HarmonyOS 端侧/云侧 A2A 双模的路由判据**：端侧吃「时延+隐私」，云侧吃「推理深度」——比笼统「端侧优先」更可执行。
3. **银行 1000+ 意图端侧 A2A 实证** —— 「隐私数据不出端」首次有了可引用的落地数字（厂商口径，待补具体 App 名）。
4. **Apple View Annotations 把屏幕感知从猜测变声明** —— `.siriAnnotation` / `.appEntityIdentifier` / 选区映射 / 集合标注，再次验证「Schema 质量决定路由上限」。
5. **App Intents 2.0 = streaming + 富实体 + 多轮** —— Schema Protocol 从「单次执行」演进为「持续对话中的结构化能力供给」。
6. **Android Agent Skill 的 KDoc Refinement 步** —— 用 AI 把「人看注释」改写成「Agent 看的工具描述」，补上 Schema 质量短板。
7. **Confirmations + entity ownership** —— 把确认从「动作级」细化到「实体归属级」，回填 [[Confirmation UI 安全机制]]。
8. **过滤纪律实例**：M365 Copilot Agentic 模式（应用层）被明确排除，证明本库对「系统级 vs 应用级」边界有执行。

## 我的问题

1. EU AI Act Article 15 对**四平台 OS Agent** 的具体合规触发条件是什么？HarmonyOS 小艺、Apple App Intents + Extensions、Android AppFunctions、Windows Agent Workspace 各自是否落入 Annex III 高风险范畴？还是说目前主要约束的是「嵌入产品的 AI 安全组件」（2027-08-02 才到）？（待补法律解读）
2. HarmonyOS 端侧 A2A 的**安全边界**如何定义？多 Agent 互写互调时，能否防止一个被污染的端侧 Agent 把载荷写回另一个？是否有类别级 XPIA 评估？（四平台均无，待补）
3. 「Per-Intent Privacy Manifest」是否真实作为独立 API 存在？本次一手检索未独立确认，需查 Apple 官方隐私清单文档。（待补）
4. Apple Extensions（Claude/GPT/Gemini）的 App Review 审查**具体审什么**？是否审「意图声明的安全性」还是仅审分发？（待补）
5. Android AppFunctions Agent Skill 的 KDoc Refinement 步，其「优化后 KDoc」是否会被 App Review/Play 审核约束？自动生成的工具描述出错谁负责？（待补）
6. Digital Omnibus 若最终通过，08-02 生效日是否会被真正推迟？截至本日仍按现行有效日记录，需持续跟踪正式文本。（待补）

## 后续动作

- [x] 提炼为概念（本次净增 0 个独立 B 节点；全部以「既有 B-note 追加」形式落库，避免重复）
- [x] 关联已有方法（本日无新建 C 层；执行安全合规动机已并入既有 [[XPIA 跨提示注入]] / [[Agent Workspace 隔离执行]] / [[Confirmation UI 安全机制]]）
- [x] **【流程改进·已执行】** 本日**正式切换为 7 日滚动窗口**（保留首次入库存量判定做去重），与记忆文件建议一致
- [ ] 跟踪 Digital Omnibus 正式文本是否通过 → 决定是否更新 Article 15 生效日口径
- [ ] 跟踪四平台对 Article 15 的合规响应（尤其 Apple Extensions 审查细则、HarmonyOS 端侧 A2A 安全边界）
- [ ] 核验 HarmonyOS 银行 App 具体名称与 1000+ 意图清单 / O2O 端到端闭环成功率
- [ ] 独立确认「Per-Intent Privacy Manifest」是否为真实 Apple API
- [ ] 回填 Android AppFunctions Agent Skill 发布日期（随 Android 17，待补具体日）
- [ ] 延续既有待办：四平台/六方 Registry+权限横向 Checklist（AgenticOS / Step AOS 仍未入表）
- [ ] 跟踪荣耀 Robot Phone 8 月发布、Måløy Word 蠕虫类别级缓解

> [!note] 概念节点双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本库对应节点**：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本次增补（不新建，仅追加到既有节点）**：[[Android AppFunctions 设备侧意图 2026]] ｜ [[A2A 端侧智能体协议]] ｜ [[Apple AppIntents Schema Protocol 2026]] ｜ [[Windows Copilot Actions 与 Agent Workspace 2026]] ｜ [[HarmonyOS Intents Kit 与 ArkAF 2026]]
>
> **既有笔记（不重写，仅指向）**：[[App Intent 的核心作用]] ｜ [[Apple Intelligence 与 App Intents]] ｜ [[国内安卓厂商做 App Intent 的阻力]] ｜ [[工业级 GUI Agent 架构（VLM+无障碍树）]] ｜ [[手机AI智能体知识库]]
