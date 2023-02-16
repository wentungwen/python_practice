import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.turn_up, "Up")
screen.onkeypress(player.turn_down, "Down")
screen.onkeypress(player.turn_left, "Left")
screen.onkeypress(player.turn_right, "Right")

is_game_on = True
count = 1
result = ""
car_manager = CarManager()

while is_game_on:
    # Generate the cars
    if count % 20 == 1:
        car_manager.create_car()
    for car in car_manager.car_list:
        car.forward(2)
    count += 1

    # Detect the collision of wall
    if player.xcor() >= 280:
        player.goto(280, player.ycor())
    elif player.xcor() <= -280:
        player.goto(-280, player.ycor())
    elif player.ycor() >= 280:
        player.goto(player.ycor(), 280)
    elif player.ycor() <= -280:
        player.goto(player.ycor(), -280)

    # Detect the collision of cars
    for car in car_manager.car_list:
        if player.distance(car) <= 40 and (player.ycor() - car.ycor()) < 12:
            result = "You lose"
            is_game_on = False
    if player.ycor() >= 280:
        result = "You win"

    time.sleep(0.05)
    screen.update()

score_board.show_result(result)
screen.exitonclick()
