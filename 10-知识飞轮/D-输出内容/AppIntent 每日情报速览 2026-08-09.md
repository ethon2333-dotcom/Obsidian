---
type: output
status: draft
created: 2026-08-09
method_used: "系统级 Intent 路由评估 SOP + WebSearch/WebFetch 直取官方源（Horizon MCP 连续 9 日 disconnected）"
tags: [AppIntent, 速览, 2026-08-09]
window: "7 日滚动窗口 2026-08-03 → 2026-08-09"
---

# AppIntent 每日情报速览 2026-08-09（自动化 21:00 版）

## 目标读者与目标

- **读者**：OS 产品经理（尤其 Ethon 自身）、做端侧 Agent / 系统级意图框架的工程师。
- **目标**：30 秒掌握本期四大 OS 在系统级意图框架 / 端侧路由 / 执行安全上的窗口增量，并知道哪些已落库、哪些待补。

## 正文或成品链接

**本期 30 秒速览**

| 维度 | 本期结论 | 重要性 | 落库位置 |
| --- | --- | --- | --- |
| 系统级执行总线 | **Windows Agent Framework / Microsoft Agent Framework 端侧 Agent 执行框架**：Build 2026-06-02 发布 OS 级栈（Windows Agent Runtime 系统服务宿主 / Agent Store 85:15 / Azure Agent Mesh 联邦控制面 Q4 GA / Copilot Workspace GA / Project Polaris 自研编码模型），加 2026-04-02 合并 SK+AutoGen 的 MAF SDK 1.0——本库此前缺这一完整框架节点 | 7–8/10 | [[Windows Agent Framework 端侧 Agent 执行框架 2026]] |
| 执行安全 XPIA | **NowSecure iOS 27 App Intents 攻击面**（08-05）：AppSec 厂商把「App Intents → agentic Siri → iOS 27」威胁模型落到可测清单（盘 App Intents / 测试完整 workflow / 监控数据流向），对应 Apple Session 347 间接 PI + 锁屏触发 | 7/10 | [[Apple AppIntents Schema Protocol 2026#2026-08-09 增补]] · [[XPIA 跨提示注入]] |
| 执行安全 XPIA | **AgentAntibody**（arXiv 2608.04053）：XPIA「学习型防御」分支——持久抗体库学用户安全边界、跨遭遇进化；AgentDojo ASR 3.8% / LBB 2.5%，但靠「中止任务」的变体会把 SU-HM 从 72→24，量化了安全-实用权衡 | 6–7/10 | [[AgentAntibody 自适应免疫防御 2026]] |
| 四平台官方渠道 | Apple / Android / HarmonyOS / Windows 经逐条复核**无新增可执行 API**（Windows 仅补全框架节点，非新 API） | — | [[AppIntent 每日情报 2026-08-09]]（索引） |

**两条最可执行的判断**

1. **Windows 的 agent 执行框架比「应用声明能力」路线更重一层**：Apple/Android/HarmonyOS 让应用声明能力、系统负责发现与路由；Windows 额外提供「OS 内建 agent 宿主（系统服务+沙箱）+ 联邦执行（Mesh）+ 分发市场（Store）」，agent 生命周期与权限由 OS 直接托管。做跨平台对标时，把 Windows 简单当成「另一套 intent 注册表」会低估它——它更接近「agent 专用 OS 子系统」。
2. **XPIA 防御正在从「静态三件套」裂出「学习型」第四支**：本库此前把 XPIA 缓解归为隔离+确认+数据视图隔离（静态），AgentAntibody 证明「用户边界可被学会、可跨遭遇迁移」。对长期运行的 OS Agent（主动触发意图），静态确认点难布，学习型防御是更现实的补充——但它是算法层、四平台均未内建，仍要自己集成。

**详细原始资料（索引）**：[[AppIntent 每日情报 2026-08-09]]

## 使用的方法

- 7 日滚动窗口检索 + 先读既有 B/C 笔记做去重（双链不新建重复节点）。
- 新事实 vs 口径变化分类；库内空白补漏标真实日期（2026-06-02 / 2026-08-04 / 2026-08-05），不冒充当日新闻。
- 诚实标注：NowSecure 为厂商视角、AgentAntibody 为预印本自报数字、Windows 部分生态组件（MXC/Entra Agent Identity）为第三方解读，均标「待官方确认」。

## 发布反馈

（自动化产出，暂无人工反馈）

## 复盘

### 有效的部分

- 延续「同日不重跑全窗口、只补净新增 + 显式列无净新增清单」的运行模式，避免重复检索。
- 在落库前用 WebSearch/WebFetch 重新核验了 Windows Agent Framework / NowSecure / AgentAntibody 三个关键事实（本 turn 上下文未带前次 fetch 原文），确保永久 B 笔记的事实底座扎实；并厘清了「Microsoft Agent Framework（SDK）」与「Windows Agent Framework（第三方对 OS 栈的俗称）」的命名混淆。

### 需要改进的部分

- 四平台 ADI 来源分级连续第 6 日未解（最高优先），下轮必须执行既定「查各平台安全白皮书 PDF」路径，不能再延。
- Windows Agent Framework 的官方 MIT 许可页、Agent Runtime 具体 Insider build 号、Agent Mesh GA 具体日期仍未闭合。

### 回流到 A 的新问题或素材

- NowSecure 的技术映射（间接 PI 经工具输出/日历/锁屏触发）需独立核验，不能只信厂商博客。
- AgentAntibody 预印本数字需在独立榜复现后才可写进横向对比。

> [!note] 关联枢纽
> **MOC**：[[意图框架·跨体系索引 MOC]] ｜ **主题枢纽**：[[意图模式规范]] · [[语义路由]] · [[端侧工具调用]] · [[确认机制]] · [[元服务]] · [[隔离执行]] · [[A2A 端侧智能体协议]] · [[XPIA 跨提示注入]]
> **本期原子笔记**：[[Windows Agent Framework 端侧 Agent 执行框架 2026]] · [[AgentAntibody 自适应免疫防御 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[XPIA 跨提示注入]]
