from turtle import Screen, Turtle
import numpy as np

# initialize previous positions:
a = [[1.0,1.0]]
pos = np.array(a)

# functions to turn players
def right():
    snake.setheading(0)

def up():
    snake.setheading(90)

def left():
    snake.setheading(180)

def down():
    snake.setheading(270)

def lizright():
    lizard.setheading(0)

def lizup():
    lizard.setheading(90)

def lizleft():
    lizard.setheading(180)

def lizdown():
    lizard.setheading(270)

# main loop of game, move each player and check if they have crossed a path
def movesnake():
    global pos
    snake.forward(20)
    lizard.forward(20)

    nx,ny = np.round(snake.pos())
    mx,my = np.round(lizard.pos())
    newn = [[nx,ny]]
    newm = [[mx,my]]
    for a in pos:
        x=a[0]
        y=a[1]
        if x == nx and y == ny:
            print('game over: lizard wins!')
            screen.bye()
        if x == mx and y == my:
            print('game over: snake wins!')
            screen.bye()
    pos = np.append(pos,newn,axis=0)
    pos = np.append(pos,newm,axis=0)


    screen.ontimer(movesnake, 300)

# create the players
snake = Turtle("turtle")
snake.speed(0)
snake.color("green")

lizard = Turtle("turtle")
lizard.shape('classic')
lizard.speed(0)
lizard.color("brown")
lizleft()

# assign buttons
screen = Screen()

screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(down, "Down")

screen.onkey(lizright, "d")
screen.onkey(lizup, "w")
screen.onkey(lizleft, "a")
screen.onkey(lizdown, "s")

# let the games begin!
screen.listen()
movesnake()
screen.mainloop()
