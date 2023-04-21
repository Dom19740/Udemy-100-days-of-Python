from turtle import Turtle

START_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("ball.gif")
        self.penup()
        self.color("white")
        self.x_move = START_SPEED
        self.y_move = START_SPEED
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        print(self.move_speed)

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
