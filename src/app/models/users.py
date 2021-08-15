from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from app.core import Base


class User(Base):
    __tablename__ = "users_router"

    id = Column(Integer, primary_key=True, unique=True, index=True, comment="ID")
    username = Column(String(length=64), unique=True, index=True, comment="Username")
    registered_datetime = Column(
        DateTime, default=datetime.utcnow(), comment="Registration date and time"
    )
    password = Column(String(length=256), comment="User password")
    email = Column(String(length=128), unique=True, index=True, comment="User email")
    is_superuser = Column(Boolean, default=False, comment="Is a SuperUser?")

    todos = relationship("Todo", back_populates="owner")
