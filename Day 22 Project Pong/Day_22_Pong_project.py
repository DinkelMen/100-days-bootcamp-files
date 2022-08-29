from turtle import Screen
from Paddle import Padle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Padle(350)
left_paddle = Padle(-350)

screen.tracer(1)
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

speed = 1

game_on = True
while game_on:
    screen.update()
    ball.move()
    # Collision with wall
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce()
    # Collision with paddles
    for i in range(9):
        right_y = right_paddle.ycor() + 40 - i * 10
        left_y = left_paddle.ycor() + 40 - i * 10
        if ball.distance(350, right_y) <= 20:
            ball.paddle_bounce()
            speed += 0.2
            ball.speed(speed)

        elif ball.distance(-350, left_y) <= 20:
            ball.paddle_bounce()
            speed += 0.1
            ball.speed(speed)

    # Out of border
    if ball.xcor() > 410:
        scoreboard.score1 += 1
        scoreboard.update_scoreboard()
        screen.tracer(0)
        ball.home()
        screen.update()
        time.sleep(1)
        screen.tracer(1)
        ball.speed(1)
        ball.paddle_bounce()
    elif ball.xcor() < -410:
        scoreboard.score2 += 1
        scoreboard.update_scoreboard()
        screen.tracer(0)
        ball.home()
        screen.update()
        time.sleep(1)
        screen.tracer(1)
        ball.speed(1)
        ball.paddle_bounce()
    continue


screen.exitonclick()

