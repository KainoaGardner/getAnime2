from sqlalchemy.orm import Session
from app.database.models import Users
from app.database.schemas import User, UserCreate

from app.password import get_password_hash


def get_all(db: Session):
    return db.query(Users).all()


def get_user_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def get_user_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()


def create_user(db: Session, new_user: UserCreate):
    hashed_password = get_password_hash(new_user.password)
    user = Users(username=new_user.username, password=hashed_password)
    db.add(user)
    db.commit()
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return user
