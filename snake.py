import turtle
import time

wait = 0.1

# Settings for the Window
wn = turtle.Screen()
wn.title("Snake Python")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


# Snake Head
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "left"

# Functions

def mov():
	if cabeza.direction == "up" :
		y = cabeza.ycor()
		cabeza.sety(y + 20)
	elif cabeza.direction == "right" :
		x = cabeza.xcor()
		cabeza.setx(x + 20)
	elif cabeza.direction == "down" :
		y = cabeza.ycor()
		cabeza.sety(y - 20)
	elif cabeza.direction == "left" :
		x = cabeza.xcor()
		cabeza.setx(x - 20)

while True :
	wn.update()
	mov()
	time.sleep(wait)

