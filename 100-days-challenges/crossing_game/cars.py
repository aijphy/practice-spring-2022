from turtle import Turtle
import random

class Cars():

    def __init__(self):
        super().__init__()
        self.list = []
        for i in range(3):
            self.add_car()
        self.mv_speed = 10

    def add_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1,2)
        ran = random.randint(1,6)
        if ran == 1:
            car.color("purple")
        if ran == 2:
            car.color("red")
        if ran == 3:
            car.color("blue")
        if ran == 4:
            car.color("yellow")
        if ran == 5:
            car.color("green")
        if ran == 6:
            car.color("orange")


        car.penup()
        y = random.randint(-240,240)
        car.goto(300,y)
        self.list.append(car)

    def move(self):
        for car in self.list:
            car.goto(car.xcor()-self.mv_speed,car.ycor())

    def speedup(self):
        self.mv_speed += 2
    