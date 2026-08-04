---
type: raw
status: inbox
date: 2026-08-03
captured: 2026-08-03
importance_score: ★★★★★
intent_category: 系统级意图框架 / 端侧 Agent 执行总线 / 执行安全（ADI / Stored IPI / 带外防御）/ 端侧 Planner 实测
source:
  - "https://developer.android.com/ai/appfunctions/add-appfunctions （AppFunctions 官方文档：1.0.0-alpha10 @AppFunctionServiceEntryPoint 架构、运行时门控、安全指引；页面末次更新 2026-07-21）"
  - "https://arxiv.org/abs/2607.05120 （Agent Data Injection Attacks are Realistic Threats to AI Agents，Choi et al., 2026-07-06）"
  - "https://labs.cloudsecurityalliance.org/research/csa-research-note-agent-data-injection-attack-class-20260718 （CSA 研究简报：ADI 新攻击类别，2026-07-18）"
  - "https://arxiv.org/abs/2607.03821 （DualView: Preventing Indirect Prompt Injection in Personal AI Agents，Kim et al., 2026-07-06）"
  - "https://www.secrss.com/articles/92279 （存储型间接提示注入与人机双视图防护架构，中文详解）"
  - "https://arxiv.org/abs/2606.26479 （Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents，2026-06）"
  - "https://www.liquid.ai/blog/lfm2-5-8b-a1b （LFM2.5-8B-A1B: An Even Better On-Device Mixture of Experts，2026-05-28）"
  - "https://www.chinaz.com/2026/0803/1768702.shtml （DroiClaw 诸葛面向中国市场正式发布，2026-08-03）"
tags: [AppIntent, OS-Agent, 端侧Planner, 执行安全, XPIA, ADI, StoredIPI, 每日情报, 跨平台2026]
---

# AppIntent 每日情报（2026-08-03）

> [!abstract] 30 秒速览
> **核心突破**：本期最重的一条是**执行安全的第三个分水岭**——首尔国立大学团队 7 月连发两篇论文，把「提示注入」的定义整个掀翻。**ADI（Agent Data Injection，arXiv 2607.05120）证明：攻击者根本不需要注入「指令」**，只要伪造 Agent 视为可信的**结构化元数据**（元素 ID、数据来源、工具调用/响应格式），Agent 就会自己走进陷阱。六款商用 Agent（Claude in Chrome / Antigravity / Nanobrowser / Claude Code / Codex / Gemini CLI）全部中招，DOM 场景成功率**最高 100%**，而同环境下经典指令注入只有 **0–0.7%**。现有防御几乎全线失守，**唯一归零的是 CaMeL Strict——代价是可用性从 81.2–84.8% 掉到 36.5%**。
> **关键指标**：ADI 成功率 JSON 31.3–43.3% / DOM 33.3–100%；真实 Agent 无专用工具即达 50%。姊妹论文 **DualView（arXiv 2607.03821）**补刀：传统 Dual LLM 对即时注入 ASR 可压到近 0，但**存储型 IPI（Stored IPI）仍有 53.3%**（Claude Haiku 4.5）——隔离机制不是被绕过，是**生命周期被绕过**。
> **OS Agent 场景**：① **Android AppFunctions 1.0.0-alpha10 引入编译时 `@AppFunctionServiceEntryPoint` 架构**（替代 `AppFunctionConfiguration.Provider`），官方给出**自动迁移 skill**；同时曝光了此前库内缺失的 Registry 硬细节：`BIND_APP_FUNCTION_SERVICE` 权限、`android.app.appfunctions.v2` / `app_metadata` manifest 属性、`isEnabled=false` + `setAppFunctionEnabled` **运行时动态门控**。② Google 官方文档**明确承认「系统智能体可能在服务器上处理用户查询」**，并把破坏性动作的确认责任**下放给 App 自己**——与 Apple 的系统级 Confirmation 形成路线分歧。
> **窗口内真增量**：DroiClaw 诸葛（卓易）**面向中国市场正式发布**（08-03），新华社发文；架构口径明确为「本地小模型 + 云端大模型」端云协同、无 App 交互、安全/可控/可观测三性。

## 检索与口径说明（诚实标注）

- **窗口**：延续 08-02 确立的 **7 日滚动窗口（2026-07-27 → 2026-08-03）**，保留「首次进入本库」判定做去重。严格窗口内 OS 级硬命中仅 **1 条**（DroiClaw 中国发布 08-03）。
- **补漏**：本期主体是**四条高价值库内空白**（Android alpha10 架构 / ADI / DualView + 带外防御 / LFM2.5-8B-A1B），**逐条标注真实一手日期，绝不冒充当日新闻**。其中 ADI 与 DualView 虽发表于 07-06，但 CSA 于 **07-18** 才发布正式研究简报、中文安全圈 7 月下旬才扩散，属本库首次入库。
- **信息源**：Horizon MCP 仍全部 disconnected（连接器状态检查确认），改用 WebSearch/WebFetch 直取官方源与 arXiv 一手页面。**合成由本 Agent 完成，未消耗外部分析额度。**
- **评测数字纪律**：ADI / DualView 数字来自论文摘要与 CSA/一手转述，**未复现**；LFM2.5 分数为 Liquid AI 自述与第三方模型库转载，**非本人实测**；所有厂商自述一律标口径。

---

## 原始内容

### 一、窗口内真增量（2026-07-27 → 2026-08-03）

#### 1. DroiClaw 诸葛面向中国市场正式发布（2026-08-03）★★★☆☆

> 库内 08-01 已记录「DroiClaw 登路透社/TechCrunch 等国际媒体」。本次是**中国市场正式发布**这一新节点，且首次拿到架构层口径。

- **发布事实**：新一代 AI 原生操作系统 **DroiClaw 诸葛**面向中国市场正式发布（chinaz 2026-08-03）。首批预装机型**酷派小方块**已于 **2026-06** 发布，完成首批终端落地。国家通讯社**新华社**刊发《卓易科技 DroiClaw 诸葛终端 AI 操作系统获全球关注》。海外经路透社、法新社、TechCrunch 等报道，**1000 余家媒体转载**。
- **架构口径（本次新增，此前只有传播层信息）**：
  - **「本地小模型 + 云端大模型」端云协同混合 AI 架构**——与 [[A2A 端侧智能体协议]] 记录的 HarmonyOS 端侧/云侧双模同构，是端云分工的又一独立实证；
  - 目标形态是**「无 App 交互」的 Agentic OS 生态**：用户不从「找 App、开 App」开始，只表达需求，系统**在授权范围内**协调能力；
  - 自称构建**安全、可控、可观测**的智能体运行体系，**从系统层保障用户隐私**；
  - **需求理解 / 任务规划 / 执行调度融入操作系统底层**（而非应用层套壳）；
  - **开放模型接入机制**，可快速适配新大模型；
  - 用户可创建 **AI Skill**（组合模型 + 工具 + 操作流程），面向资料整理 / 内容翻译 / 日程规划等场景。
- ⚠️ **口径**：以上全部为**厂商与转载稿口径**。「安全、可控、可观测」三性**无公开技术白皮书或第三方评测支撑**（待补）；「1000 余家海外媒体转载」为企业统计口径；未见开发者接入文档、Registry 设计、权限模型公开细节（待补）。价值在于**又一家把「意图驱动」写进 OS 底层调度**的独立样本，可并入 [[Agentic OS 意图调度内核]] 的六方对照。

---

### 二、库内空白补漏（非窗口内，已标真实日期）

#### 2. 🔑 Android AppFunctions 1.0.0-alpha10：编译时 `@AppFunctionServiceEntryPoint` 架构 + Registry 硬细节（官方文档末次更新 2026-07-21）★★★★★

> 库内此前只到「Agent Skill 四步生命周期」（08-02）与「Android 17 GA」（07-31）**高层描述**，**从未拿到 Registry / manifest / 权限 / 运行时门控的 API 级细节**。本次直取官方文档补齐，并**部分推进了挂了 4 天的「四平台 Registry/权限横向 Checklist」待办**。

**A. 架构级变更：alpha10 用编译时入口点替代运行时配置提供者**

- 官方原文：**「In version 1.0.0-alpha10, AppFunctions introduced a compile-time `@AppFunctionServiceEntryPoint` architecture that consolidates library dependencies and replaces legacy configuration providers (`AppFunctionConfiguration.Provider`).」**
- 新写法（官方 TODO app 示例）：

  ```kotlin
  @RequiresApi(36)
  @AndroidEntryPoint
  @AppFunctionServiceEntryPoint(
      serviceName = "TaskAppFunctionService",
      appFunctionXmlFileName = "task_app_function_service",
  )
  abstract class BaseTaskAppFunctionService : AppFunctionService() {
      @Inject internal lateinit var taskRepository: TaskRepository

      @AppFunction(isDescribedByKDoc = true)
      suspend fun createTask(createTaskParams: CreateTaskParams): Task = ...
  }
  ```

- **KSP 编译器负责生成**：具体 service 类（`TaskAppFunctionService`，继承你的抽象入口类）+ `assets/` 目录下的对应 **XML schema**。也就是说，**Schema 不是手写的，是从 Kotlin 注解 + KDoc 编译产出的**——这把「Schema 质量」问题从「开发者自觉」推进到「工具链保证」。
- **迁移路径官方化**：alpha09 → alpha10 可用 [AppFunctions agent skill](https://github.com/android/skills/tree/main/device-ai/appfunctions) 在 Gemini in Android Studio 里**自动迁移**，skill 内含专门迁移规则（整合 build 依赖 / 创建 `@AppFunctionServiceEntryPoint` service wrapper / **解耦 context 参数** / 更新 manifest 声明）。官方甚至给了 prompt 原文。
- **含义**：这是本库首次看到 **OS 厂商把「框架版本迁移」本身做成 Agent Skill 交付**。Android 的打法很清晰——**Schema 编写与迁移都交给 Agent，人只管业务逻辑**。

**B. Registry / 权限硬细节（此前库内空白，本次补齐）**

| 维度 | Android AppFunctions 实测细节（官方文档） |
|---|---|
| 编译要求 | `compileSdk` ≥ **API level 36**；`@RequiresApi(36)` |
| 依赖 | `androidx.appfunctions:appfunctions:1.0.0-alpha10` + `appfunctions-compiler`（KSP） |
| 能力探测 | `AppFunctionManager` 支持则返回实例，不支持返回 **null**（App 无需自检） |
| 服务绑定权限 | `android:permission="android.permission.BIND_APP_FUNCTION_SERVICE"` |
| Intent action | `android.app.appfunctions.AppFunctionService` |
| Manifest 属性 | `android.app.appfunctions.schema`（`app_functions_schema.xsd`）、`android.app.appfunctions.v2`（生成的 XML）、`android.app.appfunctions.app_metadata`（`@xml/app_metadata`） |
| 服务导出 | `android:exported="true"` |
| **运行时动态门控** | `@AppFunction(isEnabled = false)` 默认禁用 → 运行时用编译器生成的 `XxxIds.CREATE_TASK_ID` 常量 + `AppFunctionManager.setAppFunctionEnabled(..., APP_FUNCTION_STATE_ENABLED/DISABLED)` 开关 |
| 错误语义 | 预定义异常 `AppFunctionInvalidArgumentException` / `AppFunctionElementNotFoundException` —— **让 Agent 知道「为什么失败」而非只知道「失败了」** |
| 验证命令 | `adb shell cmd app_function list-app-functions \| grep -A 10 $pkg`；`execute-app-function --package --function 'Class#method' --parameters '{...}'` |
| 函数标识符 | `"$enclosingClassName#$methodName"` |

- **运行时门控是本次最被低估的一条**：官方给出的场景是「账号状态门控」——**功能未解锁前，Registry 里就不应该出现这个工具**。两步法：先 `isEnabled = false` 防止 feature flag 校验完成前被访问，再在运行时按状态开启。⚠️ 官方还提示 `setAppFunctionEnabled` 在 App 初次启动时可能因**索引未完成**抛异常，需 try-catch。
- 对 PM 的含义：**Registry 不是静态清单，是随用户状态实时变化的动态视图**。这直接影响「Planner 看到的工具集」——同一台设备、同一个 App，不同账号状态下 Agent 能做的事不同。这是四平台里目前**唯一有公开 API 的动态可见性机制**（Apple/HarmonyOS/Windows 侧待补）。

**C. 🔴 官方安全指引（两处路线分歧信号，价值极高）**

- **⚠️「系统智能体可能在服务器上处理用户查询」**：官方原文 **「system agents may process user queries on the server to leverage advanced LLM capabilities」**。这是 Google 对**端侧 MCP ≠ 端侧推理**的明确澄清——**执行在端侧，理解可能在云端**。此前库内 [[Android AppFunctions 设备侧意图 2026]] 强调「local-first execution」，本条是必须补上的边界修正。
- **四条选型指引**：① 优先暴露「自然语言比 UI 导航更好表达」的任务；② **窄访问**（只给完成该请求所需的最小数据与动作）；③ **非敏感信息**（只共享不高度私密、或用户在该动作语境下明确同意共享的数据）；④ **破坏性动作必须无歧义确认**。
- **🔴 确认责任归属分歧**：官方原文 **「While the agent might invoke them, your app should include its own confirmation step... It's also helpful to add more than one confirmation step」**——Android 把破坏性动作的确认**下放给 App 自己实现**，甚至建议**多重确认**。这与 Apple Session 343 的 **系统级 Confirmations + entity ownership**（系统据实体归属差异化提示）是**两条不同路线**：
  - **Apple**：系统统一提供确认 UI，App 只需声明实体归属 → 体验一致，但 App 灵活性低；
  - **Android**：系统不保证确认，App 自己负责 → 灵活但**一致性与可审计性全靠自觉**，且「多加一步确认」是把安全成本转嫁给用户体验。
  - 这一条应直接回填 [[Confirmation UI 安全机制]]，是四平台确认机制对比表里此前缺的一格。

#### 3. 🔴 Agent Data Injection（ADI）：攻击不再需要「指令」（arXiv 2607.05120，2026-07-06；CSA 简报 2026-07-18）★★★★★

> **本期最重要的一条。它让本库此前建立的整个 XPIA 认知框架需要打补丁。**

- **团队**：Woohyuk Choi、Juhee Kim、Taehyun Kang、Jihyeon Jeong、Luyi Xing、Byoungyoung Lee（**首尔国立大学 + 伊利诺伊大学厄巴纳-香槟分校 + Largosoft**）。论文 19 页 / 19 图 / 7 表，2026-07-06 提交 arXiv。⚠️ 部分二手报道把机构写成「印第安纳/威斯康星大学」，与 CSA 简报及作者页不一致，**以 arXiv 与 CSA 口径为准**。
- **核心论点（一句话）**：此前所有 IPI 研究与防御都假设「攻击 = 伪装成数据的**指令**」，于是防御去找命令式语气、去过滤祈使句。**ADI 反过来——它注入的是伪装成可信数据的「数据」**：资源标识符、数据来源标记、发件人字段、工具调用/响应格式。Agent 从不用怀疑的眼光审视这些结构，于是**自己得出了攻击者想要的结论**，全程没读到一句「指令」。
- **技术核心：概率性分隔符注入（probabilistic delimiter injection）**：LLM 解析大括号、引号、转义符这类**结构分隔符是概率性、近似的**，而非确定性解析器那样要求精确匹配。攻击者因此可以**在一个 Agent 视为纯文本的字段里，伪造出看起来可信的结构**。
- **三类攻击场景**：
  1. **任意点击（web agents）**：伪造界面元素标识符 → Agent 点到攻击者想要的位置。任何含 UGC 的页面都成为载体。中招：**Claude in Chrome / Antigravity / Nanobrowser**。
  2. **RCE（coding agents）**：攻击者在 GitHub issue 下**冒充项目维护者**发评论 → Agent 在开发者机器上执行恶意命令。
  3. **供应链攻击**：伪造**工具执行历史**，让 Agent 相信 PR 已被验证 → 合入恶意 PR 而未真正检查。中招（2/3）：**Claude Code / Codex / Gemini CLI**。
- **📊 数字（论文/CSA 口径，未复现）**：

  | 项目 | 数值 |
  |---|---|
  | ADI 成功率（JSON 结构化数据） | **31.3% – 43.3%** |
  | ADI 成功率（网页 DOM 数据） | **33.3% – 最高 100%** |
  | 真实商用 Agent（无专用攻击工具） | **最高 50%** |
  | 同环境经典指令注入（对照） | **0 – 0.7%** |
  | 输入/输出过滤器 | **完全失效** |
  | dual-LLM（无严格策略）/ CaMeL-No-Policy | 仍有 **25.0%** 成功 |
  | CaMeL Normal | **23.1%**（作者报告存在污点传播 bug） |
  | Progent | **22.2%** |
  | 数据格式随机化 | **28.7%** |
  | **CaMeL Strict** | **0%** —— 但可用性从 **81.2–84.8% → 36.5%** |

- **披露与工具**：作者已在发表前向 **Anthropic、OpenAI、Google、Nanobrowser** 报告，**前三家确认问题**。团队公开了**测试套件与 AgentDojo 扩展版**，可供第三方独立验证自家 Agent——这点使它区别于一次性 PoC 报告。
- **作者结论（原文）**：**「current agents do not isolate trusted data from untrusted data」**——这不是实现 bug，是**当代 Agent 系统架构级缺失的基础安全原则**。CSA 的类比很准：**这就是 Agent 时代的 SQL 注入**，而修复 SQL 注入靠的是参数化查询这种**架构改造**，不是加过滤器。
- **对 OS Agent 的直接冲击（本库视角）**：
  - Android AppFunctions 的 **`AppFunctionMetadata`**（由 KDoc 编译产出）、Apple 的 **AppEntity 标识符 / View Annotations**、HarmonyOS 的 **A2A 消息格式**——**全都是 ADI 定义的「安全关键元数据」**。目前**四平台均无公开的 ADI 类别评估**（待补）。
  - 尤其值得警惕：Apple Session 343 的 `.appEntityIdentifier` 把「屏幕上的实体」映射为标识符，**这正是 ADI 场景一（伪造元素标识符）的靶心形态**。Apple 的实现是否有来源校验，官方文档未见说明（待补）。

#### 4. DualView：Stored IPI 与「Agent 视图 / 人类视图」分离（arXiv 2607.03821，2026-07-06）★★★★☆

> 与 ADI 同一批首尔国立大学作者（Juhee Kim、Woohyuk Choi、Taehyun Kang、Youngmin Kim、Byoungyoung Lee）的姊妹论文。**它给隔离执行提出了一个全新的架构原语。**

- **发现的漏洞：Stored IPI（存储型间接提示注入）**
  - 传统 **Dual LLM 模式**把不可信数据换成符号（如 `$web_01.content`），Agent 只能引用、不能读取 → 对**即时型** IPI 有效。
  - **但数据要离开模型上下文时就破功了**：Agent 把摘要写入文件，为了让用户能正常打开，系统会在落盘前**还原真实文本**。一旦真实文本进入普通文件系统，**符号关系就消失了**；后续任务重读该文件，高权限 LLM 直接看到原文。
  - **📊 实测（Claude Haiku 4.5）**：传统 Dual LLM 对即时型 IPI 的 ASR 可降到**接近 0**，但面对 **Stored IPI 仍达 53.3%**。
  - **一句话**：**攻击没有绕过隔离机制，而是绕过了隔离机制的生命周期。**
- **DualView 方案：同一份数据，两套视图**
  - **AgentView**：可信内容保原文，不可信内容**恒为符号**——Agent 写文件写的是符号，重读还是同一个符号，**Stored IPI 从根上断掉**。
  - **HumanView**：用户和普通程序（编辑器、文件管理器）看到的是**正常原文**，环境照常工作。
  - **视图路由**：工具不需要看原文（如本地文件读写）→ 在 AgentView 执行；工具必须处理原文（如网络请求）→ 路由到 HumanView，调用前**去符号化**、返回后把新产生的不可信内容**重新符号化**。
  - **实现**：Agent File System 用 **Git Worktrees** 管理，双文件环境（Agent 操作符号化文件，人类访问真实文件）。作为 **OpenClaw 插件**部署，**仅用 tool hooks**，不改 Agent 的 tool-call 逻辑，也不改工具实现。
  - **策略分两层**：**数据可信策略**（检查工具输出：schema 规则 / origin 规则，如 `api.github.com/*` 可信、`imports/*.csv` 不可信、`agent:public-chat` 不可信）+ **数据使用策略**（检查发往 HumanShell 的命令：`exec(git status)` 免审批，`exec($web1.text)` **必须人工审批**，并有命令重写规则防 `python -c` 绕过）。
- **📊 结果**：在 IPI benchmark 与 **PinchBench**（147 任务，114 读文件、121 写文件）上，DualView **阻断了包括 Stored IPI 在内的全部 IPI 攻击**，可用性接近无防护基线。作者强调**因为是设计层隔离，防护不局限于已知攻击模板**。
- **对 OS Agent 的含义（本期第二重要的洞见）**：
  - [[Agent Workspace 隔离执行]] 记录的 Windows 方案是**「另起一个低权限账号 + ACL + 独立会话」**——隔离的是**执行主体**。
  - DualView 隔离的是**数据的可见形态**：同一个文件系统，Agent 和人看到不同内容。**这是比进程/账号隔离更细的粒度**，且恰好覆盖了账号隔离覆盖不了的场景——**Agent 有合法权限读写的文件，内容本身却不可信**。
  - 对系统级 Agent 的启发：**OS 该不该提供「Agent 视图文件系统」作为一等公民？** 四平台目前均无此设计（待补/建议方向）。

#### 5. 带外防御系统化：「门不能是模型」（arXiv 2606.26479，2026-06）★★★★☆

- **核心命题**：把参考监视器（reference monitor）**移到模型之外**，用**确定性门控**而非模型守卫。论文用经典安全视角重述（Biba 完整性模型、reference monitor、Saltzer–Schroeder 原则、capabilities/IFC），并做 8 维度系统化。
- **关键判断（原文精神）**：**in-band 防御没有保证**——Nasr 等人已在 >90% 成功率下攻破 12 种；**「guardrail 模型本身也是模型，它自己就可被注入」**（呼应 OWASP LLM01:2025）。检测输了，**结构赢了**。
- **📊 复现数字（Qwen2.5-7B，论文 §11）**：ASR **25.8% → 4.2% → 2.6%**；代价是可用性 **~45% → ~26%**、LLM 调用量 **~15×**。作者自己标注该 7B 是弱 agent，绝对数字有 artifact 成分。
- **🔑 与 Confirmation UI 直接冲突的一条（AIMS）**：**Agent Identity Management System（AIMS）** 主张 **「LLM MUST NOT hold credentials」**，且**授权应由授权服务器完成，而不是由本地 UI 确认**。
  - 这对本库 [[Confirmation UI 安全机制]] 是个**必须记下的反向论点**：**用户在本地点「确认」，不等于完成了授权**。如果 Agent 已被 ADI 污染，它呈现给用户的确认内容本身就可能是被操纵的——**用户确认的是攻击者写好的文案**。
  - 结合 Android「确认交给 App 自己做」的路线，这个风险被放大：**被污染的 Agent + App 自实现的确认 UI = 确认环节整体不可信**。
- **未答问题（论文自陈）**：白盒优化攻击（GCG）能否攻破确定性门？Progent 的策略是 **LLM 撰写**的——「门不能是模型」原则在**策略作者仍是模型**时是否成立？~15× 调用开销在生产规模是否经济？

#### 6. LFM2.5-8B-A1B + LocalCowork：端侧 Agent 循环的可引用实证（Liquid AI，2026-05-28）★★★★☆

> 库内 [[Function Calling 端侧工具调用]] 的评测表止于 TinyLLM/BFCL 与 Needle 26M，**缺少「端侧模型真的跑完整 Agent 循环」的落地样本**。本条补齐。

- **模型规格**：8.3B 总参 / **1.5B 激活**（MoE）；24 层（18 个双门控 LIV 卷积块 + 6 个 GQA 层）；**128K 上下文**（上代 32K）；词表 **128K**（上代 65K，非拉丁语系分词效率显著改善）；预训练 **38T tokens**（上代 12T）+ 大规模 RL；**reasoning-only** 模式（回答前显式生成 CoT）。
- **📊 分数（Liquid AI 自述 / 第三方模型库转载，未复现）**：**BFCLv3 64.36**、**IFEval 91.84**、**Tau2 Telecom 13.60 → 88.07**（对比上代 LFM2-8B-A1B）、AIME25 42.53（推理深度是明显短板）。
- **📊 速度**：M5 Max **253 tok/s**、Ryzen AI Max+ 395 **146 tok/s**，内存 **< 6 GB**；**手机上约 30 tok/s**。首日支持 llama.cpp / MLX / vLLM / SGLang / ONNX / LEAP。
- **🔑 LocalCowork 实证（本条真正的价值）**：Liquid AI 的开源桌面 Agent demo 在**一台笔记本**上跑 **13 个 MCP server 的 67 个工具**，**无云、无 API key、数据不出机**。官方描述的循环是：**「ask, propose, confirm, run, repeat」**，**每次 dispatch 远低于 1 秒**，并保有**完整审计轨迹（full audit trails）**。
  - 这是本库第一次拿到「端侧 Planner + 数十个工具 + 确认环 + 审计日志」**全部齐备**的可引用样本。它同时回答了两个此前只有推测的问题：**(a)** 67 个工具的工具菜单，1.5B 激活参数的端侧模型选得动；**(b)** 「确认 + 审计」在亚秒级 dispatch 下**不必然破坏交互感**。
  - ⚠️ 口径：为**厂商自家 demo**，工具集与任务难度由厂商选定，**无第三方复现**（待补）。**不可**据此推断「端侧模型已可替代云端 Planner」。
- **同期参考（非本条重点）**：Liquid AI 2026 发布节奏为 LFM2.5-350M（03-31）、LFM2.5-8B-A1B（05-28）、LFM2.5 Retrievers（06-18）、LFM2.5-230M（06-25）。

---

### 三、边界判定（已评估后排除，展示过滤纪律）

| 条目 | 日期 | 排除理由 |
|---|---|---|
| 荣耀 Robot Phone 8 月发售 / AgenticOS | 07-18 WAIC 发布，8 月发售 | AgenticOS 本身 08-01 已入库；**Robot Phone 截至今日仍为预约状态，未实际发售**，无新的 OS 级 API/Registry 信息。**保留为待办跟踪**，不重复记录。 |
| Microsoft Project Polaris / GitHub Copilot 换引擎 | 2026-08 上线 | **编码模型替换**，非 OS 级意图框架/执行总线变更。低于阈值。 |
| M365 Copilot UI 统一 / 经典版 Outlook 加 Copilot 入口 | 2026-08 | **应用层 SaaS**，延续 08-02 的同类排除判定。 |
| HalluSquatting 僵尸网络式注入 | 07-08（Ars Technica） | 目标是 **AI 编码助手**而非 OS Agent 执行总线；且威胁模型（注入可自我复制/规模化）已被 08-01 的「文档型 XPIA 自传播蠕虫」覆盖。**仅作 [[文档型 XPIA 自传播蠕虫]] 的旁证提及，不单列。** |
| Apple iOS 27 Siri AI 候补名单 / SiriKit 弃用时间线 | 06-08 起 | 库内 07-31 / 08-01 / 08-02 已覆盖。**唯一值得记的新点**：Siri AI 因 **DMA 在欧盟延迟**（见下方拆解 ②C）。 |

---

## 正文拆解

### ① Schema 定义与语义路由机制

**A. Android 把「写 Schema」和「迁移 Schema」双双交给了 Agent，这是与 Apple 最大的路线差异。**

Apple 的 Schema 靠开发者手写 Swift 声明（`@AppIntent(schema:)`、`IndexedEntity`、View Annotations），系统提供强约束与统一体验。Android 的 alpha10 走到了另一头：**Kotlin 注解 + KDoc → KSP 编译 → 自动生成 service 类和 XML schema**，连 alpha09→alpha10 的架构迁移都由**官方 agent skill** 自动完成。

这印证并推进了本库的长期论断——**[[意图模式规范]] 的质量决定端侧路由上限**——但换了个解法：Apple 用**规范约束**保质量，Android 用**工具链自动化**保质量。风险也随之不同：**Android 的 Schema 质量下限取决于 KDoc 写得好不好，而 KDoc 现在是 Agent 生成的**。这引出一个尚无人回答的问题：**自动生成的工具描述若有歧义导致误执行，责任在谁？**（08-02 提出，今日仍待补。）

**B. Registry 是动态的，不是静态清单——这条被严重低估。**

`isEnabled = false` + `setAppFunctionEnabled` 意味着**同一个 App 在不同账号状态下，向系统 Agent 暴露的工具集不同**。对 [[语义路由]] 的直接影响是：Planner 面对的**工具空间随用户状态实时变化**，路由决策不能基于安装时的静态快照。对 PM 的实操含义：

- 端侧 Planner 的**评测集必须包含「工具不可用」分支**，否则线上会出现「Agent 承诺了它当下做不到的事」；
- 「工具是否可见」本身成了**产品策略与权限设计的交汇点**——付费墙、灰度、地域限制都会落到 Registry 上。

这是四平台里目前**唯一有公开 API 的动态可见性机制**。Apple / HarmonyOS / Windows 侧是否有等价能力，**待补**——这一格填上，六方 Registry Checklist 就能真正成表。

**C. 「执行在端侧」不等于「理解在端侧」——Google 亲口澄清。**

官方文档白纸黑字：**system agents may process user queries on the server**。这修正了本库 [[Android AppFunctions 设备侧意图 2026]] 里偏向「local-first」的表述。准确的说法应该是：**AppFunctions 保证的是「执行发生在你的 App 进程内、用本地状态」，不保证「用户说的话不出设备」**。

这条对隐私叙事影响很大。对比 HarmonyOS 端侧 A2A 主打的「**隐私数据不出端**」（银行 1000+ 意图案例）、DroiClaw 的「本地小模型 + 云端大模型」，三家的端云边界划在了不同位置：

| 平台 | 意图理解 | 动作执行 | 公开口径 |
|---|---|---|---|
| Android AppFunctions | **可能在云端**（官方明示） | 端侧 App 进程内 | 「OS 级本地 hook」但不承诺理解在端 |
| HarmonyOS 端侧 A2A | 端侧 | 端侧 | 「隐私数据不出端」（厂商口径，待补） |
| HarmonyOS 云侧 A2A | 云端 | 端云协同 | 主打「复杂任务深度推理」 |
| DroiClaw 诸葛 | 本地小模型 + 云端大模型 | 系统底层调度 | 「端云协同混合」（厂商口径，待补） |
| Apple | 端侧 Foundation Models + PCC + Gemini | 端侧 App Intents | 分层，Extensions 走 App Review |

**给 PM 的判据**：以后看到「端侧 Agent」宣传，要拆成**三问**——理解在哪？执行在哪？数据落哪？三者可以分别在端或云，混着说就是话术。

---

### ② 系统安全与用户体验（Confirmation / 隔离 / 防注入）

**A. 🔴 ADI 是执行安全的第三个分水岭，而且它打的是本库自己的认知框架。**

本库已记录两个分水岭：**08-01 Word 蠕虫**（注入会自我复制）、**08-02 EU AI Act Article 15 生效**（防护成为法律义务）。**今天是第三个，而且性质不同——前两个是「威胁变强 / 约束变硬」，这个是「威胁的定义变了」。**

此前包括本库在内，整个防御思路都建立在一个假设上：**攻击载荷是「伪装成数据的指令」**。所以 Article 15 点名 "prompt injection"，所以 Confirmation UI 拦「危险动作」，所以过滤器找祈使句。ADI 直接证明这个前提不完整：

> **攻击者可以只伪造「结构」，不写一句指令，让 Agent 自己推出错误结论。**

同环境对照数字最能说明问题：**经典指令注入 0–0.7%，ADI 最高 100%**。这不是「防御强度不够」，是**防御打错了靶子**。

对四平台的具体拷问（**均待补，无一家有公开的 ADI 类别评估**）：

| 平台 | ADI 潜在靶面 | 是否有公开来源校验 |
|---|---|---|
| **Apple** | `.appEntityIdentifier` / View Annotations 的实体标识符——**正是 ADI 场景一的靶心形态** | 官方文档未见说明（待补） |
| **Android** | `AppFunctionMetadata`（KDoc 编译产出）、`app_metadata` manifest 属性、工具响应格式 | 未见（待补） |
| **HarmonyOS** | A2A 端侧/云侧消息格式、Skill 元数据 | 未见（待补） |
| **Windows** | Agent Workspace 内的工具调用/响应格式 | 未见（待补） |

**B. Confirmation UI 今天同时挨了两记，需要重新审视。**

- **第一记（架构侧，AIMS）**：**「授权应由授权服务器完成，而非本地 UI 确认」**。若 Agent 已被 ADI/IPI 污染，**它呈现给用户的确认文案本身就是被操纵的产物**——用户确认的是攻击者写好的话。**本地点击 ≠ 授权**。
- **第二记（责任侧，Android）**：Android 把破坏性动作的确认**下放给 App 自己实现**，还建议「多加一步」。两条叠加的后果很直白：**被污染的 Agent + App 自实现的确认 UI = 确认环节整体不可信**，而且体验代价（多次点击）由用户承担。

这意味着 [[确认机制]] 的设计原则需要升级。本库此前记的维度是「动作级 → 实体归属级（Apple Session 343）→ 是否可逆（08-01）」。今天要补第四维：**确认内容的完整性来自哪里？** 三种档次：

1. **最弱**：Agent 自己组织确认文案 → ADI 一破全破；
2. **中等**：系统据结构化元数据渲染确认（Apple 的 entity ownership 路线）→ **但元数据本身若可伪造，仍不安全**；
3. **最强**：确认/授权走**带外**通道，由不可被模型影响的组件（授权服务器 / 硬件级审批）完成 → 对应 [[Agent 身份与硬件级审批]]。

**四平台目前都在第 1–2 档。这是一条可以直接写进产品需求的判据。**

**C. DualView 提出了一个 OS 该考虑的新原语：Agent 视图文件系统。**

Windows [[Agent Workspace 隔离执行]] 隔离的是**执行主体**（低权限账号 + ACL + 独立会话）。DualView 隔离的是**数据的可见形态**（AgentView 恒为符号 / HumanView 保原文）。两者正交，且后者覆盖了前者的盲区——**Agent 有合法权限读写的文件，内容本身却不可信**。Stored IPI 53.3% 就是这个盲区的量化。

值得注意的是 DualView 的**工程可行性**很高：OpenClaw 插件、仅用 tool hooks、不改 tool-call 逻辑、Git worktrees 做双文件环境、可用性接近基线。**这不是需要重写 OS 才能落地的方案。**

留给四平台的问题：**OS 是否应该把「Agent 视图」做成文件系统的一等公民？** 目前无一家有此设计。这是本库可以主动提出的一条产品建议，而非被动跟踪的新闻。

**D. 「门不能是模型」与端侧的成本现实相撞。**

带外防御论文给出的确定性门控效果好（ASR 25.8%→2.6%），但代价是可用性 ~45%→~26%、**LLM 调用 ~15×**。CaMeL Strict 更极端——ADI 归零，可用性从 81.2–84.8% 掉到 **36.5%**。

**放到端侧语境，这个账更难算**：LFM2.5-8B-A1B 在笔记本上 253 tok/s、手机 30 tok/s，本来就是靠「小」换来的可用；再乘 15× 调用，端侧 Agent 的交互感会直接崩塌。所以短期内**端侧不可能全量上带外确定性门控**，现实路径大概率是**按动作风险分层**：

- 只读 / 可逆动作 → 快路径，不加门；
- 破坏性 / 不可逆 / 涉钱涉隐私 → 走带外门 + 硬件级审批。

这恰好可以和 08-01 的 [[Agent 写回路径 XPIA 风险评估 SOP]] 拼成完整的双向判据：**写回路径管「Agent 往外写什么」，读入路径管「Agent 信了什么」**。本期为此新建 C 层 SOP（见下）。

**E. 顺带一条容易漏的合规交叉信号。**

Apple 因 **DMA** 在欧盟**延迟**发布 iOS 27 / iPadOS 27 的 Siri AI（Apple Newsroom 2026-06-08）。把它和 08-02 记的 **EU AI Act Article 15 已于 08-02 生效**放一起看：**欧盟同时在用 DMA（互操作性）和 AI Act（安全鲁棒性）两把尺子量 OS 级 Agent，而这两把尺子的方向是相反的**——DMA 要求开放互操作，AI Act 要求可控可举证。Apple 选择的是在欧盟**先不上**。这个张力值得持续跟踪，可能是 2026 下半年 OS Agent 区域化分裂的起点。

---

## 值得保留的点

1. **🔴 ADI 改写了「注入」的定义** —— 攻击者不需要写指令，只需伪造 Agent 视为可信的**结构化元数据**。同环境对照：经典指令注入 0–0.7%，ADI 最高 **100%**。**这是 Agent 时代的 SQL 注入**，只能靠架构改造（隔离可信/不可信数据）解决，加过滤器无效。
2. **CaMeL Strict 是唯一归零的防御，代价是可用性 81.2–84.8% → 36.5%** —— 「安全与可用」在 ADI 面前的兑换率极其残酷，这个数字应作为所有 Agent 安全方案的基准锚点。
3. **Stored IPI = 隔离机制的生命周期漏洞** —— 传统 Dual LLM 即时注入 ASR≈0，但存储型仍 **53.3%**。攻击没绕过隔离，绕过的是隔离的**有效期**。
4. **DualView 的「AgentView / HumanView」是一个 OS 级新原语** —— 同一份数据两套视图，Agent 恒见符号、人见原文。比进程/账号隔离粒度更细，且工程可行（插件 + tool hooks + Git worktrees，可用性近基线）。
5. **Android alpha10 `@AppFunctionServiceEntryPoint`：Schema 从「手写」变「编译产出」** —— KSP 生成 service 类 + XML schema；连版本迁移都做成官方 agent skill。与 Apple 的「规范约束」路线正面分叉。
6. **Registry 是动态视图，不是静态清单** —— `isEnabled=false` + `setAppFunctionEnabled` 让工具集随账号状态实时变化。**四平台唯一有公开 API 的动态可见性机制**，端侧 Planner 评测集必须覆盖「工具不可用」分支。
7. **🔴 Google 明示「系统智能体可能在服务器处理用户查询」** —— 「执行在端侧」≠「理解在端侧」。看端侧宣传要**三问**：理解在哪？执行在哪？数据落哪？
8. **确认机制路线分歧 + 双重打击** —— Apple 系统级统一确认 vs Android「App 自己做，建议多加一步」；叠加 AIMS 的「本地 UI 确认不构成授权」。得出确认完整性三档判据（Agent 自组织 / 系统据元数据渲染 / 带外授权），**四平台都还在 1–2 档**。
9. **LocalCowork：端侧 Agent 循环首个齐备样本** —— 单笔记本 13 个 MCP server / 67 工具，`ask-propose-confirm-run` 亚秒级 dispatch + **完整审计轨迹**，数据不出机（厂商 demo，待第三方复现）。
10. **端侧算不起 15× 的安全税** —— 带外门 ASR 25.8%→2.6% 但调用 ~15×。端侧必然走**按动作风险分层**：只读走快路径，不可逆走带外门。

## 我的问题

1. **四平台的意图元数据（AppFunctionMetadata / AppEntity 标识符 / A2A 消息格式）是否做了来源校验与完整性保护？** 有没有任何一家做过 ADI 类别评估？（**四平台均待补——这是本期最该追的一条**）
2. Apple 的 `.appEntityIdentifier` 恰是 ADI 场景一的靶心形态。**Apple 对屏幕标注实体的标识符做了签名/来源绑定吗？** 还是纯字符串信任？（待补，官方文档未见说明）
3. **OS 该不该提供「Agent 视图文件系统」作为一等公民？** DualView 证明了插件级可行且可用性近基线，那么系统级实现的阻力是什么？（无一家有此设计，属可主动提出的产品建议）
4. Android 把破坏性动作确认**下放给 App**，**是否会有 Play 审核层面的强制要求？** 还是纯靠开发者自觉？若 App 不做确认，系统会兜底吗？（待补）
5. Android Registry 的动态门控（`setAppFunctionEnabled`），**Apple / HarmonyOS / Windows 是否有等价 API？** 填上这一格，六方 Registry Checklist 即可成表。（待补，挂了 5 天）
6. **CaMeL Strict 的 36.5% 可用性能否被优化？** 还是说「ADI 归零」与「Agent 可用」在当前架构下就是不可兼得？（论文未答）
7. 带外防御的 ~15× 调用开销在**端侧**是否有更省的等价物？例如把确定性门放进 TEE / 安全芯片，避开重复 LLM 调用？（与 [[Agent 身份与硬件级审批]] 交叉，待研究）
8. DMA（要开放互操作）与 AI Act Article 15（要可控可举证）方向相反，Apple 已选择在欧盟**先不上** Siri AI。**其余三家会怎么选？** 这是否是 OS Agent 区域化分裂的起点？（待跟踪）

## 后续动作

- [x] 提炼为概念（本次 B 层：净新增 2 个独立节点 + 既有节点追加 6 处）
- [x] 关联已有方法（本次 C 层净新增 1：读入路径判据，与 08-01 的写回路径 SOP 构成双向闭环）
- [x] **部分推进挂了 5 天的「Registry/权限横向 Checklist」待办** —— Android 一列已用官方文档填实（权限 / manifest 属性 / 动态门控 / 验证命令 / 错误语义），其余三列标待补
- [ ] **【本期最高优先级】** 追四平台是否有 ADI 类别评估 / 意图元数据来源校验机制
- [ ] 核验 Apple `.appEntityIdentifier` 是否有来源绑定或签名
- [ ] 补齐 Apple / HarmonyOS / Windows 的 Registry 动态可见性 API（填满六方 Checklist）
- [ ] 跟踪 Anthropic / OpenAI / Google 对 ADI 的类别级缓解（三家均已确认问题）
- [ ] 用作者公开的 AgentDojo 扩展版测试套件，评估是否值得自建端侧 Agent 的 ADI 回归集
- [ ] 延续待办：Digital Omnibus 正式文本；HarmonyOS 银行 App 名与 1000+ 意图清单；Per-Intent Privacy Manifest 是否真实 API；Android Agent Skill 发布日期；荣耀 Robot Phone 8 月实际发售；Måløy Word 蠕虫类别级缓解

> [!note] 概念节点双链
> [[意图模式规范]] ｜ [[语义路由]] ｜ [[端侧工具调用]] ｜ [[确认机制]] ｜ [[元服务]] ｜ [[隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本库对应节点**：[[Intent Schema Protocol 意图模式规范]] ｜ [[Intent Router 语义路由]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Confirmation UI 安全机制]] ｜ [[Atomic Service 元服务]] ｜ [[Agent Workspace 隔离执行]] ｜ [[A2A 端侧智能体协议]] ｜ [[XPIA 跨提示注入]]
>
> **本次净新增节点**：[[Agent Data Injection 数据注入攻击]] ｜ [[Dual View 智能体数据视图隔离]]
>
> **本次增补（不新建，仅追加到既有节点）**：[[Android AppFunctions 设备侧意图 2026]] ｜ [[XPIA 跨提示注入]] ｜ [[Confirmation UI 安全机制]] ｜ [[Agent Workspace 隔离执行]] ｜ [[Function Calling 端侧工具调用]] ｜ [[Agentic OS 意图调度内核]]
>
> **既有笔记（不重写，仅指向）**：[[App Intent 的核心作用]] ｜ [[Apple Intelligence 与 App Intents]] ｜ [[国内安卓厂商做 App Intent 的阻力]] ｜ [[工业级 GUI Agent 架构（VLM+无障碍树）]] ｜ [[手机AI智能体知识库]] ｜ [[安卓厂商意图识别破局策略]] ｜ [[App Infra 应用基建]]
