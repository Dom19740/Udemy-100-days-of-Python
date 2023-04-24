import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Road
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

player = Player()
road_lower = Road(-265)
road_upper = Road(270)

# Set up control button
screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # reset when turtle reaches top
    if player.ycor() > 270:
        player.reset()




screen.exitonclick()