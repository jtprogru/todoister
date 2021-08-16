"""Сервисный модуль для базы данных."""
from app.core import Base, SessionLocal, engine


class DatabaseException(Exception):
    """Класс исключений."""

    def with_traceback(self, tb) -> str:
        """Возврат трейсбека.

        Args:
            tb: трейсбек

        Returns:
            str: форматированная строка
        """
        return f'{self.__class__.__name__}: {self.__traceback__}'


async def create_database() -> Base:
    """Создание базы данных.

    Returns:
        Base.metadata.create_all(bind=engine): создание базы
    """
    return Base.metadata.create_all(bind=engine)


async def get_db() -> SessionLocal:
    """Получение экземпляра базы данных.

    Yields:
        db: SessionLocal экземпляр
    """
    db = SessionLocal()
    try:
        yield db
    except DatabaseException as err:
        err.with_traceback(tb=err)
    finally:
        db.close()
