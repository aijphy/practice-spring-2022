from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xv = 20
        self.yv = 15
        self.mv_speed=0.5

    def move(self):
        self.goto(self.xcor()+self.xv*self.mv_speed,self.ycor()+self.yv*self.mv_speed)

    def bounce_y(self):
        self.yv *= -1

    def bounce_x(self):
        self.xv *= -1
        self.mv_speed += 0.05

    def reset_position(self):
        self.goto(0,0)
        self.xv *= -1
        self.mv_speed = 0.5
    