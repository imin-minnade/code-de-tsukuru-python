import matplotlib.pyplot as plt
import math

# 描きたいパターンをリストにまとめる
freq_x_list = [1, 1, 3, 5]
freq_y_list = [2, 3, 4, 7]
phase_list  = [math.pi / 2, math.pi / 2, math.pi / 4, math.pi / 2]
color_list  = ["red", "blue", "green", "purple"]

plt.figure(figsize=(10, 10))

for i in range(4):
    x_list = []
    y_list = []
    for j in range(1000):
        angle = j * 2 * math.pi / 1000
        x_list.append(math.sin(freq_x_list[i] * angle + phase_list[i]))
        y_list.append(math.sin(freq_y_list[i] * angle))

    plt.subplot(2, 2, i + 1)
    plt.plot(x_list, y_list, color=color_list[i])
    plt.axis("equal")
    plt.axis("off")
    plt.title(f"{freq_x_list[i]}:{freq_y_list[i]}, phase={phase_list[i]:.2f}")

plt.tight_layout()
plt.show()