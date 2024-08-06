import turtle

# Set the turtle's speed to the maximum
turtle.speed(0)

# Define the flag's dimensions
flag_width = 300
flag_height = 200

def draw_blue_field():
    # Move the turtle to the starting position of the blue field
    turtle.penup()
    turtle.goto(-flag_width / 2, flag_height / 2)

    # Draw the blue field
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(flag_width)
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.right(90)
    turtle.forward(flag_width)
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.end_fill()

def draw_white_stripe():
    # Move the turtle to the starting position of the white stripe
    turtle.penup()
    turtle.goto(-flag_width / 2, flag_height / 2)

    # Draw the white stripe
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.right(90)
    turtle.forward(flag_width / 13)
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.right(90)
    turtle.forward(flag_width / 13)
    turtle.end_fill()

def draw_red_stripe():
    # Move the turtle to the starting position of the red stripe
    turtle.penup()
    turtle.goto(-flag_width / 2 + flag_width / 13, flag_height / 2 - flag_height / 2)

    # Draw the red stripe
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(flag_width * 11 / 13)
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.right(90)
    turtle.forward(flag_width * 11 / 13)
    turtle.right(90)
    turtle.forward(flag_height / 2)
    turtle.end_fill()

def draw_white_star():
    # Move the turtle to the starting position of the first white star
    turtle.penup()
    turtle.goto(-flag_width / 2 + flag_width / 13 + flag_width / 13 / 2, flag_height / 2 - flag_height / 2 + flag_height / 2 / 5)

    # Draw the first white star
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(flag_height / 10)
    turtle.right(144)
    turtle.forward(flag_height / 10)
    turtle.right(144)
    turtle.forward(flag_height / 10)
    turtle.right(144)
    turtle.forward(flag_height / 10)
    turtle.right(144)
   
    turtle.mainloop()