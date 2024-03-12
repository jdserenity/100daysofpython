import tkinter


def handle_calc():
    num_label['text'] = str(int(user_input.get()) * 1.60934)


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('Mile to Km Converter')
    window.minsize(width=100, height=100)
    window.config(padx=50, pady=50)

    user_input = tkinter.Entry()
    user_input.insert(1,  '0')
    user_input.grid(column=2, row=1)

    miles_label = tkinter.Label(text='Miles')
    miles_label.grid(column=3, row=1)

    equal_label = tkinter.Label(text='is equal to')
    equal_label.grid(column=1, row=2)

    num_label = tkinter.Label(text='0')
    num_label.grid(column=2, row=2)

    km_label = tkinter.Label(text='Km')
    km_label.grid(column=3, row=2)

    calc_button = tkinter.Button(text='Calculate', command=handle_calc)
    calc_button.grid(column=2, row=3)

    window.mainloop()
