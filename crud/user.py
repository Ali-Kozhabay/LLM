from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select 
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from typing import Optional

class UserCRUD:
    async def get_by_email(self, db: AsyncSession, email: str) -> Optional[User]:
        res=await db.execute(select(User).where(User.email == email))
        return res.scalar_one_or_none()
    
    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        res=await db.execute(select(User).where(User.username == username))
        return res.scalar_one_or_none()

    async def get_by_id(self, db: AsyncSession, user_id: int) -> Optional[User]:
        res=await db.execute(select(User).where(User.id == user_id))
        return res.scalar_one_or_none()

    async def create(self, db: AsyncSession, user_in: UserCreate) -> User:
        hashed_password = get_password_hash(user_in.password)
        db_user = User(
            email=user_in.email,
            username=user_in.username,
            hashed_password=hashed_password,
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            role=user_in.role
        )
        try:
            db.add(db_user)
            await db.commit()
            await db.refresh(db_user)
            return db_user
        except IntegrityError:
            await db.rollback()
            raise ValueError("User with this email or username already exists")

    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        user = await self.get_by_username(db, username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
    
    async def update(self, db: AsyncSession, user_id: int, user_in: UserUpdate) -> Optional[User]:
        user = await self.get_by_id(db, user_id)
        if not user:
            return HTTPException(status_code=404, detail="User not found")
        
        update_data = user_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        await db.commit()
        await db.refresh(user)
        return user

user_crud = UserCRUD()