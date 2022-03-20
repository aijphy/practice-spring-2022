from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Scoreboard
import random
import time

#setup screen:
screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.setup(width=600,height=600)
screen.title("Turtle Crossing")

#main player:
tim = Player()

# level counter:
scoreboard = Scoreboard()

# add pause functionality:
paused = False
def pause():
    global paused

    if not paused :
        paused = True

    else:
        paused = False

# setup event listeners:
screen.listen()
screen.onkeypress(tim.start,"Up")
screen.onkeyrelease(tim.stop,"Up")
screen.onkey(pause,"space")


# get cars randomly placed instead of all coming at the same time
car_prob = 0.2
cars = Cars()
for _ in range(200):
    #add car?
    if random.random() < car_prob:
        cars.add_car()
    cars.move()
screen.update()


# main game loop:
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if not paused:
        #add car?
        if random.random() < car_prob:
            cars.add_car()
        cars.move()
        tim.move()

        if tim.ycor() > 280:
            cars.speedup()
            tim.reset_position()
            scoreboard.updatelevel()

        hit = False
        for car in cars.list:
            if abs(car.ycor() - tim.ycor()) < 20 and abs(car.xcor() - tim.xcor()) < 20:
                scoreboard.game_over()
                game_is_on = False


screen.exitonclick()