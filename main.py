import pandas as pd
from turtle import Turtle, Screen

IMAGE = "blank_states_img.gif"
DATA_FILE = "50_states.csv"
FONT = ("Arial", 8, "normal")
ALIGNMENT = "center"

screen = Screen()
screen.setup(725, 491)
screen.bgpic(IMAGE)
screen.tracer(0)


def play_game():
    data = pd.read_csv(DATA_FILE)
    states = data.state.to_list()
    are_states_undiscovered = 1
    count = 0
    guessed_states = []

    while are_states_undiscovered:
        state_name = screen.textinput(f"{count}/50 - Name-a-State", "Please, enter the name of a state:")
        screen.update()
        if state_name.title() in states:
            count += 1
            guessed_states.append(state_name.title())
            state_info = data[data.state == state_name.title()]
            new_state = Turtle()
            new_state.hideturtle()
            new_state.color("red")
            new_state.penup()
            new_state.goto(int(state_info.x), int(state_info.y))
            new_state.write(f"{state_name.title()}", align=ALIGNMENT, font=FONT)
            states.remove(state_name.title())
        elif state_name.title() == "Exit":
            are_states_undiscovered = 0
            # not_guessed_states = list(set(states).difference(guessed_states))
            pd.DataFrame(states).to_csv("states_to_learn.csv")
        if count == 50:
            are_states_undiscovered = 0
            continue_gaming = screen.textinput("Do you want to play again?")
            if continue_gaming == "y":
                play_game()



play_game()
screen.exitonclick()
