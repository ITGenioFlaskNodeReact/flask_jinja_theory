from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# st_list = ["Иванов Иван",
#            "Петров Пётр",
#            "Сидоров Егор"]

# subjects = {'Математика': 5, 'История': 4, 'Информатика': 4}

st_list = [("Иванов Иван", {'Математика': 5, 'История': 4, 'Информатика': 4}),
           ("Петров Пётр", {'Математика': 3, 'История': 5, 'Информатика': 4}),
           ("Сидоров Егор", {'Математика': 5, 'История': 5, 'Информатика': 5}),
           ("Прогулов Вася", {})]

films = ['Гарри Поттер', 'Титаник', 'Ирония судьбы']


@app.route("/students")
def students():
    return render_template('students.html',
                           st_list=st_list,
                           # subjects = subjects
                           )


@app.route("/workshop")
def workshop():
    return render_template('workshop.html', films=films)
