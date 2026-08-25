---
type: daily-index
status: index
captured: 2026-08-09
window: "同日增补跑（21:00 版之后的净新增），不重跑 7 日全窗口"
intent_category: "执行安全 / 读写分级 / 确定性门控 / 跨源数据外泄防护"
importance_score: "★★★★☆（8/10，连续 6 日最高优先待办取得第二次实质进展）"
tags: [AppIntent, 情报, 索引, 增补跑, 2026-08-09]
source: "https://security.googleblog.com/ · https://techcrunch.com/2025/12/08/google-details-security-measures-for-chromes-agentic-features/ · https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini"
---

# AppIntent 每日情报 2026-08-09-晚（索引 · 增补跑）

> [!abstract] 30 秒速览
> **性质**：同日 21:00 版已跑完整 7 日窗口，本轮为**增补跑**——不重跑全窗口，把检索预算集中投给**连续 6 日未解的最高优先待办**（四平台意图元数据来源分级），并按 08-03 定下的路径改走**官方安全文档 / 白皮书**。
> **核心突破**：待办取得**第二次实质进展**，且层级与 08-04 完全不同。08-04 找到的是**治理层**答案（微软 AGT），本轮找到的是**客户端层已产品化**的答案——**Chrome Agent Origin Sets**（read-only / read-writeable 双集合 + 确定性门控函数 + 隔离评判模型）。结论由「两层」精化为**三层：研究层有方案 / 治理层有模型 / 客户端层已产品化 / OS 意图层仍全空白**。
> **最可迁移的一句**：Chrome **把 tool call 也划成 read-vs-write** 并检查其是否适合当前任务——OS 意图框架里每个 intent 本质就是一次 tool call，**这是可直接抄进意图 Registry 的最低成本原语**。
> **关键指标**：VRP agentic 类别赏金 **$20,000**；Chrome 首版**仅实现 read-writeable 集合**（官方自陈）。

## 本期条目索引

| 重要性 | 条目 | 原子笔记（完整内容） | 主题枢纽 | 一手来源 |
|---|---|---|---|---|
| 8/10 | **Chrome Agent Origin Sets + User Alignment Critic**：读 / 写分级 + 确定性门控 + 隔离评判器；**tool call 同样划读写**（真实日期 **2025-12-08**，库内空白补漏） | [[Chrome Agent Origin Sets 与用户对齐评判器 2026]] | [[XPIA 跨提示注入]] · [[隔离执行]] · [[意图框架·跨体系索引 MOC]] | Nathan Parker, Chrome security team, security.googleblog.com（2025-12-08）· [TechCrunch 2025-12-08](https://techcrunch.com/2025/12/08/google-details-security-measures-for-chromes-agentic-features/) |
| 8/10 | **最高优先待办第二次实质进展**：三层结论 + 四平台清单新增「跨层参照」列 + 新增最低成本判据 `readOrWrite` 声明位 | [[Agent Data Injection 数据注入攻击#2026-08-09晚 增补：待办第二次实质进展——结论从「两层」精化为「三层」]] | [[XPIA 跨提示注入]] · [[意图模式规范]] | 同上（层级校准经本库交叉判读） |
| 7/10 | **Google 官方六层防御口径**（classifiers / security thought reinforcement / markdown sanitization + URL redaction / user confirmation framework / **end-user mitigation notifications** / model resilience），此前本库仅有二手转述 | [[XPIA 跨提示注入#2026-08-09晚 增补：Google 官方六层防御口径 + NCSC 的「混淆代理」定性]] | [[确认机制]] · [[XPIA 跨提示注入]] | [Google Workspace 管理员帮助（更新 2026-03-17）](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini) |
| 7/10 | **「门不能是模型」的工业校验 → 提炼出第三条路线「隔离门」**：裁决者仍是模型，但输入面被架构性收窄到攻击者不可写入的部分 | [[带外防御与确定性门控#2026-08-09晚 增补：「门不能是模型」的第一次工业现实校验]] | [[确认机制]] · [[隔离执行]] | 同条目 1（本库提炼） |
| 6–7/10 | **确认「触发器」三档分类法**（模型自决 / 分类器判定 / **确定性规则**），与既有「确认内容」三档正交，组成 3×3 矩阵；另立「事后知情」为第二类用户在环形态 | [[Confirmation UI 安全机制#2026-08-09晚 增补：Chrome 的「确认触发器由谁判定」——三档触发器分类法]] | [[确认机制]] | 同条目 1 + Chrome Enterprise "Future Mode Part 2"（**日期待补**） |
| 6/10 | **英国 NCSC 定性提示注入为 "confused deputy"，称可能永远无法完全缓解**；Gartner 建议企业封禁 AI 浏览器 | [[XPIA 跨提示注入#2026-08-09晚 增补：Google 官方六层防御口径 + NCSC 的「混淆代理」定性]] | [[XPIA 跨提示注入]] | Computerworld 转述（**原文链接与日期待补**） |

> 说明：本笔记为**索引**，不内联分析。完整技术细节、字段清单、待补项均在上方原子笔记链接中。

## 已复核·无净新增（避免重复检索）

- **Apple**：`support.apple.com/guide/security` Apple Intelligence 章节直取**失败**（返回目录页），**未能确认 App Intents 是否有来源绑定 / 签名**——待办对 Apple 一格**仍为空**。App Attest / Gatekeeper 属传统完整性机制，与意图元数据来源分级**不同层**，不计入。
- **Android**：`app_metadata.xml` 的 `description`（LLM-facing）与 `displayDescription`（用户可见）双层描述、AppSearch JoinSpec 关联静态 / 运行时元数据等细节，均已在 [[Android AppFunctions 设备侧意图 2026]]（08-03 记录）覆盖，无新 API。
- **HarmonyOS / Windows**：本增补跑未见新增可执行 API，与 21:00 版一致。
- **21:00 版三条**（Windows Agent Framework / NowSecure iOS 27 / AgentAntibody）本轮**不重复检索**，见 [[AppIntent 每日情报 2026-08-09]]。

## 排除项

- Chrome 用 Gemini 做**漏洞挖掘**（Chrome 149/150 修复 1,072 个漏洞、13 年历史 V8 沙箱逃逸）——属 **AI 辅助安全工程**，非 OS 意图框架 / 端侧路由 / 执行安全机制，低于阈值排除。
- Google Cloud Model Armor / Agent Identity Codelab —— 云侧企业服务，非 OS 级。

## 未决问题（→ 各自 B 笔记跟踪）

- 【**连续第 7 日未解**】**Apple** 是否对 `.appEntityIdentifier` 做来源绑定 / 签名 → [[Agent Data Injection 数据注入攻击]]。**下轮换路径**：Apple Platform Security PDF 全文下载 + WWDC26 Session 347 逐字，勿再走 support.apple.com 网页直取（本轮已证失败）。
- Chrome 官方 URL 逐字复核（`blog.chromium.org` 本轮 404，现依赖转载 + TechCrunch 引述）→ [[Chrome Agent Origin Sets 与用户对齐评判器 2026]]
- critic 的自指漏洞：被污染的 planner 能否伪造「看起来对齐」的动作元数据 → 与 [[带外防御与确定性门控]] 既有「Progent 策略由 LLM 撰写」合并跟踪
- NCSC / Gartner / OWASP 三组表述均为 Computerworld 二手转述，需回一手 → [[XPIA 跨提示注入]]
- Chrome Enterprise "Future Mode Part 2" 发布日期 → [[Chrome Agent Origin Sets 与用户对齐评判器 2026]]
- 延续：Windows Agent Framework MIT 许可页 / Runtime build 号 / Mesh GA 日期；Berkeley 官方 BFCL v4 博客原文

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[Chrome Agent Origin Sets 与用户对齐评判器 2026]] · [[Agent Data Injection 数据注入攻击]] · [[XPIA 跨提示注入]] · [[带外防御与确定性门控]] · [[Confirmation UI 安全机制]]
> **同日上午版**：[[AppIntent 每日情报 2026-08-09]]
