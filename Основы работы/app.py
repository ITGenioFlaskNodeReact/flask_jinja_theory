from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
                           name='Айтигеник',
                           title='Шаблонизатор Jinja',
                           count=10)


@app.route("/<int:new_count>")
def change_count(new_count):
    return render_template('index.html',
                           name='Айтигеник',
                           title='Шаблонизатор Jinja',
                           count=new_count)
