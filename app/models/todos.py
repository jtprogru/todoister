from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from app import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, unique=True, index=True, comment="ID")
    title = Column(String(length=128), comment="Title of Todos")
    description = Column(String(length=512), comment="Description of Todos")
    created_date = Column(DateTime, default=datetime.utcnow(), comment="Date when created")
    resolved_date = Column(DateTime, default=datetime.utcnow(), comment="Date when resolved")

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = Column(ForeignKey, relationship="Todo", back_populates="todos")
