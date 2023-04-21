from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Put constants at the t
BALLSPEED = 0.1  # Lower is faster

# Set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Belinda ❤s ping PONG")
screen.register_shape("ball.gif")
screen.tracer(0)  # turn off screen animation

# Add objects
paddle_r = Paddle((350, 0), "red")
paddle_l = Paddle((-350, 0), "blue")
ball = Ball()

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
    time.sleep(BALLSPEED)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    else:
        ball.move()




screen.exitonclick()
