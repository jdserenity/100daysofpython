from turtle import Screen
import threading
import read_data
from label import Label
from stats import Stats


def main():
    s = Screen()
    s.setup(width=725, height=491)
    s.title("Guess all 50 states!")
    s.bgpic('./blank_states_img.gif')

    stats = Stats()

    countdown_thread = threading.Thread(target=stats.countdown, args=[stats.timer_minutes])
    countdown_thread.start()

    quiz_is_on = True
    while quiz_is_on:
        if user_input := s.textinput(f"{stats.states_guessed_correctly}/50 States Correct",
                                     "What's another state name?"):
            if read_data.check_input(user_input):
                stats.states_guessed_correctly += 1

                x_and_y = read_data.get_x_and_y(user_input)

                Label(user_input, x_and_y)

            if stats.states_guessed_correctly == 50 or stats.timer_finished:
                quiz_is_on = False

    s.exitonclick()


if __name__ == '__main__':
    main()
