from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user
from app.core.database import get_db
from app.crud.user import user_crud
from app.models.user import User
from app.schemas.user import UserInDB, UserUpdate

router = APIRouter()

@router.get("/me", response_model=UserInDB)
async def read_user_me(current_user: User = Depends(get_current_active_user)):
    """Get current user profile"""
    return current_user

@router.put("/me", response_model=UserInDB)
async def update_user_me(
    user_in: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user profile"""
    user = await user_crud.update(db, user_id=current_user.id, user_in=user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
