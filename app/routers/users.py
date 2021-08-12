from app.schemas.users import UserCreate
from app.services.db import get_db
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends

from app.database import SessionLocal
from app.schemas import User
from app import services

users_router = APIRouter(
    prefix='/users',
    tags=["users"],
)


__default_user_list = list([
        {
            "username": "Masha",
            "email": "masha@email.com",
        },
        {
            "username": "Pasha",
            "email": "pasha@email.com",
        },
    ])


@users_router.get("/", response_model=List[User])
async def get_users_list(db: SessionLocal = Depends(get_db)):
    return await services.get_users_list(db=db)



@users_router.get("/{user_id}", response_model=User)
async def get_single_user(user_id:  int, db: SessionLocal = Depends(get_db)):
    return await services.get_user(db=db, user_id=user_id)



@users_router.post("/", response_model=User)
async def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    return await services.create_user(db=db, user=user)
