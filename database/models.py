from database.connection import get_connection


class EmployeeModel:

    def add_employee(self, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO employees (
                employee_id,
                full_name,
                gender,
                phone,
                email,
                department,
                designation,
                salary,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["employee_id"],
            data["full_name"],
            data["gender"],
            data["phone"],
            data["email"],
            data["department"],
            data["designation"],
            data["salary"],
            data["status"]
        ))

        conn.commit()
        conn.close()

    def get_all_employees(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                employee_id,
                full_name,
                gender,
                phone,
                email,
                department,
                designation,
                salary,
                status
            FROM employees
        """)

        rows = cursor.fetchall()
        conn.close()

        return rows

    def update_employee(self, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE employees
            SET
                full_name=?,
                gender=?,
                phone=?,
                email=?,
                department=?,
                designation=?,
                salary=?,
                status=?
            WHERE employee_id=?
        """, (
            data["full_name"],
            data["gender"],
            data["phone"],
            data["email"],
            data["department"],
            data["designation"],
            data["salary"],
            data["status"],
            data["employee_id"]
        ))

        conn.commit()
        conn.close()

    def delete_employee(self, employee_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id=?",
            (employee_id,)
        )

        conn.commit()
        conn.close()