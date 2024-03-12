from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.high_score_name = 'AAA'
        self.get_high_score()
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score} by {self.high_score_name}",
                   align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.write_score()

    def update_score(self, step=1):
        self.score += step
        self.write_score()

    def get_high_score(self):
        with open('high_score.txt', mode='r') as file:
            contents = list(file.read())
            new_line_i = contents.index('\n')
            self.high_score = int(''.join(contents[0:new_line_i]))
            self.high_score_name = ''.join(contents[new_line_i + 1:])

    def set_high_score(self, screen):
        self.high_score = self.score
        self.high_score_name = screen.textinput('You beat the high score!',
                                                'What name would you like to be displayed?')

        with open('high_score.txt', mode='w') as file:
            file.write(f"{self.high_score}\n{self.high_score_name}")
