from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class TelegramUser(Base):
    __tablename__ = "telegram_user"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String, nullable=True, unique=True)
    tasks = relationship('Tasks', backref='user', lazy='dynamic')


class Tasks(Base):
    __tablename__ = "tasks"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('user.id'))
    body: str = Column(String)
    register_data: datetime.utcnow = Column(TIMESTAMP, default=datetime.utcnow())
