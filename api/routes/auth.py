import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.config import settings
from app.core.database import get_db
from app.core.security import create_access_token
from app.crud.user import user_crud
from app.schemas.user import Token, UserCreate, UserInDB


logger= logging.getLogger(__name__)
router = APIRouter()

@router.post("/register")
async def register(user_in: UserCreate=Depends(), db: AsyncSession = Depends(get_db)):
    """Register a new user"""
    try:
        user = await user_crud.create(db, user_in=user_in)
        logger.info(f"User registered: {user.email}")
        return user
    except ValueError as e:
        logger.error(f"User registration failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    """Login and get access token"""
    user = await user_crud.authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.username, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
