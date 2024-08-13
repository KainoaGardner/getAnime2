import requests
from sqlalchemy.orm import Session
from app.database.models import Entries
from app.database.schemas import Entry

from app.password import get_password_hash
from app.env import MAL_API_URL, MAL_API_HEADERS


def get_all(db: Session, user_id: int):
    return db.query(Entries).filter(Entries.user_id == user_id).all()


def add_show(db: Session, user_id: int, show_ids: list[int]):
    result = []
    for show_id in show_ids:
        response = mal_get_anime(show_id)
        if response.ok:
            data = response.json()
            new_entry = add_anime(
                db, user_id, show_id, data
            )  # make new anime if not already in database add to database
            if new_entry:
                result.append(new_entry)
        else:
            print(response.json())

    db.commit()

    return result


def mal_get_anime(show_id: int):
    return requests.get(
        f"{MAL_API_URL}/anime/{show_id}?fields=alternative_titles",
        headers=MAL_API_HEADERS,
    )


def add_anime(db: Session, user_id: int, show_id: int, data: dict):
    anime = get_anime_info(data)
    return add_new_entry(db, user_id, show_id, anime)


def get_anime_info(data: dict):
    title = data["title"]
    japanese_title = data["alternative_titles"]["ja"]
    image = data["main_picture"]["large"]
    return {"title": title, "japanese_title": japanese_title, "image": image}


def add_new_entry(db: Session, user_id: int, show_id: int, anime: dict):
    if not (
        db.query(Entries)
        .filter(Entries.user_id == user_id, Entries.show_id == show_id)
        .first()
    ):
        new_entry = Entries(
            title=anime["title"],
            japanese_title=anime["japanese_title"],
            show_id=show_id,
            show_image=anime["image"],
            user_id=user_id,
        )
        db.add(new_entry)
        return new_entry
    return None


def remove_show(db: Session, user_id: int, show_ids: list[int]):
    result = []
    for show_id in show_ids:
        removed = remove_anime(db, user_id, show_id)
        if removed:
            result.append(removed)

    db.commit()
    return result


def remove_anime(db: Session, user_id: int, show_id: int):
    anime = (
        db.query(Entries)
        .filter(Entries.user_id == user_id, Entries.show_id == show_id)
        .first()
    )
    if anime:
        db.delete(anime)
        return anime
    return None
