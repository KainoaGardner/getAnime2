from fastapi import HTTPException, APIRouter, Depends

from sqlalchemy.orm import Session
from app.database.schemas import Entry
from app.database.database import get_db

from app.functions import entries
from app.functions.authentication import user_dependency


router = APIRouter(prefix="/entries", tags=["Watchlist Entries"])


@router.get("/all", response_model=list[Entry])
def get_user_entries(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]

    return entries.get_all(db, user_id)


@router.post("/add", response_model=list[Entry])
def get_add_show(
    auth: user_dependency, show_ids: list[int], db: Session = Depends(get_db)
):
    user_id = auth["id"]

    return entries.add_show(db, user_id, show_ids)


@router.delete("/remove", response_model=list[Entry])
def get_remove_show(
    auth: user_dependency, show_ids: list[int], db: Session = Depends(get_db)
):
    user_id = auth["id"]

    return entries.remove_show(db, user_id, show_ids)
