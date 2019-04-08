import turtle


def drawLine(draw):     # 绘制直线
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDight(dight):       # 绘制单个数字
    drawLine(True) if dight in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if dight in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if dight in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if dight in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if dight in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if dight in [0, 2, 3, 7, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if dight in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for i in date:
        drawDight(eval(i))


def main():
    turtle.Turtle().screen.delay(0)     # 设置无延迟
    turtle.setup(800, 350, 200, 200)
    turtle.pensize(5)
    turtle.speed(0)
    turtle.penup()
    turtle.fd(-300)
    drawDate('20190408')
    turtle.hideturtle()
    turtle.done()


main()
