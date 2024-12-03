import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from main import app
from db.models import DbUser
from db.database import get_db
from schemas.user import RoleEnum

@pytest.fixture
def mock_db_session():
    mock_session = MagicMock()
    
    mock_session.query().filter().first.return_value = DbUser(
        id=1, username="user1", email="user1@example.com", password="password123", role="films"
    )
    
    mock_session.query().all.return_value = [
        DbUser(id=1, username="user1", email="user1@example.com", password="password123", role="admin"),
        DbUser(id=2, username="user2", email="user2@example.com", password="password123", role="films")
    ]

    def mock_commit():
        return None

    mock_session.commit = mock_commit

    return mock_session

@pytest.fixture
def client(mock_db_session):
    app.dependency_overrides[get_db] = lambda: mock_db_session
    client = TestClient(app)
    return client

@pytest.fixture
def user_data(mock_db_session):
    mock_db_session.query().filter().first.return_value = DbUser(
        id=1, username="user1", email="user1@example.com", password="password123", role="admin"
    )
    
    return {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "password": "password123",
        "role": "admin"
    }

@pytest.fixture
def updated_data():
    return {
        "username": "user1_updated",
        "email": "updateduser@example.com",
        "password": "password456",
        "role": "admin"
    }

@pytest.fixture
def user_data_no_admin(mock_db_session):
    mock_db_session.query().filter().first.return_value = DbUser(
        id=2, username="user2", email="user2@example.com", password="password123", role="films"
    )
    
    return {
        "username": "user2",
        "email": "user2@example.com",
        "password": "password123",
        "role": "films"
    }
    
@pytest.fixture
def auth_token():
    return "mocked_token"

@pytest.fixture
def role_data():
    return [role.value for role in RoleEnum]

@pytest.fixture
def existing_user_by_username(mock_db_session):
    def setup_mock(username):
        mock_db_session.query().filter().first.return_value = DbUser(
            id=2, username=username, email="user2@example.com", password="password123"
        )
    return setup_mock

@pytest.fixture
def existing_user_by_email(mock_db_session):
    def setup_mock(email):
        def query_filter_by_email(*args, **kwargs):
            if DbUser.email == email:
                return MagicMock(first=lambda: DbUser(
                    id=2, username="user2", email=email, password="password123"
                ))
            return MagicMock(first=lambda: None)
        mock_db_session.query().filter.side_effect = query_filter_by_email
    return setup_mock

@pytest.fixture
def no_users_found(mock_db_session):
    mock_db_session.query().filter().first.return_value = None
    return mock_db_session

@pytest.fixture
def existing_user_with_id(mock_db_session):
    def setup_mock(user_id):
        mock_db_session.query().filter().first.return_value = DbUser(
            id=user_id, username="user1", email="user1@example.com", password="password123"
        )
    return setup_mock