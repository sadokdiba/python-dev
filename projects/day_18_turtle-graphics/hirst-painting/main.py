import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)
tim.hideturtle()

color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (221, 179, 218)]

def draw_ten_dots():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
def main():
    x = -250, y = -250
    for _ in range(10):
        tim.penup()
        tim.setposition(x, y)
        draw_ten_dots()
        y += 45

main()


screen = turtle.Screen()
screen.exitonclick()
