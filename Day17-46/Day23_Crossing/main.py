import time
import random
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager, Road
from scoreboard import Scoreboard

TIMER = 0.1


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

# Add objects
road_lower = Road(-265)
road_upper = Road(270)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()




# Set up control button
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(TIMER)
    screen.update()

    # create cars
    car_manager.create_car()

    # move cars
    for car in car_manager.all_cars:
        # Move the car forward by a random distance
        car.backward(random.randint(1, 10))  # Modify this line to get the car's speed

        # Check if the car has reached the left edge of the screen
        if car.xcor() < -300:
            car.hideturtle()  # Optional: Hide the car when it goes off the screen
            car_manager.all_cars.remove(car)  # Remove the car from the list

    # if a car hits player
    for car in car_manager.all_cars:
        if player.distance(car) < 20:

            # if all lives lost, end game
            if scoreboard.lives < 1:
                game_is_on = False
                scoreboard.game_over()
            else:
                scoreboard.lose_life()
                player.reset()

    # reset when player when turtle reaches top
    if player.ycor() > 270:
        scoreboard.level_up()
        player.reset()
        TIMER *= 0.9




screen.exitonclick()