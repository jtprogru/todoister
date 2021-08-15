from .users import users_router
from fastapi import APIRouter

base_router = APIRouter(prefix="/api/v1",)

base_router.include_router(users_router)


@base_router.get("/healthcheck", tags=["healthcheck"])
async def healthcheck():
    return {"message": "OK"}
