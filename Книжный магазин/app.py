from flask import Flask, render_template

from book import Book

app = Flask(__name__)

all_books = [
    Book('Стихотворения', 'Есенин С.А.', 14.99, 'poems', 'С первых поэтических сборников («Радуница», 1916; «Сельский часослов», 1918) выступил как тонкий лирик, мастер глубоко психологизированного пейзажа, певец крестьянской Руси, знаток народного языка и народной души.'),
    Book('Мастер и Маргарита', 'Булгаков М.А.', 17.49, 'master_and_margarita', '«Ма́стер и Маргари́та» — роман Михаила Афанасьевича Булгакова, работа над которым началась в конце 1920-х годов и продолжалась вплоть до смерти писателя. Роман относится к незавершённым произведениям; редактирование и сведение воедино черновых записей осуществляла после смерти мужа вдова писателя — Елена Сергеевна.'),
    Book('Идиот', 'Достоевский Ф.М.', 13.49, 'idiot', '«Идио́т» — роман Фёдора Михайловича Достоевского, впервые опубликованный в номерах журнала «Русский вестник» за 1868 год. Являлся одним из самых любимых произведений писателя, наиболее полно выразившим и нравственно-философскую позицию Достоевского, и его художественные принципы в 1860-х годах.'),
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
@app.route('/catalog')
@app.route('/books/index')
def books():
    return render_template('books/index.html', books=all_books, title='Книги')


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


@app.route('/books/book<int:id>')
def book(id):
    b = all_books[id]
    return render_template(f'books/book.html', book=b, title=f'{b.name} - {b.author}')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
