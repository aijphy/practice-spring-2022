import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim = t.Turtle()
tim.speed("fastest")
tim.screen.colormode(255)

n_circles = 30
delta = int(360/n_circles)
deg = 0
while deg < 360:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(deg)
    deg += delta

screen = t.Screen()
screen.exitonclick()