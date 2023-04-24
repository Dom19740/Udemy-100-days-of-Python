from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    pass


class Road:
    def __init__(self, y_pos):
        super().__init__()
        start_line = Turtle()
        start_line.hideturtle()
        start_line.penup()
        start_line.setpos(-280, y_pos)
        start_line.pendown()
        start_line.forward(560)
