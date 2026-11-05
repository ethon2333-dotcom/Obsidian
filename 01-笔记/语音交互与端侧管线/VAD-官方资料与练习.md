# VAD-官方资料与练习

> 纸上谈兵难以理解 VAD 的细微边界。在工程落地中，调优 VAD 的关键在于**掌握流式分块状态传递（Stateful Streaming）**与**双门限时序平滑器**。
> 本篇汇集权威官方源码库，并提供可以直接在端侧 Python / ONNX 运行环境执行的工业级最小流式实操代码。

---

## 一、官方权威资料与开源仓库

| 项目名称 | 官方仓库 / 地址 | 技术栈 | 特点与选型建议 |
| :--- | :--- | :--- | :--- |
| **Silero VAD** | [GitHub: snakers4/silero-vad](https://github.com/snakers4/silero-vad) | PyTorch / ONNX / C++ / WebAssembly | **当前跨平台 SOTA 首选**。体积仅 ~1.5MB，单块处理 512 采样点（32ms），提供官方 ONNX Runtime 跨端绑定与 C++ 纯享版。 |
| **WebRTC Native VAD** | [Chromium WebRTC Audio](https://chromium.googlesource.com/external/webrtc/+/master/common_audio/vad/) | 纯 C 代码 (C89) | Google 工业级基石。零依赖、超低能耗，支持 10/20/30ms 帧，适合裸机 MCU 或极低功耗 Linux 守护进程。 |
| **FunASR FSMN-VAD** | [ModelScope: speech_fsmn_vad](https://www.modelscope.cn/models/iic/speech_fsmn_vad_zh-cn-16k-common-onnx) | Python / ONNX / C++ | 阿里语音团队开源的前馈记忆网络 VAD。擅长中文会议、长音频自动断句切分，配套完整的逆文本处理工具。 |
| **Sherpa-ONNX VAD** | [GitHub: k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | C++ / JNI (Android/iOS) | 新一代 Kaldi 团队封装，开箱即用支持 Android AAR、Flutter，底层直接集成 Silero VAD ONNX。 |

---

## 二、实战练习 1：Silero VAD 流式 ONNX 极轻量推理

在真实端侧系统（如 Android C++ 或 Python 守护进程）中，我们不能依赖庞大的 PyTorch 框架，必须直接使用 **ONNX Runtime** 加载 `silero_vad.onnx`。

> [!IMPORTANT]
> Silero VAD 内部基于 LSTM/GRU，在流式处理音频块时**必须维护内部隐藏状态（State: `h` 和 `c`）并在前后帧之间透传**，否则每一帧都是孤立推断，准确率会断崖式下跌。

```python
import numpy as np
import onnxruntime as ort

class SileroVADStreaming:
    """
    基于 ONNX Runtime 的纯轻量级流式 VAD 引擎
    无 PyTorch 依赖，可直接迁移至嵌入式与移动端环境
    """
    def __init__(self, onnx_model_path: str, sample_rate: int = 16000):
        assert sample_rate in [8000, 16000], "仅支持 8000 或 16000 采样率"
        self.sample_rate = sample_rate
        # 16kHz 下，Silero VAD 每次接收固定 512 个采样点 (32毫秒)
        self.window_size_samples = 512 if sample_rate == 16000 else 256
        
        # 初始化 ONNX 推理引擎
        opts = ort.SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = 1
        self.session = ort.InferenceSession(onnx_model_path, sess_options=opts)
        
        # 重置内部隐状态 (2, 1, 64)
        self.reset_states()

    def reset_states(self):
        """对话结束或重新拾音时，清空 RNN 内部隐状态"""
        self._state = np.zeros((2, 1, 128), dtype=np.float32)

    def process_chunk(self, audio_chunk: np.ndarray) -> float:
        """
        输入: 512 长度的 float32 数组，幅值范围 [-1.0, 1.0]
        输出: 当前 32ms 片段属于有效人声的概率值 (0.0 ~ 1.0)
        """
        if len(audio_chunk) != self.window_size_samples:
            raise ValueError(f"Chunk 大小必须为 {self.window_size_samples} 采样点")

        # 构造模型输入 Tensor: (Batch=1, Samples=512)
        input_data = np.expand_dims(audio_chunk.astype(np.float32), axis=0)
        sr_data = np.array(self.sample_rate, dtype=np.int64)

        ort_inputs = {
            'input': input_data,
            'state': self._state,
            'sr': sr_data
        }
        
        # 前向推理
        out, new_state = self.session.run(None, ort_inputs)
        self._state = new_state # 更新并保留状态供下一帧使用
        
        speech_prob = float(out[0][0])
        return speech_prob

# === 模拟使用示例 ===
if __name__ == "__main__":
    # 假设已下载官方 silero_vad.onnx
    # vad = SileroVADStreaming("silero_vad.onnx", sample_rate=16000)
    # mock_chunk = np.random.uniform(-0.1, 0.1, 512).astype(np.float32)
    # prob = vad.process_chunk(mock_chunk)
    # print(f"当前人声概率: {prob:.4f}")
    pass
```

---

## 三、实战练习 2：端侧双门限时序状态机实现

光有逐帧人声概率不够，必须用状态机聚合出**语音片段的物理起止毫秒时间戳**，并实现 **Pre-speech Padding（防止吞句首）** 与 **Hangover（防止吞句尾）**。

```python
from collections import deque
from typing import List, Dict

class VADStateMachine:
    def __init__(
        self,
        start_threshold: float = 0.5,     # 判定说话的概率门限
        end_threshold: float = 0.35,      # 判定静音回落的门限
        min_speech_duration_ms: int = 250, # 最小有效发音时长（过滤咳嗽噪声）
        hangover_duration_ms: int = 400,  # 尾部静音等待时长（用户说完判定）
        pre_padding_ms: int = 200,        # 句首回溯缓冲补偿时长
        chunk_duration_ms: int = 32       # 每一块的物理时长
    ):
        self.start_threshold = start_threshold
        self.end_threshold = end_threshold
        self.min_speech_frames = min_speech_duration_ms // chunk_duration_ms
        self.hangover_frames = hangover_duration_ms // chunk_duration_ms
        self.pre_padding_frames = pre_padding_ms // chunk_duration_ms
        self.chunk_duration_ms = chunk_duration_ms

        self.state = "SILENCE"  # 状态: SILENCE | SPEECH
        self.current_time_ms = 0
        self.speech_start_ms = 0
        self.silence_counter = 0
        self.speech_counter = 0
        
        # 环形回溯缓冲区，用于向前追溯句首辅音
        self.ring_buffer = deque(maxlen=self.pre_padding_frames)

    def step(self, prob: float, audio_chunk: bytes) -> Dict:
        """
        每 32ms 音频帧调用一次
        返回事件字典: {'event': 'NONE' | 'SPEECH_START' | 'SPEECH_END', ...}
        """
        self.current_time_ms += self.chunk_duration_ms
        self.ring_buffer.append(audio_chunk)
        event = {"event": "NONE", "timestamp_ms": self.current_time_ms}

        if self.state == "SILENCE":
            if prob >= self.start_threshold:
                self.speech_counter += 1
                if self.speech_counter >= 3: # 连续 3 帧确认人声，防止偶发爆音
                    self.state = "SPEECH"
                    self.speech_counter = 0
                    self.silence_counter = 0
                    # 语音起始时间戳往前追溯 Pre-padding 时长
                    self.speech_start_ms = max(0, self.current_time_ms - (self.pre_padding_frames * self.chunk_duration_ms))
                    event = {
                        "event": "SPEECH_START",
                        "start_ms": self.speech_start_ms,
                        "buffered_audio": list(self.ring_buffer) # 附带前置补偿音频送入 ASR
                    }
            else:
                self.speech_counter = 0

        elif self.state == "SPEECH":
            if prob < self.end_threshold:
                self.silence_counter += 1
                if self.silence_counter >= self.hangover_frames:
                    # 持续静音超过 Hangover 阈值，正式切断整句！
                    self.state = "SILENCE"
                    speech_end_ms = self.current_time_ms - (self.hangover_frames * self.chunk_duration_ms)
                    total_duration = speech_end_ms - self.speech_start_ms
                    self.silence_counter = 0

                    if total_duration >= (self.min_speech_frames * self.chunk_duration_ms):
                        event = {
                            "event": "SPEECH_END",
                            "start_ms": self.speech_start_ms,
                            "end_ms": speech_end_ms,
                            "duration_ms": total_duration
                        }
            else:
                # 依然在说话，重置静音计数器
                self.silence_counter = 0

        return event
```

---

## 四、自测练习与调优实验指南

1. **练习任务 1：用真实噪音音频检验虚警率（FAR）**：
   - 录制一段 1 分钟纯打字声与办公室环境底噪（无真人说话）。
   - 将该音频切成 512 点分块，依次喂入上述 VAD 状态机。
   - **验收指标**：输出的 `SPEECH_START` 次数必须为 **0 次**。若有误触发，适当将 `start_threshold` 从 0.5 调高到 0.6，或将起步确认帧数从 3 帧增加到 4 帧。
2. **练习任务 2：轻声与辅音尾音截断检验（吞字测试）**：
   - 录制一段带轻声尾音的语句，例如：“帮我把空调调到二十六度**吧**（最后‘吧’字极轻）”。
   - 观察 `SPEECH_END` 输出的时间戳是否将最后的“吧”字音频完整包裹。
   - **验收标准**：如果 ASR 识别结果丢失了最后一个字，需将 `hangover_duration_ms` 从 400ms 延长至 500ms，或把 `end_threshold` 从 0.35 降到 0.25。

---

## 五、关联导航
- 原理机制与 PM 决策：[[VAD-原理与端点检测]]
- 收集到的干净语音送往：[[ASR-官方资料与练习]]
- 语种判断与路由：[[LID-官方资料与练习]]
- 总控全貌：[[语音交互与端侧管线 MOC]]
