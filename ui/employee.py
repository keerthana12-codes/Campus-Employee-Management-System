import tkinter as tk
from ui.employee_form import EmployeeForm
from ui.employee_table import EmployeeTable


class EmployeePage:

    def __init__(self, parent):

        self.main_frame = tk.Frame(parent, bg="#F4F6F9")
        self.main_frame.pack(fill="both", expand=True)

        # ---------------- Header ----------------

        header = tk.Frame(
            self.main_frame,
            bg="white",
            height=60
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="Employee Management",
            bg="white",
            fg="#1E3A8A",
            font=("Segoe UI", 22, "bold")
        ).pack(side="left", padx=20, pady=10)

        # ---------------- Body ----------------

        body = tk.Frame(
            self.main_frame,
            bg="#F4F6F9"
        )

        body.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Panel

        left = tk.Frame(
            body,
            bg="white",
            width=420
        )

        left.pack(side="left", fill="y", padx=(0, 15))
        left.pack_propagate(False)

        # Right Panel

        right = tk.Frame(
            body,
            bg="white"
        )

        right.pack(side="right", fill="both", expand=True)

        # Create Table First

        self.employee_table = EmployeeTable(right)

        # Create Form

        self.employee_form = EmployeeForm(left)

        # Connect Form ↔ Table

        self.employee_form.table = self.employee_table
        self.employee_table.form = self.employee_form