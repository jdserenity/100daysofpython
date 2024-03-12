from turtle import Turtle
UP = 90
DOWN = 270
PADDLE_SPEED = 20


class Paddle(Turtle):

    def __init__(self, side='left'):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(5, 1)
        self.side = self.move_paddle_to_side(side)
        self.color('white')

    def move_paddle_to_side(self, side):
        if side == 'right':
            self.teleport(x=350, y=0)
        else:
            self.teleport(x=-360, y=0)

        return side

    def up(self):
        if self.ycor() < 248:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(x=self.xcor(), y=new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(x=self.xcor(), y=new_y)

    def refresh(self):
        self.move_paddle_to_side(self.side)
