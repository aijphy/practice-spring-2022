from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font=("Arial",24,"normal"))
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align = "center", font=("Arial",50,"normal","bold"))
        self.goto(0,-30)
        self.write(f"Score: {self.score}", align = "center", font=("Arial",24,"normal"))
