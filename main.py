
from turtle import Screen
from paddle import *
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time


# Creating a screen, main logic.


screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle(RIGHT_PADDLE_POSITION)
l_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
line.draw_line()

while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with the paddles

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
#     detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
