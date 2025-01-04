from turtle import Turtle, Screen

#
sad_tot = Turtle()
# # sadok_turtle.shape("turtle")
# sad_tot.color("red", "blue")
# sad_tot.shapesize(3, 3)
#
def draw_dashed_line():
    for _ in range(25):
        sad_tot.forward(10)
        sad_tot.penup
        sad_tot.forward(10)
        sad_tot.pendown()

draw_dashed_line()





















screen = Screen()
screen.exitonclick()