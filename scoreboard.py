from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_value()

    def score_value(self):
        self.clear()
        self.write(f"Score : {self.score} High Score :{self.high_score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.score_value()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_value()
