from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import userCrud
from app.schemas.userSchema import UserCreate, UserUpdate, UserResponse
from app.core.dependencies import get_db, require_admin, require_manager_or_admin, require_role
from typing import List
from app.services.activity_logger import log_activity

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return userCrud.get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):

    user = userCrud.get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    updates: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role)
):

    user = userCrud.update_user(db, user_id, updates)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    log_activity(
        db=db,
        action= f"Updated user to {user.full_name}",
        user_id=user_id
    )
    return user

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):

    user = userCrud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    log_activity(
        db=db,
        action= f"Admin: {current_user.full_name} deleted user: {user.full_name}",
        user_id=user_id
    )
    userCrud.delete_user(db, user)
    return {"message": "User deleted"}
