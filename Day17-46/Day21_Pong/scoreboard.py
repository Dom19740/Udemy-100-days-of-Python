from turtle import Turtle

# Put constants at the top so you can change them easily
FONT = ('impact', 60, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l,  align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=FONT)

    def point_l(self):
        self.score_l += 1
        self.update_scoreboard()

    def point_r(self):
        self.score_r += 1
        self.update_scoreboard()


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        for step in range(15):
            self.setheading(90)
            self.width(5)
            self.forward(20)  # Draw dash
            self.penup()  # Lift pen up
            self.forward(20)  # Move without drawing (gap)
            self.pendown()  # Put pen down again
