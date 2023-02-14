from turtle import Turtle, Screen
ALIGN = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def show_score(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f"The Fianl Score is: {self.score}", align=ALIGN, font=FONT)



