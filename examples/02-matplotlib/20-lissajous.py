import matplotlib.pyplot as plt
import math

# 周波数比（行）と位相のズレ（列）の組み合わせ
freq_pairs = [(1, 1), (1, 2), (1, 3), (2, 3)]
phases = [0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi]
phase_labels = ["0", "π/2", "π", "3π/2", "2π"]

points = 2000

fig, axes = plt.subplots(4, 5, figsize=(12, 10))
fig.patch.set_facecolor("black")

for row, (freq1, freq2) in enumerate(freq_pairs):
    for col, (phase, label) in enumerate(zip(phases, phase_labels)):
        ax = axes[row][col]
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        ax.axis("off")

        x_list = []
        y_list = []
        for i in range(points):
            angle = i * 2 * math.pi / points
            x_list.append(math.sin(freq1 * angle + phase))
            y_list.append(math.sin(freq2 * angle))
        ax.plot(x_list, y_list, color="cyan", linewidth=0.8)

        if row == 0:
            ax.set_title(label, color="white", fontsize=10)
        if col == 0:
            ax.text(-1.6, 0, f"{freq1}:{freq2}", color="white", fontsize=10,
                    ha="center", va="center")

plt.suptitle("Lissajous Figures", color="white", fontsize=14)
plt.tight_layout()
plt.show()
