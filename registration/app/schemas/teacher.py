from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    phone_number: str
    email: str
    department: str
    teacher_id: int