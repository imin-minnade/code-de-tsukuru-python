import matplotlib.pyplot as plt
import math

lines = 30   # 線の本数
points = 200  # 1本の線を構成する点の数

plt.figure(figsize=(6, 6))
for i in range(lines):
    x_list = []
    y_list = []
    for j in range(points):
        pos = j / points  # 横方向の位置（0から1）
        x_list.append(pos)
        y_list.append(i / lines + 0.02 * math.sin(20 * pos + i))
    plt.plot(x_list, y_list, color="black", linewidth=0.5)

plt.axis("off")
plt.show()