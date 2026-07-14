from database import get_connection


def add_teachers(name, phone_number, email, department, teacher_id):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, phone_number, email, department, teacher_id) VALUES(?, ?, ?, ?, ?)',
            (name, phone_number, email, department, teacher_id)
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def get_teacher(id):
    with get_connection() as connection:
        return connection.execute(
            'SELECT * FROM teachers WHERE id = ?', (id,)
        ).fetchone()

def update_teacher(id, name, phone_number, email, department, teacher_id):
    with get_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name = ?, phone_number = ?, email = ?, department = ?, teacher_id = ? WHERE id = ?',
            (name, phone_number, email, department, teacher_id, id)
        )

def delete_teacher(id):
    with get_connection() as connection:
        connection.execute(
            'DELETE FROM teachers WHERE id = ?', (id,)
        )
