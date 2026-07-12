from openpyxl import Workbook
from database.connection import get_connection


def export_employees():

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

    wb = Workbook()
    ws = wb.active
    ws.title = "Employees"

    headers = [
        "Employee ID",
        "Full Name",
        "Gender",
        "Phone",
        "Email",
        "Department",
        "Designation",
        "Salary",
        "Status"
    ]

    ws.append(headers)

    for row in rows:
        ws.append(row)

    wb.save("Employee_Report.xlsx")

    conn.close()

    return "Employee_Report.xlsx"
    