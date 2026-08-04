---
type: output
status: draft
created: 2026-08-04
method_used: "[[系统级 Intent 路由评估 SOP]] ｜ [[Agent 读入路径可信数据边界 SOP]]"
source_note: "[[AppIntent 每日情报 2026-08-04]]"
importance_score: ★★★★☆
intent_category: [评测口径, 执行安全, 数据治理]
tags: [AppIntent, 速览, BFCL, ADI, 数据溯源, OS-Agent]
---

# AppIntent 每日情报速览 2026-08-04

## 目标读者与目标

**读者**：我自己（OS/Android PM），以及未来复盘「端侧意图路由该怎么选模型、Registry 该带哪些字段」时的自己。
**目标**：把今天 7 天滚动窗口内的 3 条净新增压缩成能直接用于产品判断的结论，并明确标出哪些是**口径变化**（会让历史数据作废）而非新事实。

## 正文或成品链接

完整原始资料见 [[AppIntent 每日情报 2026-08-04]]。三条结论浓缩如下：

### ① BFCL v4 换了权重，你库里所有 Function Calling 分数都过期了（8/10）

| 维度 | v4 权重 |
|---|---|
| **Agentic** | **40%** |
| **Multi-Turn** | **30%** |
| Live（真实用户 API） | 10% |
| Non-Live（经典单轮） | 10% |
| **Hallucination** | **10%** |

- 经典单轮从「几乎全部」压到 **20%**（Live+Non-Live），端到端 agentic 与多轮合计 **70%**。
- **直接后果**：Bonsai 73.3%、qwen3-0.6b-tool-router 90.42% 这些库内旧分全是 **v3 时代的「格式合规分」**，与 v4 不可比。已在 [[Function Calling 端侧工具调用]] 与 [[Local Agent Bench 端侧智能体基准]] 打上版本标签。
- **对我的意义**：意图路由最怕的是「该说不会时硬编一个函数调用」，而这恰好是 v4 新增的 **Hallucination 10%**。选端侧 Planner 时，这 10% 比总分更值得看。
- ⚠️ 权重数字来自二手快照，**Berkeley 官方 v4 原文未核实（最高优先待补）**。

### ② ADI 的「正面答案」出现了，但不在 OS 层（8/10）

挂了 3 天的跨日待办「四平台是否对意图元数据做来源校验」，今天有实质进展但**仍未解决**——结论从「没人做」精化为**「治理层有成熟模型，OS 层全空白」**。

微软 **Agent Governance Toolkit**（开源，非 Windows 内建）给出可抄的字段级 schema：

- **六类来源**：`tool_output` / `api_response` / `agent_message` / `user_input` / `database` / `file`
- **四级密级 + 单调棘轮**：`public → internal → confidential → restricted`，**只升不降**
- **两阶段闸口**：`post_tool` 打标 + `pre_output` 复核；打标必须早于模型读到内容
- 对齐 **EU AI Act Article 10**（数据治理，与 Article 15 同日 2026-08-02 生效）

已 WebFetch 复核 Windows 官方 agentic security 文档：**OS 层没有数据来源分级**。Agent Workspace 的 scoped file access 管的是「能读哪个文件夹」（位置维度），不管「读进来的内容可不可信」（来源维度）——两个维度正交，目前只覆盖前者。

→ 新建概念节点 [[数据溯源分级与单调棘轮]]；跨日待办**继续挂起（第 4 日）**。

### ③ Project Perception 公开预览：隔离 ≠ 检查（7/10）

Defender for Endpoint 开始检查 agent loop 三段流量——**用户提示 / 工具调用 / 工具响应**——并在执行前阻断。这是首个把「工具调用/响应」当作**可检查流量**的端点侧机制（此前防御全在模型/框架层）。

架构上的转折点：Agent Workspace 解决「Agent 跑坏了炸不到系统」（**隔离**），Project Perception 解决「Agent 在被骗的路上就被拦下」（**检查**）。Windows 此前只有前者。

⚠️ 口径冲突未消：CyberGym **95.95% vs 96%**，模型名 **MAI-Cyber-1-Flash vs MAI-Cyber-Flash-1**，两处并存待官方确认。

### 已复核·无净新增

Apple / Android / HarmonyOS / Windows 四家官方渠道在本窗口内**无新增可执行 API 或框架变更**，与库内既有 B 平台卡一致，不再重复检索。

### 已排除（附理由）

钉钉 Agent OS、TOS 7、PilotDeck、Windows Patch Tuesday —— 非 OS 级意图框架/端侧路由/执行安全，或属常规安全更新，按重要性 ≥6 与主题过滤规则剔除。

## 使用的方法

- 检索：7 天滚动窗口（2026-07-29 → 08-04）+ 首次入库去重；Horizon MCP 连续第 6 日断连，全程 WebSearch/WebFetch 直击官方源。
- 判读：对每条「新数字」先分类为**新事实**还是**口径变化**——今天最大的一条（BFCL v4）属于后者，价值在于让旧数据作废而非新增知识。
- 落库：[[Agent 读入路径可信数据边界 SOP]]（本次据此升级步骤 2）。

## 发布反馈

（自用，无外部发布）

## 复盘

### 有效的部分

- **把「口径变化」单独拎出来判**是今天最有价值的动作。如果按常规「又一个 benchmark 更新」处理，就会漏掉「库内十几条分数集体失效」这个真正的后果。
- **层级校准**（治理层 ≠ OS 层）避免了一次误判。AGT 的模型足够成熟，很容易让人写成「Windows 已支持数据分级」，WebFetch 官方文档一查就发现不是。这条纪律要保持。
- 3 天待办终于从「查不到」变成「查到了但答案在别的层」，这本身就是产品判断的升级。

### 需要改进的部分

- **二手数据比例仍偏高**。BFCL v4 权重、CyberGym 分数都来自二手，且后者出现两个版本。应优先建立「官方原文优先」的检索次序，二手只做线索。
- Berkeley 官方 v4 原文这次没拿到，属于**核心结论建立在未核实数据上**——已在 A 层与两个 B 节点均标注待补，但下次应先花 1 次检索预算专攻官方源。

### 回流到 A 的新问题或素材

- [ ] **核实 Berkeley 官方 BFCL v4 权重原文**（最高优先，未解）
- [ ] **跟踪四平台是否采纳来源分级**（跨日待办，连续第 4 日）
- [ ] Project Perception 口径统一：CyberGym 95.95/96、模型名两种写法
- [ ] 荣耀 Robot Phone 8 月发布，关注是否涉及系统级意图/端侧 Agent 能力
- [ ] 新问题：如果 OS 不提供来源分级，**应用侧自己打标能否防住 ADI？** 打标器本身会不会成为新靶面（谁给打标器提供来源信息）？

> [!note] 概念双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]

#标签/AppIntent #标签/速览 #标签/BFCL #标签/ADI #标签/数据溯源
