import numpy as np
import sounddevice as sd

def midi_to_freq(midi_number):
    """MIDI番号を周波数（Hz）に変換する"""
    return 440 * 2 ** ((midi_number - 69) / 12)

def play_chord(frequencies, duration=1.0):
    """複数の周波数を同時に鳴らす（和音）"""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = sum(0.2 * np.sin(2 * np.pi * freq * t) for freq in frequencies)
    sd.play(wave, sample_rate)
    sd.wait()

# Cメジャー（ド・ミ・ソ）
c_major = [midi_to_freq(60), midi_to_freq(64), midi_to_freq(67)]
play_chord(c_major)

# Fメジャー（ファ・ラ・ド↑）
f_major = [midi_to_freq(65), midi_to_freq(69), midi_to_freq(72)]
play_chord(f_major)

# Gメジャー（ソ・シ・レ↑）
g_major = [midi_to_freq(67), midi_to_freq(71), midi_to_freq(74)]
play_chord(g_major)