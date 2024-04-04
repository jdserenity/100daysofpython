from flask import Flask, render_template; import requests;

app = Flask(__name__)
posts = requests.get('https://api.npoint.io/df674b681c547302b3a0').json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def blog_post(id):
    return render_template("post.html", post=posts[id-1])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
