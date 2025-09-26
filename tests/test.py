import pytest
import asyncio


from app.api.deps import get_current_user, get_current_superuser

def test_deps_get_current_user():
    res=get_current_user( "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTg4NjgzODYsInN1YiI6ImFsaSJ9.cK01N81zL2u7ExAvUMHX6hYYZ277jSqgvho_92f9HR0")
    assert res is not None
@pytest.mark.asyncio
async def test_deps_get_current_superuser():
    res=await get_current_superuser( "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTg4NjgzODYsInN1YiI6ImFsaSJ9.cK01N81zL2u7ExAvUMHX6hYYZ277jSqgvho_92f9HR0")
    assert res.role == "admin"