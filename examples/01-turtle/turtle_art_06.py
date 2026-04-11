import turtle

turtle.speed(0)  # 最速で描く

for i in range(100):
    turtle.forward(i * 2)  # i が増えるにつれて線が長くなる
    turtle.right(91)       # 90度ではなく91度がポイント

turtle.done()