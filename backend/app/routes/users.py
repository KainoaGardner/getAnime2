from fastapi import HTTPException, APIRouter, Depends

from sqlalchemy.orm import Session
from app.database.schemas import User, UserCreate, Settings
from app.database.database import get_db

from app.functions import users
from app.functions.authentication import user_dependency


router = APIRouter(prefix="/api/users", tags=["Users"])


# @router.get("/all", response_model=list[User])
# def get_all_users(db: Session = Depends(get_db)):
#     return users.get_all(db)
#


@router.get("/current", response_model=User)
def get_current_user(auth: user_dependency, db: Session = Depends(get_db)):
    return auth


@router.get("/settings", response_model=Settings)
def get_settings(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]
    print("test")
    return users.get_settings(db, user_id)


@router.put("/settings", response_model=Settings)
def update_settings(
    auth: user_dependency, new_settings: Settings, db: Session = Depends(get_db)
):
    user_id = auth["id"]
    return users.put_settings(db, user_id, new_settings)


@router.post("/create", response_model=User)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    if users.get_user_username(db, new_user.username):
        raise HTTPException(status_code=404, detail="Username already taken")

    return users.create_user(db, new_user)


@router.delete("/delete", response_model=User)
def delete_user(auth: user_dependency, db: Session = Depends(get_db)):
    user_id = auth["id"]
    user = users.get_user_id(db, user_id)

    return users.delete_user(db, user)
