from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.teleport(x=0, y=250)
        self.color('white')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.left_score} {self.right_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_left_score(self, step=1):
        self.left_score += step
        self.write_score()

    def update_right_score(self, step=1):
        self.right_score += step
        self.write_score()
