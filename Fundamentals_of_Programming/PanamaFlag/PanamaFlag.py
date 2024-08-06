# File: PanamaFlag.py

# Description of Program: Program uses turtle functions to draw an image of the Flag of Panama.

import turtle

myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)

def Rectangles ( flag, x, y, length, width, color ):
    flag.penup ()
    flag.goto (x,y)
    flag.setheading (0)
    flag.pendown ()

    flag.fillcolor(color)
    flag.begin_fill()

    for count in range (2):
        flag.forward (length)
        flag.right (90)
        flag.forward (width)
        flag.right (90)
    flag.end_fill()
    flag.penup ()

def Draw_Stars (flag, x, y, length, color):
    flag.penup()
    flag.goto(x,y)
    flag.setheading (288)
    flag.pendown ()

    flag.fillcolor(color)
    flag.begin_fill()

    for i in range(5):
        Bobby.forward(length)
        Bobby.left(72)
        Bobby.forward(length)
        Bobby.right(144)
    flag.end_fill()
    flag.penup ()


Bobby = turtle.Turtle ()
Bobby.speed (10)
Bobby.pensize (3)
Bobby.screen.colormode(255)

Rectangles(Bobby, -300, 0, 300, 200, myBlue)
Rectangles(Bobby, 0, 200, 300, 200, myRed)
Rectangles(Bobby, 0, 0, 300, 200, white)
Rectangles(Bobby, -300, 200, 300, 200, white)

Draw_Stars(Bobby, -150, 150, 42, myBlue)
Draw_Stars(Bobby, 150, -50, 42, myRed)

Bobby.hideturtle()
turtle.done()
