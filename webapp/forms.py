from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField('', validators = [DataRequired()], render_kw={"class": "form-control", "placeholder" : "Имя пользователя"})
    password = PasswordField('', validators = [DataRequired()], render_kw={"class": "form-control", "placeholder" : 'Пароль'})
    submit = SubmitField('Войти',  render_kw={"class":"btn btn-primary"})


class CityForm(FlaskForm):
    city = StringField('', validators=[DataRequired(), Length(3, 20)], render_kw={"class": "form-control", "placeholder" : "Введите город" })
    gender = SelectField('', choices=[('female', 'Девушка'), ('male', 'Парень')], render_kw={"class": "form-control"})
    submit = SubmitField('Узнать погоду', validators=[DataRequired()], render_kw={"class": "btn btn-primary"}) 


class RegistationForm(FlaskForm):
    username = StringField('', validators = [DataRequired()], render_kw={"class": "form-control", "placeholder" : "Имя пользователя"})
    email = StringField('', validators = [DataRequired(), Email()], render_kw={"class": "form-control", "placeholder" : "Почта"})
    gender = SelectField('', choices=[('female', 'female'), ('male', 'male')], render_kw={"class": "form-control", "placeholder" : "Ваш пол: female/male"})
    city = StringField('', validators = [DataRequired()], render_kw={"class": "form-control" , "placeholder" : "Город"})
    password = PasswordField('', validators = [DataRequired()], render_kw={"class": "form-control", "placeholder" : 'Пароль'})
    password2 = PasswordField('', validators = [DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder" : 'Повторите пароль' })
    submit = SubmitField('Регистрация',  render_kw={"class":"btn btn-primary"})


    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')


    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')

