import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("darkblue")
        self.speed("fastest")
        self.penup()
        self.goto(0, 0)

    def refresh(self):
        random_y = random.randint(-300, 300)
        random_x = random.randint(-500, 500)
        self.goto(x=random_x, y=random_y)
