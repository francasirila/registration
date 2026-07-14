from database import get_connection

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone_number INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    department TEXT NOT NULL,
                    teacher_id INTEGER NOT NULL
                    )''')