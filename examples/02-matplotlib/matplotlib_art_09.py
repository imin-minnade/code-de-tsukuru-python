import matplotlib.pyplot as plt
import random
import math

random.seed(42)  # 毎回同じ結果になるように固定する

# 1つの星雲クラスターを作る
def gaussian_cluster(cx, cy, spread, n, color_base):
    x = []
    y = []
    colors = []
    for _ in range(n):
        angle = random.uniform(0, 2 * math.pi)
        radius = abs(random.gauss(0, spread))
        x.append(cx + radius * math.cos(angle))
        y.append(cy + radius * math.sin(angle))
        colors.append(color_base + random.uniform(-0.1, 0.1))
    return x, y, colors

plt.figure(figsize=(8, 8), facecolor="black")

# 4つのクラスターを配置する
clusters = [
    (0, 0, 2.0, 800, 0.6),
    (4, 3, 1.2, 400, 0.1),
    (-3, 4, 1.5, 500, 0.85),
    (2, -4, 1.0, 300, 0.35),
]

for cx, cy, spread, n, color_base in clusters:
    x, y, colors = gaussian_cluster(cx, cy, spread, n, color_base)
    plt.scatter(x, y, c=colors, cmap="inferno", s=2, alpha=0.6, vmin=0, vmax=1)

plt.axis("equal")
plt.axis("off")
plt.show()