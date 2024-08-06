import turtle

def drawSquare (ttl, x, y, length):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range(4):
        ttl.forward(length)
        ttl.right(90)
    ttl.penup()


Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)
drawSquare(Bob, 0, 0, 100)


def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.penup()
    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.goto(x3,y3)
    ttl.goto(x1,y1)
    ttl.penup()

Tom = turtle.Turtle()
Tom.speed(10)
Tom.pensize(3)

Tom.pencolor(1,0,0)
drawTriangle(Tom, 0,0,50,100,100,0)
Tom.pencolor(0,1,0)
drawTriangle(Tom,0,0,50,-100,100,0)
Tom.hideturtle()

turtle.done()
