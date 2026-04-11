import turtle

turtle.speed(0)
turtle.bgcolor("black")  # 背景を黒にする

colors = ["red", "yellow", "cyan", "magenta", "lime", "orange"]  # 色のリスト

for color in colors:       # リストから1色ずつ取り出して繰り返す
    turtle.color(color)    # その色で描く
    turtle.forward(20)
    turtle.right(91)

turtle.done()