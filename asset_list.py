import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date, datetime
from db_query import DatabaseConnection, DBQuery
from validation import Validation
import json

# Initialize Database Connection
db_conn = DatabaseConnection()
db_query = DBQuery(db_conn)

def load_session_from_file():
    try:
        with open("session.json", "r") as file:
            session = json.load(file)
        return session
    except FileNotFoundError:
        return None  # Handle the case if the session file is not found

class AssetList(tk.Frame):
    def __init__(self, parent, text):
        super().__init__(parent, background="white")
        self.pack(expand=True, fill="both")
        self.text = text

        self.frame = tk.Frame(self, bg="silver", borderwidth=0, relief="solid")
        self.frame.pack(fill=tk.X, padx=0, pady=0)

        title_label = tk.Label(self.frame, bg="silver", text=self.text, font=("Arial", 12, "bold"), anchor="w")
        title_label.grid(row=0, column=0, sticky="w", padx=10)

        # Add form fields
        self.create_form()

    def go_back(self):
        self.destroy()

    def create_form(self):
        self.entry_frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.entry_frame.pack(fill=tk.X, padx=0, pady=0)
        self.button_frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.button_frame.pack(fill=tk.X, padx=0, pady=0)

        self.tree_frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.tree_frame.pack(fill=tk.X, padx=0, pady=0)

        rpos = 2
        rgap = 2

        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        # Fetch asset types from the database
        asset_types = db_query.asset_type()

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type = ttk.Combobox(self.entry_frame, values=asset_types, state="readonly", width=30)
        self.asset_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_type.bind("<<ComboboxSelected>>", self.update_sub_type)
        self.asset_type.bind("<Return>", lambda event: self.focus_next(event, self.asset_sub_type))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Sub Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_sub_type = ttk.Combobox(self.entry_frame, state="readonly", width=60)
        self.asset_sub_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_sub_type.bind("<Return>", lambda event: self.focus_next(event, self.submit_button))

        rpos += rgap
        self.submit_button = ttk.Button(self.button_frame, text="View", command=lambda: self.submit_form(1))
        self.submit_button.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_form(1))

        self.submit_button = ttk.Button(self.button_frame, text="View All", command=lambda: self.submit_form(2))
        self.submit_button.grid(row=rpos, column=2, padx=5, pady=5, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_form(2))

        self.submit_button = ttk.Button(self.button_frame, text="View All Under Asset Type", command=lambda: self.submit_form(3))
        self.submit_button.grid(row=rpos, column=3, padx=5, pady=5, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_form(3))

        self.asset_type.focus_set()

    def update_sub_type(self, event):
        selected_category = self.asset_type.get()[:2]
        subcategories = db_query.asset_sub_type(selected_category)
        self.asset_sub_type["values"] = subcategories
        self.asset_sub_type.set('')

    def submit_form(self, report_type):
        # Retrieve form data
        asset_type = self.asset_type.get()[:2]
        asset_sub_type = self.asset_sub_type.get()[:6]

        # Validate form data
        if report_type == 1:
            if not asset_type or not asset_sub_type :
                messagebox.showerror("Error", "Fill all required fields!")
                return
        elif report_type == 2:
            pass
        elif report_type == 3:
            if not asset_type:
                messagebox.showerror("Error", "Fill all required fields!")
                return

        view_asset = db_query.view_asset(asset_type, asset_sub_type, report_type)
        if view_asset:
            self.view_report(view_asset)
        else:
            messagebox.showerror("Error", "Failed to view assets.")

    def focus_next(self, event, next_widget):
        next_widget.focus_set()
        return "break"  # Prevents the default behavior of Enter key

    def view_report(self, view_asset):
        style = ttk.Style()
        style.configure("Treeview", borderwidth=3, relief="solid")  # Apply borders
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Style headings

        # Create a frame to hold the table
        self.frame4 = ttk.Frame(self.tree_frame, padding=10, borderwidth=2, width=200)
        self.frame4.grid(row=0, column=0, sticky="nsew")

        # Define columns
        columns = [
            [0, 'Asset Serial', 100, 'center'],
            [1, 'Inventory Number', 100, 'center'],
            [2, 'Description', 200, 'w'],
            [3, 'Date Purchase', 100, 'center'],
            [4, 'Purchase Price', 100, 'center'],
            [5, 'Vender Name', 200, 'w'],
            [6, 'Asset Location', 200, 'w'],
            [7, 'AMC Expiring Date', 100, 'center'],
        ]
        # Create Treeview widget
        self.tree = ttk.Treeview(self.frame4, columns=columns, show="headings", height=25)

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

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in view_asset:
            self.tree.insert("", "end", values=row)
