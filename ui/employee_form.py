import tkinter as tk
from tkinter import ttk, messagebox
from controllers.employee_controller import EmployeeController


class EmployeeForm:

    def __init__(self, parent):

        self.parent = parent
        self.controller = EmployeeController()
        self.table = None

        title = tk.Label(
            parent,
            text="Employee Details",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#1E3A8A"
        )

        title.pack(pady=10)

        form = tk.Frame(parent, bg="white")
        form.pack(fill="x", padx=20, pady=10)

        self.entries = {}

        labels = [
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

        for i, field in enumerate(labels):

            tk.Label(
                form,
                text=field,
                bg="white",
                font=("Segoe UI", 10)
            ).grid(row=i, column=0, sticky="w", pady=6)

            if field == "Gender":

                widget = ttk.Combobox(
                    form,
                    values=["Male", "Female", "Other"],
                    state="readonly",
                    width=28
                )

            elif field == "Status":

                widget = ttk.Combobox(
                    form,
                    values=["Active", "Inactive"],
                    state="readonly",
                    width=28
                )

            else:

                widget = ttk.Entry(
                    form,
                    width=30
                )

            widget.grid(
                row=i,
                column=1,
                padx=10,
                pady=6
            )

            self.entries[field] = widget

        # ---------------- Buttons ----------------

        btn = tk.Frame(parent, bg="white")
        btn.pack(pady=15)

        ttk.Button(
            btn,
            text="Add",
            width=12,
            command=self.add_employee
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            btn,
            text="Update",
            width=12,
            command=self.update_employee
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            btn,
            text="Delete",
            width=12,
            command=self.delete_employee
        ).grid(row=1, column=0, pady=10)

        ttk.Button(
            btn,
            text="Clear",
            width=12,
            command=self.clear_form
        ).grid(row=1, column=1)

    # ------------------------------------------------

    def add_employee(self):

        success, message = self.controller.add_employee(self.entries)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    # ------------------------------------------------

    def update_employee(self):

        success, message = self.controller.update_employee(self.entries)

        if success:

            messagebox.showinfo("Success", message)

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    # ------------------------------------------------

    def delete_employee(self):

        employee_id = self.entries["Employee ID"].get()

        if employee_id == "":

            messagebox.showwarning(
                "Warning",
                "Select an employee first."
            )

            return

        confirm = messagebox.askyesno(
            "Delete",
            "Delete this employee?"
        )

        if not confirm:
            return

        success, message = self.controller.delete_employee(employee_id)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    # ------------------------------------------------

    def clear_form(self):

        for widget in self.entries.values():

            if isinstance(widget, ttk.Combobox):
                widget.set("")
            else:
                widget.delete(0, tk.END)


        # ------------------------------------------------

    def set_data(self, values):

        self.clear_form()

        fields = [
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

        for field, value in zip(fields, values):

            widget = self.entries[field]

            if isinstance(widget, ttk.Combobox):
                widget.set(str(value))
            else:
                widget.insert(0, str(value))

    # ------------------------------------------------
     