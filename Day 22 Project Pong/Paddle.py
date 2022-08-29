from turtle import Turtle


class Padle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.y = 0
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(self.x, self.y)

    def up(self):
        self.y += 30
        self.goto(self.x, self.y)

    def down(self):
        self.y -= 30
        self.goto(self.x, self.y)


