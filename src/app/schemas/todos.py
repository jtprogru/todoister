"""Схемы предоставляемых и получаемых данных для модели Todo."""
from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    """Базовая схема для объектов Todo."""

    title: str
    description: str

    class Config:
        """Конфигурирующий класс."""

        orm_mode = True


class TodoCreate(Todo):
    """Базовая схема для создания объектов Todo."""

    created_datetime: datetime


class TodoUpdate(Todo):
    """Базовая схема для обновления объектов Todo."""

    id: int
    resolved_datetime: datetime
