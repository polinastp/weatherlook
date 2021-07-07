from getpass import getpass
import sys

from webapp import create_app
from webapp.models import User
from webapp.db import db_session

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже существует')
        sys.exit(0)
    
    password1 = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if  password1 != password2:
        sys.exit(0)
    
    gender = input('Ваш пол Ж/М: ')

    city = input('Введите город: ')

    email = input('Введите почту: ')
    
    new_user = User(username = username, gender = gender, city = city, email = email, role ='user')
    new_user.set_password(password1)

    db_session.add(new_user)
    db_session.commit()
    print(f'ID пользователя <id = {new_user.id}>')