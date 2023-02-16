from turtle import Turtle, Screen
import time
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.speed_time = 0.5

    def create_ball(self):
        self.penup()
        self.goto(x=0, y=random.randint(-200, 200))
        self.shape("circle")
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_pedal(self):
        self.speed_time *= 0.9
        self.x_move *= -1

    def refresh_game(self):
        self.speed_time = 0.5
        self.goto(0, 0)


