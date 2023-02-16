from turtle import Turtle, Screen
from pedals import Pedal
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pingpong")
screen.tracer(0)

ball = Ball()

pedal_left = Pedal((-390, 0))
pedal_right = Pedal((380, 0))
score_right = ScoreBoard()
score_left = ScoreBoard()

screen.listen()
screen.onkeypress(pedal_left.move_up, "Up")
screen.onkeypress(pedal_left.move_down, "Down")
screen.onkeypress(pedal_right.move_up, "Left")
screen.onkeypress(pedal_right.move_down, "Right")

game_is_start = True


while game_is_start:
    time.sleep(ball.speed_time)
    screen.update()
    ball.move()
    score_right.show_score((50, 200))
    score_left.show_score((-50, 200))

    # Detect the ball collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_wall()

    # Detect the collision with the pedals
    if (ball.distance(pedal_right) <= 50 and ball.xcor() >= 350) or \
            ball.distance(pedal_left) <= 50 and ball.xcor() <= -360:
        ball.bounce_pedal()

    # Detect if ball cross the pedal
    if ball.xcor() >= 400:
        ball.refresh_game()
        score_left.increase_score()

    elif ball.xcor() <= -400:
        ball.goto(0, 0)
        score_right.increase_score()



screen.exitonclick()
