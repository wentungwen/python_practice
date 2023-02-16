from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = ScoreBoard()

game_is_start = True

while game_is_start:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect touching the food
    if snake.head.distance(food) < 30:
        scoreboard.hideturtle()
        snake.extend_snake()
        scoreboard.increase_score()
        food.refresh_food()

    # detext collision to the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        scoreboard.update_score()
        snake.reset()

    # detect collision with the tail
    if snake.check_body_collision():
        scoreboard.reset()
        scoreboard.update_score()
        snake.reset()



screen.exitonclick()

