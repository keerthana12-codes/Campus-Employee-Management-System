import tkinter as tk
from ui.salary_form import SalaryForm
from ui.salary_table import SalaryTable


class SalaryPage:

    def __init__(self, parent):

        self.main_frame = tk.Frame(parent, bg="#F4F6F9")
        self.main_frame.pack(fill="both", expand=True)

        # Header
        header = tk.Frame(self.main_frame, bg="white", height=60)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Salary Management",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#1E3A8A"
        ).pack(side="left", padx=20, pady=10)

        # Body
        body = tk.Frame(self.main_frame, bg="#F4F6F9")
        body.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Panel
        left = tk.Frame(body, bg="white", width=420)
        left.pack(side="left", fill="y", padx=(0, 15))
        left.pack_propagate(False)

        # Right Panel
        right = tk.Frame(body, bg="white")
        right.pack(side="right", fill="both", expand=True)

        self.salary_table = SalaryTable(right)
        self.salary_form = SalaryForm(left)

        self.salary_form.table = self.salary_table
        self.salary_table.form = self.salary_form