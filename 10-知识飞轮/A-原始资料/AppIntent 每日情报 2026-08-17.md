---
type: daily-index
status: index
captured: 2026-08-17
window: "7 日滚动窗口 2026-08-11 → 2026-08-17（本期重点：收口连续第 8 日最高优先待办——四平台意图元数据来源轴）"
intent_category: "四平台意图 Registry 来源轴确认空白 / Apple Core AI 与多模型路由 / HarmonyOS A2UI / 执行安全确认机制硬件锚点"
importance_score: "★★★★☆（8/10：1 净新增跨平台 B 落定 + 5 既有 B 补漏 + 连续 8 日最高优先待办收口）"
tags: [AppIntent, 情报, 索引, 2026-08-17]
---

# AppIntent 每日情报 2026-08-17（索引）

> [!abstract]
> 本期四大 OS 官方执行总线（ODR / Agent Framework / Agent Workspace / Agent Launchers / AppFunctions / App Intents Schema / Intents Kit）**无新增可执行 API**；重心在「**收口连续第 8 日最高优先待办** + 库内空白补漏」：① **四平台意图 Registry 来源轴（provenance）经逐平台核验确认全空白**（Apple 用副作用轴 + 零信任输入处理回答「动作多危险 / 数据可不可信」，但 Registry 不记 provenance）——从「待查」升级为「**架构性空白 confirmed**」，落独立跨平台 B 节点；② **Apple Core AI 框架 + Dynamic Profiles + 多模型 Foundation Models（Claude/Gemini 经 Language Model 协议）+ Evaluations 框架**补全（iOS 27 指南，2026-06 库内空白补漏）；③ **HarmonyOS A2UI 生成式 UI + insight_intent.json 三步 + 1200 底层能力 Skill 化**；④ **Apple Secure Enclave「Secure intent」硬件确认锚点**补入确认机制分层。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 8/10 | 四平台意图 Registry 来源轴与权限模型对比（收口 8 日最高优先待办） | [[四平台意图 Registry 来源轴与权限模型对比 2026]] | [[意图模式规范]] · [[XPIA 跨提示注入]] | [iOS 27 guide](https://developer.apple.com/wwdc26/guides/ios) · [Android 17](https://developer.android.google.cn/blog/posts/android-17-is-here) · [HarmonyOS blog](https://developer.huawei.com/consumer/cn/blog/topic/03220919589498064) · [Windows agentic](https://developer.microsoft.com/en-nz/windows/agentic/) |
| 7/10 | Apple Core AI 框架 + Dynamic Profiles + 多模型 Foundation Models + Evaluations 框架（库内空白补漏·2026-06） | [[Apple AppIntents Schema Protocol 2026]] | [[端侧工具调用]] · [[语义路由]] | [iOS 27 guide](https://developer.apple.com/wwdc26/guides/ios) |
| 6/10 | Session 347 逐字稿补 `.onToolCall`/`.historyTransform`/`.SessionProperty` + 来源轴收口确认 | [[意图风险元数据与鉴权策略棘轮 2026]] | [[确认机制]] | [WWDC26 S347](https://developer.apple.com/videos/play/wwdc2026/347/) |
| 6/10 | Apple Secure Enclave「Secure intent」硬件确认锚点（物理按键→不可伪造） | [[Confirmation UI 安全机制]] | [[隔离执行]] | [Platform Security](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web) |
| 6/10 | HarmonyOS A2UI 生成式 UI + insight_intent.json 三步 + 1200 底层能力 Skill 化（库内空白补漏·HDC2026） | [[HarmonyOS Intents Kit 与 ArkAF 2026]] | [[元服务]] | [华为 blog](https://developer.huawei.com/consumer/cn/blog/topic/03220919589498064) |

> 说明：本笔记为**索引**，不内联分析。每条信息的完整技术细节、字段清单、待补项均在上方「原子笔记」链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：App Intents Schema 主体（240/343/345/347）+ Beta 5 增量 + Core AI/Dynamic Profiles/多模型 FM/Evaluations（本期补漏，均属 WWDC26/2026-06 指南，非 24h 新公告）；Session 347 逐字稿仅补代码级护栏细节。
- **Android**：AppFunctions 仍 1.0.0-alpha10 实验态、Gemini 私测；Android 17 GA（2026-06-16）已录。无新 API。
- **HarmonyOS**：Intents Kit / ArkAF 2.0 / A2UI 属 HDC2026（2026-06），本期仅补代码级接入细节与口径冲突（2100+ vs 1200+ 能力数）。无新 API。
- **Windows**：ODR / Agent Framework / Agent Workspace / Agent Launchers 窗口内无新 API；8-14 Copilot 应用改名（copilot.cloud.microsoft）、8-11 Patch Tuesday（83 CVE）属常规/安全更新，**非 OS 意图框架/执行总线**，低于阈值排除。
- **端侧 Planner**：Needle 2（08-11 发布）已于 08-16 录；本期仅补量产落地（Pebble Index 01）+ 发布日期锚定。FunctionGemma v4 第三方聚合分 27.03 标待补（来源日期晚于本运行日）。

## 排除项

- **Android 17 正式发布（2026-06-16）**：属库内已录（08-15/08-16），本期不重复收录。
- **Windows 8-14 Copilot 应用品牌更新 / 8-11 Patch Tuesday**：应用层改名与常规安全更新，非 OS 级意图框架/端侧路由/执行安全，低于阈值排除（同 08-04 排除纪律）。
- 纯大模型发布（非直接用于端侧意图路由）低于阈值，见排除纪律。

## 未决问题（→ 各自 B 笔记跟踪）

- 【已收口为确认结论】四平台意图元数据**来源轴（provenance）**全空白（架构性空白 confirmed）；最低成本补丁仍是意图 Registry 加 `readOrWrite` 声明位，仍非完整 provenance → [[四平台意图 Registry 来源轴与权限模型对比 2026]]。
- Needle 2 BFCL v4 42.6 / FunctionGemma v4 27.03 均为厂商自述/第三方，非 Berkeley 官方榜，待复核 → [[端侧 Router 置信度门控与工具可达性收缩 2026]] · [[Function Calling 端侧工具调用]]。
- Windows Agent Framework MIT 许可页 / build 号；Watch OS 26 是否 Trust Insights 类；NowSecure / AgentAntibody 独立核验；Berkeley 官方 BFCL v4 博客原文；Chrome Origin Sets 官方 URL 逐字复核（延续）。
- HarmonyOS `insight_intent.json` 字段全量 + API level 冲突（26 vs 23）待官方澄清 → [[HarmonyOS Intents Kit 与 ArkAF 2026]]。

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[四平台意图 Registry 来源轴与权限模型对比 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[意图风险元数据与鉴权策略棘轮 2026]] · [[Confirmation UI 安全机制]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[端侧 Router 置信度门控与工具可达性收缩 2026]] · [[Function Calling 端侧工具调用]]
