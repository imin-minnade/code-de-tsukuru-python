import numpy as np
import sounddevice as sd

def midi_to_freq(midi_number):
    """MIDI番号を周波数（Hz）に変換する"""
    return 440 * 2 ** ((midi_number - 69) / 12)

def play_note(frequency, duration=0.5):
    """指定した周波数の音を、指定した秒数だけ鳴らす"""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.3 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, sample_rate)
    sd.wait()

# カエルの歌（MIDI番号のリスト）
melody = [60, 62, 64, 65, 64, 62, 60,   # ドレミファミレド
          64, 65, 67, 69, 67, 65, 64]    # ミファソラソファミ

for note in melody:
    play_note(midi_to_freq(note), 0.4)