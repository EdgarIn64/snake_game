import turtle
import time
import random

wait = 0.1

# Settings for the Window
wn = turtle.Screen()
wn.title("Snake Python")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


# Snake Head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "left"

# Food
food = turtle.Turtle()
snakeHead.shape("circle")
snakeHead.color("red")
snakeHead.penup()
snakeHead.goto(0,100)


# Functions
def up():
	snakeHead.direction = "up"
def right():
	snakeHead.direction = "right"
def down():
	snakeHead.direction = "down"
def left():
	snakeHead.direction = "left"

def mov():
	if snakeHead.direction == "up" :
		y = snakeHead.ycor()
		snakeHead.sety(y + 20)
	elif snakeHead.direction == "right" :
		x = snakeHead.xcor()
		snakeHead.setx(x + 20)
	elif snakeHead.direction == "down" :
		y = snakeHead.ycor()
		snakeHead.sety(y - 20)
	elif snakeHead.direction == "left" :
		x = snakeHead.xcor()
		snakeHead.setx(x - 20)

# Keyboard
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(right, "Right")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")

while True :
	wn.update()

	if snakeHead.distance(food) < 20 :
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x, y)

	mov()
	time.sleep(wait)

