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

# キラキラの星（MIDI番号のリスト）
melody = [
    60, 60, 67, 67, 69, 69, 67,
    65, 65, 64, 64, 62, 62, 60,
    67, 67, 65, 65, 64, 64, 62,
    67, 67, 65, 65, 64, 64, 62,
    60, 60, 67, 67, 69, 69, 67,
    65, 65, 64, 64, 62, 62, 60,
]


for note in melody:
    play_note(midi_to_freq(note), 0.4)