from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

game_is_on = True

screen.title("Snake Game")

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    
screen.exitonclick()