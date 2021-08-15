from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class TodoCreate(Todo):
    created_datetime: datetime


class TodoUpdate(Todo):
    id: int
    resolved_datetime: datetime
