from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import users as user_schemas
from ..models import users as user_models
from passlib.context import CryptContext
from ..middleware.auth import create_access_token, get_current_user

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=user_schemas.Token)
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Debug wrapper: Catch any exceptions during registration
    try:
        # Check if user exists
        db_user = db.query(user_models.User).filter(user_models.User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create new user
        hashed_password = pwd_context.hash(user.password)
        db_user = user_models.User(
            email=user.email,
            hashed_password=hashed_password,
            full_name=user.full_name,
            user_type=user.user_type,
            phone=user.phone
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        # Create access token
        access_token = create_access_token(data={"sub": str(db_user.id)})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        # Debug: Print the actual error to server logs
        print(f"Registration error: {str(e)}")
        # Return a more detailed error message to client for debugging
        # Note: In production, you might want to hide detailed errors
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", response_model=user_schemas.Token)
def login(user_credentials: user_schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(user_models.User).filter(user_models.User.email == user_credentials.email).first()
    if not user or not pwd_context.verify(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=user_schemas.User)
def get_current_user(current_user: user_models.User = Depends(get_current_user)):
    return current_user
