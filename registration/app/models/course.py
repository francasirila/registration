from database import get_connection


def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            department TEXT NOT NULL,
            credits INTEGER NOT NULL,
            course_id INTEGER NOT NULL
            )''')