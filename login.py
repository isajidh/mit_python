import tkinter as tk
from tkinter import messagebox
import mysql.connector
import hashlib
import subprocess
import json
from PIL import Image, ImageTk
from db_query import DatabaseConnection, DBQuery
from datetime import date, datetime
import socket

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
        query = "SELECT user_name, role, password FROM user_account WHERE user_id = %s AND password = %s and is_current=%s"
        cursor.execute(query, (userID, hashed_password, 1,))
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

            USER_ID = userID
            hostname = socket.gethostname()
            LOGIN_IP = socket.gethostbyname(hostname)
            LOGIN_TIME = datetime.now()
            LOGIN_STATUS = 'S'
            LOGIN_ERR = ''
            LOGOUT_TIME = ''

            data = [USER_ID, LOGIN_IP, LOGIN_TIME, LOGIN_STATUS, LOGIN_ERR, LOGOUT_TIME]
            query = """INSERT INTO user_login (USER_ID, LOGIN_IP, LOGIN_TIME, LOGIN_STATUS, LOGIN_ERR, LOGOUT_TIME) VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, data)
            connection.commit()

            #messagebox.showinfo("Login Success", f"Welcome!, {username},{user_role}")

            root.destroy()  # Close the login window
            open_main_window(userID)  # Open the main app window
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def focus_next(event, next_widget):
    next_widget.focus_set()
    return "break"  # Prevents the default behavior of Enter key

# Function to open the main window after successful login
def open_main_window(userID):
    # Open a new Python file after login
    subprocess.Popen(["python", "menu.py"])  # Opens the main_app.py file
    exit()  # Exit the current login script

# Main Login Window
root = tk.Tk()
root.title("Login to CMS")

# Set window size and make it non-resizable
root.geometry(f"350x250+{(root.winfo_screenwidth()-350)//2}+{(root.winfo_screenheight()-300)//2}")
root.resizable(False, False)  # Make the window non-resizable

# Create a frame for a more organized layout
frame = tk.Frame(root)
frame.pack(padx=5, pady=5, expand=True)
frame.config(bg="lightgray")

frame_top = tk.Frame(frame)
frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
frame_top.config(bg="white")

main_image_path = "login_left.jpg"
main_image = Image.open(main_image_path)
main_image = main_image.resize((120, 170))  # Resize if needed
main_photo = ImageTk.PhotoImage(main_image)

frame_left = tk.Frame(frame)
frame_left.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
frame_left.config(bg="lightgray")

# Create a label for the main image
main_label = tk.Label(frame_left, image=main_photo)
main_label.pack()

frame_right = tk.Frame(frame)
frame_right.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
frame_right.config(bg="lightgray")

# Username and Password Labels and Entries with larger font
label_userID = tk.Label(frame_right, text="UserID:", font=("Helvetica", 12))
label_userID.grid(row=0, column=0, pady=5, sticky="w")
label_userID.config(bg="lightgray")

entry_var1 = tk.StringVar()
entry_userID = tk.Entry(frame_right, font=("Helvetica", 12), width=15, textvariable=entry_var1)
entry_var1.set("")
entry_userID.grid(row=1, column=0, pady=5)
entry_userID.bind("<Return>", lambda event: focus_next(event, entry_password))

label_password = tk.Label(frame_right, text="Password:", font=("Helvetica", 12))
label_password.grid(row=2, column=0, pady=5, sticky="w")
label_password.config(bg="lightgray")

entry_var2 = tk.StringVar()
entry_password = tk.Entry(frame_right, show="*", font=("Helvetica", 12), width=15, textvariable=entry_var2)
entry_var2.set("")
entry_password.grid(row=3, column=0, pady=5)
entry_password.bind("<Return>", lambda event: focus_next(event, login_button))

# Login Button with larger font and increased padding
login_button = tk.Button(frame_right, text="Login", font=("Helvetica", 12), command=check_login, height=0, width=12)
login_button.grid(row=4, column=0, pady=10, sticky="nsew")

entry_userID.focus_set()

root.bind('<Return>', lambda event=None: check_login())
root.config(bg="lightgray")
# Start the main loop of the login window
root.mainloop()