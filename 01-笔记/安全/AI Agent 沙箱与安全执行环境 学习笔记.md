---
title: AI Agent 沙箱与安全执行环境 学习笔记
tags: #安全 #Agent沙箱 #执行隔离 #代码安全 #云原生
created: 2026-09-17
source: "WebSearch/WebFetch 联网核实"
---

> **本文与 [[工具调用安全 学习笔记]]、[[端侧模型安全与越狱 学习笔记]]、[[AI 评测红队与对齐 学习笔记]] 的关系**：三篇分别聚焦「工具调用的鉴权/allowlist（不涉执行隔离）」「模型层被提示注入/越狱攻击」「模型红队测试与对齐」。本文只讲第 4 层——**Agent 运行时隔离/沙箱技术**：Agent 生成的代码与命令究竟在哪、被怎样隔离地跑。即「执行边界」问题，而非「能否调用工具」「模型是否被攻破」「模型是否对齐」。

**一句话心智模型**：Agent 沙箱 = 把「不可信的、由 LLM 现写的代码/命令」关进一个**独立内核 + 有限资源 + 受限网络 + 可审计**的笼子里跑，让任意代码执行（RCE）的爆炸半径止步于笼内，不波及宿主机与宿主凭据。

---

## 一、定义：为什么 Agent 必须有隔离执行环境

传统 LLM 应用只是「生成文字」，被 prompt injection 攻破的影响有限。Agent 的根本差异是**有了行动能力**——能写代码、跑 shell、读文件、调 API。**一旦 agent 会执行自己生成的代码，它运行的就不是可信软件，而是「输入即代码」的不可信负载**（agentic coding / computer-use / 代码解释器皆如此）。

不隔离的后果（媒体口径汇总，待核实）：
- **任意代码执行**：`os.system()` / `subprocess` 被诱导执行系统命令，甚至 `rm -rf /`。
- **资源耗尽**：死循环打满 CPU、无限递归撑爆内存。
- **文件系统越权**：无路径限制则读遍整盘（含密钥、配置、用户数据）。
- **网络数据外泄**：代码里藏一个 HTTP 请求把敏感数据发到攻击者服务器。

沙箱的三大核心价值（隔离 / 限制 / 审计）即对应上述四类风险的缓解。OWASP 在 2025-12-09 发布 **Agentic Top 10（ASI01–ASI10）**，其中 ASI05「Unexpected Code Execution」直接把「sandboxed execution」列为关键缓解项（见文末来源）。

---

## 二、分类：三种隔离基元（核心维度）

隔离粒度从弱到强，是选型的第一轴：

| 隔离基元 | 隔离机制 | 内核隔离 | 启动速度 | 安全边界 | 适用场景 |
|---|---|---|---|---|---|
| 进程 / 普通容器（Docker, Linux namespaces） | namespace + cgroups | ❌ 共享宿主内核 | ~100ms（最快） | 弱：内核 CVE 可逃逸 | 可信代码、开发测试 |
| gVisor（用户态内核 Sentry） | 拦截并重实现 syscall | ⚠️ 过滤 syscall | ~300ms | 中强：缩小攻击面 | 不可信但行为规矩的代码 |
| MicroVM（Firecracker / Cloud Hypervisor / Kata） | KVM 硬件虚拟化 | ✅ 独立内核 | 100–800ms | 强（黄金标准） | 可能有敌意的不可信代码 |

> 心智锚点（来自 Agent runtime taxonomy L4）：可信人类写的代码→容器即可；LLM 生成的「跑一次」代码→gVisor 甜点区；LLM 生成且持有 secret 或跑浏览器会话→MicroVM（启动成本被整段会话摊薄）。

**关键技术点（点到为止）**：
- **隔离粒度**：进程 < 容器 < VM；同一宿主上多租户必须 VM 级防跨会话逃逸。
- **资源限制**：CPU / 内存 / 磁盘配额 + 执行超时（kill 长时间运行的任务）。
- **网络出口控制**：allow-all（默认）/ deny-all（含 DNS）/ 域名+IP 白名单；敏感负载须默认拒绝 + DNS 过滤。
- **文件系统隔离**：scoped filesystem + readOnlyRootFilesystem，禁止 `allowPrivilegeEscalation`。
- **seccomp / capabilities**：收紧容器/MicroVM 自身能向宿主发起的 syscall（Firecracker VMM 自身即用 seccomp 最小化攻击面）。
- **快照恢复（Snapshot/Restore）**：先预热池 + Pod 快照，长任务被抢占后可秒级恢复，已成为主流平台「Table Stakes」。

---

## 三、主流方案对比（2025-2026 产品景观）

> 下表的隔离类型、启动速度、价格口径多来自厂商/媒体评测，**具体数字与定价以官方为准，待核实**。

| 方案 | 隔离基元 | 定位 | 备注 |
|---|---|---|---|
| **E2B** | Firecracker microVM | 专用 agent 代码沙箱（开源核心可自托管） | 冷启动 sub-200ms；网络 allowlist/deny-all；被称 2025-2026 最广泛应用（厂商口径「88% 财富 100」待核实） |
| **Modal** | gVisor 容器 | 含 GPU 的无服务器沙箱 | 50,000+ 并发；A100/H100 等 GPU；环境可运行时动态定义；SOC2 Type II |
| **Daytona** | Kata/Firecracker（可配） | 持久化 devbox | 2025 从 dev-env 转向 agent-native；sub-90ms 冷启动靠预热 VM 池；会话级网络策略 |
| **AWS Bedrock AgentCore** | Serverless 容器 / microVM | 云厂托管运行时 | 8h 会话；CloudTrail+VPC；A2A 协议；策略在 LLM 循环外强制 |
| **Google Agent Sandbox / Agent Substrate** | gVisor + Pod 快照 | GCP/Gemini 执行层 | 开源；默认 gVisor + 默认拒绝网络；可插拔 Kata；300 沙箱/秒、90% 在 200ms 内（厂商口径，待核实） |
| **Cloudflare Sandboxes** | 容器 + V8 isolates（Dynamic Workers） | 边缘沙箱 | 2026-04 GA；V8 isolates ~ms 级；egress proxy 注入凭据；无空闲计费 |
| **Morph Cloud** | MicroVM 分支（Infinibranch） | VM 快照克隆并行探索 | <250ms 分支/恢复；适合 tree-of-thought 并行；联系销售定价（待核实） |
| **Runloop** | 裸金属 hypervisor | 企业可靠 | 2x vCPU；Blueprints+Snapshots 环境标准化；2025-07 种子轮（待核实） |
| **NanoClaw** | Docker 隔离（开源 harness） | 自托管小团队 | Agent-in-sandbox 长会话；开源 |
| **OpenHands Runtime** | 可插拔（Docker/Daytona/K8s） | 框架集成运行时 | 完整事件日志；开源 |
| **Code Interpreter / 代码解释器** | 厂商托管隔离 | 用户代码执行 | OpenAI Code Interpreter、Judge0、sandboxed.sh 等；多租户须隔离，禁止共享进程 |

> 架构选型轴：**Sandbox-as-tool**（只把工具调用丢进沙箱，低延迟）vs **Agent-in-sandbox**（harness 与工作区都进笼，适合长会话如 NanoClaw/Bytebot 式）。

---

## 四、代表产品形态（按执行模型分七类）

媒体将 2024-2026 沙箱从「通用运行时」分化为七类（Agent Harness 综述，2026-05，待核实归类口径）：
1. **通用托管沙箱**：Daytona / E2B / Modal / Northflank / OpenSandbox / Docker Sandboxes
2. **计算机使用（computer-use）基础设施**：Anthropic Computer Use、CUA、OSWorld（基于 VM 的 GUI 环境）
3. **代码专用沙箱**：Judge0 / OpenAI Code Interpreter / sandboxed.sh / langchain-sandbox
4. **框架集成运行时**：OpenHands Runtime、agent-infra、smolagents executor
5. **浏览器评估环境**：WebArena / VisualWebArena / BrowserGym / WorkArena（兼沙箱与评测）
6. **OS 级权限沙箱**：Anthropic sandbox-runtime、Claude Code 沙箱、IsolateGPT
7. **沙箱抽象层**：SWE-ReX、smolagents executor 接口、Kubernetes Agent Sandbox

**远程浏览器沙箱（remote browser）**：computer-use 把 GUI（鼠标/键盘/屏幕）当作 action surface。代表：OpenAI Operator 的**云浏览器**（运行在 OpenAI 服务器上，为 agent 提供沙盒，降低触碰用户本地文件/账户的风险）、Microsoft **MagenticLite**（Fara1.5 浏览器 agent 的沙盒浏览器界面，构成 agent 与用户设备的安全边界）、Google Project Mariner / Gemini Computer Use、字节 **UI-TARS**。注意：云浏览器降低本地风险，但**不消除 prompt injection 风险**（OWASP/媒体共识）。

---

## 五、2025-2026 进展

- **Agentic coding 沙箱爆发**：从 2024「Docker 凑合」到 2026「必须真隔离」——间接 prompt injection、供应链投毒（攻击者发布恶意 Python 包）、监管关注推动。媒体称沙箱化 agent 相比无限制宿主机访问「安全事件降低约 90%」（待核实，来源口径不一）。
- **Computer-use 浏览器沙箱**：OpenAI Operator / 云浏览器、Microsoft MagenticLite、Google Mariner 把浏览器/桌面自动化关进沙盒；GUI 成为一线公认「下一代通用 action surface」。
- **云厂托管沙箱**：AWS AgentCore、Google Agent Substrate/Sandbox、Cloudflare Sandboxes（2026-04 GA）、Vercel Sandbox 将沙箱变成云厂标配 SKU，从独立 SaaS 走向「独立层 + 云捆绑层」并存。
- **快照/分支成标配**：预热池、Pod 快照、VM 分支（Morph Infinibranch <250ms）让长程 agent 可恢复、可并行探索。
- **微软 Agent Governance Toolkit（2026-04，开源）**：首个覆盖 OWASP 10 项 agentic AI 风险的确定性策略执行工具（sub-ms 级，待核实）。
- **OWASP 三标准成形**：2025-2026 陆续发布 LLM Top 10 / Agentic Top 10 / MCP Top 10，形成「模型层→Agent 层→协议层」三重基准；缓解建议反复指向 sandbox execution + 网关 + per-agent 身份 + kill switch。

---

## 六、威胁模型（为什么需要沙箱）

| 威胁 | 含义 | 沙箱如何缓解 |
|---|---|---|
| **任意代码执行（RCE）** | agent 生成的代码/命令越出预期范围（ASI05） | 独立内核 + seccomp + 资源限制，越界止于笼内 |
| **数据外泄** | 代码藏 HTTP 请求把敏感数据发往外网 | 默认拒绝网络出口 + DNS 过滤 + egress proxy 注入凭据 |
| **权限提升** | 容器内逃逸拿宿主 root / 跨租户（ASI03） | MicroVM 硬件隔离；per-agent 短时效 scoped token |
| **供应链攻击** | 恶意 MCP server / 投毒包 / Rug Pull（ASI04） | 沙箱执行 + 签名校验 + allowlist + 行为审计 |

> 「Lethal Trifecta」快筛：当 agent **同时**持有私有数据、读取不可信内容、能触网时，上述风险直接可被利用——沙箱 + 默认拒绝网络是首要防线。

---

## 七、留白：待 Ethon 深挖的盲区（BREADTH > DEPTH）

- [ ] 待解问题：Firecracker vs gVisor vs Kata 在「真实 agent 负载」下的性能/逃逸基准测试数字（而非厂商口径）到底差多少？
- [ ] 待解问题：MicroVM 快照恢复的「恢复延迟」对长程 coding agent 的实际影响，有无公开 benchmark？
- [ ] 待解问题：GPU 在 MicroVM（Firecracker）内如何暴露？Modal 用 gVisor 而非 Firecracker 是否牺牲了隔离换来 GPU 易用性？
- [ ] 待解问题：V8 isolates（Cloudflare）与容器/MicroVM 的隔离强度差异，能否跑任意原生代码？
- [ ] 待解问题：Claude Code / Codex 自带的 sandbox 用的是哪层基元？是否与「托管 microVM」一致？
- [ ] 待解问题：MCP server 自身若运行在沙箱内，能否阻断 Tool Poisoning / Rug Pull（协议层弱点沙箱能否补偿）？

---

## 附：来源清单

- OWASP Agentic Top 10（ASI01–ASI10），2025-12-09 — isitpatched.com / cloudandsre.com（ASI05 代码执行、缓解建议 sandbox execution）
- Agent Sandbox 对比（E2B/Modal/Daytona/AWS AgentCore/Google Agent Sandbox）：alignify.co/blog/agent-sandbox
- Remote Tool Execution & Cloud Sandbox Platforms（2026-06，含 Cloudflare/Morph/Runloop/OpenHands 数据）：zylos.ai/research/2026-06-13
- Agentic Sandboxing 2026（E2B/Daytona/Modal/Firecracker 模式）：callsphere.ai/blog
- Sandboxed Code Execution 2026（E2B vs Modal vs Daytona，含隔离基元对比）：agentmarketcap.ai/blog/2026/04/10
- MicroVM vs gVisor vs container（L4 runtime taxonomy）：autogentlabs.com/lab/microvm-sandboxes-for-tool-use
- gVisor / Kata / Firecracker 中文深度对比：juejin.cn/post/7553482516629143593
- Agent Sandbox 搭建指南（Docker/gVisor/Firecracker + GKE Agent Sandbox）：eastondev.com/blog/zh/posts/ai/20260323-agent-sandbox-guide
- Agent Harness 综述（沙箱七分类）：finance.sina.com.cn/wm/2026-05-29
- Google Agent Substrate / Agent Sandbox：news.qq.com/rain/a/20260730A07NN000
- Microsoft Fara1.5 + MagenticLite 沙盒浏览器：tech.ifeng.com/c/8tMBO1bWgRY
- OpenAI 关闭 Atlas 浏览器、Codex microVM 隔离被移除的安全迁移讨论：news.qq.com/rain/a/20260712A04BQA00
- OWASP 三标准 + MCP 七大攻击面（Cisco 2026 调查 83%/29% 待核实）：meta-intelligence.tech/insight-ai-agent-security
- 一线 agent post-training / computer-use / 执行环境信号（OpenAI/Anthropic/Google/Seed）：WebSearch 聚合（2026-09-17）

## ⚠️ 待核实清单

- 「沙箱化 agent 相比无限制宿主机访问安全事件降低约 90%」——媒体口径，未见原始研究报告，待核实。
- E2B「88% 财富 100 采用」——厂商营销口径，待核实。
- Google Agent Sandbox「300 沙箱/秒、90% 在 200ms 内」「5 个月规模增长 ~16 倍」——厂商口径，待核实。
- Cloudflare Sandboxes「2026-04 GA」「V8 isolates ~ms」——发布时间/数字待核实。
- Microsoft Agent Governance Toolkit「2026-04 开源、覆盖 OWASP 10、sub-ms」——发布时间与性能待核实。
- 各类价格（E2B ~$0.05/vCPU-hour、Modal/Daytona 计费）——以官方定价页为准，本文未列具体金额。
- Morph Cloud / Runloop 种子轮与定价——联系销售/媒体口径，待核实。
- Cisco 2026「83% 部署、29% 自认就绪」——调查口径，待核实。
- Firecracker 启动 100–800ms、gVisor ~300ms、容器 ~100ms 等性能区间——不同评测差异大，仅作量级参考。

#标签/安全 #Agent沙箱 #执行隔离 #代码安全
