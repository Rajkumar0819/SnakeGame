from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.random_position()


    def random_position(self):
        random_x = random.randint(-220,220)
        random_y = random.randint(-220, 220)
        self.goto(random_x,random_y)

