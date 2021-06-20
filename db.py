from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session



engine = create_engine('postgresql://wgdnxdbv:6GZx9w8zdZ4uk_jG3EyJo8aqYmyYjGSG@hattie.db.elephantsql.com/wgdnxdbv') # создаем движок для подключения
db_session = scoped_session(sessionmaker(bind=engine)) # создаем сессию

Base = declarative_base()
Base.query = db_session.query_property()