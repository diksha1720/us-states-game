import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

data = pd.read_csv("50_states.csv")

while len(guessed_states) < 50:
    user_input = screen.textinput(title=(f"Score: {len(guessed_states)}/50"), prompt="Enter a state name").title()
    if user_input == "Exit":
        break
    if (len(data[data["state"] == user_input])) == 0:
        continue
    x_val = int(data[data["state"] == user_input]["x"])
    y_val = int(data[data["state"] == user_input]["y"])
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x_val, y_val)
    state.write(f"{user_input}", align="center", font=("Courier", 12, "normal"))
    guessed_states.append(user_input)

all_states = data.state.tolist()
missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

df = pd.DataFrame(missed_states)
df.to_csv("missed_states.csv")


screen.exitonclick()