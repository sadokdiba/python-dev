from turtle import Turtle, Screen

class Snake():
    def __init__(self):
        self.y_axis = 0
        self.x_axis = 0
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        
    def create_snake(self):
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.goto(x=self.x_axis, y=self.y_axis)
            segment.color("white")
            self.snakes.append(segment)
            self.x_axis -= 20

    def move(self):
        for seg in range (len(self.snakes)-1, 0, -1):
            new_x_axis = self.snakes[seg - 1].xcor()
            new_y_axis = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x_axis, new_y_axis)
        self.snakes[0].forward(20)

        screen = Screen()
        screen.listen()
        def turn_up():
            if self.head.heading() != 270:
                self.head.setheading(90)
        def turn_down():
            if self.head.heading() != 90: 
                self.head.setheading(270)
        def turn_right():
            if self.head.heading() != 180:    
                self.head.setheading(0)
        def turn_left():
            if self.head.heading() != 0:
                self.head.setheading(180)

        screen.onkey(turn_up, "w")
        screen.onkey(turn_down, "z")
        screen.onkey(turn_right, "s")
        screen.onkey(turn_left, "a")
