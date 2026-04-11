import turtle

turtle.speed(0)
turtle.bgcolor("black")

golden_angle = 137.508       # 自然界の黄金角。ひまわりの種がこの角度で並んでいる
colors = ["yellow", "gold", "orange"]

for i in range(300):         # 300回繰り返す
    turtle.color(colors[i % 3])  # 3色を順番に繰り返して色を選ぶ
    turtle.forward(i * 0.3)  # i が増えるにつれて少しずつ前進距離が伸びる
    turtle.right(golden_angle)   # 黄金角だけ回転する
    turtle.dot(5)            # 現在位置に直径5の点を打つ

turtle.done()