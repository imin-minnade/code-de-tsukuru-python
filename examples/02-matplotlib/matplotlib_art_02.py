import matplotlib.pyplot as plt
import math

x_list = []
y_list_01 = []
y_list_02 = []
y_list_03 = []
angle = 0
while angle < 2 * math.pi:
    x_list.append(angle)
    y_list_01.append(math.sin(angle) ** 2)
    y_list_02.append(math.cos(angle) ** 2)
    y_list_03.append(math.sin(angle) ** 2 + math.cos(angle) ** 2)
    angle += 0.01

plt.plot(x_list, y_list_01, color="red", linewidth=3)
plt.plot(x_list, y_list_02, color="green", linewidth=3)
plt.plot(x_list, y_list_03, color="blue", linewidth=3)
plt.title("Trigonometric Functions")
plt.show()