import turtle
import math

turtle.bgcolor("black")
turtle.tracer(0)     # 描画をまとめて行う（途中の描画を非表示にして高速化）

a = 3.001            # 非整数にすることで曲線が閉じず、少しずつずれていく
b = 2
delta = math.pi / 2  # 位相差
scale = 150          # 図形の大きさ
steps = 512          # 描画の細かさ（多いほど滑らか）
layers = 10          # 何周描くか

colors = ["cyan", "magenta", "yellow", "lime", "orange",
          "red", "skyblue", "white", "gold", "hotpink"]

turtle.penup()

for i in range(steps * layers + 1):
    t = 2 * math.pi * i / steps              # 0〜2πをsteps分割して少しずつ進む
    x = scale * math.sin(a * t + delta)      # x座標：振動数aのsin波
    y = scale * math.sin(b * t)              # y座標：振動数bのsin波
    turtle.color(colors[(i // steps) % len(colors)])  # 1周ごとに色を変える
    if i == 0:
        turtle.goto(x, y)   # 最初の点へ移動（線を引かずに）
        turtle.pendown()    # ここからペンを下ろして描き始める
    else:
        turtle.goto(x, y)   # 次の点へ移動しながら線を引く

turtle.update()      # 全て描き終わってから一括で画面に表示する
turtle.done()