from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# define instances:
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# add pausing function:
paused = False
def pause():
    global paused
    if not paused :
        paused = True
    else:
        paused = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# make screen listen for input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(pause,"space")

# main game loop:
game_is_on = True
while game_is_on:
    screen.update()
    if not paused:
        code = snake.move()
        if code == 1:
            scoreboard.game_over()
            snake.reset()
            time.sleep(1)
            scoreboard.reset()
            pause()
            #game_is_on = False
            #break
        if snake.turtles[0].distance(food) < 15:
            food.refresh()
            snake.addturtle()
            scoreboard.increase_score()
        time.sleep(0.1)



screen.exitonclick()


