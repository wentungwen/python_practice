from turtle import Screen, Turtle
from Snake import Snake
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
    time.sleep(0.5)
    snake.move()


    # detect touching the food
    if snake.head.distance(food) < 10:
        scoreboard.hideturtle()
        scoreboard.update_score()
        food.refresh_food()







screen.exitonclick()

