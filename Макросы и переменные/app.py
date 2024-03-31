from flask import Flask, render_template

app = Flask(__name__)


def get_sum(x, y=0):
    return "Это функция!"


@app.route("/")
def index():
    return render_template('index.html',
                           get_sum=get_sum)


@app.route("/workshop")
def workshop():
    return render_template('workshop.html')
