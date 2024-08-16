import pytest
from app.password import verify_password, get_password_hash


def test_get_password_hash_hashed_value():
    password = "password"
    password2 = "password2"
    assert get_password_hash(password) != password and get_password_hash(
        password
    ) != get_password_hash(password2)


def test_get_password_hash_not_string():
    password = 1
    with pytest.raises(TypeError):
        get_password_hash(password)


def test_verify_password_same_password():
    password = "password"
    hashed = get_password_hash("password")
    assert verify_password(password, hashed)


def test_verify_password_hash_not_string():
    password = 1
    hashed = 1
    with pytest.raises(TypeError):
        verify_password(password, hashed)
