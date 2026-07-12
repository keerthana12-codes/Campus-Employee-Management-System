from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from database.connection import get_connection


def export_employees_pdf():

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

    data = [[
        "ID",
        "Name",
        "Gender",
        "Phone",
        "Email",
        "Department",
        "Designation",
        "Salary",
        "Status"
    ]]

    for row in rows:
        data.append(list(row))

    pdf = SimpleDocTemplate("Employee_Report.pdf")

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

    ]))

    pdf.build([table])

    return "Employee_Report.pdf"