from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_step = 15
        self.x_step = 15
        self.shape('circle')
        self.shapesize(1, 1)
        self.color('white')
        self.speed(1)
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_step *= -1

    def paddle_bounce(self):
        self.x_step *= -1





