"""Схемы предоставляемых и получаемых данных для модели User."""
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """Базовая схема для объектов User."""

    username: str
    email: str

    class Config:
        """Конфигурирующий класс."""

        orm_mode = True


class UserCreate(User):
    """Базовая схема для создания объектов User."""

    password: str
    registered_datetime: datetime


class UserUpdate(User):
    """Базовая схема для обновления объектов User."""

    id: int
    password: str
