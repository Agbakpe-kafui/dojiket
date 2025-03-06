from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import users as user_schemas
from ..models import users as user_models
from ..middleware.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=user_schemas.User)
def read_user_me(current_user: user_models.User = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
