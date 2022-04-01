from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("high_score.txt", "r") as hs_file:
            self.high_score = (int) (hs_file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = "center", font=("Arial",24,"normal"))
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.update_high_score()
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align = "center", font=("Arial",50,"normal","bold"))
        self.goto(0,-30)
        self.write(f"Score: {self.score}", align = "center", font=("Arial",24,"normal"))
        

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as hs_file:
            hs_file.write(f"{self.high_score}")


    def reset(self):
        self.goto(0,270)
        self.score = 0
        self.update_scoreboard()
