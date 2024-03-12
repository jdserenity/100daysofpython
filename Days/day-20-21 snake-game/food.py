from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.turtlesize(0.5, 0.5, 1)
        self.speed('fastest')
        self.regen()

    def regen(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
