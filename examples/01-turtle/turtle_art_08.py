import turtle

turtle.speed(0)
turtle.bgcolor("black")  # 背景を黒にする

colors = ["red", "yellow", "cyan", "magenta", "lime", "orange"]  # 色のリスト（6色）

for i in range(150):               # 150回繰り返す（回数指定の書き方）
    color = colors[i % 6]          # 0〜5を繰り返して色を選ぶ
    turtle.color(color)
    turtle.forward(i * 2)          # i が増えるにつれて線が長くなる
    turtle.right(91)

turtle.done()