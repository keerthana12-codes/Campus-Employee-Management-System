import tkinter as tk
from ui.employee import EmployeePage
from ui.attendance import AttendancePage
from ui.salary import SalaryPage
from ui.reports import ReportsPage

class Dashboard:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Campus Employee Management System")
        self.root.state("zoomed")
        self.root.configure(bg="#F4F6F9")

        # ================= Sidebar =================

        sidebar = tk.Frame(
            self.root,
            bg="#1E3A8A",
            width=230
        )

        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Logo

        tk.Label(
            sidebar,
            text="🏢 CAMPUS EMS",
            bg="#1E3A8A",
            fg="white",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=20)

        # Menu Buttons

        menus = [

            ("🏠 Dashboard", self.show_dashboard),
            ("👨 Employees", self.show_employee),
            ("🏢 Departments", self.not_available),
            ("📅 Attendance", self.show_attendance),
            ("💰 Salary", self.show_salary),
            ("📄 Reports", self.show_reports),
            ("⚙ Settings", self.not_available),
            ("🚪 Logout", self.logout)

        ]

        for text, command in menus:

            tk.Button(
                sidebar,
                text=text,
                command=command,
                bg="#1E3A8A",
                fg="white",
                relief="flat",
                bd=0,
                activebackground="#2563EB",
                activeforeground="white",
                anchor="w",
                padx=20,
                font=("Segoe UI", 11)
            ).pack(fill="x", ipady=12)

        # ================= Main Content =================

        self.content = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        self.content.pack(fill="both", expand=True)

        self.show_dashboard()

        self.root.mainloop()

    # ===============================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ===============================================

    def show_dashboard(self):

        self.clear_content()

        header = tk.Frame(
            self.content,
            bg="white",
            height=70
        )

        header.pack(fill="x")

        tk.Label(
            header,
            text="Dashboard",
            bg="white",
            font=("Segoe UI", 24, "bold")
        ).pack(side="left", padx=20, pady=15)

        # -------- Dashboard Cards --------

        card_frame = tk.Frame(
            self.content,
            bg="#F4F6F9"
        )

        card_frame.pack(fill="x", padx=20, pady=20)

        cards = [

            ("Employees", "0"),
            ("Departments", "0"),
            ("Attendance", "0%"),
            ("Salary", "₹0")

        ]

        for title, value in cards:

            card = tk.Frame(
                card_frame,
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
                text=value,
                bg="white",
                fg="#1E3A8A",
                font=("Segoe UI", 26, "bold")
            ).pack()

        # Welcome Area

        welcome = tk.Frame(
            self.content,
            bg="white"
        )

        welcome.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        tk.Label(
            welcome,
            text="Welcome to Campus Employee Management System",
            bg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=80)

    # ===============================================

    def show_employee(self):

        self.clear_content()

        EmployeePage(self.content)

    
    # ===============================================
    
    def not_available(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="🚧 Module Under Development",
            font=("Segoe UI", 28, "bold"),
            bg="#F4F6F9"
        ).pack(expand=True)

    # ===============================================

    def logout(self):

        self.root.destroy()
    
    def show_attendance(self):

        self.clear_content()

        AttendancePage(self.content)
    
    def show_salary(self):

        self.clear_content()

        SalaryPage(self.content)

    def show_reports(self):

        self.clear_content()

        ReportsPage(self.content)