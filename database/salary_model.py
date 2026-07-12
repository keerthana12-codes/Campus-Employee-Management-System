from database.connection import get_connection


class SalaryModel:

    def add_salary(self, data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO salary(
            employee_id,
            employee_name,
            department,
            basic_salary,
            bonus,
            deductions,
            net_salary,
            salary_month
        )
        VALUES(?,?,?,?,?,?,?,?)
        """, (

            data["employee_id"],
            data["employee_name"],
            data["department"],
            data["basic_salary"],
            data["bonus"],
            data["deductions"],
            data["net_salary"],
            data["salary_month"]

        ))

        conn.commit()
        conn.close()

    def get_all_salary(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            department,
            basic_salary,
            bonus,
            deductions,
            net_salary,
            salary_month
        FROM salary
        ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows