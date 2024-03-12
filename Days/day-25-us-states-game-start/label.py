from turtle import Turtle


class Label(Turtle):

    def __init__(self, name, x_and_y_tuple):
        super().__init__()
        self.hideturtle()

        self.name = name.title()
        self.x = x_and_y_tuple[0]
        self.y = x_and_y_tuple[1]

        self.penup()
        self.color('black')
        self.speed('fastest')
        self.goto(self.x, self.y)

        self.write(self.name, align='center')
