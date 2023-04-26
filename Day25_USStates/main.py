import turtle
import pandas
from state import State

NUMBER_TO_GUESS = 5


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title(f"Guess {NUMBER_TO_GUESS} U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Get x and y values of each state via click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# import data
data = pandas.read_csv("50_states.csv")

# set up
correct_states = []
state = State()
states_to_learn = data["state"].to_list()

# while all states aren´t guessed
while len(correct_states) < NUMBER_TO_GUESS:

    # prompt for guess and convert to Title case
    guess = (screen.textinput(title=f"{len(correct_states)}/{NUMBER_TO_GUESS} States Correct",
                              prompt="Name a state: ")).title()

    if guess == "Exit":
        data = pandas.DataFrame(states_to_learn)
        data.to_csv("states_to_learn.csv")
        break

    # Check if the value is present in the column
    if guess in data["state"].values:
        answer = data[data["state"] == guess]
        x = int(answer.x.values[0])
        y = int(answer.y.values[0])
        state.write_state(guess, x, y)
        correct_states.append(guess)

        state_to_remove = states_to_learn.index(guess)
        states_to_learn.pop(state_to_remove)

if len(correct_states) == NUMBER_TO_GUESS:
    state.game_over(NUMBER_TO_GUESS)
turtle.mainloop()


