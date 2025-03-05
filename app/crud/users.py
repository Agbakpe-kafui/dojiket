from sqlalchemy.orm import Session
from ..models import users as user_models

def get_user(db: Session, user_id: str):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_models.User).filter(user_models.User.email == email).first()

def create_user(db: Session, user: user_models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 