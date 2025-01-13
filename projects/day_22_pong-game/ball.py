from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("circle")  
        self.color("white")  
        self.penup()  
        self.x_move = 10  
        self.y_move = 10  

    def move_ball(self):
        """Move the ball by its current x and y movement speeds."""
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move  
        self.goto(new_x, new_y)  

    def bounce(self):
        """Reverse the vertical direction of the ball's movement."""
        self.y_move *= -1  
