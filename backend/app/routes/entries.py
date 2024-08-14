from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.database.schemas import Entry
from app.database.database import get_db

from app.functions import entries, lists
from app.functions.authentication import user_dependency


router = APIRouter(prefix="/entries", tags=["Watchlist Entries"])


@router.get("/all", response_model=list[Entry])
def get_user_entries(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]

    return entries.get_all(db, user_id)


@router.get("/watchlist/airing", response_model=list[Entry])
def get_airing_watchlist(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]
    return lists.get_watchlist(db, user_id)


@router.post("/add", response_model=list[Entry])
def add_entries(
    auth: user_dependency, anime_ids: list[int], db: Session = Depends(get_db)
):
    user_id = auth["id"]

    return entries.add_anime(db, user_id, anime_ids)


@router.delete("/remove", response_model=list[Entry])
def delete_entries(
    auth: user_dependency, anime_ids: list[int], db: Session = Depends(get_db)
):
    user_id = auth["id"]

    return entries.remove_anime(db, user_id, anime_ids)


@router.delete("/clear", response_model=list[Entry])
def clear_all_entries(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]

    return entries.clear_watchlist(db, user_id)
