import tkinter as tk
from tkinter import ttk

from controllers.salary_controller import SalaryController


class SalaryTable:

    def __init__(self, parent):

        self.controller = SalaryController()
        self.form = None

        top = tk.Frame(parent, bg="white")
        top.pack(fill="x", padx=15, pady=10)

        tk.Label(
            top,
            text="Salary Records",
            bg="white",
            font=("Segoe UI", 11, "bold")
        ).pack(side="left")

        ttk.Button(
            top,
            text="Refresh",
            command=self.load_data
        ).pack(side="right")

        columns = (
            "Employee ID",
            "Employee Name",
            "Department",
            "Basic Salary",
            "Bonus",
            "Deductions",
            "Net Salary",
            "Salary Month"
        )

        self.tree = ttk.Treeview(
            parent,
            columns=columns,
            show="headings",
            height=20
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)

        scrollbar = ttk.Scrollbar(
            parent,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(15, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            pady=10
        )

        self.load_data()

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.controller.get_all_salary()

        for row in rows:
            self.tree.insert("", "end", values=row)