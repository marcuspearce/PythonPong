# using python3

# module that allows basic graphics -> good for games
import turtle
import os 		# allows to interact w/ operating system using text commands

# Window 
win = turtle.Screen()
win.title("Pong by MP")		# title of window
win.bgcolor("black")
win.setup(width=800, height=600)	# 400 to -400 || 300 to -300
win.tracer(0)				# stops window from updating (so manually update) -> speeds up games


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=.5)
paddle_a.penup() 	# since default turtles draw line in motion
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("cyan")
paddle_b.shapesize(stretch_wid=5, stretch_len=.5)
paddle_b.penup() 	# since default turtles draw line in motion
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() 	# since default turtles draw line in motion
ball.goto(0,0)

baseSpeed = 3
ball.dx = baseSpeed		# change in speed - every time ball moves moves by 2 pixel
ball.dy = baseSpeed	


# Score variables 
score_a = 0
score_b = 0


# Pen - use to write text on scoreboard
pen = turtle.Turtle()
pen.speed(0)	# animation speed
pen.color("white")
pen.penup()
pen.hideturtle()

pen.goto(0,260)
# init score to 0 : 0
pen.write("Red: {}  Blue: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


# FUNCTIONS

# paddle motion
paddle_move_rate = 25
def paddle_a_up():
	y = paddle_a.ycor()		# .ycor() from turtle object
	y += paddle_move_rate		# add paddle_move_rate pixels to y var
	paddle_a.sety(y)
def paddle_a_down():
	y = paddle_a.ycor()		
	y -= paddle_move_rate	
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()		# .ycor() from turtle object
	y += paddle_move_rate	
	paddle_b.sety(y)
def paddle_b_down():
	y = paddle_b.ycor()		
	y -= paddle_move_rate	
	paddle_b.sety(y)


def updateScore():
	pen.clear()
	pen.write("Red: {}  Blue: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

def resetBallSpeed():
	ball.dx = baseSpeed
	ball.dy = baseSpeed

def incBallSpeed():
	ball.dx *= 1.2
	ball.dy *= 1.2


# Keyboard binding
win.listen()

win.onkeypress(paddle_a_up, "w")	# on keypress "w" call paddle_a_up func
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up, "Up")	# on keypress "w" call paddle_a_up func
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
	win.update()	#every time loop runs will update screen


	# move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


	# border checking - ball 

	#top border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1	# reverse direction in y direction
		# used to play sound -> mac specific || ampersand at end so that doesn't stop game loop for duration of sound
		os.system("afplay bounce.wav&")	
	#bottom border
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1	# reverse direction in y direction
		# used to play sound -> mac specific || ampersand at end so that doesn't stop game loop for duration of sound
		os.system("afplay bounce.wav&")
	#right border - WIN CONDITION
	if ball.xcor() > 390:
		ball.goto(0,0)	# put ball back in centre
		ball.dx *= -1 	# reverse starting direction of ball
		score_a += 1
		resetBallSpeed()
	#left border - WIN CONDITION
	if ball.xcor() < -390:
		ball.goto(0,0)	# put ball back in centre
		ball.dx *= -1 	# reverse starting direction of ball
		score_b += 1
		resetBallSpeed()


	# border checking - paddles

	# paddle a
	if paddle_a.ycor()+40 > 290:
		paddle_a.sety(290-40)		# don't allow to move any further up
	if paddle_a.ycor()-40 < -290:
		paddle_a.sety(-280+40)		# don't allow to move any further down
	# paddle b
	if paddle_b.ycor()+40 > 290:
		paddle_b.sety(290-40)		# don't allow to move any further up
	if paddle_b.ycor()-40 < -290:
		paddle_b.sety(-280+40)		# don't allow to move any further down



	# paddle and ball collisions

	# paddle a (left)
		# check if ball within area of paddle - NOTE y coords are not symmetric cuz centre of ball is not true centre (changes orientation w/ direction)
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)	# so doesn't get stuck inside paddle
		ball.dx *= -1
		incBallSpeed()	# speed of ball increases w/ each paddle hit
		# used to play sound -> mac specific || ampersand at end so that doesn't stop game loop for duration of sound
		os.system("afplay bounce.wav&")
	# paddle b (right)
		# check if ball within area of paddle
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
		ball.setx(340)	# so doesn't get stuck inside paddle
		ball.dx *= -1
		incBallSpeed()
		# used to play sound -> mac specific || ampersand at end so that doesn't stop game loop for duration of sound
		os.system("afplay bounce.wav&")

	# update score
	updateScore()








