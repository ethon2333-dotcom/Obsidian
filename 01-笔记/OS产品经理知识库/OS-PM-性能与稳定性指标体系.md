---
tags: [product, pm, os, 性能指标, 稳定性, 埋点, 知识库]
aliases: ["OS 性能指标", "ANR Crash PSS", "性能诊断"]
source: "Gemini 对话导出 (gemini-code-1785420276458.txt)"
created: 2026-07-30
---

# 📑 OS 产品经理：性能与稳定性指标体系及诊断逻辑

> [!note] 笔记定位
> App PM 关注单 App 业务转化；OS PM 必须掌控**全局资源健康度**。性能与稳定性是系统「基建」，决定用户对 OS 流畅度的直观感知。

## 模块一：核心指标详解

### 1. 流畅度与帧率
- **VSYNC 驱动**：60Hz 单帧窗口 16.6ms；120Hz 仅 8.3ms。超窗口未完成即**丢帧 Jank**。
- **FPS**：基本指标，但单独看无法评估微小卡顿。
- **丢帧率 Jank Rate**：
  - Slow Frame：渲染 > 单 VSYNC 周期（如 >16.6ms）的帧占比
  - Frozen Frame：渲染 > **700ms** 的严重卡顿（用户感到死机）
- **触控响应时延 Touch-to-Response**：硬件中断到首帧渲染。优秀 OS 控制在 **30~50ms**。

### 2. 启动与切换时延
- **冷启动 Cold Start**：进程不在内存，点击到首帧。系统应用标准 **1~1.5s**（含 TTID）。
- **热启动 Warm/Hot**：进程在内存，恢复状态。通常 **< 500ms**。
- **窗口转场时延 Window Transition**：触发跳转到动画播完可响应触控。

### 3. 系统稳定性（红线）
```text
崩溃/卡死分类
 ├── App Crash（Java/Native 未捕获异常）
 ├── System UI Crash（桌面黑屏/闪烁）
 ├── Kernel Panic / Watchdog Dump（内核崩溃/重启）
 └── ANR（主线程阻塞）
```
- **Crash 率**：UV Crash 率 = 崩溃用户数 / DAU，行业要求 **< 0.1%~0.5%**。
- **ANR 触发阈值**：
  - Input 5s 未响应 / 前台 Service 20s / 后台 200s
  - BroadcastReceiver 前台 10s / 后台 60s
  - **User-Perceived ANR Rate** 官方警告阈值 **0.47%**（Google Play）。

### 4. 资源与内存消耗
- **PSS（Proportional Set Size）**：**OS PM 看内存最核心指标**（独占 + 按比例平摊共享）。
- **Base RAM**：开机无任何三方 App 的基础占用。
- **LMK 触发频率**：频繁杀后台 = 保活率差。
- **功耗/热**：Excessive Partial WakeLock（异常锁 CPU）、Thermal Throttling 热降频触发率（阈值 ~45~50°C）。

## 模块二：埋点与日志采集（低开销 / 无侵入 / 隐私优先）
```text
操作 ─> 框架/内核 Hook ─> 环形缓冲区 Ring Buffer
                ├─> [常态指标] 低频聚合: 平均FPS/PSS峰值 → 夜间WiFi充电批量上报
                └─> [异常事件] 高精度Trace: 丢帧>700ms/ANR/Crash → 即锁Ring Buffer导出堆栈
```
- **UI 卡顿监控**：Choreographer 帧监听，间隔 > 16.6ms×N 即算丢帧 N。
- **ANR 监控**：Looper 消息队列前后打点，单条 > 2s 抓主线程堆栈。
- **内存监控**：订阅 `proc/meminfo` 与 `lmkd` 事件。
- **分层上报**：常态只记统计值（WiFi+充电批量）；异常才固化导出 Systrace/Perfetto。

## 模块三：诊断三步法（收到「桌面滑动卡顿」类需求）
```text
[发现问题] → Step1 归因: 单App自身问题 or 系统级资源争抢
          → Step2 抓 Trace: MainThread阻塞? RenderThread延迟? CPU被抢占?
          → Step3 定位: 锁争抢→异步回调 / 内存瓶颈→调ZRAM / 硬件降频→调温控
```

### 核心诊断工具
- **Perfetto / Systrace**：CPU 调度、线程状态、VSync 同线展开。主线程处于 **Runnable** = CPU Bound；**D 态(Uninterruptible Sleep)** = I/O Bound。
- **Heap Dump / Page Fault**：高 GC 伴随卡顿 → 查内存泄露 / Page In-Out 频繁。
- **Batterystats / Bugreport**：查熄屏下谁在频繁 Alarm 唤醒或持 WakeLock。

> [!tip] 关联
> 端侧 LLM 会直接恶化上述多项指标（内存膨胀、NPU 长占、热降频），详见 [[OS-PM-端侧大模型系统级挑战]]。
