"""Модель Todo."""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core import Base


class Todo(Base):
    """Класс описывающий модель Todo."""

    _title_length = 128
    _description_length = 512

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, unique=True, index=True, comment='ID')
    title = Column(String(length=_title_length), comment='Title of Todos')
    description = Column(String(length=_description_length), comment='Description of Todos')
    created_datetime = Column(DateTime, default=datetime.utcnow(), comment='Date when created')
    resolved_datetime = Column(DateTime, default=datetime.utcnow(), comment='Date when resolved')
    resolved_status = Column(Boolean, default=False, comment='Resolved status')

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='todos')
