from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

print('here1')
screen = Screen()
print('here1.1')
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
print('here2')

l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_dn,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_dn,"Down")


ball = Ball()


game_is_on=True
while game_is_on:
    screen.update()

    ball.move()
    time.sleep(0.1)

screen.exitonclick()
