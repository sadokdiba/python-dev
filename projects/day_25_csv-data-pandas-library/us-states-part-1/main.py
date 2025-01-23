import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True
correct_states = []
read_states = pandas.read_csv("./50_states.csv")
all_states = pandas.DataFrame(read_states)
print(read_states)

# while game_on:

#     entered_state = screen.textinput(title=f"{len(correct_states)}/50", prompt="Enter the state name")

screen.exitonclick()