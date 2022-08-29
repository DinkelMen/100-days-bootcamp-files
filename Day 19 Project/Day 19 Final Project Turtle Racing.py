from turtle import Turtle, Screen
import random

screen = Screen()
choice = screen.textinput('Make your bet', 'Which turtle wil be the first? Enter a color of rainbow!')

# rafael = Turtle(shape='turtle')
# rafael.color('red')
#
# michelangelo = Turtle(shape='turtle')
# michelangelo.color('orange')
#
# tom = Turtle(shape='turtle')
# tom.color('yellow')
#
# tim = Turtle(shape='turtle')
# tim.color('green')
#
# josh = Turtle(shape='turtle')
# josh.color('blue')
#
# leonardo = Turtle(shape='turtle')
# leonardo.color('DeepSkyBlue')
#
# donatello = Turtle(shape='turtle')
# donatello.color('purple')

turtle_color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'DeepSkyBlue', 'purple']

y = 150.0
x = -250.0
turtles = []

for i in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle_color_list[i])
    new_turtle.penup()
    new_turtle.setpos(x=x, y=y)
    turtles.append(new_turtle)
    y -= 50

if choice:
    flag = True

border_turtle = Turtle()
border_turtle.hideturtle()
border_turtle.penup()
border_turtle.pensize(3)
border_turtle.pencolor('grey')
border_turtle.goto(-250, -200)
border_turtle.pendown()
border_turtle.forward(500)
border_turtle.left(90)
border_turtle.forward(400)
border_turtle.left(90)
border_turtle.forward(500)
border_turtle.left(90)
border_turtle.forward(400)


while flag:
    for turtle in turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 250:
            flag = False
            win_color = turtle.fillcolor()
            if choice == win_color:
                print('Congratulation! Tou win!')
            else:
                print(f'Sorry, you lose. Wn {win_color} turtle.')
            break

screen.exitonclick()
