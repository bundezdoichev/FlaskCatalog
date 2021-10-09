from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Login')

