import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import Base as TestBase
from app.main import app
from app.services import get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


TestBase.metadata.create_all(bind=test_engine)


def override_get_db():
    try:
        test_db = TestingSessionLocal()
        yield test_db
    finally:
        test_db.close()


app.dependency_overrides[get_db] = override_get_db



