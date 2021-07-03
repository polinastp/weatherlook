from webapp.config import ELEPHANT_DATABASE
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session



engine = create_engine(ELEPHANT_DATABASE) # создаем движок для подключения
db_session = scoped_session(sessionmaker(bind=engine)) # создаем сессию

Base = declarative_base()
Base.query = db_session.query_property()