from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class TodoCreate(Todo):
    created_date: datetime


class TodoUpdate(Todo):
    id: int
    resolved_date: datetime
