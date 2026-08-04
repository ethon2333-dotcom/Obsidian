# App Intent 的核心作用

> 在手机发展史上，App Intent 最核心的作用是：**将手机交互的重心从「以 App 为中心」转向「以用户任务为中心」**。

## 交互范式的转变

- **以前**：找到 App → 打开 App → 寻找功能 → 执行操作
- **现在（有 App Intent）**：识别需求 → 调取 App 的底层能力 → 完成任务

系统或 AI 能够直接「识别需求 → 调取 App 的底层能力 → 完成任务」，用户不再需要关心手机里装了哪些 App。

## App Intent 扮演的 4 个关键角色

### 1. 打破「应用孤岛」，实现真正的跨应用协作
移动操作系统早期，各 App 像封闭的高墙花园，彼此无法通信。App Intent 定义了一套通用的**系统级协议**，让应用能安全地把核心功能（发消息、拍照、创建日程）暴露给系统和其他应用。

### 2. 驱动系统级交互（小组件、灵动岛、快捷指令）
现代手机界面不再只是图标网格。桌面小组件（Widgets）、iOS 灵动岛（Dynamic Island）、锁屏快捷方式、控制中心按钮，本质上都依赖 App Intent。开发者无需重写界面逻辑，只需把功能包装成 Intent，就能让能力嵌入系统各组件。

### 3. 充当 AI Agent（智能体）的「手脚」
在大模型时代，这是最具颠覆性的作用。LLM 擅长理解自然语言（大脑），但无法直接控制软件。App Intent 充当**结构化的 API 契约（Schema）**：
- **精准执行**：让 AI 以高准确率点外卖、查机票、发邮件，避免 GUI Agent 屏幕点击容易点错、失效的缺点。
- **参数传递**：自动将自然语言实体（「明天上午 10 点」「张三」）解析并填入 App 参数列表。

### 4. 建立标准化隐私与安全边界
若不经过 App Intent，AI / 系统要控制手机就得依赖「全屏录屏 + 模拟人手点击」，隐私泄露与误操作风险极大。App Intent 提供**沙盒化、声明式的授权机制**——系统 / AI 只能调用 App 明确暴露且获用户许可的能力。

## 演进历程

| 阶段 | 时间 | 代表 |
|------|------|------|
| 基础跨应用通信时代 | 2008–2017 | Android Intent 机制，解决应用间分享图片、打开链接等基础数据传递 |
| 快捷指令与组件化时代 | 2018–2021 | 苹果 Siri Shortcuts，App 能力渗透进桌面小组件、锁屏 |
| App Intents 框架标准化 | 2022–2023 | iOS 16 正式推出 App Intents 框架，将 Action / Entity / Query 高度结构化 |
| AI Agent 驱动全场景时代 | 2024–现在 | Apple Intelligence、系统级 Phone Agent，App Intent 升级为 AI 的 Tool Call |

## 意义
App Intent 的普及标志手机操作系统从 **GUI（图形界面）向 LUI / Agent UI（意图驱动）** 跨越。未来用户只需表达需求，系统通过 App Intent 在后台完成调度。

## 深化补充（2026-08）

### 一句话心智模型
**App Intent 改变的是「寻址方式」**：过去系统按包名寻址（我要 `com.xxx.yyy` 这个东西），现在按语义寻址（我要「给张三发条消息」这个能力）。一旦寻址单位从 App 降到能力，App 图标就退化成能力的一个展示外壳，而不再是唯一入口。上面写的「以任务为中心」是现象，寻址单位变了才是机制。

### 谁来定义能力目录：四平台分成了两派（2026-08 官方文档核实）

| 平台 | 登记方式 | Schema 由谁定义 |
|---|---|---|
| Apple | `@AppIntent(schema: .audio.addToPlaylist)` 对齐系统 App Schema Domains | **平台预定义**，开发者对齐 |
| HarmonyOS | `insight_intent.json` 注册，声明 `intentName` / `domain` / `intentVersion` | **平台预定义**——官方文档明示「当前仅支持预置垂域意图，**不允许自定义**」 |
| Android | `@AppFunction(isDescribedByKDoc = true)`，KDoc 注释即工具描述，KSP 构建期生成 XML Schema | **开发者自由声明** |
| Windows | MCP 连接器注册进 ODR（On-Device Registry） | 连接器自述 + 平台受控发现 |

- **预定义派（Apple / 鸿蒙）**：语义统一、免训练泛化好、确认提示可标准化；代价是**平台没定义的垂域你就进不来**。
- **自由声明派（Android）**：覆盖无上限；代价是**路由质量完全取决于开发者写的那段 KDoc**。Google 官方 AppFunctions Agent Skill 的四步生命周期里专门有一步就叫 **KDoc Refinement**，本质是在给这个洞打补丁——「文档从写给人看，变成写给模型看」。
- **这条分歧的产品含义**：预定义派需要平台有足够生态号召力才推得动。国内任何单一安卓厂商都不具备，所以只剩「自由声明 + 行业联盟统一」一条路（见 [[安卓厂商意图识别破局策略]] 第四节）。

### 演进历程补一行

| 阶段 | 时间 | 代表 |
|------|------|------|
| 设备侧 MCP 时代 | 2026– | Android AppFunctions 官方定位为「MCP 中工具的**移动端等效实现**」，App 像设备端 MCP 服务器一样对外供给工具；调用方须持 `EXECUTE_APP_FUNCTIONS` 权限；适用 Android 16+，与 Gemini 的集成自 2026-05 起对可信测试人员私测（官方文档标注**实验性预览**） |

### 待解问题
- [ ] 语义寻址普及后，App 的品牌资产靠什么承载？「被 Intent 命中的次数」会不会变成新的商店排名——**谁定排序规则、能不能买？**
- [ ] 预定义 Schema 覆盖不到的长尾垂域（政务、企业内部系统、小众工具）怎么办？鸿蒙「不允许自定义」这条限制多久会松、松了之后语义一致性怎么保？
- [ ] 我一直默认「Intent 一定比 GUI 好」。但同一能力：走 Intent 会被 App 关掉（Registry 可动态禁用），走 GUI 会被风控封——**如果两条都堵，是不是说明这层的胜负根本不在技术侧？**

## 关联
- 苹果的具体实现见 [[Apple Intelligence 与 App Intents]]
- 支撑 App 的底层架构见 [[App Infra 应用基建]]
- 国内落地的阻力见 [[国内安卓厂商做 App Intent 的阻力]]
- 四平台机制横向对照 → [[Intent Schema Protocol 意图模式规范]]
- 各平台官方实现深读 → [[Android AppFunctions 设备侧意图 2026]] · [[Apple AppIntents Schema Protocol 2026]] · [[HarmonyOS Intents Kit 与 ArkAF 2026]] · [[Windows Copilot Actions 与 Agent Workspace 2026]]
- 「这个能力走哪条通道」→ [[端侧执行通道 GUI 与 MCP 路线之争]]
- 主题综览 → [[端侧意图框架 学习笔记]]

#标签/AppIntent #标签/手机AI
