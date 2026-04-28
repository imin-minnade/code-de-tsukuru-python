import matplotlib.pyplot as plt
import math

# 同じ周波数比（1:2）で、位相のずれだけを変えた4パターン
curves = [
    dict(freq_x=1, freq_y=2, phase=0,           color="red"),
    dict(freq_x=1, freq_y=2, phase=math.pi / 6, color="blue"),
    dict(freq_x=1, freq_y=2, phase=math.pi / 3, color="green"),
    dict(freq_x=1, freq_y=2, phase=math.pi / 2, color="purple"),
]

plt.figure(figsize=(10, 10))

for i, curve in enumerate(curves):
    x_list = []
    y_list = []
    for j in range(1000):
        angle = j * 2 * math.pi / 1000
        x_list.append(math.sin(curve["freq_x"] * angle + curve["phase"]))
        y_list.append(math.sin(curve["freq_y"] * angle))

    plt.subplot(2, 2, i + 1)
    plt.plot(x_list, y_list, color=curve["color"])
    plt.axis("equal")
    plt.axis("off")
    plt.title(f'1:2, phase={curve["phase"]:.2f}')

plt.tight_layout()
plt.show()