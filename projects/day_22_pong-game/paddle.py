from turtle import Screen, Turtle

class Paddle:
    def __init__(self,x_coordinate):
        self.x_coordinate_value = x_coordinate
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()
        self.paddle.setposition(x_coordinate, 0)

        self.screen = Screen()
        self.screen.listen()

        if self.x_coordinate_value > 0:
            self.screen.onkey(self.go_up, "Up")
            self.screen.onkey(self.go_down, "Down")
        else:
            self.screen.onkey(self.go_up, "w")
            self.screen.onkey(self.go_down, "z")

    def go_up(self):
        new_y_coor = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y_coor)

    def go_down(self):
        new_y_coor = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y_coor)

    