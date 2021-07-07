from sqlalchemy.sql.sqltypes import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators = [DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Войти',  render_kw={"class":"btn btn-primary"})


class CityForm(FlaskForm):
    city = StringField('Введите город', validators=[DataRequired(), Length(3, 20)], render_kw={"class": "form-control"})
    submit = SubmitField('Узнать погоду', validators=[DataRequired()], render_kw={"class": "btn btn-primary"})