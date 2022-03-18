from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? (Enter a color): ")
print(f"You bet on {user_bet}")
colors = ["red","orange","yellow","green","blue","purple"]
yp=-90
all_turtles = []

tim = Turtle()
tim.speed(0)
tim.penup()
tim.setheading(90)
tim.goto(220,-200)
for i in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
tim.penup()
tim.color("green")
tim.goto(-215,-200)
for i in range(10):
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()
tim.hideturtle()

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y = yp+turtle_index*40)
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while(is_race_on):
    for tim in all_turtles:
        if tim.xcor() > 195:
            winner = tim.pencolor()
            if winner == user_bet:
                print(f"You've won! {winner} won the race!")
            else:
                print(f"You've lost! {winner} won the race!")
            is_race_on = False
        rand_dist = random.randint(0,10)
        tim.forward(rand_dist)

screen.exitonclick()
