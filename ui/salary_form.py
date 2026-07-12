import tkinter as tk
from tkinter import ttk, messagebox

from controllers.salary_controller import SalaryController


class SalaryForm:

    def __init__(self, parent):

        self.controller = SalaryController()
        self.table = None

        tk.Label(
            parent,
            text="Salary Details",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#1E3A8A"
        ).pack(pady=10)

        form = tk.Frame(parent, bg="white")
        form.pack(fill="x", padx=20, pady=10)

        fields = [
            "Employee ID",
            "Employee Name",
            "Department",
            "Basic Salary",
            "Bonus",
            "Deductions",
            "Salary Month"
        ]

        self.entries = {}

        for i, field in enumerate(fields):

            tk.Label(
                form,
                text=field,
                bg="white",
                font=("Segoe UI", 10)
            ).grid(row=i, column=0, sticky="w", pady=6)

            entry = ttk.Entry(form, width=30)
            entry.grid(row=i, column=1, padx=10, pady=6)

            self.entries[field] = entry

        btn = tk.Frame(parent, bg="white")
        btn.pack(pady=15)

        ttk.Button(
            btn,
            text="Save",
            width=12,
            command=self.save_salary
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            btn,
            text="Clear",
            width=12,
            command=self.clear_form
        ).grid(row=0, column=1, padx=5)

    def save_salary(self):

        success, message = self.controller.add_salary(self.entries)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    def clear_form(self):

        for widget in self.entries.values():
            widget.delete(0, tk.END)