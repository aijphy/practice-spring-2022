from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xv = self.yv = 20

    def move(self):
        self.goto(self.xcor()+self.xv,self.ycor()+self.yv)