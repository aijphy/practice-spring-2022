from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#setup screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

#setup pong components:
l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()

# add pausing function:
paused = False
def pause():
    global paused
    if not paused :
        paused = True
    else:
        paused = False


# add event listeners:
screen.listen()
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_dn,"s")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_dn,"Down")
screen.onkeyrelease(l_paddle.stop,"w")
screen.onkeyrelease(l_paddle.stop,"s")
screen.onkeyrelease(r_paddle.stop,"Up")
screen.onkeyrelease(r_paddle.stop,"Down")
screen.onkeypress(pause," ")


game_is_on=True
while game_is_on:
    
    time.sleep(0.05)
    screen.update()

    if not paused:
        ball.move()
        l_paddle.move()
        r_paddle.move()


    # detect collision with wall
    if abs(ball.ycor()) > 280 :
        ball.bounce_y()
    
    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.xv > 0) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.xv < 0):
        ball.bounce_x()

    # check if scored
    if (ball.xcor() > 400):
        scoreboard.increase_l_score()
        ball.reset_position()

    if (ball.xcor() < -400):
        scoreboard.increase_r_score()
        ball.goto(0,0)
        ball.reset_position()

screen.exitonclick()
