"""Сервисный модуль для пользователей."""
from datetime import datetime

from sqlalchemy.orm import Session

from app import schemas
from app.models.users import User
from app.services.security import get_password_hash


async def get_user(db: Session, user_id: int) -> User:
    """Получение пользователя из БД.

    Args:
        db: - Сессия к БД
        user_id: - ID пользователя

    Returns:
        User: - экземпляр записи из БД
    """
    return db.query(User).filter(User.id == user_id).first()


async def get_user_by_email(db: Session, email: str) -> User:
    """Получение пользователя по email.

    Args:
        db: - Сессия к БД
        email: - email пользователя

    Returns:
        User: - экземпляр записи из БД
    """
    return db.query(User).filter(User.email == email).first()


async def get_users_list(db: Session, skip: int = 0, limit: int = 100) -> list:
    """Получение списка пользователей.

    Args:
        db: - Сессия к БД
        skip: - сколько пропустить
        limit: - сколько выдать

    Returns:
        list: - список записей из БД
    """
    users_list = db.query(User).offset(skip).limit(limit).all()
    if users_list:
        return users_list
    return []


async def create_user(db: Session, user: schemas.UserCreate) -> User:
    """Получение пользователя по email.

    Args:
        db: - Сессия к БД
        user: - схема с пользовательскими данными

    Returns:
        User: - экземпляр записи из БД
    """
    fake_hashed_password = get_password_hash(user.password)
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


async def delete_user_by_id(db: Session, user_id: int) -> dict:
    """Удаление пользователя по ID.

    Args:
        db: - Сессия к БД
        user_id: - ID пользователя

    Returns:
        dict: - сообщение об удалении пользователя
    """
    user_db = db.query(User).filter(User.id == user_id).first()
    db.delete(user_db)
    db.flush()
    return {'message': f'User with {user_id} was deleted'}
