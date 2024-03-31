from flask import Flask, render_template

app = Flask(__name__)


class Person:
    def __init__(self, name, age, prog):
        self.name = name
        self.age = age
        self.prog = prog

    def say_hello(self):
        return f"Привет, {self.name}!"

    def verification(self):
        if self.age >= 10 and self.prog == 'Да':
            return 'Добро пожаловать на курс по Flask!'
        elif self.age >= 10 and self.prog == 'Нет':
            return 'Для изучения курса Flask требуется опыт программирования!'
        elif self.age < 10 and self.prog == 'Да':
            return 'Добро пожаловать, юный гений! Приступим к изучению Flask!'
        else:
            return 'Доступ к курсу Flask закрыт.'



def rating(*args):
    sum = 0;
    for n in args:
        sum += n
    return sum / len(args)


def get_multiply(*args):
    multi = 1;
    for n in args:
        multi *= n
    return multi


@app.route("/")
def index():
    vasia = Person('Вася', 15, 'Да')
    return render_template('index.html',
                           # say_hello=say_hello,
                           # verification=verification,
                           rating=rating,
                           user=vasia)


@app.route("/workshop")
def workshop():
    return render_template('workshop.html',
                           get_multiply=get_multiply)
