import turtle

# 「関数」の定義（第3回で詳しく扱います）
# koch() は「辺の長さ」と「深さ」を受け取り、コッホ曲線を描く
def koch(length, depth):
    if depth == 0:               # 深さが0になったら、ただ線を引く（再帰の終了条件）
        turtle.forward(length)
    else:
        koch(length / 3, depth - 1)  # 左の1/3を描く
        turtle.left(60)              # 60度左へ
        koch(length / 3, depth - 1)  # 山の左斜面を描く
        turtle.right(120)            # 120度右へ
        koch(length / 3, depth - 1)  # 山の右斜面を描く
        turtle.left(60)              # 60度左へ
        koch(length / 3, depth - 1)  # 右の1/3を描く
        # ↑ 関数が自分自身を呼ぶ（再帰）ことで、同じパターンが無限に小さく繰り返される

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("cyan")
turtle.penup()
turtle.goto(-200, 100)  # 描き始める位置へ移動（ペンを上げたまま移動）
turtle.pendown()

for _ in range(3):   # 三角形の3辺それぞれにコッホ曲線を適用する
    koch(400, 4)     # 長さ400、深さ4でコッホ曲線を描く
    turtle.right(120)  # 120度回転して次の辺へ

turtle.done()