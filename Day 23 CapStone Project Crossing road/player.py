from turtle import Turtle
STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)
