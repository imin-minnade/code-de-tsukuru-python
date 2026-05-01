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

# 音名とMIDI番号の対応表
notes = {
    "ド": 60, "レ": 62, "ミ": 64, "ファ": 65,
    "ソ": 67, "ラ": 69, "シ": 71, "ド↑": 72
}

# カエルの歌
kaeru = ["ド", "レ", "ミ", "ファ", "ミ", "レ", "ド",
         "ミ", "ファ", "ソ", "ラ", "ソ", "ファ", "ミ"]

for name in kaeru:
    play_note(midi_to_freq(notes[name]), 0.4)