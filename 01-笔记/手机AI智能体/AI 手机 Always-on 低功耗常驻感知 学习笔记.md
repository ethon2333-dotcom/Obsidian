---
title: AI 手机 Always-on 低功耗常驻感知 学习笔记
tags: [手机AI智能体, 端侧, 功耗, 感知, 常驻, 情境]
created: 2026-10-11
source: "WebSearch 核实：Sensing Hub / always-on perception / ambient computing 2025-2026"
---

> 心智模型：**Always-on 常驻感知** = 在手机"睡着"时仍有一块极低功耗的专用硅（Sensing Hub / NPU / DSP）在后台持续监听世界，把原始传感器流压缩成"上下文状态"，只在真正需要时唤醒主芯片——它是 Agent 从"被动应答"走向"主动在场"的物理底座。

## 一、定义（广度扫盲）

| 概念 | 含义 | 关键区别 |
| --- | --- | --- |
| Always-on perception | 设备在不唤醒主 AP（应用处理器）的前提下，持续处理传感信号 | 强调"持续"而非"事件触发" |
| Sensing Hub | 芯片内独立低功耗子系统，聚合麦克风/IMU/光感/超低分辨率摄像头 | 专用硅，与主 NPU/GPU 隔离 |
| Ambient computing | "环境计算"——设备隐于背景、按需感知与回应 | 体验层概念，常驻感知是其硬件前提 |
| Personal context model | 由常驻感知累积出的"用户/环境状态"持久模型 | 由感知结果喂养，区别于原始传感 |

与 [[AI 手机的情境感知与传感器融合 学习笔记]] 的关系：本篇聚焦"**常驻/不唤醒**"这一运行范式与硬件分层；融合机制（IMU+光感+麦克风怎么算成情境）那是那篇的主场，本篇不展开。与 [[端侧 AI 功耗与散热约束 学习笔记]] 的关系：那篇讲总功耗/散热预算，本篇讲"如何把感知这一项的常驻功耗压到可忽略"。

## 二、分类（按感知通道）

| 通道 | 典型常驻任务 | 代表硬件 |
| --- | --- | --- |
| Always-on audio | 唤醒词、语音活动检测（VAD）、关键词/说话人存在 | DSP + micro-NPU，功耗毫瓦级 |
| Always-on visual | 超低分辨率存在检测、人脸是否在场、肩部偷窥检测 | 低分辨率摄像头 + Sensing Hub |
| Sensor-fusion context | 活动识别（走/坐/睡）、设备姿态、环境光/位置 | IMU/光感/GPS 常驻聚合 |
| Cross-modal ambient | 音频+视觉+传感融合出"环境语义"（如附近是否有人） | 多源汇入 Sensing Hub |

## 三、主流方案（横向对比）

| 厂商 | 方案 | 常驻层级 | 已核实要点 |
| --- | --- | --- | --- |
| Qualcomm | Sensing Hub（骁龙） | 双 micro-NPU 独立子系统 | 2026 新一代：性能 +85%、功耗 -20%；可本地跑最高 ~2 亿参数小模型、不唤醒主 AP |
| Apple | Neural Engine + Always-On 显示/协处理器 | ANE 后台常驻 + AoD | A19(2025) GPU 内置 Neural Accelerators；A20 Pro(2026, 2nm, 32 神经核)；后台持续 AI 已成新耗电项 |
| MediaTek | APU / Dimensity Agentic AI Engine (DAE) | NPU 890（第 8 代 APU） | 天玑 9400 主打 agentic AI、端侧 LoRA 训练；低功耗 AI 调度由 APU 承担（常驻传感表述较弱，待核实） |
| Samsung | NPU + 前摄 always-on 感知 | 主 NPU 驱动常驻视觉 | Galaxy S26 "AI Privacy Shield" 用前摄+NPU 检测偷窥（来源偏弱，待核实） |
| Google | Tensor + Titan M + Gemini Nano | Tensor G6(2026) + 端侧 Nano | Pixel 相机转向"AI 感知平台"，相机流常驻本地理解 |

## 四、2025-2026 进展（时间线广度）

| 时间 | 事件 | 备注 |
| --- | --- | --- |
| 2025 | Apple A19 引入 GPU 内 Neural Accelerators；Apple Intelligence 后台常驻化 | 持续性后台 AI 成为新耗电类目 |
| 2026-09 | 高通骁龙峰会：第六代骁龙 8 至尊版 + 新一代 Sensing Hub（双 micro-NPU） | Personal Scribe 功能：本地索引对话、构建个人知识图谱 |
| 2026-09 | 高通发布 Sensing Hub 集成**超低分辨率感知摄像头**：检测"是否有人/人脸在场"，刻意无法识别身份，分辨率远低于 FHD | 隐私优先设计；面向持续低功耗环境感知 |
| 2026 | Pixel 11 / Tensor G6：更激进端侧 AI，相机即"常驻感知平台"，主动 ambient 推荐 | 分析师报告（Moor Insights） |
| 2026 | Samsung Galaxy S26 AI Privacy Shield（前摄 always-on 检测肩部偷窥） | 媒体源偏弱，标待核实 |

## 五、代表产品 / 平台

- **Qualcomm Sensing Hub + Personal Scribe**：把"常驻感知 → 个人知识图谱 → Agent 主动建议"串成闭环，是当下最完整的常驻感知叙事。
- **Apple Always-On Display + on-device ANE**：AoD 本身就是"屏幕常驻低功耗"的成熟范式，ANE 后台处理通知/摘要，是常驻感知的体验先例。
- **Google Pixel ambient / Camera-as-sensing**：相机从"拍照"转向"持续理解世界流"。
- **可穿戴延伸**：带摄像头 AirPods（代号 B790，~1MP）、AI 眼镜——常驻感知从手机外溢到贴身设备（见 [[AI 眼镜与可穿戴意图入口 学习笔记]]）。

## 六、核心张力（本篇主线）

- **持久性 vs 电池**：常驻越久、上下文越丰富，但毫瓦级累积也是真实耗电（Apple M5 iPad Pro 案例已显现）。
- **感知 vs 隐私**：always-listening / always-watching 天然引发信任问题。高通"超低分辨率+不识别身份"、Android 相机/麦克风访问指示灯、Pixel 本地处理优先，都是缓解手段。
- **唤醒策略**：何时该"叫醒"主芯片？这是常驻感知与 [[时序事件驱动与 Agent 主动服务 学习笔记]] 的交界——本篇只铺硬件/范式，触发逻辑留给那篇。

## 七、与已有笔记的衔接

- 融合算法 → [[AI 手机的情境感知与传感器融合 学习笔记]]
- 功耗/散热总账 → [[端侧 AI 功耗与散热约束 学习笔记]]
- 事件触发 → [[时序事件驱动与 Agent 主动服务 学习笔记]]
- 端侧视觉理解 → [[端侧多模态 VLM 学习笔记]]
- 贴身入口外溢 → [[AI 眼镜与可穿戴意图入口 学习笔记]]

# 深度盲区（待 Ethon 补充）

- [ ] Qualcomm 双 micro-NPU Sensing Hub 的**实测常驻功耗（毫瓦）**与唤醒延迟具体数值？
- [ ] Apple 是否有独立于 ANE 的"always-on 协处理器"层级，还是纯靠 ANE 后台调度？
- [ ] MediaTek APU 在"不唤醒主 AP"的常驻感知上，与高通 Sensing Hub 的架构差异？
- [ ] Android 隐私指示灯对 always-on 摄像头/麦克风的法律与 UX 约束边界？
- [ ] 常驻感知的"上下文状态"如何与端侧记忆/知识图谱（[[个性化与端侧用户记忆 学习笔记]]）对接？
- [ ] 超低分辨率感知摄像头的误检率（有人/无人）实测？

# 附：来源清单（2026-10-11）

1. 高通 2026 骁龙峰会 Sensing Hub / 超低分辨率感知摄像头 —— CNMO、IT之家、Converge Digest、新浪财经（高通官方披露）
2. Apple Neural Engine / A19 / A20 Pro 路线 —— Silicon Update、Apple Wiki（粉丝维基，参数待官方核对）
3. MediaTek Dimensity 9400 / NPU 890 / DAE —— MediaTek 官网
4. Google Pixel 11 / Tensor G6 ambient 转向 —— Moor Insights & Strategy（分析师报告）
5. Samsung Galaxy S26 AI Privacy Shield —— 多家媒体（偏弱，见待核实）

# ⚠️ 待核实清单

- [ ] MediaTek APU 是否明确具备"独立常驻传感子系统"（还是仅低功耗 AI 调度）？
- [ ] Samsung Galaxy S26 "Flex Magic Pixel / AI Privacy Shield" 产品真实性、上市时间、NPU 常驻功耗（来源为 newsvot/techsathi 等媒体，非官方）。
- [ ] Pixel 相机"always-on AI sensing platform"具体落地版本与本地处理占比（部分来自 thearabianpost 行业简报）。
- [ ] Apple A20 Pro 32 神经核 / 2nm 参数（来自粉丝维基，需官方规格书核对）。
- [ ] 高通"~2 亿参数本地小模型"在 Sensing Hub 上的具体模型规格与帧率。

#标签/手机AI智能体/端侧/常驻感知
