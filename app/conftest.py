import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from app.orm import start_mappers, metadata

@pytest.fixture(scope="module")
def test_db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # in-memory SQLite 
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    start_mappers()
    metadata.create_all(engine)
    return engine

@pytest.fixture(scope="module")
def session(test_db):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_db)
    session = SessionLocal()
    try:
        session.begin_nested()  # nested transaction
        yield session
    finally:
        session.close()  
        clear_mappers()  