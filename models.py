from sqlalchemy import Column, Integer, String
from db import Base, engine


class User(Base):
    """Создаем модель пользователя с данными, которые указываются при регистрации
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), index=True, unique=True)
    password = Column(String(100))
    gender = Column(String(10))
    city = Column(String(50))
    email = Column(String(100), unique=True)
    role = Column(String(10), index=True)


    def __repr__(self):
        return f'User {self.id}, {self.name}, {self.city}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine) # создание таблички в базе данных