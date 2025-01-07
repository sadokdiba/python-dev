import turtle as t
import random

colors = ["red", "blue", "green", "purple", "orange", "pink", "brown", "black", 
    "gray", "cyan", "magenta", "black", "indigo", "violet", "gold", "silver",
]
tim = t.Turtle()

# directions = [0, 90, 180, 270]

angle = 90
def random_turn():
    if random.choice([True, False]):
        tim.left(angle)
    else:
        tim.right(angle)

tim.pensize(10)
tim.speed(10)

for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(30)
    random_turn()
    # tim.setheading(random.choice(directions))

















screen=t.Screen()
screen.exitonclick()
