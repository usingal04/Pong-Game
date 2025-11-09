from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(height=600, width=800)
screen.title('Pong Game!')
screen.bgcolor('black')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
