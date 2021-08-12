from fastapi import APIRouter

base_router = APIRouter(
    prefix='/api/v1',
    tags=["api", "v1"],
)
