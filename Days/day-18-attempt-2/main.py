import turtle as t
from turtle import Turtle, Screen
import random
from random import randint
import colorgram

tim = Turtle()
screen = Screen()
screen.setup(width=800, height=800)
t.colormode(255)

y = -380
tim.pensize(1)
tim.speed('fastest')
tim.hideturtle()

extract = colorgram.extract('image.webp', 24)

colours = []
for colour in extract:
    colours.append(colour.rgb)
print(colours)

for _ in range(0, 20):
    tim.teleport(-380, y)
    for _ in range(0, 20):
        tim.color(random.choice(colours))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.up()
        tim.forward(39.5)
    y += 39.5

screen.exitonclick()
