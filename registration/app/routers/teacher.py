from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import(
    add_teachers,
    get_teachers,
    get_teacher,
    update_teacher,
    delete_teacher,
)




router = APIRouter(prefix ="/teachers", tags =["teachers"])





@router.get("")  
def list_teachers_end():
    return get_teachers()

@router.get("/{id}")
def teacher_details_end(id: int):
    return get_teacher(id)

@router.post("")
def register_teachers_end(teacher: Teacher):
    add_teachers(teacher.name, teacher.phone_number, teacher.email, teacher.department, teacher.teacher_id)
    return {"message": "Teacher registered successfully", "teacher": teacher}

@router.put("/{id}")
def update_teacher_end(id: int, teacher: Teacher):
    update_teacher(id, teacher.name, teacher.phone_number, teacher.email, teacher.department, teacher.teacher_id)
    return {"message": "Teacher updated successfully", "teacher": teacher}

@router.delete("/{id}")
def delete_teacher_end(id: int):
    delete_teacher(id)
    return {"message": "Teacher deleted"}