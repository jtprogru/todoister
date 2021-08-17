#!/usr/bin/env python
"""Альтернативный скрипт запуска."""
import uvicorn

from app.core import settings
from app.main import app


def main():
    """Основная функция запуска через uvicorn."""
    uvicorn.run(
        app=app,
        host=settings.server_host,
        port=settings.server_port,
        log_level=settings.log_level,
        debug=settings.debug,
    )


if __name__ == '__main__':
    main()
