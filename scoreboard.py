from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("grey")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=335)
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Courier", 25, "normal"))

        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Courier", 25, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Courier", 25, "normal"))



    def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="a") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(arg=f"Score:{self.score} High Score:{self.high_score}", move=False, align="center", font=("Courier", 25, "normal"))
