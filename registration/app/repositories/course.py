from database import get_connection

def add_courses(name, description, department, credits, course_id):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (name, description, department, credits, course_id) VALUES(?, ?, ?, ?, ?)',
            (name, description, department, credits, course_id)
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def get_course(id):
    with get_connection() as connection:
        return connection.execute(
            'SELECT * FROM courses WHERE id = ?', (id,)
        ).fetchone()

def update_course(id, name, description, department, credits, course_id):
    with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET name = ?, description = ?, department = ?, credits = ?, course_id = ? WHERE id = ?',
            (name, description, department, credits, course_id, id)
        )

def delete_course(id):
    with get_connection() as connection:
        connection.execute(
            'DELETE FROM courses WHERE id = ?', (id,)
        )