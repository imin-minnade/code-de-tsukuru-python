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

while True:
    key = input("キー (a=ド s=レ d=ミ f=ファ g=ソ h=ラ j=シ / q=終了): ")

    if key == "q":
        print("終了します")
        break
    elif key == "a":
        play_note(midi_to_freq(60))  # ド
    elif key == "s":
        play_note(midi_to_freq(62))  # レ
    elif key == "d":
        play_note(midi_to_freq(64))  # ミ
    elif key == "f":
        play_note(midi_to_freq(65))  # ファ
    elif key == "g":
        play_note(midi_to_freq(67))  # ソ
    elif key == "h":
        play_note(midi_to_freq(69))  # ラ
    elif key == "j":
        play_note(midi_to_freq(71))  # シ
    else:
        print("そのキーには音が割り当てられていません")