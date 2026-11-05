---
date: 2026-10-06
tags:
  - AppIntent
  - 每日情报
  - 复核型运行
  - 无净新增
source:
  - https://www.ithome.com/1/009/905.htm
  - https://dev.igeeksblog.com/ios-27-2-developer-beta-3
  - https://thelivetoday.com/?p=1130
  - https://www.163.com/dy/article/L8II0AKK0511BLFD.html
  - https://www.163.com/dy/article/L8ILIB400519QIKK.html
  - https://www.toutiao.com/a7693076797948265004
  - https://agentlocker.ai/news/microsoft-copilot-ai-agents-gain-ground-in-defense-work-as-ai-spending-grows
  - https://cowork.ink/blog/background-agents
  - https://www.toutiao.com/article/7693361592880202282/
  - https://anothergptwrapper.com/tools/llm-pricing/evals/bfcl-v4
  - https://anotherwrapper.com/tools/llm-pricing/evals/bfcl
  - https://hellomarvisaitoday.com/articles/f5879a1c-7b3f-445f-a5a1-d827a31571e6
  - https://developer.aliyun.com/article/1768150
  - https://juejin.cn/post/7692814441561964544
importance_score: "—（复核型运行·无净新增）"
intent_category: "四平台官方框架层 + 跨平台 BFCL + XPIA 复核（2026-10-06 07:33 → 21:00，约 13.5h）"
---

# AppIntent 每日情报 2026-10-06-晚（窗口 2026-10-06 07:33 → 21:00，约 13.5h）

> [!abstract] 30 秒速览
> **核心结论：四大 OS 官方框架层 + 跨平台 BFCL v4 + XPIA 研究线，本 13.5h 窗口（2026-10-06 07:33 → 21:00）均无净新增。** 与当日晨间跑（窗口 10-05→10-06 07:33）结论完全连续一致，再次印证「OS 框架不日更」规律。本期为**同一日内的日间复核运行**，把「已复核·无净新增」显式落档，避免下次重复检索。
> - Apple：iOS/iPadOS 27.2 **Beta 3 于今日（10-06）发布**（内部版本 24B5099f），但早期覆盖已确认**无新功能、无新 App Intents Schema API**；Siri Gemini 五语言扩展来自更早的 27.2 beta，属复述；iOS 27.1 仍锚定 iPhone Duo 10-23 出厂、未发 beta。
> - Android：Gemini「代拨电话」(Gemini Calling) 由商务场景扩展至个人联系人（Android Authority APK 拆解，10-05/06 报道）——属 **Gemini 应用层消费功能，非 AppFunctions / EXECUTE_APP_FUNCTIONS / Registry 框架**；AppFunctions 仍守 `alpha12` 无 `alpha13`。
> - HarmonyOS：余承东 10-06 宣布「鸿蒙出海」计划 + 生态数字（90M+ 设备、45 万+ 应用）——属**商业/生态叙事，非 OS API 变更**；ArkAF 2.0 / 元服务为既有内容。
> - Windows：Copilot Autopilot（原 Scout）/ 防御行业用例 / Computer Use 公测（GitHub，10-01）均为 **M365 / 云端 / GitHub 治理层**，非 Windows OS 执行总线新 Registry API；26H2 已 GA、ODR/Agent Workspace 无变化。
> - 跨平台 BFCL v4：Clef 决策模型遭中文媒体二次转述（10-06，已 10-02 收录）；聚合镜像榜 anothergptwrapper/anotherwrapper 仍 Qwen3.7 Max 75% / Llama 3.1 405B 88.5% 居首，端侧 Planner 无新入榜。
> - XPIA：窗口内命中的「MCP protocol pivoting」(CVE-2026-97228 Rapid7 2.7 等)、camel-ai/bisheng/DB-GPT 代码执行 CVE、恶意 README 注入、DW 沙箱逃逸报道——经核查均**非四平台 OS 框架执行总线**（MCP/LLM 应用框架/通用 agent 安全），按筛选规则丢弃（同 10-06 晨间丢弃 GitLab AI Gateway CVE 口径）。

## ① Schema 定义与语义路由机制

- 逐一核验四大平台官方源与权威媒体：Apple iOS 27.2 Beta 3、Android AppFunctions `alpha13`、HarmonyOS 新 API、Windows OS 执行总线新 Registry API 均**无本窗口新增**。语义路由 / 意图分发机制停留在既有基线（iOS 27 Schema Protocol / AppFunctions `alpha12` `scope` / ArkAF 2.0 / ODR + Agent Launchers）。
- iOS 27.2 Beta 3（10-06，build 24B5099f）据 iGeeksBlog / IT之家覆盖「未浮现任何 beta 3 独有变更」；早于本窗口的 27.2 已含 Health 改版、欧盟 ATT 新提示、Siri Gemini 五语言（法/日/韩/葡/西）等，本次 beta 3 仅为新测试构建而非功能投放。**Siri 的 Gemini 多语言扩展不引入新的 `@AppIntent(schema:)` Schema API**——其「更深第三方 App 集成」是对既有 App Intents 框架的复用，非 schema 层变更。
- Android Gemini Calling 拆解出的「精细权限设置」针对 Gemini 自身的通话能力，不构成 AppFunctions 的 `EXECUTE_APP_FUNCTIONS` 闸门或 Registry 维度变更；属 Gemini app 的运行时权限 UI，与端侧意图框架无关。

## ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

- 四平台执行安全机制（Apple FDA 收紧 / Android `EXECUTE_APP_FUNCTIONS` 一次性授权 / HarmonyOS 端云协同安全认证 / Windows 低权账号 + ODR consent + Execution Containers）在本窗口**无新机制发布**。
- GitHub Computer Use 公测（10-01）提出的「应用 / 动作 / 数据三维门禁」与 `始终允许` 风险、任务级最小权限、策略器置于模型之外——**概念上**与库内 [[确认机制]] / [[隔离执行]] 高度同构，但其落地是 **GitHub Copilot CLI 的应用级能力，非 Windows OS 执行总线 API**，按范围不计入 OS 框架增量；其论证（「应用身份 ≠ 业务意图」「安全检查应在决策已结构化、执行尚未发生的窗口进行」）可作为既有 B 笔记的概念佐证，但无新 OS 机制，故**不新建/不增补节点**。
- XPIA 窗口内仅「MCP protocol pivoting」「camel-ai/bisheng/DB-GPT 代码执行 CVE」「恶意 README 注入」「DW 沙箱逃逸」等高显著度条目，但其攻击面落在 **MCP 工具链 / LLM 应用开发框架 / 前沿实验室测试沙箱**，**与四平台 OS 意图执行总线无直接关系**。按本库一贯口径（MCP 工具链 CVE、应用层 RCE 均不计入 OS 框架）丢弃；其价值（「agent 间零信任」「注入使沙箱失去意义」「最小权限须含时间维度」）已在历史 B 笔记（[[XPIA 跨提示注入]] / [[隔离执行]] / [[确认机制]]）涵盖，无需新建节点。

## 已复核·无净新增（避免重复检索）

- **Apple**：iOS 27.2 Beta 3（10-06，24B5099f）无新功能、无新 App Intents Schema；Siri Gemini 五语言为更早 beta 内容；iOS 27.1 未发 beta（锚定 10-23 iPhone Duo 出厂）；27.0.1（09-29）仅修 Bug。App Intents Schema Protocol（Sauce Labs GA 转述）为既有复述。
- **Android**：AppFunctions 守 `1.0.0-alpha12`（09-23）无 `alpha13`；A2UI 守 `alpha01`；Gemini Calling 为 Gemini app 消费功能（非 AppFunctions 框架）；Gemini Nano v3 端侧 Function Calling 为 Android 18 既有叙事。
- **HarmonyOS**：无新 OS API；余承东「鸿蒙出海」+ 生态数字（90M+ 设备 / 45 万+ 应用 / 1100 万注册开发者）为商业/生态叙事；小艺 2.0 / ArkAF 2.0 / HDC2026 为既有内容复述。
- **Windows**：Copilot Autopilot（原 Scout，09-25 私有预览）/ 防御行业用例 / SharePoint Copilot GA（09-30）/ GitHub Computer Use 公测（10-01）均为 M365/云端/GitHub 治理层，非 Windows OS 执行总线新 Registry API；26H2 GA 09-29 已记录。
- **跨平台 BFCL v4**：端侧 Planner 无新入榜；anothergptwrapper（10-06）Qwen3.7 Max 75% 居首、anotherwrapper（10-06）Llama 3.1 405B 88.5% 居首，均为聚合镜像、口径与历史快照一致；Clef 决策模型（10-06 中文媒体）为 10-02 已收录项复述；腾讯新闻转述的「运筹学 RL 训练法 BFCL v4 +2.84 分」为通用研究方法、未命名具体端侧 tool-router 模型，低于范围阈值丢弃。
- **XPIA**：MCP protocol pivoting（CVE-2026-97228 Rapid7 2.7、Google IP allow-list 修复）/ camel-ai CVE-2026-51857 / bisheng CVE-2026-51861 / DB-GPT CVE-2026-51869 / 恶意 README 注入 / DW 沙箱逃逸报道——均非四平台 OS 框架，按口径丢弃。

## 诚实标注 / 待补

- iOS 27.1 beta 实际发布日与是否带新 `@AppIntent(schema:)` Schema（iPhone Duo 折叠屏适配之外）待 Apple 逐字；10-19~23 为第三方汇总。
- AppFunctions `alpha13` 是否存在、是否引入调用方身份注入新机制（`alpha12` 移除 `AppFunctionContext` 后）待 developer.android.com/ai/appfunctions 官方文档。
- Gemini Calling 精细化权限是否为独立 Android 系统级 API 还是纯 Gemini app 内权限 UI，待 Google 官方文档；不归入 OS 意图框架。
- GitHub Computer Use 三维门禁的「应用/动作/数据 + 有效期」模型与 [[确认机制]] 同构，但其为 GitHub 应用级能力、非 Windows OS；若未来 Windows Agent Workspace 借鉴此模型再纳入。
- CVE-2026-97228 / camel-ai / bisheng / DB-GPT 等已丢弃（非四平台 OS 框架）；若未来出现四平台 OS 层 agent 隔离逃逸再纳入。
- 沿用手柄：Per-Intent Privacy Manifest 官方逐字 / Watch OS 26 / AppFunctions GA 日期 / A2UI alpha02 / 高通 NPU exact specs / **Berkeley 官方 BFCL v4 博客**（连续多轮待办，端侧 Planner 历史分数仍未被官方榜逐条复核）/ NowSecure / AgentAntibody / Chrome Origin Sets。

> [!note] 概念节点双链
> [[意图模式规范]] [[语义路由]] [[端侧工具调用]] [[确认机制]] [[元服务]] [[隔离执行]] [[A2A 端侧智能体协议]] [[XPIA 跨提示注入]]
