from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import users as user_schemas
from ..models import users as user_models
from ..middleware.auth import get_current_user
from uuid import UUID

router = APIRouter()

@router.get("/me", response_model=user_schemas.User)
def read_user_me(current_user: user_models.User = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    # Debug: Print the user_id we're looking for
    print(f"Looking for user with ID: {user_id}")

    # Try to convert string to UUID
    try:
        user_uuid = UUID(user_id)
    except ValueError as e:
        print(f"Invalid UUID format: {e}")
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()

    # Debug: Print query result
    if db_user:
        print(f"Found user: {db_user.email}")
    else:
        print("No user found")

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
