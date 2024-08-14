import requests
from sqlalchemy.orm import Session
from app.database.models import Entries

from app.env import MAL_API_URL, MAL_API_HEADERS


def get_all(db: Session, user_id: int):
    return db.query(Entries).filter(Entries.user_id == user_id).all()


def add_anime(db: Session, user_id: int, anime_ids: list[int]):
    result = []
    for anime_id in anime_ids:
        response = mal_get_anime(anime_id)
        if response.ok:
            data = response.json()
            new_entry = add_anime_entry(
                db, user_id, anime_id, data
            )  # make new anime if not already in database add to database
            if new_entry:
                result.append(new_entry)
        else:
            raise ValueError(response.json())

    db.commit()

    return result


def mal_get_anime(anime_id: int):
    return requests.get(
        f"{MAL_API_URL}/anime/{anime_id}?fields=alternative_titles",
        headers=MAL_API_HEADERS,
    )


def add_anime_entry(db: Session, user_id: int, anime_id: int, data: dict):
    anime = get_anime_info(data)
    return add_new_entry(db, user_id, anime_id, anime)


def get_anime_info(data: dict):
    title = data["title"]
    japanese_title = data["alternative_titles"]["ja"]
    image = data["main_picture"]["large"]
    return {"title": title, "japanese_title": japanese_title, "image": image}


def add_new_entry(db: Session, user_id: int, anime_id: int, anime: dict):
    if not (
        db.query(Entries)
        .filter(Entries.user_id == user_id, Entries.mal_id == anime_id)
        .first()
    ):
        new_entry = Entries(
            title=anime["title"],
            japanese_title=anime["japanese_title"],
            mal_id=anime_id,
            image=anime["image"],
            user_id=user_id,
        )
        db.add(new_entry)
        return new_entry
    return None


def remove_anime(db: Session, user_id: int, anime_ids: list[int]):
    result = []
    for anime_id in anime_ids:
        removed = remove_anime_entry(db, user_id, anime_id)
        if removed:
            result.append(removed)

    db.commit()
    return result


def remove_anime_entry(db: Session, user_id: int, anime_id: int):
    anime = (
        db.query(Entries)
        .filter(Entries.user_id == user_id, Entries.mal_id == anime_id)
        .first()
    )
    if anime:
        db.delete(anime)
        return anime
    return None


def clear_watchlist(db: Session, user_id: int):
    watchlist = db.query(Entries).filter(Entries.user_id == user_id).all()
    for anime in watchlist:
        db.delete(anime)
    db.commit()

    return watchlist
