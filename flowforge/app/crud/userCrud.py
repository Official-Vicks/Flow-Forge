from sqlalchemy.orm import Session
from app.models.userModel import User
from app.schemas.userSchema import UserCreate
from app.core.security import get_password_hash


# -----------------------------
# Get User by Email
# -----------------------------

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# -----------------------------
# Get User by ID
# -----------------------------

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# -----------------------------
# Create User
# -----------------------------

def create_user(db: Session, user_in: UserCreate):
    hashed_pw = get_password_hash(user_in.password)

    user = User(
        full_name=user_in.full_name,
        email=user_in.email,
        hashed_password=hashed_pw,
        role=user_in.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# -----------------------------
# List Users (Admin use later)
# -----------------------------

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()