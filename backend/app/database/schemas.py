from pydantic import BaseModel
from sqlalchemy import Date
from datetime import date


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


class EntryBase(BaseModel):
    title: str
    japanese_title: str
    show_id: int
    show_image: str


class EntryCreate(EntryBase):
    user_id: int


class Entry(EntryBase):
    id: int
    user_id: int


class Anime(BaseModel):
    title: str
    japanese_title: str
    show_id: int
    show_image: str


class Token(BaseModel):
    access_token: str
    token_type: str
    id: int
