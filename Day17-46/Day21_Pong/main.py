from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Field

import time

# Put constants at the t

# Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Belinda ❤s ping PONG")
screen.register_shape("ball.gif")
screen.tracer(0)

# Add objects
paddle_r = Paddle((350, 0), "red")
paddle_l = Paddle((-350, 0), "blue")
ball = Ball()
scoreboard = Scoreboard()
field = Field()

# Set up control buttons
screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeyrelease(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeyrelease(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeyrelease(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")
screen.onkeyrelease(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect goal to the right
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.point_l()

    # detect goal to the left
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.point_r()

screen.exitonclick()
