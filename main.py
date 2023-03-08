import turtle
from turtle import Turtle, Screen
import pandas as pd

myScreen = Screen()
myScreen.title("U.S. states game")
image = "blank_states_img.gif"
myScreen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
x_cors = data["x"].to_list()
y_cors = data["y"].to_list()

correct_state = []

while len(correct_state) < 50:
    answer_state = myScreen.textinput(title=f"Guess: {len(correct_state)}/50"
                                      , prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in correct_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_state.append(answer_state)


