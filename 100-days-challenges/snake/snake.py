from turtle import Turtle
COLOR = "green"


class Snake():

    def __init__(self):
        self.turtles = []
        for i in range(3):
            tim = Turtle()
            tim.speed(0)
            tim.penup()
            tim.shape("square")
            tim.color(COLOR)
            x = -i*20
            p = (x,0)
            tim.goto(p)
            self.turtles.append(tim)

    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            kid = self.turtles[i]
            newx = self.turtles[i-1].xcor()
            newy = self.turtles[i-1].ycor()
            if kid.distance(self.turtles[0]) < 5:
                 return 1
            kid.goto(newx,newy)
            kid.setheading(self.turtles[i-1].heading())
        self.turtles[0].forward(20)
        if abs(self.turtles[0].xcor()) > 280 or abs(self.turtles[0].ycor()) > 280:
            return 1
        return 0    

    def addturtle(self):
        new = Turtle()
        new.penup()
        x = self.turtles[len(self.turtles)-1].xcor()
        y = self.turtles[len(self.turtles)-1].ycor()
        new.color(COLOR)
        new.shape("square")
        new.goto(x,y)
        self.turtles.append(new)



    def up(self):
        if(self.turtles[1].heading() != 270):
            self.turtles[0].setheading(90)

    def down(self):
        if(self.turtles[1].heading() != 90):
            self.turtles[0].setheading(270)

    def left(self):
        if(self.turtles[1].heading() != 0):
            self.turtles[0].setheading(180)

    def right(self):
        if(self.turtles[1].heading() != 180):
            self.turtles[0].setheading(0)

    def reset(self):
        for tim in self.turtles:
            tim.reset()
        #self.turtles[:].reset()
        self.__init__()
