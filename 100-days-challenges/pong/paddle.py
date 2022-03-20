from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(350, 0)
        self.goto(x,0)
        self.vel = 0

    def move(self):
        new_y = self.ycor() + self.vel
        new_y = min(new_y, 250)
        new_y = max(new_y,-250)
        self.goto(self.xcor(), new_y)

    def go_up(self):
        self.vel = 25

    def go_dn(self):
        self.vel = -25
        #new_y = max(self.ycor() - 20,-250)
        #self.goto(self.xcor(), new_y)

    def stop(self):
        self.vel = 0

