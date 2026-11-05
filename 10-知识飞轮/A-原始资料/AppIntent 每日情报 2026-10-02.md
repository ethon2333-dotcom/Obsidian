---
date: 2026-10-02
tags: [情报, AppIntents, 系统级意图框架, 端侧Agent, 执行安全, XPIA, Windows, 策略治理]
source:
  - https://www.163.com/dy/article/L85Q4G630511BLFD.html
  - https://tech-insider.org/ios-27-release-date-siri-ai-features-2026/
  - https://appauxin.com/ios-27-1-release-date
  - https://developer.apple.com/documentation/updates/appintents
  - https://developer.android.google.cn/jetpack/androidx/releases/appfunctions
importance_score: "★★★★☆"
intent_category: 执行安全 / 控制面治理 / OS 部署里程碑
---

# AppIntent 每日情报 2026-10-02（系统级 Agent 与 OS 意图框架前沿）

> [!abstract] 30 秒速览
> - **核心突破**：本窗口（2026-09-30 → 10-02，约 2 天）**四大 OS 官方框架层仍零净新增 API**——iOS 27.1 无新 `@AppIntent(schema:)` Schema / AppFunctions 守 alpha12 无 alpha13 / A2UI 守 alpha01 / HarmonyOS 无新 API / Windows 26H2 无新 Registry API。唯一 OS 级真增量 = **Windows agent 连接器策略治理面（组策略/MDM 命名首次公开）**：`ConfigureAgentConnectors` / `AgentConnectorAccessPolicy` / `AgentConsentDuration`，把「连接器的开关、白名单、授权持久化时长」落到可治理策略项，且**仅企业版/教育版/IoT 企业版**可完整管控，家庭版/专业版无法彻底关闭连接器。
> - **关键指标**：iOS 27.1 公开版预期 **2026-10-19~23**（9to5Mac/MacRumors 经第三方汇总，Apple 未官方确认）；Windows 26H2 已于 **09-29 GA**（本窗口 10-01 媒体确认）。BFCL v4 仍 Llama 3.1 405B **88.5%** 居首，端侧 MiniCPM5-2B 66.6 / FunctionGemma-270m 27.0 不变。
> - **OS Agent 执行安全**：执行总线「受控发现 + 授权持久化」控制面具体化——连接器白名单 = 执行边界，consent 时长 = 授权窗口；直击 [[确认机制]] / [[隔离执行]] / [[XPIA 跨提示注入]]。家庭/专业版不可控这一事实，暴露「降级可控性」的版本割裂风险。

## ① Schema 定义与语义路由机制（四大 OS 框架层）

**Apple（无净新增）**：`developer.apple.com/documentation/updates/appintents` 最新条目仍为 **June 2026**（App schema domains / `IndexedEntityQuery` / `OwnershipProvidingEntity` / `EntityCollection` 等），**无 October 新 Schema API**。iOS 27.1 首个 beta **仍未放出**；公开版预期 **2026-10-19~23**（tech-insider 引 9to5Mac / MacRumors；appauxin 给「10-23 前、大概率 10-19~21」的 iPhone Duo 绑定硬 deadline）。无新 `@AppIntent(schema:)` Schema、无 App Intents Domains 新域。延续「OS 框架不日更」。

**Android（无净新增）**：`developer.android.google.cn/jetpack/androidx/releases/appfunctions` 最新仍为 **`1.0.0-alpha12`（2026-09-23）**；本窗口检索（含官方 release notes 与 alpha-channel）**无 alpha13 信号**。`a2ui` 守 `1.0.0-alpha01`。无新 Registry/权限/scope API。

**HarmonyOS（无净新增）**：HC2026（9-17~21）内容已覆盖；本窗口检索命中的均为 HDC2026（6 月）/ HarmonyOS 7 Beta1 / 7.0 Beta1 旧文，**无新框架/API**。Intents Kit（Want）/ 元服务（installationFree）/ ArkAF 2.0（意图/Skills/A2A 三层）/ A2UI 不变。

**Windows（部署确认 + 控制面细节，非 API 新增）**：26H2 已于 **09-29 GA**（本窗口 10-01 cnBeta/163 媒体确认「微软近日向公众发布 Windows 11 26H2」），仍为 enablement package 形态。本窗口**无新 Registry API**，但**首次公开 agent 连接器治理的策略命名**（见②）——这是执行安全控制面的具象化，非框架 API 进位。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**★6/10 真增量：Windows agent 连接器策略治理面（2026-10-01，cnBeta/163 引 Neowin）**。报道披露 Windows 26H2 中 agentic 能力的**具体组策略/MDM 控制项**，把「谁能连、连什么、授权留多久」落到可治理策略：

- **`DisableSettingsAgent`**：关闭「设置 AI 代理」（以本地 AI 概览替代传统设置搜索）。⚠️ **仅企业版/教育版/IoT 企业版**支持；家庭版/专业版不在官方支持范围（即便专业版带 gpedit，手动加注册表值也绕不过版本限制）。
- **`ConfigureAgentConnectors`**：开关 agent 连接器（即 Agent 可访问的 **MCP server / host**）。⚠️ 仅企业/教育/IoT 企业版。
- **`AgentConnectorAccessPolicy`**：**限制连接器可访问范围（allow-list）**。⚠️ 仅企业/教育/IoT 企业版。
- **`AgentConsentDuration`**：控制**授权决定保留多久**（consent 持久化时长）。⚠️ 仅企业/教育/IoT 企业版。
- **File Explorer 连接器**：可读取/创建/移动/重命名/修改本地文件，访问仍需**用户明确授权**（confused-deputy 面）。

**为什么是执行安全增量**：此前本库记的 ODR 受控发现 + 三档 consent（Ask every time / Allow always / Never allow，见 09-17 增补）是**产品设计态**；本次披露的是**把同一逻辑落到 OS 控制面（Group Policy/MDM）的具体策略项**——连接器白名单 = 执行边界（缩小 XPIA 受控面），consent 时长 = 授权窗口（缩短被劫持后的行动窗口）。这是「受控发现 + 授权持久化」从原则到治理件的第一步公开证据。

**版本割裂风险（OS PM 视角）**：家庭版/专业版用户**无法通过策略彻底关闭连接器**，也**无法限制 agent 可用 MCP server**——意味着多数 Copilot+ PC 消费者实际处于「连接器常开、白名单不可控」状态。这与「用户应能按偏好调整系统体验」形成张力，也可能成为企业合规（EU AI Act Article 15 抗注入可举证性）的落地缺口。

**性质判定**：非新 OS API（仍是 Group Policy/MDM 控制面），但属**执行安全治理机制的具体化**，达 ★6/10 收录阈值；家庭/专业版限制为新增事实点。

**去伪/无新增（已复核）**：XPIA 本窗口检索命中的 Microsoft RAMPART（GitHub 测试框架工件）、agentmelt、treza、futureagi 均为**既有工具与综述**，**无 09-30→10-02 窗口内新 CVE / 新研究突破**；多智能体注入（arXiv:2609.22949）/ 自复制注入 / SearchLeak 等维持 09-30 状态。BFCL v4 仍 Llama 3.1 405B **88.5%** 居首；端侧 Planner MiniCPM5-2B 66.6 / LFM2.5-8B-A1B 49.7 / Needle2 42.6 / FunctionGemma-270m 27.0 不变，**无新端侧 Planner 入榜**。

## 诚实标注 / 待办

- cnBeta/163（2026-10-01）文章为媒体汇总，政策项命名与版本限制来自 **Neowin 转述**，**待 learn.microsoft.com 逐字复核**——尤其 `ConfigureAgentConnectors` / `AgentConnectorAccessPolicy` / `AgentConsentDuration` 是否确为 Group Policy 项、家庭/专业版限制是否准确。
- iOS 27.1 beta 与公开版日期（10-19~23）为 9to5Mac/MacRumors 经第三方（tech-insider/appauxin）汇总，**Apple 未官方确认**；本库此前预期「10 月底~11 月初」需下修为「10 月中下旬」。
- 沿用待办：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / NowSecure / AgentAntibody / Chrome Origin Sets / 高通 NPU exact specs / Berkeley 官方 BFCL v4 博客 / AppFunctions alpha13 / A2UI alpha02 / iOS 27.1 正式 beta Schema / 多智能体注入一手论文 / 自复制注入 OpenAI 原文。

> [!note] 概念节点双链
> - [[Intent Schema Protocol 意图模式规范]]
> - [[Intent Router 语义路由]]
> - [[Function Calling 端侧工具调用]]
> - [[Confirmation UI 安全机制]]
> - [[Atomic Service 元服务]]
> - [[Agent Workspace 隔离执行]]
> - [[A2A 端侧智能体协议]]
> - [[XPIA 跨提示注入]]

## 24h 复核补捕（2026-10-02 21:01 re-trigger，窗口 2026-10-01 21:01 → 10-02 21:01）

> 本段为当日 09:00 自动化跑后的 24h 复检（re-trigger）。晨间跑已覆盖 7 日窗口（09-30→10-02）并结论「四大 OS 官方框架层 API 零净新增」；本次聚焦过去 24h，结论一致：**仍零净新增 OS 框架 API**（Apple iOS 27.1 无新 `@AppIntent(schema:)` Schema / Android AppFunctions 守 alpha12 / HarmonyOS 无新 API / Windows 无新 Registry API）。以下为窗口内/窗口邻的新进展与跨窗口补强。

**①（★5/10，消费级 OS Agent 商业化信号）HarmonyOS Mate 90 / 小艺Claw（10-01 发布会）**：小艺升「个人专属智能体」，可感知 200+ 系统级数据、调用 2100+ 系统能力、协同 2000+ 鸿蒙智能体；**小艺Claw 订阅 49 元/月**，尝鲜版遭体验倒退吐槽（响应变慢、识别错误、「高级功能要充钱」落差）。→ 补 [[HarmonyOS Intents Kit 与 ArkAF 2026]]。性质判定：产品/UX 层，非框架 API 新增；但「意图执行被订阅化 + 体验倒退 backlash」是四平台首个消费级 OS Agent 商业化的真实信号（OS PM 视角）。来源：今日头条/机锋网 10-01，媒体/厂商口径。

**②（★5/10，跨平台路由/决策模型市场升温）Cloudflare Clef + Clef-flash（10-01 开源 Apache 2.0）+ 同日 Amazon Strands Decider 2B**：直击 Typesafe Jev「决策模型」品类（agent 工具路由层）。Clef BFCL case-exact **98.5**、中位延迟 **209ms vs Jev 524ms**；Clef-flash 基于 **Qwen3.5-9B**、p95 122ms。→ 补 [[Function Calling 端侧工具调用]]（决策模型子类）。⚠️ Clef/Strands 为 **edge/cloud 部署（Cloudflare Workers AI / Amazon），非 on-device**；BFCL 98.5 为 **Cloudflare 厂商自报、未经独立复现**；属「意图路由模型」品类扩张，不计入端侧 Planner 榜。

**③（★5/10，XPIA 防御量化，待一手）DecodingTrust-Agent(DTAP) 红队实证（techwalker 10-01 综述）**：在 DTAP 上搜出 15 套独立安全方案，平均攻击成功率 **45.6% → 10.0%**，正常任务完成率仅降 **3.3pp**（对比固定方案 Progent 完成率 79.8%→56.4%，可用性掉 23pp）。→ 补 [[XPIA 跨提示注入]]。⚠️ 媒体综述，论文日期/评测协议待一手复核；文件系统场景残留失败 43/57 来自直接攻击（须判操作本身是否合规），金融场景 24/41 来自间接注入（须核实来源）——与库内「间接注入靠溯源、直接攻击靠授权边界」二分一致。

**④（跨窗口补强，非 24h，★5/10 治理收敛）Android 17 企业策略可关 AppFunctions 数据**：iseC7 引 Google 企业页（09-16 更新）`setAppFunctionsPolicy` + 标志 `APP_FUNCTIONS_DISABLED` 全局禁用 AppFunctions 数据给 on-device agents；`setNearbyAppStreamingPolicy` 关 AI 自动化；工作 Profile 默认不返回 AppFunctions 数据。→ 补 [[Android AppFunctions 设备侧意图 2026]]。含义：与晨间跑的 Windows 连接器策略治理（ConfigureAgentConnectors / AgentConnectorAccessPolicy）构成**跨平台「agent 能力可经 MDM 关闭/白名单」收敛**——Google 用 `APP_FUNCTIONS_DISABLED`、Microsoft 用 Allow-list + consent 时长，方向相反但同构（均把 agent 执行边界交给企业管控）。⚠️ 来源为 09-16 企业页，非 24h 窗口；作治理面 corroboration 收录。

**⑤（跨窗口 backlog，非 24h，★5/10 权威中文数据）2026 大模型安全众测（CN-SEC，09-15 国家网络安全宣传周）**：2467 名白帽子测 25 家厂商 54 款产品，发现 **873 漏洞（其中智能体特有 608 个）**；六类典型风险含提示注入（最普遍）、代理身份与权限滥用、代理目标劫持、非预期代码执行。→ 建议下个完整窗口正式补 [[XPIA 跨提示注入]]（本库尚无此权威中文监管数据）。⚠️ 09-15 发布，非 24h。

**去伪/无新增（已复核）**：BFCL v4 仍 Llama 3.1 405B **88.5%** 居首（anotherwrapper 10-02 更新）；端侧 MiniCPM5-2B 66.6 / FunctionGemma-270m 27.0 / Needle2 42.6 不变；Spark-X2.5-4B BFCL 65.1 为厂商自测（标待补，不可与官方榜并列）；iOS 27.1 beta 仍未出、公开版预期维持 10-19~23（第三方汇总）；AppFunctions alpha13 / A2UI alpha02 仍未发布。
