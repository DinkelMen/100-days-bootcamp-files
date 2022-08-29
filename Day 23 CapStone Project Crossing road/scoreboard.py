from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-200, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 200)
        self.clear()
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)

    def win(self):
        self.goto(0, 0)
        self.write('You win!\nYou have passed 10 levels!', align='center', font=FONT)
