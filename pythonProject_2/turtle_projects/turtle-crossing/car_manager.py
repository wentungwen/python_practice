from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.count = 0

    def create_car(self):
        car = Turtle(shape="square")
        car.penup()
        car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.goto(x=-240, y=random.randint(-280, 280))
        self.car_list.append(car)

    # def create_car(self):
    #     self.shape("square")
    #     self.penup()
    #     self.color(COLORS[random.randint(0, len(COLORS) - 1)])
    #     self.shapesize(stretch_wid=1, stretch_len=3)
    #     self.goto(x=-240, y=random.randint(-280, 280))
    #
    # def append_(self):
    #     self.car_list.append(self.create_car())


