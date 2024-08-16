import pytest

from app.functions.cache import save_cache, read_cache


def test_read_cache_bad_file_path():
    with pytest.raises(FileNotFoundError):
        read_cache("bad_path")


def test_read_cache_season():
    cache = read_cache("app/cache/season.json")
    assert "season" in cache


def test_save_cache_test_file():
    data = {"data": "test"}
    save_cache("app/tests/test.json", data)

    cache = read_cache("app/tests/test.json")
    assert cache["data"] == "test"
