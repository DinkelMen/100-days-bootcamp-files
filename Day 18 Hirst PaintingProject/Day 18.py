import turtle
from turtle import Turtle, Screen
import random
from main import lis


timmy = Turtle()
timmy.shape('turtle')
timmy.color('DeepSkyBlue')

# for n in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
#
# for i in range(15):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
screen = Screen()
screen.colormode(255)
# colors = ['DeepSkyBlue', 'black', 'yellow', 'grey', 'red', 'orange', 'chocolate4', 'DeepPink', 'DeepPink4', 'pink']
# f = 0
# n = 3
# while n <= 10:
#     angle = 360 / n
#     timmy.pencolor(colors[f])
#     for i in range(n):
#         timmy.forward(100)
#         timmy.right(angle)
#     n += 1
#     f += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


timmy.pensize(1)
# for _ in range(100):
#     timmy.color(random_color())
#     dir = random.choice(['right', 'left', 'forward', 'backward'])
#     if dir == 'right':
#         timmy.right(90)
#     elif dir == 'left':
#         timmy.left(90)
#     elif dir == 'backward':
#         timmy.right(180)
#     else:
#         timmy.forward(20)
#     timmy.forward(20)

timmy.ht()
timmy.speed(10)
# for _ in range(130):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(4)
#     timmy.circle(100)


timmy.penup()
timmy.home()
row = -200
timmy.setpos(-200, -200)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(lis))
        timmy.forward(50)
    row += 50
    timmy.setpos(-200, row)


screen.exitonclick()
