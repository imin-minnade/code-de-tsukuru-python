import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100

def midi_to_freq(midi_number):
    """MIDI番号を周波数（Hz）に変換する"""
    return 440 * 2 ** ((midi_number - 69) / 12)

def make_square_wave(frequency, duration, volume=0.25):
    """矩形波（ファミコンのメロディ音）を生成する"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * np.sign(np.sin(2 * np.pi * frequency * t))

def make_triangle_wave(frequency, duration, volume=0.2):
    """三角波（ファミコンのベース音）を生成する"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return volume * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequency * t))

# オリジナル曲「冒険の始まり」
# メロディ（MIDI番号, 長さ秒）のリスト
melody_notes = [
    (67, 0.25), (69, 0.25), (71, 0.25), (72, 0.25),  # ソラシド↑（上昇）
    (72, 0.25), (71, 0.25), (69, 0.25), (67, 0.5),   # ド↑シラソ（下降）
    (65, 0.25), (67, 0.25), (69, 0.25), (71, 0.25),  # ファソラシ（上昇）
    (72, 0.75), (None, 0.25),                          # ド↑（長め）→ 休符
    (69, 0.25), (67, 0.25), (65, 0.25), (64, 0.25),  # ラソファミ（下降）
    (62, 0.25), (64, 0.25), (65, 0.25), (67, 0.25),  # レミファソ（上昇）
    (60, 0.5),  (62, 0.25), (64, 0.25),               # ド ＋ レミ
    (60, 1.0),                                         # ド（締め）
]

# ベース（メロディに合わせたコード根音）
bass_notes = [
    (55, 1.0),  # ソ（低）
    (55, 1.0),
    (53, 1.0),  # ファ（低）
    (53, 1.0),
    (50, 1.0),  # レ（低）
    (48, 1.0),  # ド（低）
    (43, 1.0),  # ソ（さらに低）
    (48, 1.0),  # ド（低）
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