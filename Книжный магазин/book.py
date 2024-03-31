from flask import url_for


class Book:
    max_id = 0

    def __init__(self, name, author, price, img, description):
        self.id = Book.max_id
        self.name = name
        self.author = author
        self.price = price
        self.__img_name = img
        self.description = description
        Book.max_id += 1

    @property
    def cover(self):
        return url_for('static', filename=f'img/{self.__img_name}_cover.jpg')
