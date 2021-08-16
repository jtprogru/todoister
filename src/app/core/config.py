"""Базовый модуль с конфигурацией проекта."""

from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Класс Settings описывает требуемые настройки."""

    project_name: str
    project_description: str = 'Simple project written with FastAPI'
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    log_level: str = 'info'
    database_uri: Optional[str] = None
    debug: bool = False
    server_reload: bool = debug

    class Config:
        """Метакласс через который указывается из какого файла брать настройки."""

        case_sensitive = False
        env_file = '.env'
        frozen = True


settings = Settings()
