"""Сервисный модуль для пользователей."""
from datetime import datetime

from sqlalchemy.orm import Session

from app import schemas
from app.models.users import User


async def get_user(db: Session, user_id: int) -> User:
    """Получение пользователя из БД.

    Args:
        db: - Сессия к БД
        user_id: - ID пользователя

    Returns:
        models.User: - экземпляр записи из БД
    """
    return db.query(User).filter(User.id == user_id).first()


async def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


async def get_users_list(db: Session, skip: int = 0, limit: int = 100):
    users_list = db.query(User).offset(skip).limit(limit).all()
    if users_list:
        return users_list
    return []


async def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'thisisnotsecure'
    db_user = User(
        username=user.username,
        registered_datetime=datetime.utcnow(),
        password=fake_hashed_password,
        email=user.email,
        is_superuser=False,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def delete_user_by_id(db: Session, user_id: int):
    user_db = db.query(User).filter(User.id == user_id).first()
    db.delete(user_db)
    db.flush()
    return
