import sqlite3
from contextlib import contextmanager

sqlite_file_name= "school.db"
@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try: 
        yield connection
        connection.commit()
    finally:
        connection.close()


def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT  NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                country TEXT NOT NULL,
                id_number INTEGER NOT NULL
                )''')



def add_student(name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, age, email, country, id_number) VALUES (?,?,?,?,?)',
            (name, age, email, country, id_number),
        )


def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()



#teachers
def teachers_table():
    with get_connection() as teacher_connection:
        teacher_connection.execute('''CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT  NOT NULL,
                email TEXT NOT NULL,
                teachers_id INTEGER NOT NULL
                class_assigned TEXT NOT NULL

                )''')
def add_teachers (name, email, teacher_id, class_assigned):
    with get_connection() as teacher_connection:
        teacher_connection.execute(
            'INSERT INTO teachers (name, email, teachers_id,class_assigned) VALUES (?,?,?,?)'
            (name, email, teacher_id, class_assigned),
        )


def get_teachers():
    with get_connection() as teacher_connection:
        return teacher_connection.execute('SELECT * FROM teachers').fetchall()

def classes(name, class_assigned):
    with get_connection() as teacher_connection:
        return teacher_connection.execute('SELECT name, class_assigned FROM teachers').fetchall()

        
def class_teach():
    with get_connection() as teacher_connection:
        return teacher_connection.execute('SELECT name, class_assigned FROM teachers').fetchall()



#courses
def courses_table():
    with get_connection() as courses_connection:
        courses_connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                name TEXT  NOT NULL,
                teacher TEXT NOT NULL,
                semester TEXT NOT NULL,
                teacher_id INTEGER NOT NULL,

                )''')


def add_course(title: str, code: str, credits: int, semester: str, teacher_id: int):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO courses (title, code, credits, semester, teacher_id) VALUES (?, ?, ?, ?, ?)",
            (title, code, credits, semester, teacher_id),
        )

def get_all_courses():
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses")
        return [dict(row) for row in cursor.fetchall()]


def delete_course(course_id: int):
    with get_connection() as connection:
        connection.execute("DELETE FROM courses WHERE id = ?", (course_id,))


def get_course_by_code(code: str):
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses WHERE code = ?", (code,))
        row = cursor.fetchone()
        return dict(row) if row else None



def update_course(course_id: int, title: str, code: str, credits: int, semester: str, teacher_id: int):
    with get_connection() as connection:
        connection.execute(
            """UPDATE courses
               SET title = ?, code = ?, credits = ?, semester = ?, teacher_id = ?
               WHERE id = ?""",
            (title, code, credits, semester, teacher_id, course_id),
        )


def get_course_by_id(course_id: int):
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
















