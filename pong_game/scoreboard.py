from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(f"{self.score_left}      {self.score_right}", align= ALIGNMENT, font=FONT)

    def update_right(self):
        self.score_right += 1

    def update_left(self):
        self.score_left += 1
    