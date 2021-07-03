from sqlalchemy.sql.sqltypes import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Пароль', validators = [DataRequired()])
    submit = SubmitField('Войти')


class CityForm(FlaskForm):
    city = StringField('Введите город', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Узнать погоду', validators=[DataRequired()], render_kw={"class": "btn btn-primary"})