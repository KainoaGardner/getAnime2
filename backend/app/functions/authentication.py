import jwt

from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.database.database import get_db
from app.database import models
from app.password import verify_password
from app.env import JWT_SECRET_KEY

ALGORITHM = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")
db_dependency = Annotated[Session, Depends(get_db)]


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    token = jwt.encode(encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: str = payload.get("id")
        if not username or not user_id:
            raise HTTPException(status_code=401, detail="Could not validate user")
        return {"username": username, "id": user_id}
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Could not validate user")


user_dependency = Annotated[dict, Depends(get_current_user)]


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    else:
        return user
