import tkinter as tk
from tkinter import ttk

from database.attendance_model import AttendanceModel


class AttendanceTable:

    def __init__(self, parent):

        self.parent = parent
        self.form = None
        self.model = AttendanceModel()

        # ---------------- Search ----------------

        top = tk.Frame(parent, bg="white")
        top.pack(fill="x", padx=15, pady=10)

        tk.Label(
            top,
            text="Search",
            bg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side="left")

        self.search = ttk.Entry(top, width=35)
        self.search.pack(side="left", padx=10)

        ttk.Button(
            top,
            text="Search",
            command=self.search_attendance
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Refresh",
            command=self.load_data
        ).pack(side="left", padx=5)

        # ---------------- Table ----------------

        table_frame = tk.Frame(parent, bg="white")
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = (
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Check In",
            "Check Out",
            "Status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_row
        )

        self.load_data()

    # ----------------------------------------

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.model.get_all_attendance()

        for row in rows:
            self.tree.insert("", "end", values=row)

    # ----------------------------------------

    def search_attendance(self):

        keyword = self.search.get().lower()

        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.model.get_all_attendance()

        for row in rows:

            if keyword in str(row).lower():
                self.tree.insert("", "end", values=row)

    # ----------------------------------------

    def select_row(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        if self.form:
            self.form.set_data(values)