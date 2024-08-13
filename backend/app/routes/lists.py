from fastapi import HTTPException, APIRouter, Depends

from sqlalchemy.orm import Session
from app.database.schemas import Anime
from app.database.database import get_db

from app.functions import lists
from app.functions.authentication import user_dependency

router = APIRouter(prefix="/lists", tags=["Anime Lists"])


@router.get("/watchlist/airing", response_model=list[Anime])
def get_user_today(auth: user_dependency, db: Session = Depends(get_db)):
    return []


@router.get("/today", response_model=list[Anime])
def get_airing_today(db: Session = Depends(get_db)):
    return []


@router.get("/season", response_model=list[Anime])
def get_season():
    lists.get_season()
    return []
