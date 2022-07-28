from fastapi.testclient import TestClient

from app.db.base import session_scope
from app.db.models.pet import Pet
from app.db.models.user import User
from app.server import app, get_users

client = TestClient(app)


def test_get_users() -> None:
    expected_email = "someone@example.com"
    expected_name = "John"
    _create_user(name=expected_name, email=expected_email)

    users = get_users()
    assert len(users) == 1
    user = users[0]
    assert user["name"] == expected_name
    assert user["email"] == expected_email


def _create_user(name: str, email: str) -> None:
    with session_scope() as db_session:
        user = User(name=name, email=email)
        db_session.add(user)
        pet = Pet(name=name, user=user)
        db_session.add(pet)
