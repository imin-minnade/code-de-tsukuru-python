import matplotlib.pyplot as plt
import math

freq_x = 3          # x方向の周波数
freq_y = 5          # y方向の周波数
phase = math.pi / 2 # 位相のずれ（x波とy波のタイミングのずれ）

# 点を1000個用意する
x_list = []
y_list = []
for i in range(1000):
    angle = i * 2 * math.pi / 1000
    x_list.append(math.sin(freq_x * angle + phase))
    y_list.append(math.sin(freq_y * angle))

plt.figure(figsize=(6, 6))
plt.plot(x_list, y_list, color="darkorange")
plt.axis("equal")
plt.axis("off")
plt.title(f"Lissajous: {freq_x}:{freq_y}, phase={phase:.2f}")
plt.show()