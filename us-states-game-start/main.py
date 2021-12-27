import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

current_score = 0
flag = True
while current_score < 50:
    user_input = screen.textinput(title=(f"Score: {current_score}/50"), prompt="Enter a state name").title()

    data = pd.read_csv("50_states.csv")
    if (len(data[data["state"] == user_input])) == 0:
        continue
    x_val = int(data[data["state"] == user_input]["x"])
    y_val = int(data[data["state"] == user_input]["y"])
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x_val, y_val)
    state.write(f"{user_input}", align="center", font=("Courier", 12, "normal"))
    current_score += 1

screen.exitonclick()