import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("pink")

for i in range(36):        # 36回、少しずつ回転させながら繰り返す
    for j in range(2):     # その中で「円を描いて180度回転」を2回（ループの中のループ＝ネスト）
        turtle.circle(100) # 半径100の円を描く
        turtle.right(180)  # 180度回転して、もう1枚の花びらを描く位置へ
    turtle.right(10)       # 花びら1枚分が終わったら10度回転して次の花びらへ

turtle.done()