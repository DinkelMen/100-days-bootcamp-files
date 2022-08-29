from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y = random.randint(-260, 270)
        self.x = random.randint(300, 900)
        self.shape('square')
        self.shapesize(1, 3)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(self.x, self.y)

    def car_move(self):
        if self.xcor() > -320:
            x = self.xcor()
            x -= STARTING_MOVE_DISTANCE
            self.goto(x, self.y)
            if x < -300:
                self.goto(330, random.randint(-270, 270))
