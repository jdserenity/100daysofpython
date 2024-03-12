from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1, 1)
        self.color('white')
        self.ball_speed = 1

        self.x_move = self.ball_speed
        self.y_move = self.ball_speed

    def move(self):
        if self.ycor() >= 290:
            self.bounce_wall()
        elif self.ycor() <= -290:
            self.bounce_wall()

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1

    def increase_speed(self):
        if self.x_move > 0:
            self.x_move += 0.1
        else:
            self.x_move -= 0.1

