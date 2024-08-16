from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    japanese_titles = Column(Boolean)
    watching = relationship("Entries", cascade="all,delete-orphan", backref="users")

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.japanese_titles = False


class Entries(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    japanese_title = Column(String, index=True)
    mal_id = Column(Integer)
    image = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
