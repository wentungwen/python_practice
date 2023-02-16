from turtle import Turtle, Screen
ALIGN = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score_data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()





