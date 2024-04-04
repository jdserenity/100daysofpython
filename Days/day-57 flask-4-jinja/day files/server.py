from flask import Flask, render_template; from datetime import datetime as dt; import requests;

CURRENT_YEAR = dt.now().year

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_year=CURRENT_YEAR)


@app.route('/guess/<string:name>')
def guess(name):
    predicted_age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    predicted_gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']

    return render_template('guess.html',
                            name=name,
                            predicted_age=predicted_age,
                            predicted_gender=predicted_gender,
                            current_year=CURRENT_YEAR
                        )


@app.route('/blog')
def blog():
    posts = requests.get('https://api.npoint.io/df674b681c547302b3a0').json()
    return render_template('blog.html', current_year=CURRENT_YEAR, posts=posts)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
