from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class RegistrationForm(FlaskForm):
    photo = TextAreaField('photo')
    submit = SubmitField('Register Me!')