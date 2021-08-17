"""Модель User."""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core import Base


class User(Base):
    """Класс описывающий модель User."""

    _username_length = 64
    _password_length = 256
    _email_length = 128

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, index=True, comment='ID')
    username = Column(String(length=_username_length), unique=True, index=True, comment='Username')
    registered_datetime = Column(DateTime, default=datetime.utcnow(), comment='Registration date and time')
    password = Column(String(length=_password_length), comment='User password')
    email = Column(String(length=_email_length), unique=True, index=True, comment='User email')
    is_superuser = Column(Boolean, default=False, comment='Is a SuperUser?')

    todos = relationship('Todo', back_populates='owner')
