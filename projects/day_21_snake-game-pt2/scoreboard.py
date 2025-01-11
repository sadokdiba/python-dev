from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.display_score()
    
    def update_score(self):
        self.score += 1
        self.clear()  # Clear previous score and line
        self.display_score()

    def display_score(self):
        # Set the position and write the score
        self.setposition(0, 220)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        # Draw the line under the score
        self.draw_line()

    def draw_line(self):
        self.setposition(-350, 215)  # Start the line to the left of the screen
        self.pendown()  # Start drawing
        self.forward(700)  # Draw the line across the screen
        self.penup()  # Stop drawing

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def head_hit_body_display(self):
        self.setposition(0, -30)
        self.write("You are not allowed to hit the body", align=ALIGNMENT, font=FONT)


