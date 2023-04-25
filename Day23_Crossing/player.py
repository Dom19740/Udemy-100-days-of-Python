from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black", "green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # control movements with arrows
    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    # rest when get to top of screen
    def reset(self):
        self.goto(STARTING_POSITION)


