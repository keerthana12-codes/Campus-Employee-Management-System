from database.connection import get_connection


class ReportController:

    def get_counts(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM employees")
        employees = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM attendance")
        attendance = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM salary")
        salary = cursor.fetchone()[0]

        conn.close()

        return {
            "employees": employees,
            "attendance": attendance,
            "salary": salary
        }