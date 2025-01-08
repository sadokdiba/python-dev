import random
from turtle import Turtle, Screen

def setup_screen(width=1000, height=700):
    """
    Create and return a Screen object with the given width and height.
    """
    screen = Screen()
    screen.setup(width=width, height=height)
    return screen

def get_user_bet(screen):
    """
    Prompt the user to place a bet on which turtle will win the race.
    Return the user's chosen color as a string.
    """
    return screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color:"
    )

def create_turtles(colors, start_x=-470, start_y=-95, y_step=45, shape_size=1.7):
    """
    Create and return a list of Turtle objects, each with a unique color.
    They will be placed at (start_x, start_y), and moved down by `y_step`
    after each turtle.
    """
    turtles = []
    for color in colors:
        racer = Turtle(shape="turtle")
        racer.penup()
        racer.shapesize(shape_size)
        racer.color(color)
        racer.goto(start_x, start_y)
        start_y += y_step
        turtles.append(racer)
    return turtles

def start_race(turtles, user_bet, finish_line_x=470):
    """
    Move the turtles forward in random steps until one crosses the finish line.
    Determine the winner and compare with the user's bet.
    """
    race_is_on = True
    while race_is_on:
        for turtle in turtles:
            turtle.speed("fast")
            turtle.forward(random.randint(0, 10))
            
            if turtle.xcor() > finish_line_x:
                race_is_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The winner is the {winner} turtle.")
                else:
                    print(f"You've lost. The winner is the {winner} turtle.")
                break

def main():
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    screen = setup_screen()
    user_bet = get_user_bet(screen)
    all_turtles = create_turtles(colors)
    if user_bet: 
        start_race(all_turtles, user_bet)
    screen.exitonclick()

if __name__ == '__main__':
    main()
