import pytest
from app.db.database import SessionLocal

@pytest.fixture
def db():
    session = SessionLocal()
    yield session
    session.close()
