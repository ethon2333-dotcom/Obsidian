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

## 关联
- App Intent 的基础概念见 [[App Intent 的核心作用]]
- 底层支撑架构见 [[App Infra 应用基建]]
- 国内类似能力为何难落地见 [[国内安卓厂商做 App Intent 的阻力]]

#标签/AppleIntelligence #标签/AppIntent
