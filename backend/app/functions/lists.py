import json
from datetime import date
from sqlalchemy.orm import Session

# from app.database.models import Users
# from app.database.schemas import User, UserCreate

from app.password import get_password_hash


def get_season():
    year, season = get_year_season()
    try:
        with open("app/cache/season.json", "r") as f:
            season_cache = json.load(f)
            if season_cache["year"] != year or season_cache["season"] != season:
                get_season_cache(year, season)
    except:
        print("test")


def get_year_season():
    current_date = date.today()
    year = current_date.year
    month = current_date.month
    match month:
        case 1 | 2 | 3:
            season = "winter"
        case 4 | 5 | 6:
            season = "spring"
        case 7 | 8 | 9:
            season = "summer"
        case 10 | 11 | 12:
            season = "fall"
        case _:
            raise ValueError("Incorrect season")

    return year, season


def get_season_cache(year, season):
    pass
