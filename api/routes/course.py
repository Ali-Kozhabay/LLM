import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.crud.course import course_crud
from app.models.user import User
from app.api.deps import get_current_superuser
from app.schemas.course import CourseCreate, CoursePublish

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)

router = APIRouter()

@router.get("/courses")
async def get_courses(db: AsyncSession = Depends(get_db)):
    logger.info("Fetching all courses")
    courses = await course_crud.get_courses_from_db(db)
    return courses.scalars().all()


@router.post("/creating_courses")
async def create_courses(
    db: AsyncSession = Depends(get_db),
    current_user: User=Depends(get_current_superuser),
    course:CourseCreate =Depends()
):
    try:
        return await course_crud.create_course_for_db(db=db,course=course)
    except Exception as e:
        raise e
    
@router.post("/publish_course")
async def publish_courses(
    db: AsyncSession = Depends(get_db),
    current_user: User=Depends(get_current_superuser),
    publish:CoursePublish =Depends()
):
    try:
        return await course_crud.publish_course(db=db,publish=publish)
    except Exception :
        raise Exception



    

