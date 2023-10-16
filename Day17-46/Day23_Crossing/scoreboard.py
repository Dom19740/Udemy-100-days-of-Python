from turtle import Turtle

# Put constants at the top so you can change them easily
LIVES = 2
FONT = ('courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = LIVES
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"Lives: {self.lives}, Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)