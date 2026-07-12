from database.models import EmployeeModel


class EmployeeController:

    def __init__(self):
        self.model = EmployeeModel()

    def add_employee(self, entries):

        data = self.get_data(entries)

        for value in data.values():
            if value == "":
                return False, "Please fill all fields."

        try:
            data["salary"] = float(data["salary"])
            self.model.add_employee(data)
            return True, "Employee added successfully."
        except Exception as e:
            return False, str(e)

    def update_employee(self, entries):

        data = self.get_data(entries)

        for value in data.values():
            if value == "":
                return False, "Please fill all fields."

        try:
            data["salary"] = float(data["salary"])
            self.model.update_employee(data)
            return True, "Employee updated successfully."
        except Exception as e:
            return False, str(e)

    def delete_employee(self, employee_id):

        try:
            self.model.delete_employee(employee_id)
            return True, "Employee deleted successfully."
        except Exception as e:
            return False, str(e)

    def get_data(self, entries):

        return {
            "employee_id": entries["Employee ID"].get().strip(),
            "full_name": entries["Full Name"].get().strip(),
            "gender": entries["Gender"].get().strip(),
            "phone": entries["Phone"].get().strip(),
            "email": entries["Email"].get().strip(),
            "department": entries["Department"].get().strip(),
            "designation": entries["Designation"].get().strip(),
            "salary": entries["Salary"].get().strip(),
            "status": entries["Status"].get().strip()
        }