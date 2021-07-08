from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators = [DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Войти',  render_kw={"class":"btn btn-primary"})


class CityForm(FlaskForm):
    city = StringField('Введите город', validators=[DataRequired(), Length(3, 20)], render_kw={"class": "form-control"})
    submit = SubmitField('Узнать погоду', validators=[DataRequired()], render_kw={"class": "btn btn-primary"})


class RegistationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators = [DataRequired(), Email()], render_kw={"class": "form-control"})
    gender = StringField('Ваш пол: female/male', validators = [DataRequired()], render_kw={"class": "form-control"})
    city = StringField('Город', validators = [DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators = [DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators = [DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Регистрация',  render_kw={"class":"btn btn-primary"})


    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')


    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')


    def validate_gender(self, gender):
        if gender.data != 'male' and gender.data != 'female':
            raise ValidationError('Введите пожалуйста male или female')