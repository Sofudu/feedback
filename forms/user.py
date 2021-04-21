from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Ваше имя', validators=[DataRequired()])
    mess = TextAreaField("Расскажите, в чем ваши пробелемы")
    submit = SubmitField('Отправить')