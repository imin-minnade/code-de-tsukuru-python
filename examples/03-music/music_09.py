import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100

def midi_to_freq(midi_number):
    return 440 * 2 ** ((midi_number - 69) / 12)

def make_square_wave(frequency, duration, volume=0.25):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * np.sign(np.sin(2 * np.pi * frequency * t))

def make_triangle_wave(frequency, duration, volume=0.2):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * t))

melody_notes = [
    (60, 0.25),  # C4
    (62, 0.25),  # D4
    (64, 0.5),   # E4
    (67, 0.5),   # G4
    (67, 0.25),  # G4
    (69, 0.25),  # A4
    (72, 0.5),   # C5
    (71, 0.5),   # B4
    (67, 0.5),   # G4
    (65, 0.25),  # F4
    (64, 0.25),  # E4
    (62, 0.5),   # D4
    (60, 0.5),   # C4
    (67, 0.5),   # G4
    (72, 0.5),   # C5
    (74, 0.5),   # D5
    (76, 1.0),   # E5
    (None, 0.5), # 休符
]

bass_notes = [
    (48, 1.0),   # C3
    (52, 1.0),   # E3
    (53, 1.0),   # F3
    (55, 1.0),   # G3
    (48, 1.0),   # C3
    (50, 1.0),   # D3
    (55, 1.0),   # G3
    (48, 1.5),   # C3
]

# メロディとベースを合成して再生する
print("「冒険の始まり」を演奏します...")
melody_wave = np.array([])
for note, dur in melody_notes:
    if note is None:
        # 休符：無音を追加
        silence = np.zeros(int(SAMPLE_RATE * dur))
        melody_wave = np.concatenate([melody_wave, silence])
    else:
        chunk = make_square_wave(midi_to_freq(note), dur)
        melody_wave = np.concatenate([melody_wave, chunk])

bass_wave = np.array([])
for note, dur in bass_notes:
    chunk = make_triangle_wave(midi_to_freq(note), dur)
    bass_wave = np.concatenate([bass_wave, chunk])

# 長さを合わせて重ねる
min_len = min(len(melody_wave), len(bass_wave))
combined = melody_wave[:min_len] + bass_wave[:min_len]

sd.play(combined, SAMPLE_RATE)
sd.wait()
print("演奏終了！")