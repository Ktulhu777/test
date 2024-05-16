from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class TelegramUser(Base):
    __tablename__ = "telegram_user"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True)
    username: str = Column(String, nullable=True, unique=True)
    tasks = relationship('Tasks', backref='user', lazy='dynamic')


class Tasks(Base):
    __tablename__ = "tasks"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('telegram_user.user_id'))
    title: str = Column(String)
    body: str = Column(Text)
    register_data: datetime.utcnow = Column(TIMESTAMP, default=datetime.utcnow())
