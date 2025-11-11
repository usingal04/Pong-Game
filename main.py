from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title('Pong Game!')
screen.bgcolor('black')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.xcor() > 330 and ball.distance(r_paddle) < 50) or (ball.xcor() < -330 and ball.distance(l_paddle) < 50) :
        ball.paddle_bounce()

    if (ball.xcor() > 380):
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()
        ball.x_move *= 1.1
        ball.y_move * 1.1

    if (ball.xcor() < -380):
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()
        ball.x_move *= 1.1
        ball.y_move * 1.1

    if (scoreboard.l_score >= 10 or scoreboard.r_score >= 10):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
