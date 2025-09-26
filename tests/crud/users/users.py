import pytest
import asyncio

from app.crud.user import user_crud
from app.models.user import UserRole
from app.schemas.user import UserCreate


from app.core.database import get_db

def testing_register():
    db = await get_db()
    name=UserCreate(
        email="test@gmail.com",
        password="test",
        username="test",
        first_name="test",
        last_name="test",)
    user = await user_crud.create(db=db,user_in=name)
    assert user.id == user.id
    assert user.email == user.email
