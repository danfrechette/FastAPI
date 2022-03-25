from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.main import app

from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command

SQLALCHEMY_DATABASE_URL = ( f'postgresql://{settings.database_username}:'
                            f'{settings.database_password}@'
                            f'{settings.database_hostname}/'
                            f'{settings.database_name}_test')

engine = create_engine( SQLALCHEMY_DATABASE_URL )

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope='module')
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture(scope='module')
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)