from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    watching = relationship("Entries", cascade="all,delete-orphan", backref="users")


class Entries(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    japanese_title = Column(String, index=True)
    mal_id = Column(Integer)
    image = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
