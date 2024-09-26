import math
import turtle
# 爱心
def heart():
    t.pensize(9)
    t.setheading(90)
    t.penup()
    t.color("deeppink")
    t.goto(-125, -135)
    t.pendown()
    t.begin_fill()
    t.fillcolor('deeppink')
    t.circle(9, 211)
    t.fd(9 * 2.4)
    t.lt(90)
    t.fd(9 * 2.4)
    t.circle(9, 211)
    t.end_fill()
# 头
def head():
    t.pensize(8)
    t.pencolor("black")
    t.penup()
    t.goto(-130, 170)
    t.pendown()
    t.setheading(220)
    for x in range(580):
        t.forward(1)
        if x < 250:
            t.left(0.5)
        elif x < 350:
            t.left(0.1)
        else:
            t.left(0.5)
# 耳朵
def ears():
    t.setheading(70)
    for i in range(150):
        t.forward(1)
        if i < 80:
            t.left(0.2)
        elif i < 90:
            t.left(10)
        else:
            t.left(0.2)
    t.setheading(160)
    for i in range(140):
        t.forward(1)
        t.left(0.15)
    t.setheading(140)
    for i in range(157):
        t.forward(1)
        if i < 65:
            t.left(0.2)
        elif i < 75:
            t.left(8)
        else:
            t.left(0.5)
# 眼睛
def eyes():
    # 左眼
    t.pensize(5)
    t.penup()
    t.goto(-100, 60)
    t.setheading(350)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    step = 0.3
    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.02
            else:
                step -= 0.02
            t.forward(step)
            t.left(3)
    t.end_fill()
    # 右眼
    t.penup()
    t.goto(50, 40)
    t.setheading(350)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    step = 0.3
    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.02
            else:
                step -= 0.02
            t.forward(step)
            t.left(3)
    t.end_fill()
# 鼻子
def nose():
    t.penup()
    t.goto(-40, 30)
    t.setheading(260)
    t.pendown()
    t.fillcolor("#ebc80e")
    t.begin_fill()
    step = 0.3
    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.02
            else:
                step -= 0.02
            t.forward(step)
            t.left(3)
    t.end_fill()
# 小花
def flower(n):
    for i in range(n):
        t.forward(0.5)
        if i < 80:
            t.left(1)
        elif i < 120:
            t.left(2.3)
        else:
            t.left(1)
# 花朵
def flowers():
    t.penup()
    t.goto(20, 180)
    t.pendown()
    t.fillcolor("#dd4a76")
    t.begin_fill()
    t.setheading(175)
    flower(200)
    t.setheading(250)
    flower(200)
    t.setheading(325)
    flower(200)
    t.setheading(40)
    flower(200)
    t.setheading(115)
    flower(170)
    t.end_fill()
    t.penup()
    t.goto(30, 180)
    t.setheading(270)
    t.pendown()
    t.fillcolor("#e7be04")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
# 胡须
def beard():
    t.penup()
    t.goto(-150, 65)
    t.pendown()
    t.setheading(170)
    t.pensize(6)
    for y in range(40):
        t.forward(1)
        t.left(0.3)
    t.penup()
    t.goto(-150, 85)
    t.pendown()
    t.setheading(160)
    for y in range(50):
        t.forward(1)
        t.left(0.3)
    t.penup()
    t.goto(-150, 45)
    t.pendown()
    t.setheading(180)
    for y in range(55):
        t.forward(1)
        t.left(0.3)
    t.penup()
    t.goto(110, 10)
    t.setheading(340)
    t.pendown()
    for y in range(40):
        t.forward(1)
        t.right(0.3)
    t.penup()
    t.goto(120, 30)
    t.setheading(350)
    t.pendown()
    for y in range(30):
        t.forward(1)
        t.right(0.3)
    t.penup()
    t.goto(115, 50)
    t.setheading(360)
    t.pendown()
    for y in range(50):
        t.forward(1)
        t.right(0.3)
def myarc(t, r, angle):
    length = 2 * math.pi * r * angle / 360  # angle角度的扇形的弧长
    n = int(length / 3) + 1  # 线段条数
    step_length = length / n  # 每条线段的长度
    step_angle = angle / n  # 每条线段的角度
    polyline(t, n, step_length, step_angle)
def polyline(t, n, length, angle):
    for index in range(n):
        t.fd(length)
        t.lt(angle)
# 身体
def body():
    t.pensize(8)
    t.penup()
    t.goto(-100, -30)
    t.setheading(230)
    t.pendown()
    t.fillcolor("#efa9c1")
    t.begin_fill()
    for z in range(140):
        t.forward(1)
        t.left(0.2)
    t.setheading(340)
    for z in range(200):
        t.forward(1)
        t.left(0.1)
    t.setheading(85)
    for z in range(140):
        t.forward(1)
        t.left(0.1)
    t.end_fill()
    t.penup()
    t.goto(-73, -33)
    t.pendown()
    t.setheading(250)
    t.fillcolor("#da4b76")
    t.begin_fill()
    myarc(t, 40, 205)
    t.setheading(170)
    t.pensize(6)
    t.forward(75)
    t.end_fill()
    # 左胳膊
    t.pensize(8)
    t.penup()
    t.goto(-120, -17)
    t.setheading(230)
    t.pendown()
    t.fillcolor("#d64b75")
    t.begin_fill()
    t.forward(50)
    t.setheading(320)
    for k in range(27):
        t.forward(1)
        t.left(1)
    t.setheading(55)
    for k in range(50):
        t.forward(1)
        t.right(0.1)
    t.end_fill()
    # 左手
    t.penup()
    t.goto(-125, -15)
    t.setheading(140)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.forward(8)
    t.setheading(50)
    myarc(t, 10, 190)
    t.setheading(150)
    for j in range(80):
        t.forward(1)
        t.left(2.2)
    t.forward(24)
    t.end_fill()
    # 右胳膊
    t.penup()
    t.goto(27, -45)
    t.pendown()
    t.fillcolor("#db4e79")
    t.setheading(350)
    t.begin_fill()
    for x in range(50):
        t.forward(1)
        t.right(1)
    t.setheading(220)
    t.forward(40)
    t.setheading(100)
    for x in range(50):
        t.forward(1)
        t.left(0.2)
    t.end_fill()
    # 右手
    t.penup()
    t.goto(70, -75)
    t.pendown()
    t.setheading(300)
    t.forward(8)
    t.setheading(30)
    for x in range(40):
        t.forward(1)
        t.right(5)
    t.setheading(280)
    for x in range(70):
        t.forward(1)
        t.right(2)
    # 右脚
    t.penup()
    t.goto(-70, -180)
    t.pendown()
    t.setheading(250)
    for x in range(30):
        t.forward(1)
        t.left(0.3)
    for x in range(160):
        t.forward(1)
        if x < 30:
            t.left(3)
        elif x < 65:
            t.left(0.1)
        else:
            t.left(1)
    # 左脚
    t.penup()
    t.goto(-150, -210)
    t.setheading(340)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    step = 1.5
    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.1
            else:
                step -= 0.1
            t.forward(step)
            t.left(3)
    t.end_fill()
# 主函数
turtle.setup(1.0, 1.0)
turtle.title("hellokitty!")
turtle.bgcolor("pink")
t = turtle.Turtle()
t.hideturtle()
t.screen.delay(0)
head()
ears()
eyes()
nose()
beard()
flowers()
body()
heart()
turtle.mainloop()
