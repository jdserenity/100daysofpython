import pandas
from tkinter import *
from game_loop import handle_button

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#9BC1B0"
CARD_FRONT_COLOR = "#FFFFFF"


def create_game():
    objects = {
        'window': create_window(),
        'df': do_pandas()
    }

    canvas_imgs = create_canvas()

    objects['canvas'] = canvas_imgs[0]
    objects['imgs'] = canvas_imgs[1]

    objects['btns'] = create_buttons(objects)

    return objects


def create_window():
    window = Tk()
    window.title('Flashify')
    window.minsize(width=900, height=726)
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    return window


def create_canvas():
    # Main Canvas
    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

    # Images
    imgs = {'card_back': PhotoImage(file='./images/card_back.png')}
    canvas.create_image(400, 263, image=imgs['card_back'])
    canvas.card_back_img = imgs['card_back']

    imgs['card_front'] = PhotoImage(file='./images/card_front.png')
    canvas.create_image(400, 263, image=imgs['card_front'])
    canvas.card_front_img = imgs['card_front']
    canvas.itemconfig(2, state='hidden')

    imgs['wrong'] = PhotoImage(file='./images/wrong.png')

    imgs['right'] = PhotoImage(file='./images/right.png')

    # Pack
    canvas.grid(column=0, row=0, columnspan=2, rowspan=3)

    return canvas, imgs


def do_pandas():
    df = pandas.read_csv('./Russian Words - Sheet1.csv')

    return df


def create_buttons(objects):
    btns = {}
    btns['wrong'] = Button(image=objects['imgs']['wrong'], command=lambda: handle_button('wrong', objects), borderwidth=0, highlightthickness=0,
                           state='disabled')
    btns['wrong'].grid(column=0, row=3, columnspan=1)

    btns['right'] = Button(image=objects['imgs']['right'], command=lambda: handle_button('right', objects), borderwidth=0, highlightthickness=0,
                           state='disabled')
    btns['right'].grid(column=1, row=3, columnspan=1)

    return btns
