from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Road:
    def __init__(self, y_pos):
        super().__init__()
        start_line = Turtle()
        start_line.hideturtle()
        start_line.penup()
        start_line.width(5)
        start_line.setpos(-280, y_pos)
        start_line.pendown()
        start_line.forward(560)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_distance = 0

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 250)
            new_car.setpos(300, random_y)
            self.all_cars.append(new_car)
            self.car_distance = random.randint(1, 10)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_distance)


