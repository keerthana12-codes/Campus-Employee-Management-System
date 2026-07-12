import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from ui.dashboard import Dashboard


class LoginWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Campus Employee Management System")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        # Left Panel
        left = tk.Frame(self.root, bg="#1E3A8A", width=350)
        left.pack(side="left", fill="y")

        tk.Label(
            left,
            text="Campus Employee\nManagement System",
            fg="white",
            bg="#1E3A8A",
            font=("Segoe UI", 24, "bold")
        ).place(relx=0.5, rely=0.4, anchor="center")

        # Right Panel
        right = tk.Frame(self.root, bg="white")
        right.pack(fill="both", expand=True)

        tk.Label(
            right,
            text="Login",
            bg="white",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=30)

        tk.Label(right, text="Username", bg="white").pack()

        self.username = ttk.Entry(right, width=30)
        self.username.pack(pady=5)

        tk.Label(right, text="Password", bg="white").pack()

        self.password = ttk.Entry(right, show="*", width=30)
        self.password.pack(pady=5)

        ttk.Button(
            right,
            text="Login",
            command=self.login
        ).pack(pady=30)

        self.root.mainloop()

    def login(self):

        conn = sqlite3.connect("database/employee.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (
                self.username.get(),
                self.password.get()
            )
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            self.root.destroy()

            Dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )