---
type: raw
status: inbox
date: 2026-07-31
captured: 2026-07-31
importance_score: ★★★★☆
intent_category: 系统级意图框架 / 端侧 Agent 执行总线 / 跨应用 Intent 工作流 / 执行安全
source:
  - "https://new.qq.com/rain/a/20260731A0A7P300 （手机助手动态 2026-07-31：努比亚 NaviX Ultra / 小艺 GUI 实测 / 豆包手机二代转 MCP / 网信协会）"
  - "https://www.toutiao.com/article/7668533555215041066 （环球网 2026-07-31：OSWorld 榜单 实在Agent 90.2%）"
  - "https://weibo.com/ttarticle/p/show?id=2309405326740158808130 （中国商报 2026-07-31：智能体互联 7 项国标 / 北京 AIP）"
  - "https://developer.android.google.cn/blog/posts/android-17-is-here （Android 17 正式发布 2026-06-16）"
  - "https://developer.android.google.cn/ai/appfunctions （AppFunctions 官方文档）"
  - "https://new.qq.com/rain/a/20260728A09FKD00 （HarmonyOS 7 / 小艺 Skill 与 A2A 接入路径 2026-07-28）"
  - "https://xie.infoq.cn/article/778d6d52e4865d76a874f11b2 （HMAF 2.0 架构拆解，二手整理）"
  - "https://www.cultofmac.com/news/siri-ai-third-party-apps-ios-27 （iOS 27 beta 3 第三方 App Intents 实测 2026-07-06）"
  - "https://ecorpit.com/ios-27-siri-ai-waitlist-app-intents-developer-prep-2026 （iOS 27 时间线与 SiriKit 弃用）"
  - "https://ar5iv.labs.arxiv.org/html/2511.22138 （TinyLLM：SLM 端侧智能体 BFCL 评测）"
  - "https://d-central.tech/local-llm-agent-capability （本地模型工具调用能力横评 2026）"
  - "https://www.digitalapplied.com/blog/small-language-models-on-device-agents-2026-guide （端侧 SLM 指南：BFCL 1–3B 甜点区）"
  - "https://huggingface.co/dcostenco/prism-coder-32b （prism-coder 路由级联，自建基准）"
  - "https://www.36kr.com/p/3916492156934023 （36氪：Agent 手机量产与 AHA / 应用侧边界）"
  - "https://learn.microsoft.com/windows/security/book/operating-system-agentic-security （Windows 智能体安全，本次无 24h 增量）"
tags: [AppIntent, OS-Agent, 端侧Planner, 执行安全, 每日情报, 跨平台2026]
---

# AppIntent 每日情报（2026-07-31）

> [!abstract] 30 秒速览
> **核心突破**：端侧 Agent 的「执行通道」之争在 24 小时内出现三个方向性信号——① OSWorld 首次被突破 **90.2%**（GUI 路线上限被抬高）；② 豆包手机二代 **放弃 GUI 视觉模拟、改走 MCP 官方接口直连**（厂商用脚投票选结构化通道）；③ 中国《人工智能智能体互联》**7 项国家标准正式发布**，覆盖「身份标识—能力描述—供需发现—协同交互—工具调用」，是四大 OS 私有 Registry 之外的第一个国家级互联规范。
> **关键指标**：OSWorld 90.2%（Agentic Framework 分榜第一，历史曲线 12%→72.6%→83.6%→90.2%）；豆包手机二代备货 3 万→20 万台；HarmonyOS 7 HMAF 2.0 复杂任务成功率 >90%、开放 2100+ 系统能力 Skill；Android 17 AppFunctions 贡献给 Android MCP（Jetpack 库 Alpha）。
> **OS Agent 场景**：一句话跨 App 执行（小艺帮帮忙已可操作支付宝/淘宝/拼多多，**微信未接入**）；支付环节强制停在原生 App 等待用户确认（WAIC Amoo × 美团跑腿）；端侧 A2A 让敏感金融意图（招商银行 1000+ 意图）数据不出端。

## 检索与口径说明（诚实标注）

- **窗口**：严格 24h（2026-07-30 20:30 → 07-31 20:30）实际命中 **4 条**（见「一、24h 真增量」）。
- **补漏**：另有 **5 条**是库内此前完全空白、但对本主题至关重要的官方/权威进展（Android 17 GA、HarmonyOS 7 HMAF 2.0 细节、iOS 27 第三方实测、端侧 Planner 新评测、Gemini 40+ App），**已逐条标注真实日期**，不冒充 24h 新闻。
- **信息源**：Horizon MCP 未在连接器列表中（不可用），改用 WebSearch/WebFetch 直取官方文档与权威媒体；合成由本 Agent 完成，未调用外部分析额度。
- **未核实项一律标「待补」**，媒体二手数据标注来源性质。

## 原始内容

### 一、24h 真增量（2026-07-31）

#### 1. OSWorld 首破 90%：实在Agent 90.2% ★★★★☆
- 全球总榜第一 + **Agentic Framework 分榜第一**，自 2024 年设立以来首次突破 90%，此前纪录由 Meta / OpenAI / Anthropic 保持。
- **历史曲线**：2024 年推出时 GPT-4o / Claude 约 **12%** → 2025 年底行业最优 **72.6%**（首超人类平均）→ 2026-05 **83.6%** → 本次 **90.2%**。
- 基准性质：港大 / CMU / 滑铁卢等联合发起，**真实操作系统内 361 项任务**（文件编辑、表格、图像、邮件、**跨应用协同**），机器自动判定。
- 强项细分：**跨应用协同**、图像处理（GIMP）、多软件联动；**系统底层操作类满分**。
- 团队观点：能力不只靠底座模型「智力」，更靠整套**工程调度系统（Harness）** 的可靠性。
- ⚠️ 口径：来源为环球网/今日头条报道，**OSWorld 官方榜单页未二次核验（待补）**。

#### 2. 豆包手机二代放弃 GUI 模拟，转 MCP 协议直连 ★★★★☆
- 钛媒体梳理：二代 NaviX Ultra **放弃一代的 GUI 视觉模拟路线，改用 MCP 协议与 App 官方接口直连**，明确动机是**规避风控封禁**。
- 备货量 **3 万 → 20 万台**；7 月 15 日网信办首批手机端侧生成式 AI 备案中，努比亚豆包大模型在列。
- 同日 ChinaJoy 展出「全球首款 AI 智能体手机」NaviX Ultra，机身右侧设 AI 场景实体按键（分发入口硬件化）。
- **意义**：这是国内厂商首个公开的「GUI → 结构化协议」路线切换实证，与 [[国内安卓厂商做 App Intent 的阻力]] 直接互文。

#### 3. 华为小艺帮帮忙 GUI Agent 实测：可操作支付宝/淘宝/拼多多，微信未接入 ★★★☆☆
- 南方都市报实测：语音指令可跨应用完成「去淘宝领金币」「支付宝查公积金」等任务。
- **微信提示「尚未接入」** —— 超级 App 对系统 Agent 的准入边界被公开可视化。
- 与 #2 形成对照：华为在官方 Intent 通道（ArkAF/Skill）之外，**同时保留 GUI 兜底**覆盖未适配长尾。

#### 4. 智能体互联国家标准与安全治理 ★★★★☆
- 《人工智能智能体互联》**系列 7 项国家标准正式发布**，搭建「**身份标识—能力描述—供需发现—协同交互—工具调用**」全覆盖规范体系（填补标准空白）。
- 北京 7-23《关于加快智能体引领发展的若干措施》首次提出 **智能体互联协议（AIP）**、Token 经济、OPC（一人公司）；单项目最高 1 亿元支持。
- 政策链：1 月《"人工智能制造"专项行动实施意见》→ 5 月《智能体规范应用与创新发展实施意见》（网信办/发改委/工信部）。
- 7-31 中国网络空间安全协会副秘书长梁博撰文：手机助手/终端智能管家/云端智能体加速涌现，需建立 **终端分级标识、可信开源代码安全** 等体系。
- 下一步（工信部/电子标准院）：补齐 **智能体审计、交易** 等关键基础标准。

### 二、库内空白补漏（非 24h，已标真实日期）

#### 5. Android 17 正式发布（2026-06-16）：AppFunctions 贡献给 Android MCP ★★★★☆
- **AOSP 源码已放出**；Android 17 **扩展 AppFunctions**，把 App 能力作为可编排「工具」贡献给 **Android MCP（设备端等效 MCP）**；Jetpack 库处于 **Alpha**，仅需类注解 + KDoc。
- 官方原文：「AI 代理和助理（例如 Google Gemini）可以发现并执行 AppFunctions，以代表用户执行工作流，**并直接访问应用的本地状态**。」
- 配套：**AppFunctions 智能体技能**（分析工作流→生成 Kotlin→优化 KDoc→给 ADB 命令）、**测试代理应用**（模拟 Agent 环境调试）、抢先体验计划 `goo.gle/eap-af`；验证命令 `adb shell cmd app_function list-app-functions`。
- Gemini 集成仍为**可信测试者私测**（自 2026-05）；AppFunctions 需 `EXECUTE_APP_FUNCTIONS`，Android 16+ 可用。
- **端侧算力显性化**：以 Android 17 为目标且需直接访问 NPU 的应用，必须在清单声明 `FEATURE_NEURAL_PROCESSING_UNIT` —— 端侧 Planner 首次被 OS 权限模型正式承认。

#### 6. HarmonyOS 7 / HMAF 2.0 细节（HDC 2026，开发者 Beta 推送中）★★★★★
- **HMAF 2.0（鸿蒙智能体框架 2.0）**：复杂任务成功率 **>90%**、**首次开放 GUI 操控能力**、开放 **20+ 系统级 AI 能力**。
- **五层架构**：用户意图层（盘古 6.0 端侧意图理解，多数推理本地完成）→ 智能体调度层（**图推理引擎 Graph Reasoning Engine**，把复杂任务拆成**子任务 DAG** 并行调度，是 >90% 成功率的关键）→ Skill 能力层（每个 Skill 声明 `describe` + `execute`）→ 分发/执行层。
- **接入两条路径**：**Agent 接入**（云 A2A / **端 A2A**）与 **Skill 接入**。
  - 云 A2A 适合服务型应用（大麦：询问演出→选座→下单→支付一次对话闭环）。
  - **端 A2A 隐私数据不出端**（招商银行覆盖 **1000+ 金融意图**，敏感数据全程不出手机）。
- **Skill 层门槛极低**：Vibe Coding 由描述自动生成 Skill；现成 API/MCP 可快速打包为 Skill；**标准化 SKILL.md 描述 + 运行时**；应用内 Skill 随包发布，`Module.json` 处理端侧能力与安全权限，**意图框架负责注册工具能力**，逻辑用 ArkTS 实现；小艺开放平台支持一键发布真机调试。
- **分发面**：4 个入口（小艺 App / 小艺建议 / 小艺搜索 / 小艺输入法）× 6 种触发（语音唤醒、长按电源键、AI Bar、拖拽、双指按压、指关节圈选）。
- 规模口径：2100+ 系统能力 Skill、500+ 生态 Skill、2000+ 鸿蒙智能体（与库内既有记录一致）。
- ⚠️ 多为媒体二手整理（腾讯网/InfoQ/今日头条），**HarmonyOS 7 官方 API 文档细节待二次确认**。

#### 7. Apple iOS 27：第三方 App Intents 首次实测生效（2026-07-06 beta 3）★★★☆☆
- 开发者实测：Siri AI 可从第三方 App **拉取实时数据**（如电车电量），**查询前弹权限确认**；Tessie、Ford 官方 App 可用，**Tesla 官方 App 反而不行** —— 说明取决于各家 App Intents 适配质量而非系统白名单。
- 时间线：WWDC26（6-08/09）Siri AI 发布并**正式弃用 SiriKit**（2~3 年迁移窗口）→ 6-08 开发者 Beta（候补名单 4~48h）→ **7-13 公测（与 dev beta 3 同构建）** → **9-14 正式发布**。
- **EU 因 DMA 延迟** iOS/iPadOS 27 的 Siri AI。
- 成本侧：App Store 小企业计划成员（累计下载 <200 万）可在 **Private Cloud Compute 上零云 API 费**调用下一代 Foundation Models。

#### 8. 端侧 Planner 评测补齐（回填库内待办）★★★★☆
- **Gemma 4 QAT（2026-06-05）**：内存约 **-72%**，质量与 FP16 相差数点；**E2B 在 LiteRT-LM 移动格式下 <1GB**；26B-A4B MoE 可跑 16GB 笔记本。→ 回填库内「Gemma 4 待补」。
- **Qwen3-Coder-Next 80B-A3B（2026-03-03）**：SWE-bench Verified **>70%**（SWE-Agent），3B 激活 MoE。→ 回填「Qwen3-Coder-Next 待补」，但**属编码智能体、非端侧路由**，不能混用。
- **IBM Granite 4.1 BFCL-v3（2026）**：8B **68.27%**，30B **73.68%**；Nano 350M/1B 面向受限边缘。
- **Phi-4-mini 3.8B**：BFCL v4 **低到中 80 分段**（第三方 ertas，2026-05，**非 Berkeley 官方行**）；MIT 许可。
- **TinyLLM（arXiv 2511.22138）BFCL 总表**：

  | 模型 | Overall | Live | Non-live | **Multi-turn** |
  |---|---|---|---|---|
  | xLAM-2-3b-fc-r (FC) | 65.74% | 81.03% | 88.22% | **55.62%** |
  | Qwen3-4B (Prompt) | 62.04% | 75.52% | 82.58% | 35.25% |
  | Qwen3-1.7B (Prompt) | 55.49% | 63.48% | 80.03% | 16.88% |
  | xLAM-2-1b-fc-r (FC) | 53.97% | 61.57% | 72.42% | 8.38% |
  | **Qwen3-0.6B (Prompt)** | 45.76% | 58.86% | 67.78% | **1.38%** |
  | TinyLlama-1.1B / TinyAgent-1.1B | ~19.7% | ~39% | 20.00% | 0.00% |

- **结论（BFCL 通用规律）**：**1–3B 是端侧单轮工具调用的甜点区**；**<1B 在 multi-turn / parallel / nested 上可靠失败**，只适合抽取与分类，不适合 Agent 循环。
- 🔴 **重要口径冲突（必须记录）**：库内既有记录「qwen3-0.6b-**tool-router** BFCL Multi-Turn Base **90.42%**」与 TinyLLM 测「Qwen3-0.6B（**Prompt 原始**）Multi-turn **1.38%**」并不矛盾，但**绝不可互换引用**——前者是**窄域 6~N 工具微调后的确定性 router**（禁 CoT + 严格 JSON + 子集 Multi-Turn Base），后者是**通用未微调 Prompt 模式全量 multi-turn**。**结论：<1B 模型只有在「窄域 + 微调 + 严格约束输出」三条件同时满足时才可上端侧主路由。**
- ⚠️ **基准污染警示**：prism-coder 8b/14b/32b 宣称「BFCL 100%」，实为**自建 6-tool 路由基准（102 用例 × 3 seed）**，**不是 Berkeley 官方 BFCL**，不可与官方分数并列。其真正可借鉴处是**级联结构**：14b 承担 **99%** 流量、1% 升级 32b、**0% 打到云端 Opus**，级联整体 100% vs Opus-solo 98.3%。

#### 9. Gemini 任务自动化扩至 40+ App（Galaxy Unpacked 2026-07-22）★★★☆☆
- Gemini task automation 从 2 月 Beta 的少数几个扩到 **40+ 应用**（购物、餐厅预订、旅行预订、活动票务）；同期发布 Gemini Nano 4 与 Galaxy Z Fold 8 / Flip 8。
- **零代码 UI Automation 早期预览**：Galaxy S26 与部分 Pixel 10，覆盖外卖、生鲜、打车，**限美国与韩国**。开发者「不接入也有覆盖，但失去执行控制权」。
- `actions.xml` 已弃用；built-in intents 保留用于「拉起并履约」，AppFunctions 用于「带类型参数调用并返回结构化结果」。

#### 10. 国内「谁接住意图」之争与支付边界（36氪，7 月）★★★☆☆
- **支付宝 AHA**：跨端协同接口；**7-15 「阿宝」与 OPPO「小布助手」跨端连接** —— 小布负责理解需求，阿宝调用支付宝内部**近 200 项生活服务**，关键授权与支付仍由用户确认。
- WAIC 演示（Amoo × 美团跑腿）：系统 Agent 完成地址推断与订单填写，**进入付款环节任务停在美团页面等待用户确认** —— 「系统理解意图 + App 保留履约与支付 + 用户保留最终决定权」的三分边界。
- 苹果 2026 开发者文档同向：App 须经 App Intents **主动声明**可被调用的动作与数据，**界面私有内容不自动开放**，敏感/破坏性操作可要求二次确认。
- 判断：MCP / App Intents / AHA 并非同一协议，但解决同一问题——**让应用主动决定哪些能力可被 Agent 调用**，而非系统 Agent 自行闯入读页面。

### 三、本次无增量的方向

- **Windows**：Copilot Actions / Agent Workspace / ODR / XPIA 官方文档 24h 内无实质更新，仍是「四大构件（用户控制开关、Agent 账户、Agent Workspace、签名与吊销）+ 6 个已知文件夹 + 默认关闭 + 管理员启用」。见 [[Windows Copilot Actions 与 Agent Workspace 2026]]。

## 值得保留的点

1. **执行通道三分格局定型**：官方 Intent/Function 直连（最可靠）→ MCP 连接器（跨生态）→ GUI 兜底（覆盖长尾但受风控与 UI 改版影响）。豆包手机从 GUI 切 MCP、小艺双轨并行，是同一判断的两种打法。
2. **OSWorld 90.2% 抬高了 GUI 路线的天花板**，但同期厂商反而在**弃用 GUI 走结构化接口** —— 说明瓶颈已从「能不能点对」转移到「被不被允许点」（风控/准入），这是产品与生态问题而非模型问题。
3. **中国 7 项智能体互联国标**给出的五段式（身份标识—能力描述—供需发现—协同交互—工具调用）与四大 OS 的私有 Registry 高度同构，是做跨平台对比的现成骨架。
4. **HMAF 2.0 的图推理引擎（DAG 并行调度）** 是四平台里唯一被明确点名的「Planner 结构」，其他家只讲 Schema 与路由，不讲编排引擎。
5. **<1B 端侧路由的真实边界**：窄域 + 微调 + 严格 JSON 三条件，缺一不可；通用 multi-turn 场景 0.6B 近乎不可用（1.38%）。
6. **Android 17 的「系统中介隐私选择器」范式**（联系人字段选择、系统渲染位置按钮、EyeDropper）本质是把「敏感数据授权」从 App 权限升级为**系统代持的一次性确认 UI** —— 这正是 Agent 时代 Confirmation UI 的正确形态。

## 我的问题

- OSWorld 90.2% 的官方榜单页与提交记录能否核验？其 361 项任务里「跨应用协同」子集的具体得分？（待补）
- 豆包手机二代走 MCP，**对端 App 是否需要单独授权/商务签约**？若需签约，与 Google `EXECUTE_APP_FUNCTIONS` 的「用户授权即可」有本质差异。
- 7 项智能体互联国标的**标准号与全文**？其「能力描述」格式与 MCP tool schema / SKILL.md 的映射关系？
- HarmonyOS 7 端 A2A 的**协议细节与鉴权模型**（招商银行 1000+ 意图如何做端侧隔离）？
- Windows ODR 与中国 AIP、Android Registry、Apple App Toolbox 的**四方 Registry/权限横向表**（库内长期待办，仍未完成）。

## 后续动作

- [x] 提炼为概念（→ B 新增 3 篇 + 增补 5 篇）
- [x] 关联已有方法（→ C 新增 [[端侧执行通道选型 SOP]]；沿用 [[系统级 Intent 路由评估 SOP]]）
- [x] 输出总览（→ D [[AppIntent 每日情报速览 2026-07-31]]）
- [ ] 核验 OSWorld 官方榜单与 7 项国标标准号（回流 A）
- [ ] 完成四平台 Registry/权限横向 Checklist（跨日待办，已挂 3 天）
- [ ] 跟踪 iOS 27 正式版（9-14）第三方 App Intents 覆盖面

> [!note] 概念节点双链
> [[Intent Schema Protocol 意图模式规范|意图模式规范]] ｜ [[Intent Router 语义路由|语义路由]] ｜ [[Function Calling 端侧工具调用|端侧工具调用]] ｜ [[Confirmation UI 安全机制|确认机制]] ｜ [[Atomic Service 元服务|元服务]] ｜ [[Agent Workspace 隔离执行|隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
> 
> 本次新增节点：[[OSWorld 计算机操作基准]] ｜ [[智能体互联国家标准与 AIP]] ｜ [[端侧执行通道 GUI 与 MCP 路线之争]]
> 既有笔记互链（未改动原文）：[[App Intent 的核心作用]] ｜ [[Apple Intelligence 与 App Intents]] ｜ [[国内安卓厂商做 App Intent 的阻力]] ｜ [[工业级 GUI Agent 架构（VLM+无障碍树）]] ｜ [[手机AI智能体知识库]]

#标签/AppIntent #标签/OSAgent #标签/每日情报 #标签/执行安全
