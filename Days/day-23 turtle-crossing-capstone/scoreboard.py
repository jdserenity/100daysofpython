from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.teleport(x=-230, y=268)
        self.color('black')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self, step=1):
        self.score += step
        self.write_score()
