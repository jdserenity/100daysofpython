from flask import Flask, render_template; import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def make_bold(function):
    def wrapper():
        bold_string = f"<b>{function()}</b>"
        return bold_string
    return wrapper


def make_italic(function):
    def wrapper():
        italic_string = f"<em>{function()}</em>"
        return italic_string
    return wrapper


def make_underlined(function):
    def wrapper():
        underlined_string = f"<u>{function()}</u>"
        return underlined_string
    return wrapper


@app.route('/bye')
@make_bold
@make_underlined
@make_italic
def bye():
    return "Bye!" 


if __name__ == '__main__':
    app.run(debug=True, port=5000)