import turtle
import random

def love(x,y):
    lv=turtle.Turtle()
    lv.hideturtle()
    lv.up()
    lv.goto(x,y)
    def curveMove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)
    lv.color('red','pink')
    lv.speed(10000000)
    lv.pensize(1)
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curveMove()
    lv.left(120)
    curveMove()
    lv.forward(22)
    lv.write('张春',font=('Arial',12,'normal'),align='center')
    lv.left(140)
    lv.end_fill()

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 20:
            t.color('green')
            t.pensize(random.uniform((branchLen+5)/4-2,(branchLen+6)/4-2))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())
            t.up()
            t.backward(branchLen)
            t.color('brown')
            return
        t.pensize(random.uniform((branchLen+5)/4-2,(branchLen+6)/4-2))
        t.down()
        t.forward(branchLen)
        ang=random.uniform(15,45)
        t.right(ang)
        tree(branchLen-random.uniform(12,16),t)
        t.left(2*ang)
        tree(branchLen-random.uniform(12,16),t)
        t.right(ang)
        t.up()
        t.backward(branchLen)

myWin = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.speed(1)
t.left(90)
t.up()
t.backward(200)
t.down()
t.color('brown')
t.pensize(32)
t.forward(60)
tree(100,t)
myWin.exitonclick()

                      
    
