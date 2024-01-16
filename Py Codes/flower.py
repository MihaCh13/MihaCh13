import turtle 
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
radius = 60
t.pensize(2)
color = ['red','white','red']
for x in range(12):
    t.color(color[x%3])
    for i in range(8):
        t.circle(radius)
        t.right(60)
        radius = radius + 4
