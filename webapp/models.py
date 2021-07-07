from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import Base, engine


class User(Base, UserMixin):
    """Создаем модель пользователя с данными, которые указываются при регистрации
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)
    gender = Column(String)
    city = Column(String)
    email = Column(String, unique=True)
    role = Column(String, index=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f'User {self.id}, {self.name}, {self.city}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine) # создание таблички в базе данных