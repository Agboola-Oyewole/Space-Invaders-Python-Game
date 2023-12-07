from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 2
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(370, 280)
        self.write(f'Lives: {self.lives}  |  Score: {self.score}', align="right",
                   font=("Courier", 14, "bold"))

    def count_point(self):
        self.score += 20
        self.update_scoreboard()

    def count_bonus_point(self):
        self.score += 100
        self.update_scoreboard()

    def count_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('white')
        self.write(f'The aliens took over the galaxy, you lose. '
                   f'Your Score is {self.score}', align="center", font=("Courier", 15, "bold"))

    def game_won(self):
        self.clear()
        self.goto(0, 0)
        self.color('white')
        self.write(f'You saved the galaxy!, Your Score is {self.score}', align="center", font=("Courier", 20, "bold"))
