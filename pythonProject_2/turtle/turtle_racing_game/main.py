from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)
racer_colors = ["red", "grey", 'blue', 'pink', 'orange']
user_bet = screen.textinput(title="BET", prompt="Which turtle will win the game?")
is_race_on = False
turtle_list = []

print(user_bet)

for idx in range(0, 5):
    turtle_racer = Turtle(shape="turtle")
    print(turtle_racer)
    turtle_racer.penup()
    turtle_racer.color(racer_colors[idx])
    turtle_racer.goto(x=-240, y=-230 + 90 * idx)
    turtle_list.append(turtle_racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        run_distance = random.randint(2, 8)
        turtle.forward(run_distance)
        if turtle.xcor() >= 250:
            is_race_on = False
            print(f"winner is {turtle.pencolor()}")
            if user_bet == turtle:
                print("You win!")
            else:
                print("You lose!")





print(Screen().canvheight)
Screen().exitonclick()
