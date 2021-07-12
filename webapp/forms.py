from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators = [DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Войти',  render_kw={"class":"btn btn-primary"})


class CityForm(FlaskForm):
    city = StringField('', validators=[DataRequired(), Length(3, 20)], render_kw={"class": "form-control", "placeholder" : "Введите город" })
    gender = SelectField('', choices=[('female', 'female'), ('male', 'male')], render_kw={"class": "form-control"})
    submit = SubmitField('Узнать погоду', validators=[DataRequired()], render_kw={"class": "btn btn-primary"}) 


class RegistationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators = [DataRequired(), Email()], render_kw={"class": "form-control"})
    gender = SelectField('Ваш пол: female/male', choices=[('female', 'female'), ('male', 'male')], render_kw={"class": "form-control"})
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

