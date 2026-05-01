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

# キーとMIDI番号の対応表
key_map = {
    "a": 60, "s": 62, "d": 64, "f": 65,
    "g": 67, "h": 69, "j": 71
}

while True:
    key = input("キー (a-j / q=終了): ")
    if key == "q":
        break
    elif key in key_map:
        play_note(midi_to_freq(key_map[key]))
    else:
        print("そのキーには音が割り当てられていません")