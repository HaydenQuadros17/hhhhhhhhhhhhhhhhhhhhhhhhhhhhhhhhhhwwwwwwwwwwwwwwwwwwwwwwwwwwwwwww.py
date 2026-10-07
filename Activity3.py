import turtle

# Create the turtle
t = turtle.Turtle()

# Set background colour
turtle.bgcolor("lightblue")

# Set pen colour
t.pencolor("purple")

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()