from turtle import Turtle
MOVE_DISTANCE = 20
LEFT_X = -390
RIGHT_X = 380


class Pedal(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        









