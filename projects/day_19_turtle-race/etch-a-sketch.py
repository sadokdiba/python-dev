from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_clockwise():
    tim.right(5)
def turn_anticlockwise():
    tim.left(5)
    
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="z", fun=move_backward)
screen.onkey(key="s", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

