import turtle
import pandas


data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US STATES")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

correct_guess = []
all_states = data.state.to_list()

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"Guess the state: {len(correct_guess)}/50", prompt="What is another state's name?").capitalize()
    answer_state_info = data[data.state == f'{answer_state}']

    if answer_state == "Exit":
        missing_states = [state for state in all_states
                          if state not in correct_guess]
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        x = int(answer_state_info.x)
        y = int(answer_state_info.y)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(x=x, y=y)
        state_name.write(f"{answer_state}", align="left", font=("Arial", 8, "normal"))
        correct_guess.append(answer_state)

# states to learn
