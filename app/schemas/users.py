from pydantic import BaseModel, EmailStr
from typing import Optional
from models.users import UserType

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    user_type: UserType

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None 