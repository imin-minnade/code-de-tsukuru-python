import matplotlib.pyplot as plt
import math

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

x_list = []
y_list = []
z_list = []
for i in range(20000):
    angle = i * 110 * math.pi / 20000
    x_list.append(math.sin(2 * angle))
    y_list.append(math.sin(5 * angle))
    z_list.append(math.sin(11 * angle))

ax.plot(x_list, y_list, z_list, color="purple", linewidth=0.5)
ax.set_axis_off()
plt.title("3D Lissajous")
plt.show()