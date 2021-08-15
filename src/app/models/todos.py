from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore

from app.core import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, unique=True, index=True, comment="ID")
    title = Column(String(length=128), comment="Title of Todos")
    description = Column(String(length=512), comment="Description of Todos")
    created_datetime = Column(DateTime, default=datetime.utcnow(), comment="Date when created")
    resolved_datetime = Column(DateTime, default=datetime.utcnow(), comment="Date when resolved")
    resolved_status = Column(Boolean, default=False, comment="Resolved status")

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="todos")
