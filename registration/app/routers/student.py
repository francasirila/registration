from fastapi import APIRouter
from schemas.student import Student
from repositories.student import(
    add_students,
    get_students,
    get_student,
    update_student,
    delete_student,
)




router = APIRouter(prefix ="/students", tags =["students"])



@router.get("")
def list_students_end():
    return get_students()

@router.get("/{id}")
def student_details_end(id: int):  
    return get_student(id)

@router.post("")
def register_student_end(student: Student):
    add_students(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully", "student": student}

@router.put("/{id}")
def update_student_end(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student updated successfully", "student": student}

@router.delete("/{id}")
def delete_student_end(id: int):
    delete_student(id)
    return {"message": "Student deleted"}