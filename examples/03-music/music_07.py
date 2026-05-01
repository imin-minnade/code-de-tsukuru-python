import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100

def midi_to_freq(midi_number):
    """MIDI番号を周波数（Hz）に変換する"""
    return 440 * 2 ** ((midi_number - 69) / 12)

def make_square_wave(frequency, duration, volume=0.3):
    """矩形波（ファミコンのメロディ音）を生成する"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * np.sign(np.sin(2 * np.pi * frequency * t))

def make_triangle_wave(frequency, duration, volume=0.3):
    """三角波（ファミコンのベース音）を生成する"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * t))

def play_wave(wave):
    """波形を再生する"""
    sd.play(wave, SAMPLE_RATE)
    sd.wait()

# 聴き比べ：sin波 vs 矩形波 vs 三角波（全部「ラ」の音）
frequency = midi_to_freq(69)  # ラ（A4）= 440Hz
duration = 1.0

t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
wave_sin      = 0.3 * np.sin(2 * np.pi * frequency * t)
wave_square   = make_square_wave(frequency, duration)
wave_triangle = make_triangle_wave(frequency, duration)

print("① sin波（なめらかな電子音）:")
play_wave(wave_sin)

print("② 矩形波（ファミコンのメロディ音）:")
play_wave(wave_square)

print("③ 三角波（ファミコンのベース音）:")
play_wave(wave_triangle)