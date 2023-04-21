from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color(color)
        self.speed("fastest")
        self.goto(position)
        self.setheading(90)

    # control movements with arrows
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


