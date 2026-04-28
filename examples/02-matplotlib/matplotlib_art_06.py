import matplotlib.pyplot as plt
import math

n = 5      # 花びらの数（奇数と偶数で形が変わる）
points = 2000

x_list = []
y_list = []
for i in range(points):
    angle = i * 2 * math.pi / points
    r = math.cos(n * angle)            # 極座標の半径
    x_list.append(r * math.cos(angle)) # 直交座標のx
    y_list.append(r * math.sin(angle)) # 直交座標のy

plt.figure(figsize=(6, 6))
plt.plot(x_list, y_list, color="crimson", linewidth=0.8)
plt.axis("equal")
plt.axis("off")
plt.show()