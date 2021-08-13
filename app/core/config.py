
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str = "Simple project written with FastAPI"
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000
    LOG_LEVEL: str = 'info'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_URI: Optional[str] = None
    DEBUG: bool = False
    SERVER_RELOAD: bool = DEBUG

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)



    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
