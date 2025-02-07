import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date, datetime
from db_query import DatabaseConnection, DBQuery
from validation import Validation
import json

db_conn = DatabaseConnection()
db_query = DBQuery(db_conn)

def load_session_from_file():
    try:
        with open("session.json", "r") as file:
            session = json.load(file)
        return session
    except FileNotFoundError:
        return None  # Handle the case if the session file is not found

# Initialize Database Connection

class UserLoginDetail(tk.Frame):
    def __init__(self, parent, text):
        super().__init__(parent, background="white")
        self.pack(expand=True, fill="both")
        self.text = text

        self.frame = tk.Frame(self, bg="silver", borderwidth=0, relief="solid")
        self.frame.pack(fill=tk.X, padx=0, pady=0)

        title_label = tk.Label(self.frame, bg="silver", text=self.text, font=("Arial", 12, "bold"), anchor="w")
        title_label.grid(row=0, column=0, sticky="w", padx=10)

        self.frame1 = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame1.pack(fill=tk.X, padx=0, pady=10)

        self.frame2 = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame2.pack(fill=tk.X, padx=0, pady=10)

        # Add form fields
        self.create_form()

    def go_back(self):
        self.destroy()

    def create_form(self):
        style = ttk.Style()
        style.configure("Custom.TLabelframe", background="white")  # Set background for frame
        style.configure("Custom.TLabelframe.Label", background="white", font=("Arial", 10, "bold"))

        vcmdn = (self.register(self.validate_integer_input), "%P")  # Register validation function
        vcmdd = (self.register(self.validate_decimal_input), "%P")  # Register validation function

        rpos = 2
        rgap = 2

        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        rpos += rgap
        ttk.Label(self.frame1, background="white", text="User ID", font=("Arial", 10, "bold")).grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.user_id = ttk.Entry(self.frame1, width=30, validate="key", validatecommand=vcmdn)
        self.user_id.grid(row=rpos, column=1, padx=20, pady=5, sticky="w")
        self.user_id.bind("<Return>", lambda event: self.show_detail())

        # Add borders using a style
        style = ttk.Style()
        style.configure("Treeview", borderwidth=3, relief="solid")  # Apply borders
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Style headings

        # Create a frame to hold the table
        self.frame4 = ttk.Frame(self.frame2, padding=10, borderwidth=2, width=200)
        self.frame4.grid(row=0, column=0, sticky="nsew")

        # Define columns
        columns = [
            [0, 'User ID', 150,'center'],
            [1, 'User Name', 150,'center'],
            [2, 'Login IP', 150,'center'],
            [3, 'Login Tine', 150,'e'],
            [4, 'Login Status', 150,'w'],
            [5, 'Logout Time', 150,'center']
        ]
        # Create Treeview widget
        self.tree = ttk.Treeview(self.frame4, columns=columns, show="headings", height=5)

        #Add column headings
        for col in columns:
            self.tree.heading(col[0], text=col[1])
            self.tree.column(col[0], anchor=col[3], width=col[2])  # Set column width

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.frame4, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Pack the tree and scrollbar into the frame
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

    def show_detail(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        amc_history = db_query.amc_history()
        for row in amc_history:
            self.tree.insert("", "end", values=row)

    def validate_integer_input(self, new_value):
        return new_value.isdigit() or new_value == ""  # Allow digits and empty input

    def focus_next(self, event, next_widget):
        next_widget.focus_set()
        return "break"  # Prevents the default behavior of Enter key