import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = 0
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=player.move_player)

cars = []


def car_generate():
    for _ in range(17):
        car = CarManager()
        cars.append(car)


var = 0.11
car_generate()

game_is_on = True
while game_is_on:
    time.sleep(var)
    screen.update()
    scoreboard.update_scoreboard()
    for car in cars:
        if player.distance(car) < 23:
            scoreboard.game_over()
            game_is_on = False
        car.car_move()

    if player.ycor() >= 280:
        player.goto(0, -290)
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        var -= 0.01
        if var < 1:
            scoreboard.win()

screen.exitonclick()
