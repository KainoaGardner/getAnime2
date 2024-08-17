import pytest
import json
from app.functions.cache import read_cache, save_cache


def test_read_cache_bad_path():
    with pytest.raises(FileNotFoundError):
        read_cache("bad_path")


def test_save_cache_valid():
    data = {"data": "test"}
    save_cache("app/tests/test.json", json.dumps(data))
    result = read_cache("app/tests/test.json")
    assert result["data"] == "test"


def test_save_cache_not_jsondumped():
    data = {"data": "test"}
    with pytest.raises(FileNotFoundError):
        save_cache("app/tests/test.json", data)
