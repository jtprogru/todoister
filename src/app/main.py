#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import settings, Base, engine
from app.routers import base_router


def get_application():
    """Функция генерации приложения с определенными настройками"""
    Base.metadata.create_all(bind=engine)

    _app = FastAPI(
        title=settings.PROJECT_NAME, description=settings.PROJECT_DESCRIPTION,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(base_router)

    return _app


app = get_application()
