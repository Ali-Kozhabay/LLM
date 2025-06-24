
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.course import Course
from app.schemas.course import CourseCreate, CoursePublish


class CourseCRUD:

    async def get_courses_from_db(self,db:AsyncSession):
        res= await db.execute(select(Course).where(Course.is_published==True))
        return res
    
    async def create_course_for_db(self, db:AsyncSession, course:CourseCreate):
        db_course=Course(
            title = course.title,
            description = course.description,
            teacher_id = course.teacher_id,
            price = course.price
        )
        db.add(db_course)
        await db.commit()
        await db.refresh(db_course)
        
        return {'message':"Course is created"}
        
    async def publish_course(self,db:AsyncSession,publish: CoursePublish):
        try:
            await db.execute(update(Course).where(Course.id == publish.id).values(is_published=publish.publish))
            await db.commit()
            return {'message':'Course is published'}
        except Exception as e:
            raise e
    
        
        
        
        
        



course_crud = CourseCRUD()
