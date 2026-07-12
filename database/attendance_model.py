from database.connection import get_connection


class AttendanceModel:

    def add_attendance(self, data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO attendance
            (
                employee_id,
                employee_name,
                department,
                date,
                check_in,
                check_out,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (

            data["employee_id"],
            data["employee_name"],
            data["department"],
            data["date"],
            data["check_in"],
            data["check_out"],
            data["status"]

        ))

        conn.commit()
        conn.close()

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

    def get_all_attendance(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                employee_id,
                employee_name,
                department,
                date,
                check_in,
                check_out,
                status
            FROM attendance
            ORDER BY date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
    def update_attendance(self, data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE attendance
            SET
                employee_name=?,
                department=?,
                date=?,
                check_in=?,
                check_out=?,
                status=?
            WHERE employee_id=?
        """, (

            data["employee_name"],
            data["department"],
            data["date"],
            data["check_in"],
            data["check_out"],
            data["status"],
            data["employee_id"]

        ))

        conn.commit()
        conn.close()

    def delete_attendance(self, employee_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM attendance WHERE employee_id=?",
            (employee_id,)
        )

        conn.commit()
        conn.close()
