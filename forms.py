from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    title = StringField(label='Tytuł', validators=[DataRequired()])
    author = StringField(label='Autor', validators=[DataRequired()])
    year = StringField(label='Rok powstania')
    description = TextAreaField(label='Opis')
    done = SelectField(label='Czy przeczytane?', choices=['Tak', 'Nie'])
