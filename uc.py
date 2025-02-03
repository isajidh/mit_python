import tkinter as tk
from tkinter import ttk, messagebox


class UserCreation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Creation Interface")
        self.geometry("400x400")
        self.resizable(False, False)

        # Add a title label
        ttk.Label(self, text="User Creation Form", font=("Arial", 16, "bold")).pack(pady=10)

        # Create a frame for the form
        self.form_frame = ttk.Frame(self, padding=10)
        self.form_frame.pack(fill="both", expand=True)

        # Add form fields
        self.create_form()

        # Add buttons
        self.create_buttons()

    def create_form(self):
        # Username field
        ttk.Label(self.form_frame, text="Username:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = ttk.Entry(self.form_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Password field
        ttk.Label(self.form_frame, text="Password:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.password_entry = ttk.Entry(self.form_frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Email field
        ttk.Label(self.form_frame, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = ttk.Entry(self.form_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Role selection
        ttk.Label(self.form_frame, text="Role:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.role_combo = ttk.Combobox(self.form_frame, values=["Admin", "User", "Manager"], state="readonly", width=28)
        self.role_combo.grid(row=3, column=1, padx=5, pady=5)
        self.role_combo.current(0)  # Set default value

    def create_buttons(self):
        # Submit button
        submit_button = ttk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack(side="left", padx=20, pady=20)

        # Reset button
        reset_button = ttk.Button(self, text="Reset", command=self.reset_form)
        reset_button.pack(side="right", padx=20, pady=20)

    def submit_form(self):
        # Retrieve form data
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        role = self.role_combo.get()

        # Validate form data
        if not username or not password or not email:
            messagebox.showerror("Error", "All fields are required!")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address!")
            return

        # Perform user creation logic (mocked here)
        messagebox.showinfo("Success", f"User '{username}' created successfully with role '{role}'!")

    def reset_form(self):
        # Clear all form fields
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.role_combo.current(0)


# Run the application
if __name__ == "__main__":
    app = UserCreation()
    app.mainloop()
