#import colorgram
import random
import turtle as t
import numpy as np

#rgb_colors = []
#colors = colorgram.extract('hirst_dots.jpg',20)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb_colors.append((r,g,b))
#
#print(rgb_colors)

rgb_colors = [(253, 251, 248), (253, 250, 252), (232, 251, 243), (199, 12, 32), (251, 238, 16), (39, 76, 190), (238, 227, 5), (38, 217, 68), (229, 159, 45), (27, 39, 158), (215, 75, 12), (15, 154, 15), (199, 14, 11), (242, 246, 251), (243, 34, 166), (231, 16, 121), (69, 10, 30), (61, 15, 8), (225, 141, 210), (10, 97, 62)]

tim = t.Turtle()
tim.speed('fastest')
tim.screen.colormode(255)
tim.penup()
tim.hideturtle()
x = 10
y = x
delta = 40
xy = int(180 + 45)
tim.setheading(xy)
tim.forward(delta*x*int(np.sqrt(2)))

for _ in range(y):
    tim.setheading(0)
    for _ in range(x):
        tim.forward(delta)
        tim.dot(20,random.choice(rgb_colors))
    tim.setheading(90)
    tim.forward(delta)
    tim.setheading(180)
    tim.forward(delta*x)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()



