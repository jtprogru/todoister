#!/usr/bin/env python
"""Основной модуль для запуска приложения."""
from fastapi import FastAPI

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
        title=settings.project_name,
        description=settings.project_description,
    )

    inner_app.include_router(base_router)

    return inner_app


app = get_application()
