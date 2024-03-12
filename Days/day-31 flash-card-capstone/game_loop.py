from tkinter import *
import random

DEBUG = False; DEBUG_TIME = 1;  # noqa E701

BACKGROUND_COLOR = "#B1DDC6"; CARD_BACK_COLOR = "#9BC1B0"; CARD_FRONT_COLOR = "#FFFFFF";  # noqa E701
COUNTDOWN_TIME = 3 if not DEBUG else DEBUG_TIME

labels_to_destroy = []
word_to_drop = None


def game_loop(objects):
    words = choose_random_word(objects['df'])
    flip_card(words['russian'], objects=objects, card_side='back')

    objects['window'].after(COUNTDOWN_TIME * 1000, flip_card, words['english'], objects,
                            'front')


def choose_random_word(df):
    words = {'russian': random.choice(df.Russian)}

    words['english'] = df[df.Russian == words['russian']]['English'].to_list()[0]

    if DEBUG: print(df[df.Russian == words['russian']]);  # noqa E701

    return words


def flip_card(word, objects=None, card_side=None):
    global labels_to_destroy, word_to_drop

    if labels_to_destroy:
        for label in labels_to_destroy:
            label.destroy()
        labels_to_destroy = []

    word_label = Label(text=word, bg=CARD_BACK_COLOR, foreground='black', font=('Arial', 60, 'bold'))
    word_label.grid(column=0, row=1, columnspan=2, rowspan=1)

    if card_side and objects:
        if card_side == 'front':
            language_label = Label(text='English', bg=CARD_FRONT_COLOR, foreground='black',
                                   font=('Arial', 40, 'italic'))
            language_label.grid(column=0, row=0, columnspan=2, rowspan=1)

            objects['canvas'].itemconfig(2, state='normal')
            word_label.config(bg=CARD_FRONT_COLOR)

            toggle_buttons(objects, 'normal')

            word_to_drop = word

            labels_to_destroy.append(language_label)

        else:
            language_label = Label(text='Russian', bg=CARD_BACK_COLOR, foreground='black', font=('Arial', 40, 'italic'))
            language_label.grid(column=0, row=0, columnspan=2, rowspan=1)

            objects['canvas'].itemconfig(2, state='hidden')

            toggle_buttons(objects, 'disabled')

            labels_to_destroy.append(language_label)

    labels_to_destroy.append(word_label)
    return word_label


def toggle_buttons(objects, toggle):
    objects['btns']['wrong'].config(state=toggle)
    objects['btns']['right'].config(state=toggle)


def handle_button(which, objects):
    if which == 'right':
        # If the person knows, the word, remove that flash card
        row_index = objects['df'].index[objects['df'].English == word_to_drop].to_list()[0]

        objects['df'].drop(row_index, inplace=True)

    game_loop(objects)
