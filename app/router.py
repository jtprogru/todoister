from fastapi import APIRouter
from .routers import users_router

base_router = APIRouter(
    prefix='/api/v1',
)

base_router.include_router(users_router)
