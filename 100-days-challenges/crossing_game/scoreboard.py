from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,280)
        self.level = 0
        self.updatelevel()

    def updatelevel(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}')
    
    def reset_level(self):
        self.level = 0
        self.updatelevel()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game Over',align="center")
        self.goto(0,-20)
        self.write(f'Max level: {self.level}',align="center")

    
