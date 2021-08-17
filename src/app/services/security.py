"""Сервисный модуль для security."""
import bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def generate_salt() -> str:
    """Генератор соли.

    Returns:
        str: рандомная строка
    """
    return bcrypt.gensalt().decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверка валидности пароля.

    Args:
        plain_password: plain password from User
        hashed_password: hashed password from DB

    Returns:
        bool: True if verified
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Получение хэша от пароля.

    Args:
        password: plain password

    Returns:
        str: hashed password
    """
    return pwd_context.hash(password)
