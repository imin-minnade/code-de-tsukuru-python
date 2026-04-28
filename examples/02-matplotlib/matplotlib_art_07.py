import matplotlib.pyplot as plt
import math

# 重ねて描くスピログラフのパラメータ
# R: 外側の歯車の半径、r: 内側の歯車の半径、d: 歯車の中心からペン穴までの距離（d < r）
layers = [
    dict(R=7,  r=2.1, d=1.8, cmap="hsv",    alpha=0.8),
    dict(R=7,  r=3.2, d=2.0, cmap="plasma", alpha=0.6),
    dict(R=7,  r=3.6, d=3.0, cmap="cool",   alpha=0.5),
]
points = 5000

plt.figure(figsize=(7, 7), facecolor="black")

for layer in layers:
    R, r, d = layer["R"], layer["r"], layer["d"]
    x_list = []
    y_list = []
    colors = []
    for i in range(points):
        angle = i * 20 * math.pi / points
        x_list.append((R - r) * math.cos(angle) + d * math.cos((R - r) * angle / r))
        y_list.append((R - r) * math.sin(angle) - d * math.sin((R - r) * angle / r))
        colors.append(i)
    plt.scatter(x_list, y_list, c=colors, cmap=layer["cmap"],
                s=0.5, alpha=layer["alpha"])

plt.axis("equal")
plt.axis("off")
plt.show()