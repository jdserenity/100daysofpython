from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
DEBUG = False
DEBUG_TIME = int(1 / 60)
WORK_MIN = 25 if not DEBUG else DEBUG_TIME
SHORT_BREAK_MIN = 5 if not DEBUG else DEBUG_TIME
LONG_BREAK_MIN = 20 if not DEBUG else DEBUG_TIME
reps = 0
after = ''


def reset_timer():
    global reps, after
    top_label.config(text='Timer')
    check_label.config(text=f"0/4")
    canvas.itemconfig(timer_text, text=f"00:00")
    if after:
        window.after_cancel(after)
    reps = 0


def start_timer(count):
    global reps, after
    if reps == 0:  # rep 0 doesn't make sense, and it isn't a rep
        top_label.config(text='Work')
        check_label.config(text=f"0/4")
        reps = 1

    if count > 0:
        minute = int(count / 60) if int(count / 60) != 0 else '00'
        second = count % 60 if count % 60 != 0 else '00'
        if count % 60 < 10:
            second = '0' + str(count % 60)
        canvas.itemconfig(timer_text, text=f"{minute}:{second}")
        after = window.after(1000, start_timer, count - 1)
    else:
        reps += 1
        mins = 0
        checks = ''

        if reps not in [9]:
            for i in range(reps):
                if not i % 2 == 0:
                    checks += '✓'

            check_label.config(text=f"{checks}/4")

        if reps in [8]:
            top_label.config(text='Break', foreground=RED)
            mins = LONG_BREAK_MIN

        if reps in [3, 5, 7, 9]:
            if reps == 9:
                reps = 0

            top_label.config(text='Work', foreground=GREEN)
            mins = WORK_MIN

        if reps in [2, 4, 6]:
            top_label.config(text='Break', foreground=PINK)
            mins = SHORT_BREAK_MIN

        start_timer(mins * 60)


def count_down(count):
    global after
    if count > 0:
        canvas.itemconfig(timer_text, text=count)
        after = window.after(1000, count_down, count - 1)
    else:
        start_timer(WORK_MIN * 60)


if __name__ == '__main__':
    window = Tk()
    window.title('Pomodoro')
    window.minsize(width=100, height=100)
    window.config(padx=100, pady=50, bg=YELLOW)

    top_label = Label(text='Timer', bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 40, 'normal'))
    top_label.grid(column=2, row=1)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file='./tomato.png')
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=('Arial', 40, 'normal'))
    canvas.grid(column=2, row=2)

    start_button = Button(text='Start', highlightbackground=YELLOW, command=lambda: count_down(5))
    start_button.grid(column=1, row=3)

    check_label = Label(text='0/4', bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 30, 'normal'), pady=30)
    check_label.grid(column=2, row=3)

    reset_button = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
    reset_button.grid(column=3, row=3)

    window.mainloop()
