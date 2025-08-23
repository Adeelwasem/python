import turtle
turtle.Screen().bgcolor("lavender")
turtle.Screen().setup(300,400)
pen = turtle.Turtle()


num_sides = 4
side_length = 90
angle = 360.0 / num_sides


for i in range(6):
    pen.forward(side_length)
    pen.right(angle)

turtle.done