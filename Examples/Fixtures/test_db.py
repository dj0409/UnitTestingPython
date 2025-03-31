import pytest
import sqlite3
from db import UserDatabase

# Fixture with in-memory SQLite DB
@pytest.fixture
def user_db():
    conn = sqlite3.connect(":memory:")     # Setup: new in-memory DB
    db = UserDatabase(conn)
    yield db                               # Pass to test
    conn.close()                           # Teardown: close DB

def test_add_and_get_user(user_db):
    user_db.add_user(1, "Bruce Wayne")
    assert user_db.get_user(1) == "Bruce Wayne"

def test_add_multiple_users(user_db):
    users = [(1, "Bruce Wayne"), (2, "Clark Kent"), (3, "Diana Prince")]
    for uid, name in users:
        user_db.add_user(uid, name)

    all_users = user_db.get_all_users()
    assert len(all_users) == 3
    assert all_users[0] == (1, "Bruce Wayne")
    assert all_users[1] == (2, "Clark Kent")
    assert all_users[2] == (3, "Diana Prince")
