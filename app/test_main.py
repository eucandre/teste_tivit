import pytest
from fastapi.testclient import TestClient
from app.main import app  


from app.models import User
from app.database import Base, SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    db = TestingSessionLocal()
    yield db
    db.close()


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def user(db):
    user_data = User(username="testuser", role="user")
    user_data.set_password("fakepassword")
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


@pytest.fixture
def admin(db):
    admin_data = User(username="testadmin", role="admin")
    admin_data.set_password("fakepassword")
    db.add(admin_data)
    db.commit()
    db.refresh(admin_data)
    return admin_data


def test_login_for_access_token(client, db, user):
    
    data = {"username": "testuser", "password": "fakepassword"}
    response = client.post("/token", data=data)
    
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


