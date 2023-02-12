from turtle import Turtle, Screen


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.hideturtle()
        self.write(f"Score: 0", align="center", font=("Arial", 20, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: 0", align="center", font=("Arial", 20, "bold"))

        # self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))



