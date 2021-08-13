#!/usr/bin/env python
import uvicorn

from app.core import settings
from app.main import app


def main():
    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL,
        debug=settings.DEBUG,
    )


if __name__ == "__main__":
    main()
