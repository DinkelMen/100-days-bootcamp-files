from turtle import Turtle

with open('high_score.txt') as file:
    # for line in file:
    MAX = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = MAX
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.high_score < self.score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as f:
                f.write(str(self.high_score))
        self.write(f"Score: {self.score}  Highest score: {self.high_score} ", align='center', font=('Arial', 14, 'normal'))

    def reset(self):
        # self.high_score = MAX
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.color('white')
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f'Game over', align='center', font=('Arial', 32, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
