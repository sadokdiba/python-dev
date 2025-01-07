import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(270)
tim.setheading(0)
tim_dots = 100


color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (221, 179, 218)]


for dots in range(1, tim_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = turtle.Screen()
screen.exitonclick()