from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
STARTING_POSITIONS = ((350,0),(-350,0))

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
game_is_on = True
screen.tracer(0)


r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_x()


    # Detect collision with the paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_y()


    # Detect if paddles miss the ball
    scoreboard.keep_score()

    if ball.xcor() > 390 and ball.distance(r_paddle) > 50:
        ball.home()
        scoreboard.update_left()
        ball.move_speed = 0.1
    if ball.xcor() < -390 and ball.distance(l_paddle) > 50:
        ball.home()
        scoreboard.update_right()
        ball.move_speed = 0.1

screen.exitonclick()
