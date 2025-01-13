from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800,height=600)
screen.bgcolor("black")

screen.tracer(0)

r_paddle = Paddle(x_coordinate=370)
l_paddle = Paddle(x_coordinate=-380)
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()