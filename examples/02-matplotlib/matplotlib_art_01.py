import matplotlib.pyplot as plt
import math

x_list = []  # x座標の値を入れるリスト
y_list = []  # y座標の値を入れるリスト
angle = 0    # 角度（ラジアン）。0から2πまで増やしていく
while angle < 2 * math.pi:
    x_list.append(angle)
    y_list.append(math.sin(angle))
    angle += 0.01

# 座標の数を表示する
print(len(x_list))

# 描画する
plt.plot(x_list, y_list)
plt.title("My First Sine Wave")
plt.show()