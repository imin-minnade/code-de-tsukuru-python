import numpy as np
import sounddevice as sd

# ラの音（440Hz）を1秒間鳴らす
frequency = 440        # 周波数（Hz）
duration = 1.0         # 秒
sample_rate = 44100    # サンプリングレート（1秒間に44,100個の点）

# sin波を生成する
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
wave = 0.3 * np.sin(2 * np.pi * frequency * t)

# 再生する
sd.play(wave, sample_rate)
sd.wait()

print("ラの音が聞こえましたか？")