# App Infra 应用基建

> 如果 App Intent 是应用暴露给外界的「标准门窗与对讲机」，App Infra（应用基建）就是支撑整栋大楼的「地基、钢筋骨架、水电管网和电梯系统」。

## 定义
App Infra 指独立于具体业务功能（购物车、聊天界面）之外的**底层技术架构、公共组件、工程流水线和性能治理体系**。用户感知不到它的存在，但 App 的流畅度、稳定性、开发效率、能否支持 AI 升级，完全取决于它的硬实力。

## 4 大核心支柱

### 1. 架构解耦与组件化（Componentization & Routing）
- **痛点**：几百人同工程写代码，容易冲突、改动 A 导致 B 崩溃。
- **解法**：搭建组件化架构与路由系统（Router）。将支付、社交、直播解耦成独立模块，模块间通过 Infra 路由协议通信。各业务团队独立开发、测试、编译。

### 2. 性能与稳定性治理（APM & Quality）
- **痛点**：内存泄漏、闪退（Crash）、滑动卡顿（掉帧）、冷启动数秒，直接流失用户。
- **解法**：建立应用性能监控（APM）体系：
  - 启动优化：控制主线程任务，并发 + 懒加载实现秒开。
  - 网络治理：弱网优化长短连接，引入 QUIC/HTTP3 协议与智能重试。
  - 存储引擎：高性能本地读写中间件（MMKV、SQLite 优化引擎）。

### 3. 工程效能与动态化（DevOps & Dynamic Infrastructure）
- **痛点**：原生发布需过商店审核，周期长，发版后无法立刻修紧急 Bug。
- **解法**：CI/CD 自动化打包流水线；热修复（Hotfix）与动态化容器（Flutter / RN 底层打包渲染容器、WebView 强化容器），免商店更新实时下发页面与修复 Bug。

### 4. 基础安全与合规（Security & Compliance）
- **痛点**：代码被逆向解包、数据被劫持、通信被监听、隐私权限调用不合规被下架。
- **解法**：统一封装代码混淆、加壳、防钓鱼检测、敏感数据加密存储，统一管理摄像头 / 定位等隐私权限调用审计。

## AI 与 App Intent 时代的演进

| 传统 App Infra | AI 时代的 App Infra |
|------|------|
| UI 路由与组件化 | Intent 自动化注册与映射 |
| 网络 / 存储中间件 | 端侧 AI 运行时（CoreML） |
| 性能监控（APM） | 本地向量数据库（RAG） |
| 渲染容器（Web / Flutter） | 上下文与隐私沙盒治理 |

### Intent 自动注册框架（降低业务开发成本）
要求业务程序员为每个功能手动写大量 App Intent 胶水代码，落地阻力极大。App Infra 设计**编译期注解（Annotation Processor）与代码生成工具**，业务开发只需在方法上加标记，Infra 自动生成符合 Apple / Google 规范的 App Intent。

### 端侧 AI 运行时基建（On-Device AI Infra）
App Infra 负责集成并优化端侧推理引擎（CoreML、ONNX Runtime、ncnn），处理 NPU/GPU 硬件加速调度、模型量化压缩、内存占用控制。

### 端侧向量数据库与内存库（Local RAG）
为给 AI 提供精准的 App 内部上下文（历史收藏、偏好设置），App Infra 引入端侧向量数据库和高效本地语义索引，配合 AI Agent 实现低延迟端侧检索。

## 一句话
App Intent 定义 App 的「对外接口」，App Infra 决定 App 的「底层底盘」。没有坚固的 App Infra，应用无法承受高效开发节奏，也无法流畅响应 AI 时代高频、自动化的工具调用需求。

## 关联
- App Intent 的基础概念见 [[App Intent 的核心作用]]
- 苹果如何结合二者见 [[Apple Intelligence 与 App Intents]]
- 国内厂商落地阻力见 [[国内安卓厂商做 App Intent 的阻力]]

#标签/AppInfra #标签/架构
