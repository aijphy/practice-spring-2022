from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", align = 'center',  font=("Courier",80,'normal'))
        

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

        
    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
