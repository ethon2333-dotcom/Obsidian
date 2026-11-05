# Punc-官方资料与练习

> 标点恢复（Punc）与逆文本正则化（ITN）是工程落地中“投入产出比极高”的模块——仅用几兆的轻量模型与纯规则 FST，就能让粗糙的 ASR 输出质变为优雅整洁的书面表达。
> 本篇整理官方工具链，并提供标点推理、ITN 规整及流式防抖动提交的实战代码练习。

---

## 一、权威开源库与官方模型索引

| 项目名称 | 官方仓库 / 地址 | 技术类型 | 适用场景与选型评价 |
| :--- | :--- | :--- | :--- |
| **CT-Transformer Punc** (阿里通义) | [ModelScope: punc_ct-transformer](https://www.modelscope.cn/models/iic/punc_ct-transformer_zh-cn-common-vocab272727-onnx) | ONNX / Python / C++ | **中文标点工业标杆**。支持可控时延流式标点，官方直接提供量化后的 ONNX 单文件，体积仅数十兆，单句打点 < 5ms。 |
| **WeTextProcessing** (出门问问/社区) | [GitHub: wenet-e2e/WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) | 基于 OpenFST 的 C++ / Python 规则编译 | **生产级 ITN / TN 事实标准**。涵盖数字、日期、货币、分数等全量语法规整，无任何幻觉风险。 |
| **PaddleSpeech Punc** (百度飞桨) | [GitHub: PaddlePaddle/PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech) | 基于 ERNIE 的序列标注网络 | 依托百度 ERNIE 强大的中文预训练语言表征，长文本离线转写标点精度极高。 |

---

## 二、实战练习 1：FunASR CT-Transformer 标点恢复

以下演示如何使用 ModelScope / FunASR 的官方 API 载入预训练标点模型，对长句进行标点与断句恢复：

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

def run_punc_restoration():
    """
    使用阿里开源的 CT-Transformer 标点模型进行文本规整
    模型名称: punc_ct-transformer_zh-cn-common-vocab272727-onnx
    """
    # 1. 实例化标点恢复 Pipeline (支持纯 CPU 推理)
    punc_pipeline = pipeline(
        task=Tasks.punctuation,
        model='damo/punc_ct-transformer_zh-cn-common-vocab272727-onnx',
        model_revision='v1.0.2'
    )

    # 2. 模拟一段没有标点的原始 ASR 识别流
    raw_asr_text = "今天下午三点在二号会议室开会请大家带上电脑如果不能参加请提前向李四请假"

    # 3. 执行推理
    result = punc_pipeline(text_in=raw_asr_text)
    
    print(">>> 原始文本:")
    print(raw_asr_text)
    print("\n>>> 标点恢复结果:")
    print(result['text'])
    # 预期输出: "今天下午三点在二号会议室开会，请大家带上电脑。如果不能参加，请提前向李四请假。"

if __name__ == "__main__":
    # run_punc_restoration()
    pass
```

---

## 三、实战练习 2：WeTextProcessing 逆文本正则化（ITN）规整

在向下游大模型或日历、闹钟等操作系统能力派发意图时，必须把中文大写数字转成标准的阿拉伯数字。

```python
# 需提前安装: pip install WeTextProcessing
from tn.chinese.inverse_normalizer import InverseNormalizer

def run_itn_demo():
    """
    使用工业级 FST 规则库执行确定性逆文本正则化 (ITN)
    """
    normalizer = InverseNormalizer(cache_dir="./itn_cache", overwrite_cache=False)

    test_cases = [
        "明天下午三点半提醒我开会",
        "把空调温度调到二十六度",
        "他的电话是一三八一二三四五六七八",
        "今年公司的营收增长了百分之十二点五",
        "账户余额还有两千五百元零八分"
    ]

    print(">>> 开始执行 ITN 逆文本正则化测试:")
    for text in test_cases:
        norm_result = normalizer.normalize(text)
        print(f"原句: {text}")
        print(f"规整: {norm_result}\n")
        
    # 预期输出效果:
    # "明天下午3:30提醒我开会"
    # "把空调温度调到26度"
    # "他的电话是13812345678"
    # "今年公司的营收增长了12.5%"
    # "账户余额还有2500.08元"

if __name__ == "__main__":
    # run_itn_demo()
    pass
```

---

## 四、实战练习 3：流式“固定提交窗”防抖动模拟器

在 Android 端侧 UI 上实时打字时，如何避免标点符号反复更正跳跃？以下是生产级前端平滑算法的最小实现：

```python
class StreamingPuncStabilizer:
    """
    流式标点稳定器 (固定提交窗机制)
    将文本划分为: 已敲定锁定区 (Committed) 与 尾部动态浮动区 (Floating)
    """
    def __init__(self, commit_window_chars: int = 6):
        self.committed_text = ""       # 永远不再修改的历史稳定文本
        self.commit_window_chars = commit_window_chars

    def update(self, current_full_asr_text: str, punc_predict_fn) -> dict:
        """
        每次流式 ASR 吐出更多文字时调用
        punc_predict_fn: 标点预测函数
        """
        # 1. 仅对未完全锁定的新增部分与浮动部分进行标点推演
        # 为保证语义连贯，将已锁定的最后几个字符作为上下文一并送入
        context_tail = self.committed_text[-4:] if self.committed_text else ""
        text_to_punc = context_tail + current_full_asr_text[len(self.committed_text):]
        
        punctuated = punc_predict_fn(text_to_punc)
        # 剥离刚才借用的 context_tail
        if context_tail and punctuated.startswith(context_tail):
            punctuated = punctuated[len(context_tail):]

        full_punctuated = self.committed_text + punctuated

        # 2. 判定提交边界: 距离末尾超过 commit_window_chars 的文本执行物理锁定
        if len(full_punctuated) > self.commit_window_chars:
            commit_idx = len(full_punctuated) - self.commit_window_chars
            # 找到提交边界最近的一个自然断句标点（，或。）
            safe_punc_pos = -1
            for i in range(commit_idx, -1, -1):
                if full_punctuated[i] in ["，", "。", "！", "？"]:
                    safe_punc_pos = i + 1
                    break
            
            if safe_punc_pos > len(self.committed_text):
                self.committed_text = full_punctuated[:safe_punc_pos]

        return {
            "stable_text": self.committed_text,                                  # UI 可用深黑色渲染 (已固定)
            "floating_text": full_punctuated[len(self.committed_text):],       # UI 可用浅灰色渲染 (动态变动中)
            "full_display": full_punctuated
        }
```

---

## 五、关联导航
- 核心原理与设计准则：[[Punc-原理与文本边界]]
- 接口协议与时间轴：[[语音集成-接口与时间轴]]
- 系统排障与常见误区：[[语音集成-排障与常见误区]]
- 全链路总控：[[语音交互与端侧管线 MOC]]
