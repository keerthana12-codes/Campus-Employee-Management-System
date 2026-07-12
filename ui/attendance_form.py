import tkinter as tk
from tkinter import ttk, messagebox

from controllers.attendance_controller import AttendanceController


class AttendanceForm:

    def __init__(self, parent):

        self.controller = AttendanceController()
        self.table = None

        title = tk.Label(
            parent,
            text="Attendance Details",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#1E3A8A"
        )
        title.pack(pady=10)

        form = tk.Frame(parent, bg="white")
        form.pack(fill="x", padx=20, pady=10)

        fields = [
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Check In",
            "Check Out",
            "Status"
        ]

        self.entries = {}

        for i, field in enumerate(fields):

            tk.Label(
                form,
                text=field,
                bg="white",
                font=("Segoe UI", 10)
            ).grid(row=i, column=0, sticky="w", pady=6)

            if field == "Status":

                widget = ttk.Combobox(
                    form,
                    values=["Present", "Absent", "Leave"],
                    state="readonly",
                    width=28
                )

            else:

                widget = ttk.Entry(
                    form,
                    width=30
                )

            widget.grid(row=i, column=1, padx=10, pady=6)

            self.entries[field] = widget

        # ---------------- Buttons ----------------
                   # ---------------- Buttons ----------------

        btn = tk.Frame(parent, bg="white")
        btn.pack(pady=15)
               
        ttk.Button(
            btn,
            text="Save",
            width=12,
            command=self.save_attendance
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            btn,
            text="Update",
            width=12,
            command=self.update_attendance
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            btn,
            text="Delete",
            width=12,
            command=self.delete_attendance
        ).grid(row=1, column=0, pady=10)

        ttk.Button(
            btn,
            text="Clear",
            width=12,
            command=self.clear_form
        ).grid(row=1, column=1)

        # ==========================================

    def update_attendance(self):

        success, message = self.controller.update_attendance(self.entries)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    # ==========================================

    def delete_attendance(self):

        employee_id = self.entries["Employee ID"].get().strip()

        if employee_id == "":

            messagebox.showwarning(
                "Warning",
                "Select an attendance record first."
            )

            return

        confirm = messagebox.askyesno(
            "Delete",
            "Delete this attendance record?"
        )

        if not confirm:
            return

        success, message = self.controller.delete_attendance(employee_id)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)
    # ==========================================

    def save_attendance(self):

        success, message = self.controller.add_attendance(self.entries)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

            if self.table:
                self.table.load_data()

        else:

            messagebox.showerror("Error", message)

    # ==========================================

    def clear_form(self):

        for widget in self.entries.values():

            if isinstance(widget, ttk.Combobox):
                widget.set("")
            else:
                widget.delete(0, tk.END)

    # ==========================================

    def set_data(self, values):

        fields = [
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Check In",
            "Check Out",
            "Status"
        ]

        self.clear_form()

        for field, value in zip(fields, values):

            widget = self.entries[field]

            if isinstance(widget, ttk.Combobox):
                widget.set(str(value))
            else:
                widget.insert(0, str(value))