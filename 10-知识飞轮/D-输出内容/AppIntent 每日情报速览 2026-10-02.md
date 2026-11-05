---
date: 2026-10-02
tags: [情报速览, AppIntents, 系统级意图框架, 执行安全, 控制面治理]
method_used: 直查官方源（WebSearch/WebFetch，Horizon MCP 未连接）
intent_category: 执行安全 / 控制面治理 / OS 部署里程碑
---

# AppIntent 每日情报速览 2026-10-02

## 目标读者与目标
OS PM / 端侧 Agent 框架研究者；快速掌握 2026-09-30 → 10-02 窗口内四大 OS 意图框架 + 执行安全新进展。

## 正文（一句话结论 + 速览表）

**窗口结论**：四大 OS 官方框架层 API 仍零净新增（延续「OS 框架不日更」规律）；唯一 OS 级真增量 = **Windows agent 连接器策略治理面首次公开**（`ConfigureAgentConnectors` / `AgentConnectorAccessPolicy` / `AgentConsentDuration`，仅企业版以上可完整管控），属执行安全控制面具体化（★6/10）。其余为状态推进与去伪。

| 平台/主题 | 本窗口状态 | 重要性 | 落点 |
|---|---|---|---|
| Apple AppIntents | iOS 27.1 beta 未出，无新 Schema；公开版预期 10-19~23 | ★3 | 已覆盖，无新增 |
| Android AppFunctions / A2UI | 守 alpha12 / alpha01，无 alpha13/alpha02 | ★3 | 已覆盖，无新增 |
| HarmonyOS Intents Kit / ArkAF | 无新 API（HC2026 已覆盖） | ★3 | 已覆盖，无新增 |
| Windows 26H2 + 连接器策略 | GA 已确认(09-29)；新增连接器策略面（企业版以上） | ★6 | [[Windows Copilot Actions 与 Agent Workspace 2026]] / [[Agent Workspace 隔离执行]] |
| XPIA | 窗口内无新 CVE/研究突破（既有 RAMPART/综述） | ★3 | 已覆盖 |
| BFCL v4 | 仍 Llama 3.1 405B 88.5%；端侧无新入榜 | ★3 | 已覆盖 |

## 使用的方法
WebSearch/WebFetch 直查官方/权威源（developer.apple.com/documentation/updates/appintents、developer.android.google.cn、cnBeta/Neowin、tech-insider、appauxin、paperswithcode/aimodao 镜像）；未调用 Horizon MCP（环境仅 `agent-mail` 在线）。

## 复盘
- **有效**：窗口无 OS 框架 API 净新增，与连续多轮结论一致；唯一真增量（Windows 连接器策略面）落为既有 B 笔记追加，0 新建 B 节点。
- **改进**：家庭/专业版「连接器不可控」这一版本割裂点为新事实，已标注待官方复核；iOS 27.1 日期预期由「10 月底~11 月初」下修为「10 月中下旬」。
- **回流到 A 的新问题**：连接器策略项官方逐字 / 家庭专业版限制核实；iOS 27.1 beta 是否带新 Schema；Per-Intent Privacy Manifest 官方逐字。

## 24h 复核补捕（2026-10-02 21:01 re-trigger）

**窗口结论**：过去 24h 四大 OS 官方框架层 API 仍零净新增；以下为窗口内/邻的新进展（均 ★5/10 状态/补强，低于 ★6 收录阈值，按惯例作状态行处理）。

| 主题 | 本 24h 状态 | 落点 |
|---|---|---|
| HarmonyOS Mate 90 / 小艺Claw | 10-01 发布，订阅化 + 体验倒退 backlash（产品/UX 非 API） | [[HarmonyOS Intents Kit 与 ArkAF 2026]] |
| 路由/决策模型（Clef/Strands） | Cloudflare Clef 开源直击 Jev，BFCL 98.5 厂商自报（edge/cloud 非 on-device） | [[Function Calling 端侧工具调用]] |
| XPIA 防御（DTAP） | 45.6%→10.0% 攻击成功率，媒体综述待一手 | [[XPIA 跨提示注入]] |
| Android 17 企业策略 | setAppFunctionsPolicy/APP_FUNCTIONS_DISABLED 可关 AppFunctions 数据（治理收敛） | [[Android AppFunctions 设备侧意图 2026]] |
| BFCL v4 | 仍 Llama 3.1 405B 88.5%，端侧无新入榜 | 已覆盖 |
