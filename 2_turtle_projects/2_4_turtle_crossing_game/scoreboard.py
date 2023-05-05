import turtle
from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

    def show_result(self, result):
        self.penup()
        self.goto(x=0, y=100)
        self.color("black")
        self.hideturtle()
        self.write(f"{result}", align=ALIGN, font=FONT)



