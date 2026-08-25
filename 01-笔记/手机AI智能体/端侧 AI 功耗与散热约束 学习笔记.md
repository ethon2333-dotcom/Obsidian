---
title: "端侧 AI 功耗与散热约束"
tags: [广度种子, 端侧AI, 功耗散热]
created: 2026-08-17
source: "WebSearch/WebFetch 联网核实 + 公开资料综述"
---

端侧 AI 功耗与散热约束，本质是「手机无风扇的被动散热 + 固定电池容量」给 AI 算力套上的一只隐形天花板——峰值性能只是纸面数字，稳态（sustained）热平衡下的可用算力才是产品真实的性能墙。

## 一、心智模型与核心概念

端侧 AI 的功耗/热约束是一条「预算链」：电池给整机一个总功率包（mW/mAh），SoC 各 IP（CPU/GPU/NPU/DRAM）共享；AI 推理一旦持续，温度爬升触发 DVFS 降频乃至 Thermal Throttling 硬限频，可用算力随之塌缩。

| 术语 | 定义（点到为止） | 对端侧 AI 的含义 |
|---|---|---|
| 功耗预算 Power Budget | 整机/单 IP 可分配的稳态功率（如手机 SoC 约数 W） | 决定能跑多大模型、跑多久 |
| TDP / 热设计功耗 | 散热系统能长期散掉的热功率 | 手机无风扇，被动散热，TDP 极低 |
| Thermal Throttle | 温度超阈值后系统强制降频/关核 | 持续推理的「性能墙」根源 |
| Sustained vs Peak | 稳态性能 vs 瞬时峰值 | 跑分峰值常虚高 1.5–2× |
| DVFS | 动态电压频率调整，温控第一道防线 | 渐进降频，粒度到各 IP 块 |
| TOPS/W | 每瓦算力，能效比核心指标 | NPU 竞赛主战场 |
| Always-on 预算 | 常驻感知的 μW/mW 级功耗 | 决定能否「永远在线」 |

## 二、主流移动 NPU 与能效（2025–2026 旗舰）

| 厂商/单元 | 代表平台 | 制程 | 算力(INT8) | 能效备注 |
|---|---|---|---|---|
| Apple Neural Engine | A19 Pro / M5 系列 | 台积电 N3E | 待核实（媒体称 A19 Pro GPU 神经加速器约 3× A18 Pro） | 软硬件协同，常年高能效标杆 |
| 高通 Hexagon NPU | 第五代骁龙 8 至尊版 / 骁龙 X2 | N3E / N3P | 待核实（45–80 TOPS 口径冲突，见文末） | 较前代能效 +16%，传感器中枢功耗 -33% |
| MediaTek APU | 天玑 9500（双 NPU） | N3E | 待核实 | 主打「强而不热、久战不衰」超低功耗常驻感知 |
| ARM Ethos-U | Ethos-U55/U85（MCU 级） | — | 低至数百 GOPS | 面向 IoT/可穿戴 Always-on 微推理 |

> 注：移动 NPU 的 TOPS/W 横向数值各媒体/test 口径差异极大，本笔记**不列具体 TOPS/W 数字**，统一标「待核实」，避免编造。

## 三、端侧推理功耗画像（实测参考，来源混杂需甄别）

| 设备/平台 | 负载 | 平均功耗 | 备注 |
|---|---|---|---|
| 骁龙 8 Gen3 手机 | 3B INT4 量化，持续推理 | ~4.5W | GPU/NPU 占功耗 >50% |
| 苹果 A18 Pro | 同档 7B 级本地推理 | ~3.2W | 能效优于同期安卓旗舰（媒体实测） |
| Pixel 8 Pro | 持续推理 ~4 min | 触发 GPU_MITIGATION | 48°C 时 GPU 900→315MHz，延迟 130→410ms |
| 智能眼镜/可穿戴 | Always-on 感知 | 1–3W（Tier1）；μW 级待机（如 AON1120 待机 80μW） | 分级唤醒是关键架构 |

**关键现象**：同一模型室温短跑延迟 85ms，连续推理 5 min 后爬到 220ms（性能退化 ~158%），**几乎全因温控降频**——这是端侧 AI 与云端最本质的区别。

## 四、模型层 & OS 层 能效优化手段

| 层级 | 手段 | 作用（点到为止） |
|---|---|---|
| 模型层 | 量化(INT8/INT4/INT2)、稀疏化、Early-exit 早退出、轻量化 SLM | 直接降「发热密度」，温控严格设备上 INT8 稳态常优于 FP16 |
| 编译层 | 算子融合、KV Cache、NPU delegate | 减少数据搬运，见 [[端侧模型量化 学习笔记]] |
| OS/调度层 | DVFS 档位（ML_INFERENCE_LOW_LATENCY 等，Android 14 引入）、Thermal API 监听、温控感知负载降级 | 温度恶化前主动降负载，呼应 [[OS-PM-AI Runtime动态调度与降级策略]] |
| 硬件层 | 3nm/4nm 制程、异构计算、存算一体（前沿） | 制程每代降漏电与动态功耗 |

## 五、2025–2026 进展 & 关键玩家

| 趋势 | 代表事件/玩家 | 状态 |
|---|---|---|
| 端侧大模型功耗压力 | 7B/8B 本地常驻推理成旗舰标配 | 已规模落地 |
| Always-on 感知 | 高通传感器中枢、Synaptics AS370、隼瞻「智翼」25mW 人脸侦测 | 量产导入 |
| Apple Intelligence 散热反馈 | iOS 18.2 Image Playground 发热投诉；iPhone 17 Pro 首引入 VC 均热板 | 媒体口径，待核实 |
| NPU TOPS/W 竞赛 | 高通/联发科/苹果/ARM 制程与架构军备赛 | 持续 |
| 中国芯入局 | 小米玄戒 O1（3nm）、华为麒麟 9030、天玑 9500 | 2025 节点性事件 |

## 六、对 OS PM 的意义（Android 语境）

1. **功能设计受功耗墙约束**：「全程本地大模型 + 持续多模态」不可无脑堆，需定义「可接受的稳态延迟/续航」而非峰值体验。
2. **降级策略是产品必选项**：高温时主动从 GPU+FP16 切 CPU+INT8、插帧间散热窗口（见 [[OS-PM-AI Runtime动态调度与降级策略]]），比硬扛降频体验好得多。
3. **指标要重 sustained 而非 peak**：把温控测试写进 CI，监控真实频率而非只看延迟（呼应 [[OS-PM-性能与稳定性指标体系]]）。
4. **Always-on 是独立预算线**：常驻感知应走 μW/mW 级 Sensor Hub，而非唤醒大 NPU，否则续航崩。
5. **散热设计成为差异化**：VC 均热板等硬件红利需 OS 调度配合才能释放。

## 七、待解问题（留白给 Ethon）

- [ ] 主流旗舰 SoC 的 NPU **实测 TOPS/W** 横向榜单应以哪个口径为准？
- [ ] 端侧 7B 模型「可持续推理时长」与电池容量/SOC 温度的定量关系？
- [ ] Android Thermal HAL 各厂商（小米/三星/OPPO）阈值与降级策略差异？
- [ ] Always-on 感知的「误唤醒率 vs 功耗」最优平衡点？
- [ ] Early-exit 在端侧 LLM 解码阶段的实际能效收益？
- [ ] 3nm→2nm 制程对端侧 AI 稳态功耗的边际改善幅度？
- [ ] Apple Intelligence 散热反馈是否真实影响了其 OS 层调度策略？
- [ ] 折叠屏/大屏设备的散热面积红利如何映射到 AI 续航？

## 附：来源清单

| 标题 | URL | 性质 |
|---|---|---|
| Android On-device AI Power and Thermal Management | https://xckevin.com/en/blog/android-on-device-ai-power-thermal-management | 社区/技术博客 |
| 深入 Android 端侧 AI 推理的功耗与热管理全链路 | https://xckevin.com/blog/2025-11-21-... | 社区/技术博客 |
| 04_端侧智能推理优化与加速技术 | https://blog.csdn.net/wayle123/article/details/159648357 | 社区/技术博客 |
| Every AI PC NPU. Ranked. | https://aipc.computer/leaderboard | 媒体/榜单 |
| 快科技2025年度评奖:手机SoC篇 | https://new.qq.com/rain/a/20251230A06GT100 | 媒体 |
| iPhone is too hot when using Apple Intelligence on iOS 18.2 | https://cartier.io.vn/... | 媒体/社区 |
| Always-On AI Glasses: A Practitioner's Guide | https://sivaro.in/articles/always-on-ai-glasses-a-practitioners-guide-to-building | 社区/实践 |
| LLM Inference at the Edge (sustained load) | https://www.pith.science/paper/2603.23640 | 论文(综述) |
| 骁龙8至尊版 MWC 2025 获奖 | https://news.mydrivers.com/1/1034/1034317.htm | 媒体 |

## ⚠️ 待核实清单

- 高通 Hexagon NPU 算力口径冲突：骁龙 8 至尊版/第五代平台，不同来源称 45 / 73 / 75 / 80 TOPS，**具体以哪代、哪款为准待核实**，本文未采用具体值。
- Apple A19 Pro「GPU 神经加速器达 A18 Pro 3 倍」为媒体表述，**官方口径未直接确认**，标传闻/媒体口径。
- iPhone 17 Pro 引入 VC 均热板及「温度 43℃ 限制 CPU 至 50%」来自媒体评测，**工程阈值待核实**。
- 端侧 LLM 各设备「平均功耗 3.2–4.5W」来自不同社区实测，**测试条件（模型/量化/温度）不一致，仅作量级参考**。
- 「手机总热预算约 5W」出自第三方博主估算，**非官方数据，待核实**。

#标签/端侧AI/功耗散热
