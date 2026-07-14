from fastapi import APIRouter
from schemas.course import Course
from repositories.course import (
    add_courses,
    get_courses,
    get_course,
    update_course,
    delete_course,
)




router = APIRouter(prefix ="/courses", tags =["courses"])



@router.get("")  
def list_courses_end():
    return get_courses()

@router.get("/{id}")  
def course_details_end(id: int):
    return get_course(id)

@router.post("")
def register_course_end(course: Course):
    add_courses(course.name, course.description, course.department, course.credits, course.course_id)
    return {"message": "Course registered successfully", "course": course}

@router.put("/{id}")
def update_courses_end(id: int, course: Course):
    update_course(id, course.name, course.description, course.department, course.credits, course.course_id)
    return {"message": "Course updated successfully", "course": course}

@router.delete("/{id}")
def delete_course_end(id: int):
    delete_course(id)
    return {"message": "Course deleted"}