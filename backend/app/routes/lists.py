from fastapi import APIRouter
from typing import Dict

from app.database.schemas import AnimeBase, WeeklyAnime

from app.functions import lists

router = APIRouter(prefix="/api/lists", tags=["Anime Lists"])


@router.get("/today", response_model=Dict[str, WeeklyAnime])
def get_airing_today():
    return lists.get_today()


@router.get("/weekly", response_model=Dict[str, WeeklyAnime])
def get_airing_weekly():
    return lists.get_weekly()


@router.get("/season", response_model=Dict[str, AnimeBase])
def get_season():
    return lists.get_season()
