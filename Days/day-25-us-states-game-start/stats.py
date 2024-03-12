from turtle import Turtle
import time


class Stats(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.states_guessed_correctly = 0
        self.timer_minutes = 10

        self.penup()
        self.goto(220, 170)
        # self.countdown(self.timer_minutes)
        self.timer_finished = False

    def countdown(self, t):
        t = t * 60
        while t > 0:
            self.clear()
            mins, secs = divmod(t, 60)
            self.write('{:02d}:{:02d}'.format(mins, secs), align='center', font=("Arial", 40, "bold"))
            time.sleep(1)
            t -= 1

        self.timer_finished = True

