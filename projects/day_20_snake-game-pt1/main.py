from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

gameis_on = True
while gameis_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    

screen.exitonclick()