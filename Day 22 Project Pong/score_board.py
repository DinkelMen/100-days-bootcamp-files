from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.goto(0, -300)
        self.setheading(90)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-90, 240)
        self.clear()
        self.write(f"{self.score1}", align='center', font=('Arial', 40, 'normal'))
        self.goto(90, 240)
        self.write(f"{self.score2}", align='center', font=('Arial', 40, 'normal'))
