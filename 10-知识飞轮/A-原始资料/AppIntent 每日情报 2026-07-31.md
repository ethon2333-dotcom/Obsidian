---
type: daily-index
status: index
captured: 2026-07-31
window: "24h 严格窗口 2026-07-30 20:30 → 2026-07-31 20:30（另含 5 条库内空白补漏，均已标注真实日期，不冒充 24h 新闻）"
intent_category: "系统级意图框架 / 端侧 Agent 执行总线 / 跨应用 Intent 工作流 / 执行安全"
importance_score: "★★★★☆（8/10，24h 真增量 4 条 + 库内空白补漏 5 条 + 生态边界判断 1 条）"
tags: [AppIntent, 情报, 索引, 2026-07-31]
---

# AppIntent 每日情报 2026-07-31（索引）

> [!abstract]
> 端侧 Agent 的「执行通道」之争在 24h 内出现三个方向性信号：① **OSWorld 首破 90.2%**（实在Agent，GUI 路线能力天花板被抬高，但仅见于中文媒体、官方榜未核验）；② **豆包手机二代放弃 GUI 视觉模拟改走 MCP 官方接口直连**（国内首个公开的路线切换实证，动机是规避风控封禁）；③ **中国《人工智能智能体互联》7 项国家标准正式发布**，覆盖「身份标识—能力描述—供需发现—协同交互—工具调用」五段式，是四大 OS 私有 Registry 之外第一个国家级互联规范。**核心判据**：GUI 路线的瓶颈已从「能不能点对」转移到「被不被允许点」——是生态准入问题而非模型问题。另补齐 5 条库内空白（Android 17 GA、HMAF 2.0 细节、iOS 27 第三方实测、端侧 Planner 评测、Gemini 40+ App）。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 8/10 | **OSWorld 首破 90%**：实在Agent 90.2%，总榜 + Agentic Framework 分榜双第一；曲线 12%→72.6%→83.6%→90.2%；归因于工程调度系统（Harness）而非底座模型 | [[OSWorld 计算机操作基准]] | [[工业级 GUI Agent 架构（VLM+无障碍树）]] | [环球网/今日头条 2026-07-31](https://www.toutiao.com/article/7668533555215041066) |
| 8/10 | **豆包手机二代 NaviX Ultra 放弃 GUI 模拟转 MCP 直连**，动机为规避风控封禁；备货 3 万→20 万台。*（原报告细节，未入 B 笔记，保留于此：7-15 网信办首批手机端侧生成式 AI 备案中努比亚豆包大模型在列；同日 ChinaJoy 展出「全球首款 AI 智能体手机」，机身右侧设 AI 场景实体按键，属分发入口硬件化）* | [[端侧执行通道 GUI 与 MCP 路线之争]] | [[国内安卓厂商做 App Intent 的阻力]] · [[MCP 与设备侧 MCP]] | [手机助手动态 2026-07-31](https://new.qq.com/rain/a/20260731A0A7P300) |
| 8/10 | **智能体互联 7 项国家标准正式发布** + 北京首提 AIP / Token 经济 / OPC（单项目最高 1 亿元）；网安协会提出终端分级标识与可信开源代码安全；下一步补齐审计、交易标准 | [[智能体互联国家标准与 AIP]] | [[意图框架·跨体系索引 MOC]] | [中国商报 2026-07-31](https://weibo.com/ttarticle/p/show?id=2309405326740158808130) |
| 8/10 | **Android 17 GA（2026-06-16）**：AppFunctions 作为可编排工具贡献给 **Android MCP**，Agent 可直接访问应用本地状态；Jetpack 库 Alpha；`FEATURE_NEURAL_PROCESSING_UNIT` 让端侧 Planner 首次获得 OS 权限身份 | [[Android AppFunctions 设备侧意图 2026]] | [[MCP 与设备侧 MCP]] · [[端侧意图框架 学习笔记]] | [Android 17 is here](https://developer.android.google.cn/blog/posts/android-17-is-here) · [AppFunctions 官方文档](https://developer.android.google.cn/ai/appfunctions) |
| 9/10 | **HarmonyOS 7 / HMAF 2.0**：复杂任务成功率 >90%、首开 GUI 操控、20+ 系统级 AI 能力；五层架构核心是**图推理引擎（子任务 DAG 并行调度）**；云 A2A / 端 A2A 双接入（招商银行 1000+ 金融意图数据不出端）；SKILL.md + Module.json 打包机制；4 入口 × 6 触发分发面 | [[HarmonyOS Intents Kit 与 ArkAF 2026]] | [[HarmonyOS 元服务 学习笔记]] · [[Atomic Service 元服务]] | [HarmonyOS 7 / 小艺 Skill 与 A2A 2026-07-28](https://new.qq.com/rain/a/20260728A09FKD00) · [HMAF 2.0 架构拆解（二手）](https://xie.infoq.cn/article/778d6d52e4865d76a874f11b2) |
| 7/10 | **iOS 27 第三方 App Intents 首次实测生效**（beta 3）：Siri AI 可拉取第三方实时数据并弹权限确认；Tessie/Ford 可用而 Tesla 官方 App 不行 → 取决于适配质量而非白名单；SiriKit 弃用、9-14 正式发布、EU 因 DMA 延迟；PCC 零云 API 费 | [[Apple AppIntents Schema Protocol 2026]] | [[Apple Intelligence 与 App Intents]] | [Cult of Mac 实测 2026-07-06](https://www.cultofmac.com/news/siri-ai-third-party-apps-ios-27) · [iOS 27 时间线与 SiriKit 弃用](https://ecorpit.com/ios-27-siri-ai-waitlist-app-intents-developer-prep-2026) |
| 8/10 | **端侧 Planner 评测补齐**：TinyLLM BFCL 全表（xLAM-2-3b 65.74% / Qwen3-0.6B multi-turn 1.38%）；**1–3B 为甜点区、<1B multi-turn 可靠失败**；Gemma 4 QAT 与 Qwen3-Coder-Next 回填待补；Granite 4.1 68.27%/73.68%；🔴 **口径冲突已记录**（tool-router 90.42% ≠ 通用 Prompt 1.38%，不可互换引用）；⚠️ prism-coder「BFCL 100%」为自建基准（可借鉴的是 14b 承 99% 流量的级联结构） | [[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] · [[通用 AI Agent 评测基准 2026]] | [[端侧意图框架 学习笔记]] | [TinyLLM arXiv 2511.22138](https://ar5iv.labs.arxiv.org/html/2511.22138) · [本地模型工具调用横评](https://d-central.tech/local-llm-agent-capability) · [端侧 SLM 指南](https://www.digitalapplied.com/blog/small-language-models-on-device-agents-2026-guide) · [prism-coder-32b](https://huggingface.co/dcostenco/prism-coder-32b) |
| 7/10 | **Gemini 任务自动化扩至 40+ App**（Galaxy Unpacked 2026-07-22）；零代码 UI Automation 早期预览限 S26/Pixel 10、美韩；`actions.xml` 弃用，built-in intents 管「拉起履约」、AppFunctions 管「带参调用返回结构化结果」、UI Automation 只兜长尾 | [[Android AppFunctions 设备侧意图 2026]] · [[端侧执行通道 GUI 与 MCP 路线之争]] | [[安卓厂商意图识别破局策略]] | Galaxy Unpacked 2026-07-22（原报告未附链接，待补一手源） |
| 7/10 | **国内「谁接住意图」之争与支付边界**：支付宝 AHA × OPPO 小布（7-15）调用近 200 项生活服务；WAIC（Amoo × 美团跑腿）付款环节停在原生 App 等待确认 → **系统理解意图 / App 保留履约与支付 / 用户保留最终决定权**三分边界；Apple 同向要求主动声明 | [[Confirmation UI 安全机制]] · [[端侧执行通道 GUI 与 MCP 路线之争]] · [[意图支付授权协议 APOP]] | [[App Intent 的核心作用]] | [36氪：Agent 手机量产与 AHA](https://www.36kr.com/p/3916492156934023) |
| 6/10 | **小艺「帮帮忙」GUI 实测**：可跨应用操作支付宝/淘宝/拼多多，**微信提示「尚未接入」** → 超级 App 准入边界被公开可视化；华为为官方 Skill 通道 + GUI 兜底双轨 | [[端侧执行通道 GUI 与 MCP 路线之争]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] | [[工业级 GUI Agent 架构（VLM+无障碍树）]] | [南都实测转载 2026-07-31](https://new.qq.com/rain/a/20260731A0A7P300) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Windows**：Copilot Actions / Agent Workspace / ODR / XPIA 官方文档 24h 内无实质更新，仍为「四大构件（用户控制开关、Agent 账户、Agent Workspace、签名与吊销）+ 限定已知文件夹 + 默认关闭 + 管理员启用」。见 [[Windows Copilot Actions 与 Agent Workspace 2026]]。来源：[Windows agentic security](https://learn.microsoft.com/windows/security/book/operating-system-agentic-security)
- **值得保留的 6 条判断**已全部落入对应 B 笔记，不在索引重述：执行通道三分格局 → [[端侧执行通道 GUI 与 MCP 路线之争]]；OSWorld 天花板与准入瓶颈换位 → [[OSWorld 计算机操作基准]]；国标五段式作为跨平台对比骨架 → [[智能体互联国家标准与 AIP]]；HMAF 图推理引擎是唯一被点名的 Planner 结构 → [[HarmonyOS Intents Kit 与 ArkAF 2026]]；<1B 端侧路由三条件 → [[Function Calling 端侧工具调用]]；Android 17 系统中介隐私选择器即 Agent 时代 Confirmation UI 正确形态 → [[Confirmation UI 安全机制]]。

## 排除项

- **检索与口径元信息**（Horizon MCP 不在连接器列表、改用 WebSearch/WebFetch、未调用外部分析额度、窗口命中计数）：属过程记录，不构成可复用知识，已丢弃。
- **已完成的日期化动作项**（提炼 B / 关联 C / 输出 D）：流程痕迹，不入库。

## 未决问题（→ 各自 B 笔记跟踪，不在本索引展开）

- OSWorld 90.2% 官方榜单页与提交记录核验；361 vs 369 任务数口径；「跨应用协同」子集分数 → [[OSWorld 计算机操作基准]]
- 豆包走 MCP 是否需对端 App 单独授权/商务签约？与 `EXECUTE_APP_FUNCTIONS` 的「用户授权即可」是否有本质差异 → [[端侧执行通道 GUI 与 MCP 路线之争]]
- 7 项智能体互联国标的**标准号与全文**；其「能力描述」格式与 MCP tool schema / SKILL.md 的映射关系 → [[智能体互联国家标准与 AIP]]
- HarmonyOS 7 端 A2A 的协议细节与鉴权模型（招商银行 1000+ 意图如何做端侧隔离）；官方 API 文档二次确认 → [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[A2A 端侧智能体协议]]
- 【长期待办·已挂 3 天】Windows ODR × 中国 AIP × Android Registry × Apple App Toolbox 四方 Registry/权限横向表 → [[Intent Schema Protocol 意图模式规范]]
- 跟踪 iOS 27 正式版（9-14）第三方 App Intents 覆盖面 → [[Apple AppIntents Schema Protocol 2026]]
- Gemma 4 的 BFCL 路由准确率仍为待补 → [[Function Calling 端侧工具调用]]

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[App Intent 的核心作用]] · [[Apple Intelligence 与 App Intents]] · [[国内安卓厂商做 App Intent 的阻力]] · [[工业级 GUI Agent 架构（VLM+无障碍树）]] · [[MCP 与设备侧 MCP]] · [[HarmonyOS 元服务 学习笔记]] · [[端侧意图框架 学习笔记]] · [[安卓厂商意图识别破局策略]] · [[手机AI智能体知识库]]
> **本期原子笔记**：[[OSWorld 计算机操作基准]] · [[端侧执行通道 GUI 与 MCP 路线之争]] · [[智能体互联国家标准与 AIP]] · [[Android AppFunctions 设备侧意图 2026]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[Function Calling 端侧工具调用]] · [[Local Agent Bench 端侧智能体基准]] · [[通用 AI Agent 评测基准 2026]] · [[Confirmation UI 安全机制]] · [[意图支付授权协议 APOP]] · [[Windows Copilot Actions 与 Agent Workspace 2026]] · [[A2A 端侧智能体协议]] · [[Intent Schema Protocol 意图模式规范]] · [[Atomic Service 元服务]]
