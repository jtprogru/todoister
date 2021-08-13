from app.schemas.users import UserCreate
from app.services.db import get_db
from typing import List, Optional
from fastapi import APIRouter
from fastapi.params import Depends

from app.core import SessionLocal
from app.schemas import User
from app import services

users_router = APIRouter(
    prefix='/users',
    tags=["users"],
)


@users_router.get("/", response_model=Optional[List[User]])
async def get_users_list(db: SessionLocal = Depends(get_db)):
    return await services.get_users_list(db=db)


@users_router.get("/{user_id}", response_model=Optional[User])
async def get_single_user(user_id:  int, db: SessionLocal = Depends(get_db)):
    return await services.get_user(db=db, user_id=user_id)


@users_router.post("/", response_model=User, status_code=201)
async def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    return await services.create_user(db=db, user=user)


@users_router.delete("/{user_id}")
async def delete_user(user_id: int, db: SessionLocal = Depends(get_db)):
    await services.delete_user_by_id(db=db, user_id=user_id)
    return {"message": f"User with {user_id=} was deleted"}
