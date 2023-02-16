from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def turn_up(self):
        self.setheading(UP)
        self.move()

    def turn_down(self):
        self.setheading(DOWN)
        self.move()

    def turn_right(self):
        self.setheading(RIGHT)
        self.move()

    def turn_left(self):
        self.setheading(LEFT)
        self.move()

    def move(self):
        self.forward(MOVE_DISTANCE)
