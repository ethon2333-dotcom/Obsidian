---
type: output
status: draft
created: 2026-08-03
method_used: "每日情报自动化（7 日滚动窗口）+ WebSearch/WebFetch 直取官方源 + 飞轮四层落库"
tags: [AppIntent, OS-Agent, 执行安全, ADI, StoredIPI, 端侧Planner, 每日情报, 跨平台2026]
---

# AppIntent 每日情报速览（2026-08-03）

## 目标读者与目标

- **读者**：OS PM / 系统级 Agent 框架负责人 / 关注四平台（Apple / Android / HarmonyOS / Windows）意图框架与执行安全的从业者。
- **目标**：用一份速览讲清本日（及近 7 日滚动窗口）四平台在「系统级意图框架 / 端侧 Planner 路由 / 跨应用 Intent 工作流 / 执行安全」的**真实进展**，并落到知识飞轮可复用节点。

## 正文或成品链接

本期三条主线 + 一个分水岭：

1. **🔴 执行安全第三个分水岭：ADI 改写「注入」定义（本期最重）**：首尔国立大学团队（arXiv 2607.05120，CSA 简报 07-18）证明攻击者**无需注入指令**，只要伪造 Agent 视为可信的结构化元数据（元素 ID、来源、工具格式），Agent 便自推错误结论。同环境对照：经典指令注入 0–0.7%，**ADI 最高 100%**；六款商用 Agent 全部中招；唯一归零的 CaMeL Strict 代价是可用性 **81.2–84.8% → 36.5%**。→ 详见 [[AppIntent 每日情报 2026-08-03]] 与 [[Agent Data Injection 数据注入攻击]]。
2. **DualView + 带外防御：隔离原语升级**：姊妹论文 DualView（arXiv 2607.03821）证明传统隔离对 **Stored IPI 仍 53.3%** 失守，提出 **AgentView/HumanView 双视图**原语；带外防御（arXiv 2606.26479）主张「门不能是模型」但代价 ~15× 调用。→ 详见 [[Dual View 智能体数据视图隔离]] 与 [[Agent Workspace 隔离执行]]。
3. **Android AppFunctions 1.0.0-alpha10：Schema 编译产出 + Registry 硬细节**：`@AppFunctionServiceEntryPoint` 取代运行时配置；补齐此前缺失的权限 / manifest / 运行时动态门控 API 级细节；Google 明示「理解可能在云端」。→ 详见 [[Android AppFunctions 设备侧意图 2026]] 与 [[Confirmation UI 安全机制]]。
4. **窗口内真增量：DroiClaw 诸葛中国市场正式发布（08-03）**：新华社发文，架构口径首次明确为「本地小模型 + 云端大模型」端云协同、无 App 交互、安全/可控/可观测——并入 [[Agentic OS 意图调度内核]] 六方对照。
5. **端侧 Agent 循环齐备样本：LFM2.5-8B-A1B + LocalCowork**（Liquid AI）：单笔记本 13 MCP server / 67 工具，亚秒级 dispatch + 完整审计，数据不出机（厂商 demo，待第三方复现）。→ 详见 [[Function Calling 端侧工具调用]]。

**被排除项（展示过滤纪律）**：荣耀 Robot Phone 仍处预约未发售；Microsoft Project Polaris / M365 Copilot UI 统一属编码模型替换与应用层 SaaS，低于 OS 级阈值；HalluSquatting 注入已被 [[文档型 XPIA 自传播蠕虫]] 覆盖。

## 使用的方法

- **7 日滚动窗口**（2026-07-27→08-03，08-02 起确立），保留「首次入库存量判定」做去重；严格窗口内 OS 级硬命中仅 1 条，四条高价值库内空白按真实一手日期补漏、不冒充当日新闻。
- **官方源优先**：Horizon MCP 全部 disconnected，改用 WebSearch/WebFetch 直取 developer.android.com / arxiv.org / CSA / Liquid AI / 新华社口径转载。
- **诚实标注**：所有评测数字标「未复现 / 厂商自述」；厂商三性声明标「待补」；二手报道机构口径冲突以 arXiv/CSA 为准。

## 发布反馈

- 自动化运行，暂无人工反馈。待用户回看后回流到 A。

## 复盘

- **本日质量**：1 条真增量 + 4 条库内空白补漏 + 2 个净新增 B 节点 + 6 处既有 B 追加 + 1 条 C 层 SOP（读入路径），信息密度为高值日。ADI/DualView 虽发表于 07-06，但本库首次入库，属关键补白。
- **最高价值**：ADI 让本库既有的 XPIA 认知框架需要打补丁——防御前提（攻击=伪装成数据的指令）不完整。这直接转化为一条可写进 PRD 的判据：四平台意图元数据是否做来源校验（目前均待补）。
- **待改进**：四平台（Apple/HarmonyOS/Windows）的 Registry 动态可见性 API 仍未补满，六方 Checklist 仅 Android 一列填实；ADI 类别级缓解官方进展未跟踪。
- **方法论沉淀**：延续「一条笔记一个概念」纪律，B 层以「既有追加」为主、仅 2 个确属新概念者新建；C 层读入路径 SOP 与 08-01 写回路径 SOP 构成双向闭环，是本期最可复用的产物。
