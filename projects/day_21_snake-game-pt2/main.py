from turtle import Screen
from snake import Snake
import scoreboard as s
import food as f
import time

screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = f.Food()
score = s.Scoreboard()

gameis_on = True
while gameis_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 200 or snake.head.ycor() < -237:
        gameis_on = False
    
    for seg in snake.snakes[1:]:
        if snake.head.position() == seg.position():
            print(snake.head.pos())
            print(seg.position())
            score.head_hit_body_display()
            gameis_on = False

score.game_over()

screen.exitonclick()