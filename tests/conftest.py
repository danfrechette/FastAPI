from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.main import app

from app.config import settings
from app.database import get_db
from app.database import Base
from app import models
from app.oauth2 import create_access_token
from alembic import command

SQLALCHEMY_DATABASE_URL = ( f'postgresql://{settings.database_username}:'
                            f'{settings.database_password}@'
                            f'{settings.database_hostname}/'
                            f'{settings.database_name}_test')

engine = create_engine( SQLALCHEMY_DATABASE_URL )

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()#scope='module'
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture()#scope='module'
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {'email':'hello123@gmail.com', 'password':'password123'}

    res = client.post("/users/",json = user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def test_user2(client):
    user_data = {'email':'hello456@gmail.com', 'password':'password123'}

    res = client.post("/users/",json = user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, test_user2, session):

    posts_data = [{
        'title': "Title #1",
        'content': "Title #1 Content",
        'owner_id': test_user['id']
    }, {
        'title': "Title #2",
        'content': "Title #2 Content",
        'owner_id': test_user['id']
    }, {
        'title': "Title #3",
        'content': "Title #3 Content",
        'owner_id': test_user['id']
    }, {
        'title': "U2 Title #1",
        'content': "U2 Title #1 Content",
        'owner_id': test_user2['id']
    }]

    def create_user_model(post):
        return models.Post(**post)

    post_map = map(create_user_model , posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    posts = session.query(models.Post).all()
    return posts