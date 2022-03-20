from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(0,-280)
        self.setheading(90)
        self.mv_speed = 0

    def reset_position(self):
        self.goto(0,-280)

    def move(self):
        self.forward(self.mv_speed)

    def start(self):
        self.mv_speed = 10

    def stop(self):
        self.mv_speed = 0
