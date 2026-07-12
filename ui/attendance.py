import tkinter as tk
from ui.attendance_form import AttendanceForm
from ui.attendance_table import AttendanceTable


class AttendancePage:

    def __init__(self, parent):

        # Main Container
        self.main_frame = tk.Frame(parent, bg="#F4F6F9")
        self.main_frame.pack(fill="both", expand=True)

        # Header
        header = tk.Frame(
            self.main_frame,
            bg="white",
            height=60
        )
        header.pack(fill="x")

        tk.Label(
            header,
            text="Attendance Management",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#1E3A8A"
        ).pack(side="left", padx=20, pady=10)

        # Body
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

        # Create Table
        self.attendance_table = AttendanceTable(right)

        # Create Form
        self.attendance_form = AttendanceForm(left)

        # Connect Form and Table
        self.attendance_form.table = self.attendance_table
        self.attendance_table.form = self.attendance_form