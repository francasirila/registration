from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel




app = FastAPI()
create_table()

class Student(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int



class Teachers(BaseModel):
    name: str
    email: str
    teacher_id: int
    department: str
    class_assigned : str
    phone: int
    employee_number: int



class Courses(BaseModel):
    name: str
    course_id: int
    teacher_id: int
    semester: str
    credit: int
    projects: str
    code:int




students =[]
teachers =[]
courses =[]


@app.get("/")  #decorator
def home():
    return {"message": "welcome to my API server"}



@app.get("/students")#route endpoint
def list_students():
    students =get_students()
    return students

       



@app.post("/students")
def register_students(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "student registered successfully", "student": student}




#teachers
@app.get("/teachers")
def list_teachers():
    return teachers



@app.put("/teachers")
def class_teacher():
    teach = class_teach()
    
    for row in db_rows:
        teacher_list.append({
            "class": row[1], 
            "is currently having their class teacher": row[0]
        })
        
    return {"teachers_schedule": teacher_list}



@app.get("/teachers")
def class_details():
    classes(teacher.name, teacher.class_assigned)
    return {"teacher": name ,"has been asigned to": class_assigned}




@app.post("/teachers")
def teachers_details(teachers : Teachers):
    add_teachers(teachers.name, teachers.email, teachers.teacher_id, teachers.class_assigned)
    return {"name of the teacher": name}




#courses

@app.post("/courses")
def register_course(course: CourseItem):
    existing_course = get_course_by_code(course.code)
    if existing_course:
        raise HTTPException(status_code=400, detail="Course with this course code already exists.")



    teacher = get_teacher_by_id(course.teacher_id)
    if not teacher:
        raise HTTPException(status_code=400, detail="Assigned Teacher ID does not exist.")

    add_course(
        title=course.title,
        code=course.code,
        credits=course.credits,
        semester=course.semester,
        teacher_id=course.teacher_id
    )
    return {"status": "success", "message": f"Course {course.title} created successfully!"}



@app.get("/courses")
def get_courses_list():
    return get_all_courses()



@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: CourseItem):
    existing = get_course_by_id(course_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Course not found.")

    teacher = get_teacher_by_id(course.teacher_id)
    if not teacher:
        raise HTTPException(status_code=400, detail="Assigned Teacher ID does not exist.")

    update_course(
        course_id=course_id,
        title=course.title,
        code=course.code,
        credits=course.credits,
        semester=course.semester,
        teacher_id=course.teacher_id
)
    return {"status": "success", "message": "Course record updated successfully!"}



@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    if not existing:
        raise HTTPException(status_code=404, detail="Course not found.")

    delete_course(course_id)
    return {"status": "success", "message": "Course record deleted successfully!"}






