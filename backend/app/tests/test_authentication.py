import pytest
from datetime import timedelta

from app.functions.authentication import create_access_token, get_current_user


def test_create_access_token_full_token():
    username = "test"
    user_id = 10
    time = timedelta(days=7)

    token = create_access_token(username, user_id, time)
    print(token)

    assert token[-1] != "." and token.count(".") == 2


def test_get_current_user_valid_output():
    token = {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb3dpZSIsImlkIjoxLCJleHAiOjE3MjQ0Mzc1NjV9.dVe5WZ7TxonBZcjK6PrHnG4gAthVw6vWVAYHjIVmgfI",
        "token_type": "bearer",
        "id": 1,
    }

    with pytest.raises(Exception):
        user = get_current_user(token)
