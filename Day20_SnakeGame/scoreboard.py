from turtle import Turtle

# Put constants at the top so you can change them easily
FONT = ('courier', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self, position, player):
        super().__init__()  # Inherit attributes and methods of Turtle Class, and expand on them
        self.keep_high_score()
        self.initialise_score(position, player)

    def keep_high_score(self):
        self.highscore = 0

    def initialise_score(self, position, player):
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.score = 0
        self.write(self.get_score_text(player), align="center", font=FONT)

    def update_score(self, player):
        self.clear()
        self.score += 1
        self.write(self.get_score_text(player), align="center", font=FONT)

    def get_score_text(self, player):
        # Helper method to generate the score text with score and highscore
        return f"{player} score: {self.score}. high score: {self.highscore}"

    def game_over(self):
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self, position, player):
        if self.score > self.highscore:
            self.highscore = self.score
        self.clear()
        self.initialise_score(position, player)
