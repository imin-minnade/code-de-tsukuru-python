import turtle

sides = 6             # 辺の数
angle = 360 / sides   # 角度を自動で計算する
length = 100

for i in range(sides):  # sides回、繰り返す
    turtle.forward(length)
    turtle.right(angle)

turtle.done()