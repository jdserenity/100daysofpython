import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []
y = -100
for colour in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 40
    turtles.append(new_turtle)

user_bet = screen.textinput('Race', 'Who do you think will win the RACE!')

race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            print(f"{turtle.pencolor()} won, {turtle.xcor()}")
            race_is_on = False
            if turtle.pencolor() == user_bet:
                print('you won you sly dog')
            else:
                print('nah')



screen.exitonclick()
