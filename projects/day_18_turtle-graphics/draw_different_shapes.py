import turtle as t
import random

colors = ["red", "blue", "green", "purple", "orange", "pink", "brown", "black", 
    "gray", "cyan", "magenta", "black", "indigo", "violet", "gold", "silver",
]

for side in range(3,11):
    t.color(random.choice(colors))
    angle = 360 / side
    for _ in range(side):
        t.forward(100)
        t.right(angle)















screen=t.Screen()
screen.exitonclick()