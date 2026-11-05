# LID-官方资料与练习

> 语种识别（LID）在端侧的实现难点不在于“训一个庞大的分类器”，而在于**如何用最低的计算代价、在最短的物理时延（< 500ms）内给出高置信度的决策**。
> 本篇整理主流官方开源工具包，并提供直接可运行的轻量级语种嗅探与动态路由分发实战练习。

---

## 一、权威开源模型与官方资料库

| 框架 / 模型 | 官方源与仓库 | 模型体积 | 语种覆盖 | 推荐场景 |
| :--- | :--- | :--- | :--- | :--- |
| **SenseVoice-Small** (阿里通义) | [ModelScope: SenseVoice-Small](https://github.com/FunAudioLLM/SenseVoice) | ~400MB (可量化至 100MB) | 中、英、日、韩、粤及富文本情感 | **原生多任务首选**。输出文本自带 `<|zh|>`、`<|en|>` 等标签，ASR 与 LID 一体化联合推断。 |
| **Whisper LID Head** (OpenAI) | [GitHub: openai/whisper](https://github.com/openai/whisper) | 复用现有 Whisper 权重 | 99 种全球语言 | 已有 Whisper 基础时，复用 Encoder 输出的首个 Decoder Token 概率分布，零额外模型开销。 |
| **SpeechBrain ECAPA-TDNN** | [HuggingFace: speechbrain/lang-id-voxlingua107](https://huggingface.co/speechbrain/lang-id-voxlingua107) | ~80MB | 107 种语言 | 独立高精度声学语种识别基线，常用于专业语音质检与长音频离线分类。 |
| **FastText LID** (Meta) | [fastText: language-identification](https://fasttext.cc/docs/en/language-identification.html) | ~1MB (压缩版) | 176 种语言 | **文本级二次校验**。针对已识别出的文本片段做纳秒级语言研判，开销微乎其微。 |

---

## 二、实战练习 1：利用 Whisper 编码器首帧快速嗅探语种

如果你已经集成了 Whisper 架构，无需引入额外的外部模型，直接利用 Whisper 的预训练权重即可在收到前 **300ms ~ 500ms** 音频时完成语种探测。

```python
import torch
import whisper
import numpy as np

class WhisperQuickLID:
    """
    复用 Whisper 骨干网络的高速低延迟语种嗅探器
    仅运行 Encoder 与 Decoder 首步，提取语言 Token 分布
    """
    def __init__(self, model_name: str = "base"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = whisper.load_model(model_name, device=self.device)

    def detect_language(self, audio_data: np.ndarray, sample_rate: int = 16000) -> dict:
        """
        输入: 16kHz float32 音频数组 (推荐时长 0.5s ~ 3.0s)
        输出: {'top_language': 'zh', 'probability': 0.982, 'candidates': {...}}
        """
        # 补齐或截断至 30 秒 (Whisper 标准 Mel 特征输入维度)
        audio = whisper.pad_or_trim(audio_data)
        
        # 提取 80 维 Log-Mel 频谱
        mel = whisper.log_mel_spectrogram(audio, n_mels=self.model.dims.n_mels).to(self.device)

        # 仅执行 Encoder 前向传播
        with torch.no_grad():
            encoder_output = self.model.encoder(mel.unsqueeze(0))
            
            # 使用 Decoder 的初始 Token 引导，预测下一个语言 Token 的概率分布
            # 官方内置的 detect_language 方法对解码器首步做了专门优化
            _, probs = self.model.detect_language(mel)

        # 获取置信度最高的 Top-3 语种
        sorted_probs = sorted(probs[0].items(), key=lambda x: x[1], reverse=True)
        top_lang, top_prob = sorted_probs[0]

        return {
            "top_language": top_lang,
            "probability": round(top_prob, 4),
            "candidates": {k: round(v, 4) for k, v in sorted_probs[:3]}
        }

# === 模拟使用 ===
if __name__ == "__main__":
    # lid = WhisperQuickLID("tiny") # 使用极小模型降低端侧资源消耗
    # mock_audio = np.random.uniform(-0.1, 0.1, 16000 * 1).astype(np.float32) # 1秒音频
    # result = lid.detect_language(mock_audio)
    # print(f"检测结果: {result}")
    pass
```

---

## 三、实战练习 2：构建多语种动态路由分发器（Dynamic Router）

下面展示端侧 OS PM 在设计“双轨投机路由”时最核心的调度状态机逻辑：

```python
from typing import Dict, Any

class MockASREngine:
    def __init__(self, name: str):
        self.name = name
    def stream_decode(self, chunk: bytes) -> str:
        return f"[{self.name}解码中...]"

class DynamicSpeechRouter:
    """
    端侧多语种动态路由中枢
    具备主语言优先投机、置信度门限控制与回退机制 (Fallback)
    """
    def __init__(self, default_lang: str = "zh", confidence_threshold: float = 0.85):
        self.default_lang = default_lang
        self.confidence_threshold = confidence_threshold
        
        # 维护轻量专有引擎池
        self.engines = {
            "zh": MockASREngine("中文专精引擎-Paraformer"),
            "en": MockASREngine("英文专精引擎-Conformer"),
            "cloud": MockASREngine("云端高精度多语种集群")
        }
        
        self.current_engine = self.engines[self.default_lang]
        self.is_routed = False # 是否已经拍板路由
        self.audio_cache = bytearray()

    def feed_audio(self, chunk: bytes, current_duration_ms: int, lid_probe_func) -> Dict[str, Any]:
        """
        每收到一段流式音频调用一次
        """
        self.audio_cache.extend(chunk)
        
        # 阶段 1: 在前 500ms 内，如果还没敲定语种，先用默认引擎投机输出
        if not self.is_routed and current_duration_ms < 500:
            partial_text = self.current_engine.stream_decode(chunk)
            return {"action": "SPECULATIVE_OUTPUT", "text": partial_text, "lang": self.default_lang}

        # 阶段 2: 积累到 500ms，触发一次 LID 决策
        if not self.is_routed and current_duration_ms >= 500:
            lid_result = lid_probe_func(bytes(self.audio_cache))
            detected_lang = lid_result["top_language"]
            conf = lid_result["probability"]
            
            self.is_routed = True # 锁定决策，避免后续反复横跳

            if conf >= self.confidence_threshold:
                if detected_lang != self.default_lang:
                    # 发现误判！触发回滚并切换引擎
                    target_engine = self.engines.get(detected_lang, self.engines["cloud"])
                    self.current_engine = target_engine
                    return {
                        "action": "ROLLBACK_AND_SWITCH",
                        "new_lang": detected_lang,
                        "rewind_audio": bytes(self.audio_cache),
                        "msg": f"检测到发音为 {detected_lang} (置信度 {conf})，回滚投机并切换引擎"
                    }
            
            # 若置信度不足或判定为默认语言，则平滑继续
            return {"action": "CONFIRM_DEFAULT", "lang": self.default_lang}

        # 阶段 3: 路由锁定后，直接送入敲定的引擎正常解码
        return {"action": "NORMAL_DECODE", "text": self.current_engine.stream_decode(chunk)}
```

---

## 四、自测练习与指标验收 Checklist

1. **短音频判决极限测试（0.3s vs 0.5s vs 1.0s）**：
   - 准备中、英、日三种语言各 20 条音频片段。
   - 分别截取前 300ms、500ms、1000ms 喂入 LID 模型。
   - **观察数据规律**：记录置信度与准确率随音频时长的衰减曲线。通常 **500ms 是准确率与延迟的最佳甜点位（Sweet Spot）**。
2. **中英混杂鲁棒性测试（Code-Switching）**：
   - 朗读句子：“我们明天去看电影，then have lunch together.”
   - 验证你的 LID 是输出 `zh` 还是 `en`，并确认底层的 ASR 引擎是否具备将两段文字同时正确转写的能力，防止英文单词被硬谐音成中文乱码汉字。

---

## 五、关联导航
- 核心原理与决策：[[LID-原理与语言路由]]
- 下游识别引擎选型：[[语音集成-模型选型比较]]
- 核心识别原理：[[ASR-原理与关键概念]]
- 总控全貌：[[语音交互与端侧管线 MOC]]
