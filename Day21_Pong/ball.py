from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("ball.gif")
        self.penup()
        self.color("white")
        self.speed("fastest")

    # control movements with arrows
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)