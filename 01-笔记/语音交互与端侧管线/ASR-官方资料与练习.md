# ASR-官方资料与练习

> 掌握 ASR 不能停留在“调一次云端 REST API”。在端侧与私有化系统构建中，你必须亲手驾驭**跨平台纯 C/ONNX 推理引擎**与**流式分块（Chunk-based）状态流转**。
> 本篇整理当前工业界最活跃的官方仓库，并提供包含流式分块解码与错误率评测的工业级代码练习。

---

## 一、工业级官方资料与核心开源仓库

| 框架与生态 | 官方主页 / 仓库 | 核心能力 | 端侧适配性与 PM 选型定位 |
| :--- | :--- | :--- | :--- |
| **Sherpa-ONNX** (新一代 Kaldi) | [GitHub: k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | C++ 跨平台核心，支持流式 Zipformer, Conformer, Whisper, VAD, TTS | **端侧与嵌入式工程落地首选**。直接提供 Android AAR、iOS 静态库、Python 绑定，无 Python 运行时依赖，包体积小至数兆。 |
| **FunASR / SenseVoice** (阿里通义) | [GitHub: modelscope/FunASR](https://github.com/modelscope/FunASR) | Paraformer 非自回归 ASR、SenseVoice-Small 富文本语音、FSMN-VAD、CT-Transformer 标点 | **中文与多任务落地首选**。涵盖 VAD+ASR+Punc 完整工业三件套，提供开箱即用的 ONNX 导出工具与 Docker 服务端镜像。 |
| **Whisper.cpp** (Georgi Gerganov) | [GitHub: ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp) | 纯 C/C++ 实现的 OpenAI Whisper 推理引擎，支持 Apple Silicon Metal、Android NPU 加速 | **端侧离线高精度转写首选**。零第三方依赖，支持 4-bit / 5-bit 量化，内存占用压低至几十兆。 |
| **WeNet** (出门问问/社区) | [GitHub: wenet-e2e/wenet](https://github.com/wenet-e2e/wenet) | 首创“流式第一遍（First-pass）+ 双向注意力第二遍（Second-pass）重打分”统一架构 | 工业级服务端与车载流式首选架构，生产环境高并发验证极其充分。 |

---

## 二、实战练习 1：Sherpa-ONNX 纯轻量流式 ASR 分块解码

Sherpa-ONNX 是目前在 Android 操作系统与 Linux 嵌入式设备上构建流式 ASR 的标杆。以下演示如何模拟麦克风硬件每 160ms 产生一块音频流，推入 `OnlineRecognizer` 并持续拉取增量文字：

```python
import sherpa_onnx
import numpy as np

def run_streaming_asr():
    """
    基于 Sherpa-ONNX 的流式端侧语音识别
    使用 Zipformer 流式模型 (模型权重可在官方 release 页面一键下载)
    """
    # 1. 配置流式模型参数
    # 注: 实际部署时填入本地 ONNX 模型与 tokens.txt 的真实绝对路径
    recognizer = sherpa_onnx.OnlineRecognizer.from_transducer(
        encoder="./zipformer-streaming/encoder-epoch-99-avg-1.onnx",
        decoder="./zipformer-streaming/decoder-epoch-99-avg-1.onnx",
        joiner="./zipformer-streaming/joiner-epoch-99-avg-1.onnx",
        tokens="./zipformer-streaming/tokens.txt",
        num_threads=2,
        sample_rate=16000,
        feature_dim=80,
        decoding_method="greedy_search", # 端侧低延迟采用贪心搜索
    )

    # 2. 为当前对话建立流式状态会话 (Stream)
    # Stream 对象内部会自动维护声学特征缓存与 RNN 状态，无需外部干预
    stream = recognizer.create_stream()

    # 3. 模拟麦克风音频流输入 (假设每次产生 160ms 音频 = 2560 采样点)
    chunk_samples = int(16000 * 0.16)
    last_text = ""

    print(">>> 开始模拟麦克风流式输入...")
    # 模拟输入 10 块音频数据
    for step in range(10):
        # 模拟生成 16kHz float32 单声道数据
        mock_chunk = np.random.uniform(-0.05, 0.05, chunk_samples).astype(np.float32)
        
        # 喂入流式音频块
        stream.accept_waveform(16000, mock_chunk)

        # 只要引擎判定已收集足够的声学特征，即推进前向计算
        while recognizer.is_ready(stream):
            recognizer.decode_stream(stream)

        # 实时拉取最新增量识别文本
        current_text = recognizer.get_result(stream).text
        if current_text != last_text:
            print(f"[流式 Partial Output {step*160}ms]: {current_text}")
            last_text = current_text

    # 4. 音频流结束 (VAD 检出静音 EOU 时触发)
    stream.input_finished()
    while recognizer.is_ready(stream):
        recognizer.decode_stream(stream)
    
    final_text = recognizer.get_result(stream).text
    print(f"\n[最终整句识别结果 (Final)]: {final_text}")

if __name__ == "__main__":
    # run_streaming_asr()
    pass
```

---

## 三、实战练习 2：中文字错误率（CER）评测脚本编写

在 PM 验收与算法版本迭代中，绝不能只凭“主观听几句”。必须掌握基于**编辑距离（Levenshtein Distance）**的自动化 CER 评测与错误分解。

```python
def compute_cer(reference: str, hypothesis: str) -> dict:
    """
    计算中文字错误率 (CER) 并拆解 S (替换), D (删除), I (插入)
    采用动态规划构建 (N+1) x (M+1) 编辑距离矩阵
    """
    # 预处理: 移除空格、标点符号，统一大小写
    ref = list("".join(reference.split()))
    hyp = list("".join(hypothesis.split()))
    n, m = len(ref), len(hyp)

    # dp[i][j] 记录达到当前对齐状态的 (编辑代价, S, D, I)
    # 代价定义: 替换=1, 删除=1, 插入=1, 匹配=0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i  # 全是删除
    for j in range(m + 1):
        dp[0][j] = j  # 全是插入

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                substitution = dp[i - 1][j - 1] + 1
                deletion = dp[i - 1][j] + 1
                insertion = dp[i][j - 1] + 1
                dp[i][j] = min(substitution, deletion, insertion)

    distance = dp[n][m]
    cer = (distance / n) if n > 0 else 0.0

    return {
        "reference_len": n,
        "hypothesis_len": m,
        "edit_distance": distance,
        "cer": round(cer * 100, 2), # 百分比表示
        "ref": "".join(ref),
        "hyp": "".join(hyp)
    }

# === 评测示例 ===
if __name__ == "__main__":
    ground_truth = "今天下午三点在二号会议室开产品周会"
    asr_output   = "今天下午3点在2号会议室开产平周会" 
    # 注: 此处数字未归一化会产生假性 CER，这也是后续必须接 ITN/Punc 的原因！
    res = compute_cer(ground_truth, asr_output)
    print(f"评测结果: CER = {res['cer']}% (距离={res['edit_distance']}, 标注长度={res['reference_len']})")
```

---

## 四、自测练习与指标验收 Checklist

1. **RTF 性能极限基准测试**：
   - 提取一段 60 秒的真实录音，使用本地 ONNX 模型在端侧单核 CPU 上进行转写。
   - 记录纯推理耗时。若耗时为 6 秒，则 $\text{RTF} = 6 / 60 = 0.1$。
   - **验收线**：手机端 CPU 纯单核 RTF 必须稳定 $\le 0.25$；若高于 0.5，必须立即启用 INT8 权重量化（见 [[端侧模型量化 学习笔记]]）。
2. **文本抖动（Flicker）观察实验**：
   - 在流式模式下，记录识别中间过程 Partial Text 的变更历史。
   - 计算被修改掉的字符占比。若抖动严重，需调大声学模型的 Lookahead 窗口（向后多看 2 帧特征），牺牲 40ms 延迟换取屏幕文字稳定性。

---

## 五、关联导航
- 核心原理拆解：[[ASR-原理与关键概念]]
- 后续文本规整与标点：[[Punc-原理与文本边界]]
- 接口与词级时间戳：[[语音集成-接口与时间轴]]
- 总控全貌：[[语音交互与端侧管线 MOC]]
