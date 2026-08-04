# Apple Intelligence 与 App Intents

> Apple Intelligence（大脑）与 App Intents（手脚）的结合，本质是 **LLM 的 Tool Calling 机制在操作系统层面的深度落地**。

传统 AI 只能聊天或生成文本（没有直接操控软件的权限）。苹果通过 App Intents 框架为系统级 AI 提供了一套**强类型、结构化的标准 API**，让 Apple Intelligence 既能理解自然语言，又能精准操控 App。

## 支撑跨应用自动化的 3 个核心组件

```
                  Apple Intelligence (端侧/云侧 LLM)
                              |
       +----------------------+----------------------+
       |                      |                      |
┌──────▼──────┐        ┌──────▼──────┐        ┌──────▼──────┐
│ App Schemas │        │ App Entities│        │  View API   │
│  (功能契约) │        │ (数据语义化) │        │  (屏幕感知) │
└─────────────┘        └─────────────┘        └─────────────┘
```

### App Schemas（应用动作契约）
苹果为常见领域（邮件、日历、照片、信息、文档等）定义了标准系统级架构（Schemas）。开发者只需把 App 内操作标记为符合某种 Schema（如「创建日程」「发送消息」），Apple Intelligence 无需针对具体 App 训练即可直接调用。

### App Entities 与语义索引（数据理解）
App Intents 不仅暴露动作，还暴露**数据实体（App Entities）**。App 将内部数据（照片、联系人、笔记）提交给 Spotlight 的语义索引（Semantic Index）。当你说「上周我在杭州吃面拍的照片」，AI 能通过语义搜索精准定位到具体 App Entity。

### 屏幕感知（On-Screen Awareness）
通过 View Annotations 等 API，App 把屏幕上渲染的视图内容与 App Entity 关联。对着屏幕说「把这个地址发给张三」，AI 能精准识别「这个」指当前界面哪部分数据。

## 案例拆解：跨应用自动化执行

**用户指令：**「把刚才小红在微信里发给我的餐厅地址保存到备忘录，并创建一个明天晚上 7 点的日历提醒。」

1. **任务拆解与意图规划（Planning）**：端侧 LLM 把单句需求拆成有依赖关系的动作链（Action Graph）：
   - 动作 A：检索微信中来自「小红」的最新消息（提取餐厅地址）
   - 动作 B：在备忘录新建笔记写入地址
   - 动作 C：在日历创建明天 19:00 事件，附带餐厅信息
2. **实体检索与参数填充（Disambiguation & Extraction）**：系统调用微信的 AppEntity 查询接口 + 语义索引匹配联系人「小红」和含地址的最新消息；模型把解析出的文本实参动态填入下一个 App Intent 的入参字段。
3. **跨应用链式执行（Action Execution）**：后台依次触发 `CreateNoteIntent`（备忘录）、`CreateEventIntent`（日历）。涉及敏感 / 不可逆操作（付款、删除）时，框架自动唤起轻量化系统 UI 弹窗确认，无需切入 App 界面。

## 相比传统自动化（模拟点击）的优势

| 维度 | 传统模拟点击（GUI Agent） | Apple Intelligence + App Intents |
|------|------|------|
| 可靠性 | 极低（界面改版或按钮位移即失效） | 极高（直接调用代码层结构化 API，不受 UI 影响） |
| 执行速度 | 慢（一步步模拟打开 App、点界面） | 毫秒级（后台静默完成参数传递与写入） |
| 隐私安全 | 差（需无限制屏幕录制 / 无障碍权限） | 高（基于沙盒和系统授权，仅响应已定义 Intent） |
| 泛化理解 | 差（须预写死板脚本） | 强（LLM 自动理解同义词与模糊表述，组合工具链） |

## 结论
App Intents 是 Apple Intelligence 接入真实软件世界的「官方桥梁」。开发者无需为 AI 重写应用，只要把数据实体与核心操作按规范注册为 App Intents，应用就自动具备被全局 AI 调度的能力。

## 深化补充（2026-08，WWDC26 后）

### 一句话心智模型
苹果的路线不是「让 AI 学会用你的 App」，而是**「让你的 App 说 AI 已经会的那门语言」**。App Schema 就是这门共同语言——所以 Siri 不需要针对某个 App 训练，也所以你只要不对齐 Schema，就永远进不了这套体系。

### 一个反直觉的机制：确认与否，看「影响谁」而不是「危不危险」
WWDC26 Session 343 里最值得记的一条（官方视频已核实）：

> **Siri 默认假定你的实体是「用户私人的」，因而可能跳过确认。** 只有当实体 conform 新的 `OwnershipProvidingEntity` 协议、把 `EntityOwnership` 声明为 `.shared` / `.public` 后，Siri 才会倾向于弹确认。

官方举的例子极其清楚：改我自己的私人日程，Siri 可能不问；改「Crew Lunch」这种带参与者的日程，Siri 会问。

- **产品含义**：Apple 把确认的触发判据定在了「**这条数据的副作用会外溢给谁**」，而不是传统的「动作是不是不可逆」。这是我之前没想到的一个维度。
- **顺带的代价**：开发者必须**实时维护 ownership 状态**（系统每次取实体时都要求是最新的）。声明错了，要么骚扰用户，要么静默改了别人的东西。

### 与 Android 的路线分歧（这条对做安卓的我最有用）

| | Apple | Android AppFunctions |
|---|---|---|
| 确认由谁做 | **系统级** Confirmation UI，据 entity ownership 差异化提示 | **下放给 App 自己实现**——官方指引原文建议开发者「加不止一步确认」 |
| 体验一致性 | 高（全系统一套） | 低（各 App 自觉） |
| App 灵活度 | 低 | 高 |
| 可审计性 | 强 | **靠开发者自觉** |
| 理解在哪跑 | 端侧 + 云端协同 | 官方明示「**system agents may process user queries on the server**」 |

→ 我的判断：Apple 是「安全成本由平台承担」，Android 是「安全成本转嫁给开发者、最终转嫁成用户多点几次」。做安卓侧产品时，**这块空缺就是厂商 ROM 可以补位的地方**。

### 另外两条 2026 的结构性变化
- **System Orchestrator**：跨 App 动作统一由系统编排者路由，**App 之间不直接互相驱动**——刻意为隐私与安全设计。上面案例里的「链式执行」其实全程有个中间人。
- **`EntityCollection`（Session 345）**：把「**解析实体本身是有成本的**」写进了 Schema 设计。Intent 执行前系统会解析每一个实体（调查询、填全属性），批量场景是灾难；改用 `EntityCollection` 只传标识符。→ Intent 设计要区分「需完整实体的语义操作」与「只需 ID 的批量操作」。
- ⚠️ **待核实**：多方报道称重推理由定制版 Google Gemini 承担，Apple 未明确拆分口径；Session 345 演示的「1000 张照片近乎瞬时」原视频未给具体秒数。

### 待解问题
- [ ] 「按影响面决定是否确认」这个判据，能不能搬到安卓？安卓侧没有 entity ownership，**厂商能从哪里推断「这条数据是不是共享的」**——从 App 声明（可伪造）还是从系统侧行为（不全）？
- [ ] Apple 把私有界面内容默认不开放、必须显式 opt-in。这条边界在国内安卓生态里会不会反而成为超级 App 拒绝开放的**合法挡箭牌**？
- [ ] 上面那张「相比模拟点击的优势」表写于 GUI 能力弱的年代。2026 年 GUI 侧 OSWorld 已到 90% 量级（媒体口径，见 [[OSWorld 计算机操作基准]]），这张表的「可靠性/泛化」两行**是不是该改口径了**？

## 关联
- App Intent 的基础概念见 [[App Intent 的核心作用]]
- 底层支撑架构见 [[App Infra 应用基建]]
- 国内类似能力为何难落地见 [[国内安卓厂商做 App Intent 的阻力]]
- WWDC26 API 级细节深读 → [[Apple AppIntents Schema Protocol 2026]]
- 确认机制四平台对照 → [[Confirmation UI 安全机制]]
- 系统编排者 → [[System Orchestrator 系统编排]] ｜ 语义路由 → [[Intent Router 语义路由]]
- 安卓侧对照 → [[Android AppFunctions 设备侧意图 2026]]

#标签/AppleIntelligence #标签/AppIntent
