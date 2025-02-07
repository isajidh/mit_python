import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import subprocess
import sys

def show_splash():
    splash_root = tk.Tk()
    splash_root.title("Welcome to AMC Tracker!")
    
    # Set the size of the splash screen window
    width, height = 400, 300
    splash_root.geometry(f"{width}x{height}")
    
    # Get the screen width and height to center the window
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    
    # Calculate the position to center the window
    position_top = (screen_height // 2) - (height // 2)
    position_left = (screen_width // 2) - (width // 2)
    
    # Set the position of the window
    splash_root.geometry(f"{width}x{height}+{position_left}+{position_top}")
    
    # Load the background image with Pillow
    img = Image.open("background.jpg")  # Replace with your image path
    img = img.resize((width, height))  # Resize the image to fit the window
    bg_image = ImageTk.PhotoImage(img)
    
    # Create a label with the background image
    background_label = Label(splash_root, image=bg_image)
    background_label.place(relwidth=1, relheight=1)  # Make the image cover the entire window
    
    # Add some text on top of the background image
    #splash_label = Label(splash_root, text="Welcome to My App", font=("Helvetica", 24), fg="white", bg="black")
    #splash_label.pack(expand=True)
    
    # Display the splash screen for 3 seconds
    splash_root.after(4000, splash_root.destroy)  # 3000 milliseconds = 3 seconds
    
    # Start the Tkinter event loop for the splash screen
    splash_root.mainloop()

    # After splash screen is closed, run another Python file
    open_other_python_file()

def open_other_python_file():
    # Replace "other_file.py" with the path to the Python script you want to open
    subprocess.run([sys.executable, 'login.py'])  # Open the file using the current Python interpreter

# Show splash screen first
show_splash()
