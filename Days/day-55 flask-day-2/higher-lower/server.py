from flask import Flask, render_template; from random import randint as ri;

app = Flask(__name__)

rand_num = ri(0,9)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:guess>')
def user_guess(guess):
    return render_template('user_guess.html', 
                           result=compare_guess(guess), 
                           color=randint()
                        )


def compare_guess(guess):
    if guess < rand_num: return "Too low, try again!"
    elif guess > rand_num: return "Too high, try again!"
    else: return "You found me!"


def randint():
    return (ri(0,255), ri(0,255), ri(0,255))


if __name__ == "__main__":
    app.run(debug=True, port=8000)