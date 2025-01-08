from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=1000, height=700)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "brown", "green", "blue","purple"]

x = -470
y = -95

all_turtles = []

for index in range(6):
    doc = Turtle(shape="turtle")
    doc.shapesize(1.7)
    doc.penup()
    doc.goto(x, y)
    doc.color(colors[index])
    y += 45
    all_turtles.append(doc)

is_game_on = True
while is_game_on:
    for turtle in all_turtles:
        turtle.speed("fast")
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 470:
            is_game_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won, the winner is {winner} Turtle")
            else:
                print((f"You've lost, the winner is {winner} Turtle"))
    
screen.exitonclick()