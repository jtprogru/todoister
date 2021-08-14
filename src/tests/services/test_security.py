import pytest
from app.services.security import get_password_hash, verify_password
from passlib.context import CryptContext


@pytest.fixture
def hashed_password(default_user_data) -> str:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_ctx.hash(default_user_data["password"])


def test_get_password_hash(default_user_data):
    hash_pass = get_password_hash(password=default_user_data["password"])
    assert isinstance(hash_pass, str)


def test_verify_password(hashed_password, default_user_data):

    assert verify_password(default_user_data["password"], hashed_password)
    assert isinstance(verify_password(default_user_data["password"], hashed_password), bool)
