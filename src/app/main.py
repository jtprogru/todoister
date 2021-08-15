#!/usr/bin/env python
"""Основной модуль для запуска приложения."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import Base, engine, settings
from app.routers import base_router


def get_application() -> FastAPI:
    """Функция генерации приложения с определенными настройками.

    Args:
        None

    Returns:
         inner_app as FastAPI() instance
    """
    Base.metadata.create_all(bind=engine)

    inner_app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
    )

    inner_app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    inner_app.include_router(base_router)

    return inner_app


app = get_application()
