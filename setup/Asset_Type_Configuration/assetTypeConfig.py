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

class AssetTypeConfig(tk.Frame):
    def __init__(self, parent, text):
        super().__init__(parent, background="white")
        self.pack(expand=True, fill="both")
        self.text = text

        self.frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame.pack(fill=tk.X, padx=0, pady=0)

        title_label = tk.Label(self.frame, bg="white", text=self.text, font=("Arial", 12, "bold"), anchor="w")
        title_label.grid(row=0, column=0, sticky="w", padx=10)
        
        self.frame1 = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame1.pack(fill=tk.X, padx=0, pady=10)

        self.frame2 = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame2.pack(fill=tk.X, padx=0, pady=10)

        # Add form fields
        self.create_form()

    def create_form(self):
        self.entry_frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.entry_frame.pack(fill=tk.X, padx=0, pady=0)

        self.entry_frame = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="Asset Type", relief="solid")
        self.entry_frame.grid(row=0, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_frame1 = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="Asset Sub Type", relief="solid")
        self.entry_frame1.grid(row=0, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_frame2 = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="Available Assets", relief="solid")
        self.entry_frame2.grid(row=1, column=0, padx=10, pady=20, sticky="nsew", columnspan=2)

        rpos = 2
        rgap = 2

        self.asset_type_form(rgap,rpos)
        self.asset_sub_type_form(rgap,rpos)

    def submit_asset_type_form(self):
        # Retrieve form data
        type = self.asset_type_code.get()[:2]
        description = self.asset_type_description.get()

        # Validate form data
        if not type or not description:
            messagebox.showerror("Error", "Fill all required fields!")
            return

        if db_query.check_type_code(type):
            messagebox.showerror("Error", f"Asset type {type} already exist")
            return

        data = [type,description]

        save_asset = db_query.add_asset_type(data)
        if save_asset:
            messagebox.showinfo("Success", f"Asset type {type +' '+ description} added successfully!")
            
            self.reset_form1()
        else:
            messagebox.showerror("Error", "Failed to add asset type!")

    def submit_asset_sub_type_form(self):
        # Retrieve form data
        type = self.asset_type.get()[:2]
        sub_type = self.sub_type_code.get()[:6]
        description = self.asset_sub_type_description.get()

        # Validate form data
        if not type or not sub_type or not description:
            messagebox.showerror("Error", "Fill all required fields!")
            return

        if db_query.check_sub_type_code(sub_type):
            messagebox.showerror("Error", f"Asset sub type {sub_type} already exist")
            return

        data = [type,sub_type,description]

        save_asset = db_query.add_asset_sub_type(data)
        if save_asset:
            messagebox.showinfo("Success", f"Asset sub type {type +' '+sub_type+ ' '+ description} added successfully!")
            self.reset_form1()
        else:
            messagebox.showerror("Error", "Failed to add asset.")

    def reset_form1(self):
        self.asset_type_code.delete(0, tk.END)
        self.asset_type_description.delete(0, tk.END)
        self.asset_type_code.focus_set()

    def reset_form2(self):
        self.asset_type.set('')
        self.sub_type_code.delete(0, tk.END)
        self.asset_sub_type_description.delete(0, tk.END)
        self.asset_type.focus_set()

    def validate_integer_input(self, new_value):
        return new_value.isdigit() or new_value == ""  # Allow digits and empty input
    def validate_decimal_input(self, new_value):
        if new_value == "":  # Allow empty input
            return True
        try:
            float(new_value)  # Check if the value can be converted to a float
            return True
        except ValueError:
            return False  # Reject non-numeric input

    def focus_next(self, event, next_widget):
        next_widget.focus_set()
        return "break"  # Prevents the default behavior of Enter key
    
    def amc_history(self):
        # Add borders using a style 
        style = ttk.Style()
        style.configure("Treeview", borderwidth=3, relief="solid")  # Apply borders
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Style headings

        # Create a frame to hold the table
        self.frame4 = ttk.Frame(self.entry_frame2, padding=10, borderwidth=2, width=200)
        self.frame4.grid(row=0, column=0, sticky="nsew")

        # Define columns
        columns = [
            [0, 'AMC Signed Date', 150,'center'],
            [1, 'AMC Start Date', 150,'center'],
            [2, 'AMC End Date', 150,'center'],
            [3, 'AMC Charge', 150,'e'],
            [4, 'Remarks', 150,'w'],
            [5, 'Is Curreny', 150,'center']
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

    def asset_type_form(self,rgap,rpos):
        #Asset Type Form ----------------------------------------------------------------------------------------------------------
        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Type Code *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type_code = ttk.Entry(self.entry_frame, width=60)
        self.asset_type_code.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_type_code.bind("<Return>", lambda event: self.focus_next(event, self.asset_type_description))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Description ").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type_description = ttk.Entry(self.entry_frame, width=60)
        self.asset_type_description.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_type_description.bind("<Return>", lambda event: self.focus_next(event, self.submit_button))

        rpos += rgap
        self.submit_button = ttk.Button(self.entry_frame, text="Save", command=self.submit_asset_type_form)
        self.submit_button.grid(row=rpos, column=0, padx=20, pady=20, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_asset_type_form())

        self.reset_button = ttk.Button(self.entry_frame, text="Reset", command=self.reset_form1)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20, sticky="w")

        self.asset_type_code.focus_set()

    def asset_sub_type_form(self,rgap,rpos):
        #Asset Sub Type Form ----------------------------------------------------------------------------------------------------------
        # Fetch asset types from the database
        asset_types = db_query.asset_type()
        #Blank line
        ttk.Label(self.entry_frame1, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="Asset Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type = ttk.Combobox(self.entry_frame1, values=asset_types, state="readonly", width=30)
        self.asset_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_type.bind("<Return>", lambda event: self.focus_next(event, self.sub_type_code))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="Sub Type Code *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.sub_type_code = ttk.Entry(self.entry_frame1, width=60)
        self.sub_type_code.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.sub_type_code.bind("<Return>", lambda event: self.focus_next(event, self.asset_sub_type_description))
        
        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="Description ").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_sub_type_description = ttk.Entry(self.entry_frame1, width=60)
        self.asset_sub_type_description.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_sub_type_description.bind("<Return>", lambda event: self.focus_next(event, self.submit__sub_button))

        rpos += rgap
        self.submit__sub_button = ttk.Button(self.entry_frame1, text="Save", command=self.submit_asset_sub_type_form)
        self.submit__sub_button.grid(row=rpos, column=0, padx=20, pady=20, sticky="w")
        self.submit__sub_button.bind("<Return>", lambda event: self.submit_asset_sub_type_form())

        self.reset_button = ttk.Button(self.entry_frame1, text="Reset", command=self.reset_form2)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20, sticky="w")
