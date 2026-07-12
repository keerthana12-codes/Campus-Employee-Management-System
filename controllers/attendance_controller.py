from database.attendance_model import AttendanceModel


class AttendanceController:

    def __init__(self):

        self.model = AttendanceModel()

    def add_attendance(self, entries):

        data = {

            "employee_id": entries["Employee ID"].get().strip(),
            "employee_name": entries["Employee Name"].get().strip(),
            "department": entries["Department"].get().strip(),
            "date": entries["Date"].get().strip(),
            "check_in": entries["Check In"].get().strip(),
            "check_out": entries["Check Out"].get().strip(),
            "status": entries["Status"].get().strip()

        }

        for value in data.values():

            if value == "":
                return False, "Please fill all fields."

        try:

            self.model.add_attendance(data)

            return True, "Attendance saved successfully."

        except Exception as e:

            return False, str(e)

    def update_attendance(self, entries):

        data = {

            "employee_id": entries["Employee ID"].get().strip(),
            "employee_name": entries["Employee Name"].get().strip(),
            "department": entries["Department"].get().strip(),
            "date": entries["Date"].get().strip(),
            "check_in": entries["Check In"].get().strip(),
            "check_out": entries["Check Out"].get().strip(),
            "status": entries["Status"].get().strip()

        }

        self.model.update_attendance(data)

        return True, "Attendance updated successfully."

    def delete_attendance(self, employee_id):

        self.model.delete_attendance(employee_id)

        return True, "Attendance deleted successfully."