from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from app.models.userModel import UserRole


# -----------------------------
# Base Schema
# -----------------------------

class UserBase(BaseModel):
    full_name: str = Field(..., max_length=100)
    email: EmailStr
    role: UserRole = UserRole.staff


# -----------------------------
# Create Schema
# -----------------------------

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


# -----------------------------
# Login Schema
# -----------------------------

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# -----------------------------
# Response Schema
# -----------------------------

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Important for SQLAlchemy compatibility


# -----------------------------
# Token Response Schema
# -----------------------------

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"