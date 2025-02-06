import tkinter as tk
from tkinter import ttk, messagebox
import mysql_conn as mysql_conn
from datetime import date, timedelta
from hashlib import sha256

class UserEdit(tk.Frame):
    def __init__(self, parent,text):
        super().__init__(parent,  background="white")  # Set background or other properties
        self.pack(expand=True, fill="both")  # Pack this frame to fill the parent
        self.text = text

        self.frame = tk.Frame(self, bg="silver", borderwidth=0, relief="solid")
        self.frame.pack(fill=tk.X, padx=0, pady=0)

        # Add a title to the frame using a Label widget
        title_label = tk.Label(self.frame, bg="silver", text=self.text, font=("Arial", 12, "bold"), anchor="w")
        title_label.grid(row=0, column=0, sticky="w", padx=10)

        # Add form fields
        self.create_form()

    def go_back(self):
        #Example callback: destroy this frame to show the main UI again
        self.destroy()

    def create_form(self):
        self.entry_frame = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.entry_frame.pack(fill=tk.X, padx=0, pady=0)

        rstart = 2
        rgap = 2
        rpos = 0

        rpos += rstart

        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        rpos += rgap
        #User ID field
        ttk.Label(self.entry_frame, background="white", text="User Id *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.userid = ttk.Entry(self.entry_frame, width=30)
        self.userid.grid(row=rpos, column=1, padx=5, pady=5)

        rpos += rgap
        #User name field
        ttk.Label(self.entry_frame, background="white", text="User Name *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.username = ttk.Entry(self.entry_frame, width=30)
        self.username.grid(row=rpos, column=1, padx=5, pady=5)

        rpos += rgap
        # Password field
        ttk.Label(self.entry_frame, background="white", text="Password *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.password = ttk.Entry(self.entry_frame, show="*", width=30)
        self.password.grid(row=rpos, column=1, padx=5, pady=5)

        rpos += rgap
        # Email field
        ttk.Label(self.entry_frame, background="white", text="Email *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.email = ttk.Entry(self.entry_frame, width=30)
        self.email.grid(row=rpos, column=1, padx=5, pady=5)

        rpos += rgap
        # Email field
        ttk.Label(self.entry_frame, background="white", text="Phone").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.phone = ttk.Entry(self.entry_frame, width=30)
        self.phone.grid(row=rpos, column=1, padx=5, pady=5)

        rpos += rgap
        # Role selection
        ttk.Label(self.entry_frame, background="white", text="Role *").grid(row=rpos, column=0, sticky="w", padx=5,pady=5)
        self.userrole = ttk.Combobox(self.entry_frame, values=["Admin", "Manager", "User"], state="readonly", width=28)
        self.userrole.grid(row=rpos, column=1, padx=5, pady=5)
        self.userrole.current(0)  # Set default value

        rpos += rgap
        # Submit button
        self.submit_button = ttk.Button(self.entry_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=rpos, column=0, padx=20, pady=20)

        # Reset button
        self.reset_button = ttk.Button(self.entry_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20)

    def submit_form(self):
        # Retrieve form data
        user_id = self.userid.get()
        user_name = self.username.get()
        email = self.email.get()
        phone = self.phone.get()
        role = self.userrole.get()
        password = sha256(self.password.get().encode('utf-8')).hexdigest()
        created_by ='1294'
        created_on =date.today()
        is_current = 1
        pw_expiry_date = date.today() + timedelta(days=180)
        pw_period = 180
        pw_type = 0

        match role:
            case 'Admin':
                role = 1
            case 'Manager':
                role = 2
            case 'User':
                role = 3
            case _:
                role = 0

        # Validate form data
        if not user_id or not user_name or not password or not email or not role:
            messagebox.showerror("Error", "All fields are required!")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address!")
            return

        mysql_conn.db_connection
        db_cursor = mysql_conn.db_connection.cursor()

        query = "INSERT INTO user_account (user_id,user_name,email,phone,role,password,created_by,created_on,is_current,pw_expiry_date,pw_period,pw_type) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (user_id,user_name,email,phone,role,password,created_by,created_on,is_current,pw_expiry_date,pw_period,pw_type)
        db_cursor.execute(query, data)
        mysql_conn.db_connection.commit()

        # Perform user creation logic (mocked here)
        messagebox.showinfo("Success", f"User '{user_id}' created successfully with role '{role}'!")

    def reset_form(self):
        # Clear all form fields
        self.userid.delete(0, tk.END)
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.userrole.current(0)
