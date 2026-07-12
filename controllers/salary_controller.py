from database.salary_model import SalaryModel


class SalaryController:

    def __init__(self):
        self.model = SalaryModel()

    def add_salary(self, entries):

        basic = float(entries["Basic Salary"].get())
        bonus = float(entries["Bonus"].get())
        deductions = float(entries["Deductions"].get())

        net_salary = basic + bonus - deductions

        data = {

            "employee_id": entries["Employee ID"].get(),
            "employee_name": entries["Employee Name"].get(),
            "department": entries["Department"].get(),
            "basic_salary": basic,
            "bonus": bonus,
            "deductions": deductions,
            "net_salary": net_salary,
            "salary_month": entries["Salary Month"].get()

        }

        self.model.add_salary(data)

        return True, "Salary saved successfully."

    def get_all_salary(self):
        return self.model.get_all_salary()