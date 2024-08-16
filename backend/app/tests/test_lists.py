from datetime import date

from app.functions.lists import get_year_season, get_week


def test_get_year_season_valid_season():
    year, season = get_year_season()
    assert season in ["winter", "spring", "summer", "fall"]


def test_get_week():
    week = int(get_week())
    assert 0 < week < 54
