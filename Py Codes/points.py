import random
import turtle 
colors = [(237, 225, 204), (199, 159, 112), (106, 108, 126), (217, 217, 225), (236, 216, 226), (139, 140, 152),
          (157, 78, 47), (220, 208, 128), (194, 149, 171), (165, 148, 62), (221, 230, 223), (42, 28, 12),
          (151, 26, 11), (20, 21, 50), (113, 117, 155), (17, 31, 17), (221, 173, 194), (133, 81, 93),
          (192, 98, 78),
          (37, 17, 32), (232, 174, 162), (50, 51, 104), (147, 23, 32), (155, 167, 158), (172, 99, 118),
          (90, 102, 91),
          (185, 184, 212), (74, 74, 37), (53, 71, 54), (183, 198, 184), (118, 134, 121), (182, 195, 199),
          (206, 206, 37), (114, 133, 139)]

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.penup()
t.setheading(225)
t.forward(250)
t.setheading(180)
t.forward(50)
t.pendown()

for i in range(10):
    for number_of_step in range(10):
        t.setheading(0)
        t.dot(20, random.choice(colors))
        t.penup()
        t.forward(50)
    t.setheading(90)
    t.penup()
    t.forward(50)
    t.setheading(180)
    for number in range(10):
        t.penup()
        t.forward(50)
t.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
