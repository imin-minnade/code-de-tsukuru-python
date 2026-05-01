import tkinter as tk
import numpy as np
import sounddevice as sd
import threading

SAMPLE_RATE = 44100

def midi_to_freq(midi_number):
    """MIDI番号を周波数（Hz）に変換する"""
    return 440 * 2 ** ((midi_number - 69) / 12)

def play_note(frequency, duration=0.4):
    """指定した周波数の音を鳴らす（エンベロープ付き）"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    # 音の立ち上がり・減衰を加える（ピアノっぽい音に近づく）
    envelope = np.exp(-3 * t / duration)
    wave = 0.3 * np.sin(2 * np.pi * frequency * t) * envelope
    sd.play(wave, SAMPLE_RATE)

def play_note_async(frequency):
    """音を別スレッドで再生する（GUIをブロックしない）"""
    threading.Thread(target=play_note, args=(frequency,), daemon=True).start()

# 白鍵のMIDI番号（ドレミファソラシ）
WHITE_KEYS = [60, 62, 64, 65, 67, 69, 71]
WHITE_NAMES = ["ド", "レ", "ミ", "ファ", "ソ", "ラ", "シ"]

# 黒鍵のMIDI番号（Noneは白鍵と白鍵の間に黒鍵がない箇所）
BLACK_KEYS = [61, 63, None, 66, 68, 70, None]

# キーボードの割り当て
KEY_MAP = {
    "a": 60, "s": 62, "d": 64, "f": 65,
    "g": 67, "h": 69, "j": 71,
    "w": 61, "e": 63, "t": 66, "y": 68, "u": 70,
}

root = tk.Tk()
root.title("Pythonピアノ")
root.resizable(False, False)

canvas = tk.Canvas(root, width=350, height=200, bg="#2b2b2b")
canvas.pack(padx=10, pady=10)

WHITE_W, WHITE_H = 46, 150
BLACK_W, BLACK_H = 28, 95
START_X = 10

white_rects = {}
black_rects = {}

# 白鍵を描く
for i, midi in enumerate(WHITE_KEYS):
    x = START_X + i * WHITE_W
    rect = canvas.create_rectangle(x, 20, x + WHITE_W - 2, 20 + WHITE_H,
                                   fill="white", outline="#888", width=1)
    canvas.create_text(x + WHITE_W // 2, 20 + WHITE_H - 18,
                       text=WHITE_NAMES[i], font=("Helvetica", 10))
    white_rects[midi] = rect

# 黒鍵を描く（白鍵の上に重ねるため、後から描く）
for i, midi in enumerate(BLACK_KEYS):
    if midi is None:
        continue
    x = START_X + i * WHITE_W + WHITE_W - BLACK_W // 2
    rect = canvas.create_rectangle(x, 20, x + BLACK_W, 20 + BLACK_H,
                                   fill="#222", outline="#000", width=1)
    black_rects[midi] = rect

def flash_key(midi, is_black):
    """クリック・キー押下時に鍵盤を光らせる"""
    rects = black_rects if is_black else white_rects
    if midi not in rects:
        return
    rect = rects[midi]
    original_color = "#222" if is_black else "white"
    highlight_color = "#555" if is_black else "#aaddff"
    canvas.itemconfig(rect, fill=highlight_color)
    root.after(200, lambda: canvas.itemconfig(rect, fill=original_color))

def on_key_press(event):
    """キーボード入力を処理する"""
    key = event.keysym.lower()
    if key in KEY_MAP:
        midi = KEY_MAP[key]
        is_black = midi in black_rects
        flash_key(midi, is_black)
        play_note_async(midi_to_freq(midi))

root.bind("<KeyPress>", on_key_press)

# 白鍵のクリック処理
for midi, rect in white_rects.items():
    canvas.tag_bind(rect, "<Button-1>",
        lambda e, m=midi: [flash_key(m, False), play_note_async(midi_to_freq(m))])

# 黒鍵のクリック処理
for midi, rect in black_rects.items():
    canvas.tag_bind(rect, "<Button-1>",
        lambda e, m=midi: [flash_key(m, True), play_note_async(midi_to_freq(m))])

# 操作説明
canvas.create_text(175, 185,
    text="キーボード: a s d f g h j（白鍵） / w e t y u（黒鍵）",
    font=("Helvetica", 9), fill="#aaa")

root.mainloop()