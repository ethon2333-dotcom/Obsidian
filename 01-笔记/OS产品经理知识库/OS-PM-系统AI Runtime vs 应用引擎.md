---
tags: [product, pm, os, 端侧AI, ai-runtime, 架构边界, 知识库]
aliases: ["系统 AI Runtime", "App 推理引擎边界", "Android/Apple AI 框架"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：系统级 AI Runtime 与应用级推理引擎的分工与边界

> [!note] 笔记定位
> 为什么 OS 厂商（Android AICore、Apple Foundation / Apple Intelligence、HarmonyOS NPU 调度框架）要死磕自研 **System AI Runtime**，而不让 App 各自集成推理引擎（如 ONNX Runtime / llama.cpp / MNN）？本篇讲清边界与 4 大护城河。

## 一、核心区别一句话
- **App 推理引擎（MNN / llama.cpp）**：目标 = 单 App 在自己进程内把模型跑起来，不管全局。
- **System AI Runtime（NNAPI / Core ML / CANN）**：目标 = **跨 App、跨硬件、跨场景的全局资源仲裁与系统级能力封装**。

## 二、为什么不能让 App 自己搞（4 大护城河）

### 1. 硬件异构与驱动碎片
- 端侧芯片极复杂：NPU（多代）、GPU、CPU、DSP/ISP 各家不一
- App 自集成要为每种 SoC 单独适配，不现实
- Runtime 统一抽象 HAL：App 只写一次，Runtime 在底层映射到高通/联发科/海思 NPU 指令集

### 2. 全局资源仲裁（最核心）
若多个 App 同时拉起 NPU 模型会直接 OOM/Crash，必须全局仲裁者。
- NPU QoS 分级：相机/AR(P0 Real-time) > 主动 AI 对话(P1) > 静默语义抽取(P2)
- 跨 App KV 缓存共享：System Prompt 的 KV 常驻共享页表，所有 App 复用，内存↓60%
- 内存压力联动：临近 OOM 由 Runtime 统一驱逐冷 KV Block，而非各 App 抢资源

### 3. 安全与隐私沙盒
- App 沙盒内模型数据可读性差，云控策略更新滞后
- Runtime 在 TEE / 安全世界加载权重、做 AI 鉴权，防权重被逆向、防 Prompt 注入越权调系统能力
- 系统级权限网关：AI Agent 调「发微信」须 Runtime 鉴权，App 自引擎易越权

### 4. 系统级特性（App 做不到）
| 能力 | App 推理引擎 | System AI Runtime |
| --- | --- | --- |
| Cocktail/混合调度 | ❌ | ✅ NPU+GPU+CPU 协同切分算子 |
| 跨 App Context Engine | ❌ | ✅ 屏幕OCR/剪切板/位置融合 |
| SpecDec 动态降级 | ❌ | ✅ 温控/电量/内存三维触发 |
| 低功耗常驻唤醒 | ❌ | ✅ 订阅 Display/传感器事件低开销触发 |
| OTA 模型热更 | ❌ | ✅ 系统级权重下发（不更 App） |

## 三、两者如何共存（现代 AI-Native OS 范式）
```text
[应用层: 字节/微信/笔记App]  ──调──> [AIDL/IPC] ──> [系统 AI Runtime]
[系统服务: 全局搜索/智慧助手] ─────────────────────> [系统 AI Runtime]
                                              └─> NNAPI/Core ML/CANN ─> 驱动 ─> NPU
```

### PM 决策建议
1. **全局、常驻、跨 App 的系统 AI 能力** → 必须进 System AI Runtime
2. **单 App 内、私有、强性能敏感的特殊模型**（如美图自研分割） → 可 App 自集成，但需向 Runtime 申请 NPU 算力配额
3. **标准开放能力**（OCR/翻译/语音） → Runtime 暴露标准 API，App 免集成

> [!tip] 关联
> Runtime 内部如何做 SpecDec 动态降级 → [[OS-PM-AI Runtime动态调度与降级策略]]
> NPU QoS 分级的冲突场景 → [[OS-PM-端侧大模型系统级挑战]]
> 跨 App KV 共享的实现机制 → [[OS-PM-PagedAttention与KV Cache剪枝]]
