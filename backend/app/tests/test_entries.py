import pytest

from app.functions.entries import get_anime_info


def test_get_anime_info():
    data = {
        "title": "title",
        "alternative_titles": {"ja": "japanese_title"},
        "main_picture": {"large": "largeimage"},
    }
    result = get_anime_info(data)
    assert (
        result["title"] == "title"
        and result["japanese_title"] == "japanese_title"
        and result["image"] == "largeimage"
    )
