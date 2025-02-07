import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date, datetime
from db_query import DatabaseConnection, DBQuery
from validation import Validation
import json
from PIL import ImageGrab
import os


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

class ListAMCExpiring(tk.Frame):
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

        rpos = 2
        rgap = 2

        # Fetch asset types from the database
        self.Label1=ttk.Label(self.frame1, background="white", text="AMC Expiring Between ", font=("Arial", 10, "bold"))
        self.Label1.grid(row=rpos, column=0, padx=5, pady=5, sticky="w")

        self.start_date = DateEntry(self.frame1, width=28, date_pattern='dd-mm-yyyy')
        self.start_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.start_date.bind("<Return>", lambda event: self.focus_next(event, self.end_date))

        self.Label2=ttk.Label(self.frame1, background="white", text=" And ", font=("Arial", 10, "bold"))
        self.Label2.grid(row=rpos, column=2, padx=5, pady=5, sticky="w")

        self.end_date = DateEntry(self.frame1, width=28, date_pattern='dd-mm-yyyy')
        self.end_date.grid(row=rpos, column=3, padx=5, pady=5, sticky="w")
        self.end_date.bind("<Return>", lambda event: self.focus_next(event, self.submit_button))

        self.submit_button = ttk.Button(self.frame1, text="View", command=lambda: self.show_amc())
        self.submit_button.grid(row=rpos, column=4, padx=5, pady=5, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.show_amc())

        self.pdf_button = ttk.Button(self.frame1, text="Save to PDF", command=lambda: self.save_frame_as_pdf(self.frame2))
        self.pdf_button.grid(row=rpos, column=5, padx=5, pady=5, sticky="w")
        self.pdf_button.bind("<Return>", lambda event: self.save_frame_as_pdf(self.frame2))
        self.show_tree()

    def show_tree(self):
        # Add borders using a style
        style = ttk.Style()
        style.configure("Treeview", borderwidth=3, relief="solid")  # Apply borders
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Style headings

        # Create a frame to hold the table
        self.frame4 = ttk.Frame(self.frame2, padding=10, borderwidth=2, width=200)
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
        self.tree = ttk.Treeview(self.frame4, columns=columns, show="headings", height=20)

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

    def show_amc(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        date_1 = self.start_date.get()
        date_2 = self.end_date.get()
        date_1 = datetime.strptime(date_1, "%d-%m-%Y").strftime("%Y-%m-%d")
        date_2 = datetime.strptime(date_2, "%d-%m-%Y").strftime("%Y-%m-%d")

        amc_expiring  = db_query.amc_expiring(date_1, date_2)
        for row in amc_expiring:
            self.tree.insert("", "end", values=row)

    def focus_next(self, event, next_widget):
        next_widget.focus_set()
        return "break"  # Prevents the default behavior of Enter key


    def save_frame_as_pdf(self,frame):
        # Get the frame position
        x = frame.winfo_rootx()
        y = frame.winfo_rooty()
        width = x + frame.winfo_width()
        height = y + frame.winfo_height()

        # Capture the frame as an image
        image = ImageGrab.grab(bbox=(x, y, width, height))

        # Save as PDF
        pdf_path = "frame_output.pdf"
        image.save(pdf_path, "PDF", resolution=100.0)

        # Open the PDF file
        os.system(pdf_path)  # Works on Windows, use 'open' for macOS and 'xdg-open' for Linux