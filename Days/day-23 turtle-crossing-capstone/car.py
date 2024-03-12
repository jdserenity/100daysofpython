from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)