from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/calc/<int:arg_a>/<arg_op>/<int:arg_b>/")
def calc(arg_a, arg_b, arg_op):
    return render_template('calc.html',
                           a=arg_a,
                           b=arg_b,
                           operation=arg_op)


@app.route("/workshop/<int:arg_a>/<int:arg_b>/")
def workshop(arg_a, arg_b):
    return render_template('workshop.html', a=arg_a, b=arg_b)


