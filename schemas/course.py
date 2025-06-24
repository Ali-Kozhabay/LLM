import enum

from pydantic import BaseModel


class CourseCreate(BaseModel):
    title : str
    description : str
    teacher_id : int
    price : float

    
class CoursePublish(BaseModel):
    id: int
    publish: bool
