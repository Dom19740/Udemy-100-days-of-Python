from turtle import Turtle

FONT = ('ariel', 8, 'bold')


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.answer = None
        self.hideturtle()
        self.color("black")
        self.penup()

    def write_state(self, guess, x, y):
        self.answer = guess
        self.goto(x, y)
        self.write(self.answer, align="center", font=FONT)

    def game_over(self, number_to_guess):
        self.goto(0, 0)
        self.write(f"YOU GUESSED {number_to_guess} STATES. WELL DONE!!", align="center", font=FONT)