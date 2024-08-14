from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserChange(BaseModel):
    username: str | None = None
    password: str | None = None


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Entry(BaseModel):
    mal_id: int
    title: str
    japanese_title: str
    image: str


class EntryCreate(Entry):
    user_id: int


class EntryId(Entry):
    id: int
    user_id: int


class AnimeBase(BaseModel):
    title: str
    japanese_title: str
    image: str


class Anime(AnimeBase):
    mal_id: int


class WeeklyAnime(BaseModel):
    title: str
    airing_day: str
    episode: str


class Token(BaseModel):
    access_token: str
    token_type: str
    id: int
