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



    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_dn(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
