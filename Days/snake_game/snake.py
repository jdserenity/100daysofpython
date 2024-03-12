from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, speed=0.1, length=3):
        self.speed = speed
        self.segments = []
        self.length = length
        self.create_snake(length)
        self.head = self.segments[0]

    def create_snake(self, length):
        for i in range(length):
            position = (0 - 20 * i, 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.goto(position)
        self.segments.append(new_square)

    def grow_length(self):
        position = self.segments[-1].position()
        self.add_segment(position)
        self.length += 1

    def move(self):
        time.sleep(self.speed)
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def direction(self, direction):
        direction = direction.lower()
        if direction == 'up' and self.head.heading() != DOWN:
            self.head.setheading(UP)
        elif direction == 'down' and self.head.heading() != UP:
            self.head.setheading(DOWN)
        elif direction == 'left' and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        elif direction == 'right' and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.length = 3
        self.create_snake(self.length)
        self.head = self.segments[0]
