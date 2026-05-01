import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 日本語フォント設定（macOS）
mpl.rcParams['font.family'] = 'Hiragino Sans'

# サンプリング設定
sample_rate = 44100
duration = 0.01  # 表示する時間（秒）
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Cメジャー（ドミソ）の周波数
freq_do  = 261.63  # ド（C4）
freq_mi  = 329.63  # ミ（E4）
freq_sol = 392.00  # ソ（G4）

# 各音の波形
wave_do  = np.sin(2 * np.pi * freq_do  * t)
wave_mi  = np.sin(2 * np.pi * freq_mi  * t)
wave_sol = np.sin(2 * np.pi * freq_sol * t)

# 合成波形（3つを足して正規化）
wave_chord = wave_do + wave_mi + wave_sol
wave_chord_normalized = wave_chord / np.max(np.abs(wave_chord))

# グラフ描画
fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
fig.suptitle('Cメジャーコード（ドミソ）の波形合成', fontsize=14, fontweight='bold')

t_ms = t * 1000  # ミリ秒に変換

plot_data = [
    (wave_do,               '#E74C3C', 'ド（C4: 261.63 Hz）'),
    (wave_mi,               '#2ECC71', 'ミ（E4: 329.63 Hz）'),
    (wave_sol,              '#3498DB', 'ソ（G4: 392.00 Hz）'),
    (wave_chord_normalized, '#9B59B6', '合成波形（ドミソ）'),
]

for ax, (wave, color, label) in zip(axes, plot_data):
    ax.plot(t_ms, wave, color=color, linewidth=1.2)
    ax.set_ylabel(label, fontsize=9)
    ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.grid(True, alpha=0.3)

axes[-1].set_xlabel('時間（ミリ秒）', fontsize=10)
plt.tight_layout()
plt.savefig('c_major_waves.png', dpi=150, bbox_inches='tight')
plt.show()
