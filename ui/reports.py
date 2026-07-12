import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from controllers.report_controller import ReportController
from utils.excel_export import export_employees
from utils.pdf_export import export_employees_pdf

class ReportsPage:

    def __init__(self, parent):

        controller = ReportController()
        data = controller.get_counts()

        frame = tk.Frame(parent, bg="#F4F6F9")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Reports Dashboard",
            font=("Segoe UI", 22, "bold"),
            bg="#F4F6F9",
            fg="#1E3A8A"
        ).pack(pady=20)

        cards = tk.Frame(frame, bg="#F4F6F9")
        cards.pack(pady=20)

        reports = [

            ("Employees", data["employees"]),
            ("Attendance Records", data["attendance"]),
            ("Salary Records", data["salary"])

        ]

        for title, value in reports:

            card = tk.Frame(
                cards,
                bg="white",
                width=220,
                height=120,
                highlightbackground="#D1D5DB",
                highlightthickness=1
            )

            card.pack(side="left", padx=15)
            card.pack_propagate(False)

            tk.Label(
                card,
                text=title,
                bg="white",
                font=("Segoe UI", 14)
            ).pack(pady=15)

            tk.Label(
                card,
                text=str(value),
                bg="white",
                fg="#1E3A8A",
                font=("Segoe UI", 28, "bold")
            ).pack()

        # Export Button
        ttk.Button(
            frame,
            text="📄 Export Employees to Excel",
            command=self.export_excel
        ).pack(pady=20)

        ttk.Button(
            frame,
            text="📄 Export Employees to PDF",
            command=self.export_pdf
        ).pack(pady=10)

    def export_excel(self):

        filename = export_employees()

        messagebox.showinfo(
            "Success",
            f"Employee report exported successfully.\n\nSaved as:\n{filename}"
        )

    def export_pdf(self):

        filename = export_employees_pdf()

        messagebox.showinfo(
            "Success",
        f"PDF report exported successfully.\n\nSaved as:\n{filename}"
     )