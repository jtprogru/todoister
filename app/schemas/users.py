from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str
    registered_datetime: datetime


class UserUpdate(User):
    id: int
    password: str
