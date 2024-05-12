import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses = []
while len(guesses) < 50:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 Correct States", prompt= "Guess a State in the U.S?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guesses.append(answer_state)
        names = turtle.Turtle()
        names.hideturtle()
        names.penup()
        state_data = data[data["state"] == answer_state]

        names.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        names.write(answer_state, font=("Arial", 8), align="left")
