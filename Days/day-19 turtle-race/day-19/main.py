import turtle as t
from turtle import Turtle, Screen

mark = Turtle()
screen = Screen()

mark.speed('fastest')


def move_forwards():
    mark.forward(20)


def move_backwards():
    mark.backward(20)


def turn_counter_clockwise():
    new_heading = mark.heading() + 20
    mark.setheading(new_heading)


def turn_clockwise():
    new_heading = mark.heading() - 20
    mark.setheading(new_heading)


def clear():
    mark.clear()
    mark.home()
    mark.clear()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear)
screen.onkey(key='u', fun=mark.penup)
screen.onkey(key='i', fun=mark.pendown)
screen.exitonclick()
