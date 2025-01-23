import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True
guessed_states = []
read_states = pandas.read_csv("./50_states.csv")
all_states = read_states.state.to_list()
print(all_states)



while game_on:
    print(guessed_states)
    entered_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter the state name (first letter must be capital)")

    if entered_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_list = pandas.DataFrame(states_to_learn)
        new_list.to_csv("./states_to_learn.csv")
        break

    if entered_state in all_states :
        guessed_states.append(entered_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = read_states[read_states.state == entered_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(entered_state)

screen.exitonclick()