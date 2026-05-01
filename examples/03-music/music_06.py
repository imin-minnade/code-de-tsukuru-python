from midiutil import MIDIFile

midi = MIDIFile(1)         # 1トラックのMIDIファイルを作る
midi.addTempo(0, 0, 120)   # トラック0、時刻0、テンポ120 BPM

# カエルの歌を書き込む
melody = [60, 62, 64, 65, 64, 62, 60, 64, 65, 67, 69, 67, 65, 64]
for i, note in enumerate(melody):
    midi.addNote(0, 0, note, i * 0.5, 0.5, 100)
    # 引数: トラック, チャンネル, 音(MIDI番号), 開始時間(拍), 長さ(拍), 強さ(0-127)

# ファイルに保存
with open("kaeru.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("kaeru.mid を保存しました。ダブルクリックで再生できます！")