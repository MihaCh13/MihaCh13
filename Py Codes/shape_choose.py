import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("black")
	brad.speed(8)
	brad.pensize(7)
	i = 0
	while i<=3:
		brad.forward(100)
		brad.right(90)
		i = i+1
	window.exitonclick()
def draw_circle():
	window = turtle.Screen()
	window.bgcolor("blue")
	katie = turtle.Turtle()
	katie.circle(100)
	katie.shape("arrow")
	katie.color("black")
	katie.speed(5)
	katie.pensize(6)
	window.exitonclick()
def draw_triangle():
	window = turtle.Screen()
	window.bgcolor("lightgreen")
	nicole = turtle.Turtle()
	nicole.shape("turtle")
	nicole.color("black")
	nicole.speed(9)
	nicole.pensize(6)
	nicole.forward(100)
	nicole.left(120)
	nicole.forward(100)
	nicole.left(120)
	nicole.forward(100)
	window.exitonclick()
def main():
	print("Turtle Menu : ")
	print("1. Draw a square turtle")
	print("2. Draw a circle turtle")
	print("3. Draw a triangle turtle")
	print("4. Exit")
	print("Enter your input number : 1, 2, 3,4")
	val = input("Input : ")
	val = int(val)
	if val==1:
		draw_square()
	elif val==2:
		draw_circle()
	elif val==3:
		draw_triangle()
	else:
		exit()
if __name__ == "__main__":
	main()
