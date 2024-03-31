from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from config import Config
from form import Form
from game_of_life import GameOfLife

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)


@app.before_first_request
def init_game(width=25, height=25):
    GameOfLife(width, height)


@app.route('/', methods=['GET', 'POST'])
def index():
    init_game()

    form = Form()
    if form.validate_on_submit():
        init_game(form.width.data, form.height.data)
        return redirect(url_for('live'))
    form.width.data = form.height.data = 25

    return render_template('index.html', form=form)


@app.route('/live')
def live():
    life = GameOfLife()
    if life.counter:
        life.form_new_generation()

    life.counter += 1

    return render_template('live.html', life=life)


if __name__ == '__main__':
    app.run()
