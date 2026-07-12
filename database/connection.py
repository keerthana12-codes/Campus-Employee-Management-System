import sqlite3

DB_NAME = "database/employee.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ================= USERS =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # ================= EMPLOYEES =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        employee_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        gender TEXT,
        phone TEXT,
        email TEXT,
        department TEXT,
        designation TEXT,
        salary REAL,
        status TEXT
    )
    """)

    # ================= ATTENDANCE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        employee_name TEXT,
        department TEXT,
        date TEXT,
        check_in TEXT,
        check_out TEXT,
        status TEXT
    )
    """)

    # ================= SALARY =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salary(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        employee_name TEXT,
        department TEXT,
        basic_salary REAL,
        bonus REAL,
        deductions REAL,
        net_salary REAL,
        salary_month TEXT
    )
    """)

    # ================= DEFAULT ADMIN =================

    cursor.execute("""
    INSERT OR IGNORE INTO users(username,password)
    VALUES('admin','admin123')
    """)

    conn.commit()
    conn.close()