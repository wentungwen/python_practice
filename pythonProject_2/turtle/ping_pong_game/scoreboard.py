from turtle import Turtle
SCOREBOARD_GAP_X = 50
SCOREBOARD_GAP_Y = 200
ALIGN = "center"
FONT = ("mono", 30, "bold")
LINE_GAP = 20


def draw_line():
    line = Turtle("square")
    line.goto(x=0, y=300)
    line.setheading(270)
    line.width(7)
    for _ in range(20):
        line.color("white")
        line.forward(LINE_GAP)
        line.penup()
        line.forward(LINE_GAP)
        line.pendown()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        draw_line()

    def show_score(self, position):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(x=position[0], y=position[1])
        self.hideturtle()
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1


