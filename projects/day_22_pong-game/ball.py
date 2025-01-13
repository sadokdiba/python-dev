from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent Turtle class
        self.shape("circle")  # Set the ball shape to a circle
        self.color("white")  # Set the ball color to white
        self.penup()  # Lift the pen so it doesn't leave marks while moving
        self.x_move = 10  # Horizontal movement speed (10 units per move)
        self.y_move = 10  # Vertical movement speed (10 units per move)

    def move_ball(self):
        """Move the ball by its current x and y movement speeds."""
        new_x = self.xcor() + self.x_move  # Calculate new x position
        new_y = self.ycor() + self.y_move  # Calculate new y position
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bounce(self):
        """Reverse the vertical direction of the ball's movement."""
        self.y_move *= -1  # Flip the vertical movement speed to make the ball bounce
