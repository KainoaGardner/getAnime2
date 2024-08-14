import requests
from typing import Dict
from datetime import date

from sqlalchemy.orm import Session
from app.functions.users import get_user_id
from app.functions.webscrape import webscrape
from app.functions.cache import read_cache, save_cache

from app.env import MAL_API_URL, MAL_API_HEADERS


def get_watchlist(db: Session, user_id: int):
    airing_today = get_today()

    user = get_user_id(db, user_id)
    airing_watchlist = {"data": []}
    for anime in user.watching:
        if str(anime.mal_id) in airing_today:
            anime_object = {
                "mal_id": anime.mal_id,
                "title": anime.title,
                "japanese_title": anime.japanese_title,
                "image": anime.image,
            }
            airing_watchlist["data"].append(anime_object)
    return airing_watchlist["data"]


def get_today():
    week = get_week()
    weekly_cache = read_cache("app/cache/weekly.json")
    if weekly_cache["week"] != week:
        webscrape(week)
        weekly_cache = read_cache("app/cache/weekly.json")
    today = get_day()
    today_cache = make_airing_today(today, weekly_cache)
    return today_cache["data"]


def get_day():
    current_date = date.today()
    return date(current_date.year, current_date.month, current_date.day).strftime("%a")


def make_airing_today(today: str, weekly_cache: Dict):
    today_cache = {"data": {}}
    for anime_id in weekly_cache["data"]:
        anime = weekly_cache["data"][anime_id]
        if anime["airing_day"] == today:
            today_cache["data"].update({anime_id: anime})
    return today_cache


def get_weekly():
    week = get_week()
    weekly_cache = read_cache("app/cache/weekly.json")
    if weekly_cache["week"] != week:
        webscrape(week)
        weekly_cache = read_cache("app/cache/weekly.json")
    return weekly_cache["data"]


def get_week():
    current_date = date.today()
    return date(current_date.year, current_date.month, current_date.day).strftime("%V")


def get_season():
    year, season = get_year_season()
    season_cache = read_cache("app/cache/season.json")
    if season_cache["year"] != year or season_cache["season"] != season:
        cache = get_season_cache(year, season)
        save_cache("app/cache/season.json", cache)
        season_cache = read_cache("app/cache/season.json")
    return season_cache["data"]


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


def get_season_cache(year: int, season: str):
    response = mal_get_season(year, season)
    if response.ok:
        data = response.json()

        season_data = make_season_data(data)
        cache = {"year": year, "season": season}
        cache.update(season_data)

        return cache

    else:
        raise ValueError(response.json())


def mal_get_season(year: int, season: str):
    return requests.get(
        f"{MAL_API_URL}/anime/season/{year}/{season}?limit=500&fields=alternative_titles",
        headers=MAL_API_HEADERS,
    )


def make_season_data(data: Dict):
    season_data = {"data": {}}
    for anime in data["data"]:
        id = anime["node"]["id"]
        title = anime["node"]["title"]
        japanese_title = anime["node"]["alternative_titles"]["ja"]
        image = anime["node"]["main_picture"]["large"]
        anime_object = {
            id: {"title": title, "japanese_title": japanese_title, "image": image}
        }
        season_data["data"].update(anime_object)
    return season_data
