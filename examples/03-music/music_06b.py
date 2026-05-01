from midiutil import MIDIFile

midi = MIDIFile(1)
midi.addTempo(0, 0, 90)  # テンポ90 BPM（ゆっくりめ）

# コード進行 C → F → G → C
chords = [
    {"name": "C", "notes": [60, 64, 67]},
    {"name": "F", "notes": [65, 69, 72]},
    {"name": "G", "notes": [67, 71, 74]},
    {"name": "C", "notes": [60, 64, 67]},
]

for i, chord in enumerate(chords):
    for note in chord["notes"]:
        midi.addNote(0, 0, note, i * 2, 2, 80)
    print(f"  {chord['name']} コードを追加")

with open("chords.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("chords.mid を保存しました")