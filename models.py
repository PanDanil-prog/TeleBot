from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from config_db import DATABASE_URL


def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine)
    return session


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    count_of_pressed_buttons = Column(Integer)
    created_at = Column(String, default=str(datetime.now()).replace('T', ' '))


class Button(Base):
    __tablename__ = 'buttons'

    name = Column(String, primary_key=True)
    pressed_count = Column(Integer)




