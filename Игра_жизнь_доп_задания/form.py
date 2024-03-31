from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import IntegerField


class Form(FlaskForm):
    width = IntegerField('Ширина мира: ')
    height = IntegerField('Высота мира: ')
    submit = SubmitField('Создать пользовательский мир')
