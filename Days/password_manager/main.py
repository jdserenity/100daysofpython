from tkinter import *
from tkinter import messagebox
import secrets
import json
PASSWORD_LENGTH = 17
DEFAULT_EMAIL = 'jdcanada00@gmail.com'
DEBUG = False


def search_database(search_key):
    if not search_key:
        messagebox.showinfo(message='No entry found')
        return

    search_key = search_key.strip().title()

    try:
        with open('./database.json', mode='r') as database:
            data = json.load(database)

            if entry := data[search_key]:
                messagebox.showinfo(title=f"{search_key}",
                                    message=f'Email is: {entry['email']}\nPassword is: {entry['password']}')
                return

            messagebox.showinfo(message='No entry found')

    except FileNotFoundError:
        messagebox.showinfo(message='No entry found')


def generate_pass():
    password = secrets.token_urlsafe(PASSWORD_LENGTH)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)


def add_pass():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {web: {"email": email, "password": password}}

    if web and email and password:
        yes_no = messagebox.askyesno(message=f'Website: {web}\nEmail: {email}\nPassword: {password}\n\nIs this okay?')

        if yes_no:
            try:
                with open('database.json', mode='r') as database:
                    data = json.load(database)
                    data.update(new_data)

                with open('database.json', mode='w') as database:
                    json.dump(data, database, indent=4)

                    # database.write(f"{web} | {email} | {password}\n")
            except FileNotFoundError:
                with open('database.json', mode='w') as database:
                    json.dump(new_data, database, indent=4)

            messagebox.showinfo(message='Password added successfully')

            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showinfo(message='Input invalid')


if __name__ == '__main__':
    window = Tk()
    window.title('Password Manager')
    window.minsize(width=100, height=100)
    window.config(padx=50, pady=70, bg='white')

    # Images
    canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
    logo_img = PhotoImage(file='./logo.png')
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    # Labels
    website_label = Label(text='Website:', bg='white', foreground='black', font=('Arial', 12, 'normal'), width=25)
    website_label.grid(column=0, row=1, sticky="W")
    email_label = Label(text='Email/Username:', bg='white', foreground='black', font=('Arial', 12, 'normal'), width=25)
    email_label.grid(column=0, row=2, sticky="W")
    password_label = Label(text='Password', bg='white', foreground='black', font=('Arial', 12, 'normal'), width=25)
    password_label.grid(column=0, row=3, sticky="W")

    # Entries
    website_entry = Entry(bg='white', fg='black', highlightthickness=0, border=1)
    website_entry.focus()
    website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    email_entry = Entry(bg='white', fg='black', highlightthickness=0, border=1)
    email_entry.insert(0, DEFAULT_EMAIL)
    email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    password_entry = Entry(bg='white', fg='black', highlightthickness=0, border=1)
    password_entry.grid(column=1, row=3, sticky="EW")

    # Buttons
    search_button = Button(text='Search', highlightbackground='white',
                           command=lambda: search_database(website_entry.get()))
    search_button.grid(column=2, row=1, sticky="EW")
    generate_button = Button(text='Generate Password', highlightbackground='white', command=generate_pass)
    generate_button.grid(column=2, row=3, sticky="EW")
    add_button = Button(text='Add', highlightbackground='white', command=add_pass, width=40)
    add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

    window.mainloop()
