import tkinter as tk
from tkinter import messagebox
import mysql.connector
import hashlib
import subprocess
import json




def save_session_to_file(session):
    with open("session.json", "w") as file:
        json.dump(session, file)

# Function to hash the password using SHA-256
def hash_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

# Function to connect to MySQL and check credentials
def check_login():
    
    #global user_logged_in, user_role
    userID = entry_userID.get()
    password = entry_password.get()

    # Hash the entered password
    hashed_password = hash_password(password)

    try:
        # Connect to the MySQL database

        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # replace with your MySQL username
            password='atm@2023',  # replace with your MySQL password
            database='amc_tracker'
        )

        cursor = connection.cursor(dictionary=True)

        # Query to check if the user exists with the given username and hashed password
        query = "SELECT * FROM user_account WHERE user_id = %s AND password = %s"
        cursor.execute(query, (userID, hashed_password))
        user = cursor.fetchone()

        # Check if the user exists and login is successful
        if user:
            
            # Example to save session after successful login
            session = {
                "userID":userID,
                "username":user['user_name'],
                "role": user['role'],
                "logged_in": True
            }
            # Save the session data to a file
            save_session_to_file(session)
            #messagebox.showinfo("Login Success", f"Welcome!, {username},{user_role}")

            root.destroy()  # Close the login window
            open_main_window()  # Open the main app window
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to open the main window after successful login
def open_main_window():
    # Open a new Python file after login
    subprocess.Popen(["python", "main.py"])  # Opens the main_app.py file
    exit()  # Exit the current login script

# Main Login Window
root = tk.Tk()
root.title("Login to Contract Management System")

# Set window size and make it non-resizable
root.geometry(f"500x300+{(root.winfo_screenwidth()-500)//2}+{(root.winfo_screenheight()-300)//2}")
root.resizable(False, False)  # Make the window non-resizable

# Create a frame for a more organized layout
frame = tk.Frame(root)
frame.pack(padx=20, pady=20, expand=True)
frame.config(bg="lightblue")

# Username and Password Labels and Entries with larger font
label_userID = tk.Label(frame, text="UserID:", font=("Helvetica", 16))
label_userID.grid(row=0, column=0, pady=10, sticky="w")
label_userID.config(bg="lightblue")

entry_userID = tk.Entry(frame, font=("Helvetica", 16), width=25)
entry_userID.grid(row=0, column=1, pady=10)
entry_userID.focus_set()

label_password = tk.Label(frame, text="Password:", font=("Helvetica", 16))
label_password.grid(row=1, column=0, pady=10, sticky="w")
label_password.config(bg="lightblue")

entry_password = tk.Entry(frame, show="*", font=("Helvetica", 16), width=25)
entry_password.grid(row=1, column=1, pady=10)


# Login Button with larger font and increased padding
login_button = tk.Button(frame, text="Login", font=("Helvetica", 16), command=check_login, height=2, width=15)
login_button.grid(row=2, column=0, columnspan=2, pady=20)
root.bind('<Return>', lambda event=None: check_login())
root.config(bg="lightblue")
# Start the main loop of the login window
root.mainloop()