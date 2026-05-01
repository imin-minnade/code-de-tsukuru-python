import numpy as np
import sounddevice as sd

def play_note(frequency, duration=0.5):
    """指定した周波数の音を、指定した秒数だけ鳴らす"""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.3 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, sample_rate)
    sd.wait()

# これだけで音が鳴る
play_note(261.63)  # ド
play_note(293.66)  # レ
play_note(329.63)  # ミ

print("ドレミの音が聞こえましたか？")