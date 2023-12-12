from turtle import*

bgcolor("black")
speed(0)
hideturtle()

for i in range(120):
    color("orange")
    circle(i * 0.5)
    color("yellow")
    circle(i*0.3)
    color("red")
    circle(i * 0.7)
    right(3)
    forward(3)

done()
