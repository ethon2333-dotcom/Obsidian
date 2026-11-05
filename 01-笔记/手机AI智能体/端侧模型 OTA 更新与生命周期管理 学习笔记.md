---
title: 端侧模型 OTA 更新与生命周期管理 学习笔记
tags: [手机AI智能体, 端侧AI, 模型生命周期, OTA, 模型下发, 模型注册表]
created: 2026-10-05
source: 厂商文档 + 媒体/博客 + 开发者论坛（混合来源，见文末来源清单）
---

> 心智模型：端侧模型不是「烧录一次就完事」的固件，而是像 App 一样需要「灰度下发 → 监控 → AB → 回滚 → 增量续命」的可运营资产；OTA 就是端侧 AI 的 CI/CD 管道。

## 广度覆盖

### ① 定义
- **端侧模型 OTA 更新**：通过无线（Wi-Fi / 蜂窝 / BLE）把新版本模型（权重、adapter、配置）安全推送到海量设备，替代「出厂即冻结」的传统 TinyML 模式。
- **生命周期管理**：覆盖「训练产出 → 注册表登记 → 灰度/AB 下发 → 设备侧 fleet 监控 → 回滚/退役」的端到端治理，是 MLOps/LLMOps 在 edge 侧的延伸。
- 与纯固件 OTA（FOTA）的区别：模型更新常常只需换权重/adapter，**架构不变即可差分**；架构变了才需要整包/全量更新（风险更高）。

### ② 分类 / 范式
| 范式 | 一句话 | 关键机制 |
| --- | --- | --- |
| 灰度 / 分段发布（Staged / Canary） | 先小批再放量 | device cohorts、按机型/地区/百分比放量 |
| A/B 测试 | 端上比新旧模型效果 | A/B 双分区、指标分流、在线评估 |
| 回滚（Rollback） | 翻车能退回稳定版 | A/B slot、双分区、保留上一版本 |
| 增量 / 差分更新（Delta） | 只传变化的权重 | bsdiff/xdelta/vcdiff、分层 base+adapter、省 70–90% 流量（厂商外资料口径，待核实） |
| 模型注册表（Model Registry） | 模型版本的「单一事实源」 | 版本号/血缘/阶段晋升（staging→production）/签名清单 |
| 端云协同下发 | 端侧跑不动的走云，新模型云聚合再下发 | 联邦学习式「仅传梯度」、云端聚合重发 |

### ③ 主流方案（厂商 / 框架）
| 玩家 | 端侧模型更新机制 | 备注 |
| --- | --- | --- |
| **Apple**（Foundation Models / Apple Intelligence） | 设备端 3B 基础模型随 **iOS 系统更新**演进；开发者需用 test set 在每次模型更新时回归 prompt（约半年~一年一次大版本） | 模型与 OS 强绑定，非独立 OTA；见 [[Apple Intelligence 与 App Intents]] |
| **Google**（AICore + ML Kit GenAI） | AICore 是 Android 系统服务，**负责下载与维护 Gemini Nano 版本**，多 App 共享一份模型；I/O 2025 推 **Play for On-Device AI（beta）** 管理自定义模型下载 | 开发者不直接管模型生命周期，由系统服务托管 |
| **华为 / 安卓厂商**（开发者论坛口径） | 增量更新 / 模型热修复 / LoRA adapter 下发；联邦学习「数据不出端、仅传梯度」范式 | 论坛讨论为主，官方完整机制待核实 |
| **TinyMLDelta**（社区方案） | TFLite Micro 的差分更新：仅发 patch（67KB 模型变更仅 475 字节），含 ABI/算子集/张量 schema 兼容性校验 + A/B slot + 崩溃安全 journaling | 面向 MCU，对手机端侧有借鉴价值 |
| **边缘 OTA 平台** | Memfault / Mender / BalenaOS：A/B 分区、可恢复下载、双分区回退、fleet telemetry | IoT/嵌入式成熟栈，手机可参考 |

### ④ 2025–2026 进展（点到为止）
- **差分更新成为共识**：binary diff（bsdiff/xdelta/vcdiff）+ 分层架构（稳定 base + 小 adapter 常更）+ 内容寻址 + 签名清单（manifest 驱动）成为边缘 AI 更新的标准工程范式。
- **分层 / adapter 化**：把更新面收敛到「小且可认证的 adapter」，减少带宽（2025 某 on-device 助手 pilot：40MB 模型 + 2–5MB delta adapter，待核实）。
- **安全与合规驱动**：EU《网络韧性法案》（CRA）、美国 Cyber Trust Mark 把「可远程打补丁」列为强制要求，倒逼 OTA 基础设施上桌。
- **原子化 + 硬件密钥**：下载到临时区 → 校验 hash+签名 → fsync → 原子 rename 替换；用硬件级密钥（密钥证明 attestation）拒绝未授权模型。
- **联邦学习式下发**：边缘本地训、加密上传梯度、云端聚合、再下发新全局模型——把「模型更新」变成「模型进化」（隐私 + 带宽双优）。
- **可观测性**：cache 命中率、更新成功率、签名校验失败、强制回滚次数等指标成为 fleet 健康看板必备。

### ⑤ 代表产品 / 玩家
- OS 厂：Apple（Foundation Models）、Google（AICore / Gemini Nano / Play for On-Device AI）。
- 模型/框架：LiteRT（TFLite）、ExecuTorch、MNN/NCNN（运行时层见 [[端侧推理框架生态 学习笔记]]）；模型产物格式见 [[端侧 AI 模型格式与部署互操作标准 学习笔记]]）。
- OTA/Registry 平台：MLflow、SageMaker / Azure ML Model Registry、Memfault、Mender、K3s 边缘编排。
- 芯片底座约束（存储/算力预算）见 [[端侧 AI 芯片架构谱系 学习笔记]]；已落地内建 AI 功能分布见 [[操作系统原生 AI 功能图谱 学习笔记]]。

## 深度盲区
- [ ] 待解问题：端侧增量更新（权重 diff）合并后是否存在数值精度漂移 / 累积误差？量化模型（INT4/2-bit）做差分更新是否安全？
- [ ] 待解问题：OTA 安全签名方案怎么选——设备端硬件密钥证明（attestation）如何与 android 厂商私钥体系协同，防篡改/防降级（rollback protection）？
- [ ] 待解问题：AB 实验在端侧怎么做——如何在亿级异构设备上对「模型效果」做随机分流与在线指标回收，且不被功耗/网络拖垮？
- [ ] 待解问题：模型版本与 OS 版本解耦到什么程度？Apple 把模型绑 OS、Google 用系统服务托管，安卓厂商自定义模型能否独立 OTA？
- [ ] 待解问题：fleet 监控口径——用什么指标判定「该回滚」（精度掉点 / 功耗激增 / crash 率），阈值谁定？
- [ ] 待解问题：联邦学习下发在手机端的合规与算力边界——本地训练耗电、梯度加密上传的隐私收益是否真能落地？

## 库内关联
- 运行时与更新管道的关系 → [[端侧推理框架生态 学习笔记]]
- 模型产物打包/互操作（影响差分粒度）→ [[端侧 AI 模型格式与部署互操作标准 学习笔记]]
- 芯片存储/算力预算约束 OTA 体积 → [[端侧 AI 芯片架构谱系 学习笔记]]
- 已落地内建 AI 功能的端云分布 → [[操作系统原生 AI 功能图谱 学习笔记]]
- Apple 设备端模型开放给开发者 → [[Apple Intelligence 与 App Intents]]

## 附：来源清单
- Apple 开发者文档 / WWDC25 Foundation Models 框架（onevcat.com 实测，2025-06；apple.com newsroom 2025-06）
- Google I/O 2025「AI on Android」官方博客（goo.gle/4kIjYwf）；iThome 170804（AICore + ML Kit GenAI）；heise.de / winbuzzer 报道
- TinyMLDelta 介绍（yourai.pro，Felix Galindo 的差分更新方案）
- 华为开发者论坛「边缘 AI 模型增量更新」讨论帖（developer.huawei.com，2025-11）
- 边缘缓存 / OTA delta 工程范式（caches.link，2025 pilot 案例）
- OTA 最佳实践：Memfault、Mender、BCloud Consulting（A/B 分区 / Delta / fleet 管理）
- 模型注册表 / edge MLOps：inferensys.com glossary、MLflow / SageMaker / Azure ML 文档、CIS MLOps 2025 综述
- OTA 市场数据：pmarketresearch.com（2025 市场规模，口径待核实）

## ⚠️ 待核实清单
- 「差分更新省 70–90% 带宽」「A/B 分区零停机」等为厂商外媒体/咨询口径，缺一手官方基准，待核实。
- 2025 on-device 助手 pilot 的「40MB 模型 + 2–5MB delta adapter、云调用降 67%」为匿名案例博客，待核实。
- OTA 市场 2025 美元规模 / 份额（pmarketresearch）为商业研究口径，仅作量级参考，待核实。
- 华为/安卓厂商具体端侧模型 OTA 机制以开发者论坛讨论为主，官方完整技术方案与命名未确认，待核实。
- Apple 端侧模型「约半年~一年一次大版本」为开发者实测推断（onevcat），非 Apple 官方节奏承诺，待核实。
- 联邦学习在手机端大规模落地的真实产品案例稀缺，目前多为范式讨论，待核实。

#标签/手机AI智能体/端侧AI/模型生命周期管理
