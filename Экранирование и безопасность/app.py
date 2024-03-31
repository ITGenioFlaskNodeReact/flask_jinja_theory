from flask import Flask, render_template

app = Flask(__name__)

text = "Символ \\n переводит на новую строку. Это известно из курса Python. <br> Но в html это не действует."
danger = "<script>while(true)alert('Я - вирус! Я сломаю твой сайт!');</script>"
heading = "<h1>Я изучаю экранирование</h1>"
task2 = ("Солнышко, играя <br>В капельках дождя, <br>Радугой сверкает. <br>В небо уходя, <br>Связывает вместе "
         "<br>Речки берега <br>Мостик поднебесный – <br>Радуга-дуга! <br>(Л. Громова)")


@app.route("/")
def index():
    return render_template('index.html',
                           text=text,
                           danger=danger,
                           heading=heading,
                           task2=task2)


