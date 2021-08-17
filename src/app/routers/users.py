"""Модуль предоставляющий users_router."""

from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Depends

from app.core import SessionLocal
from app.schemas import User, UserCreate
from app.services import db_services, users_services

users_router = APIRouter(
    prefix='/users',
    tags=['users'],
)

depends_db = Depends(db_services.get_db)


@users_router.get('/', response_model=Optional[List[User]])
async def get_users_list(db: SessionLocal = depends_db) -> Optional[List[User]]:
    """Функция возвращает список пользователей или пустой список.

    Args:
        db: SessionLocal подлючение к БД через Depends

    Returns:
        Optional[List[User]]: опционально возвращает список User или пустой список
    """
    return await users_services.get_users_list(db=db)


@users_router.get('/{user_id}', response_model=Optional[User])
async def get_user_by_id(user_id: int, db: SessionLocal = depends_db) -> Optional[User]:
    """Функция получает конкретного пользователя по ID.

    Args:
        user_id: int идентификатор пользователя
        db: SessionLocal подлючение к БД через Depends

    Returns:
        Optional[User]: опционально возвращает одного пользователя
    """
    return await users_services.get_user(db=db, user_id=user_id)


@users_router.post('/', response_model=User)
async def post_create_user(user: UserCreate, db: SessionLocal = depends_db) -> User:
    """Функция создает пользователя на основе UserCreate.

    Args:
        user: UserCreate схема для создания пользователя
        db: SessionLocal подлючение к БД через Depends

    Returns:
        User: возвращает только что созданного пользователя
    """
    user_db = await users_services.create_user(db=db, user=user)
    return users_services.get_user(db=db, user_id=user_db.id)


@users_router.delete('/{user_id}')
async def delete_user(user_id: int, db: SessionLocal = depends_db) -> dict:
    """Функция удаляет пользователя с определенным ID.

    Args:
        user_id: int схема для создания пользователя
        db: SessionLocal подлючение к БД через Depends

    Returns:
        dict: возвращает информацию об удалении пользователя
    """
    await users_services.delete_user_by_id(db=db, user_id=user_id)
    return {'message': f'User with {user_id=} was deleted'}
