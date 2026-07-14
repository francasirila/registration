from pydantic import BaseModel


class Course(BaseModel):
    name: str
    description: str
    department: str
    credits: int
    course_id: int
