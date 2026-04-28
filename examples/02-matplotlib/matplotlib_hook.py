import matplotlib.pyplot as plt
import math

steps = 20000    # 描く点の数
t_max = 500.0     # シミュレーションの総時間（秒）
decay = 0.004     # 減衰の速さ（大きいほど早く中心に収束する）

# 2つの振り子の周波数と位相のずれ
freq1 = 2.0
freq2 = 3.0
phase = math.pi / 4   # 45度のずれ

x_list = []
y_list = []

for i in range(steps):
    t = i * t_max / steps
    fade = math.exp(-decay * t)   # 時間とともに小さくなる係数
    x = fade * math.sin(freq1 * t + phase)
    y = fade * math.sin(freq2 * t)
    x_list.append(x)
    y_list.append(y)

plt.figure(figsize=(6, 6), facecolor="black")
plt.plot(x_list, y_list, color="yellow", linewidth=0.3, alpha=0.7)
plt.axis("equal")
plt.axis("off")
plt.show()