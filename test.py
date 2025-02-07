from tkinter import Tk, ttk
from tkcalendar import DateEntry
import tkinter as tk
from PIL import ImageGrab
from reportlab.pdfgen import canvas


def export_to_pdf():
    # Get the frame's position
    x = root.winfo_rootx() + frame.winfo_x()
    y = root.winfo_rooty() + frame.winfo_y()
    width = x + frame.winfo_width()
    height = y + frame.winfo_height()

    # Capture the frame content as an image
    img = ImageGrab.grab(bbox=(x, y, width, height))

    # Save the image as a temporary file
    img_path = "frame_content.png"
    img.save(img_path)

    # Create a PDF
    pdf_path = "frame_content.pdf"
    c = canvas.Canvas(pdf_path)

    # Add image to the PDF
    c.drawImage(img_path, 50, 500, width=400, height=200)

    c.save()
    print("PDF saved successfully!")

    # Tkinter Window
    root = tk.Tk()
    root.geometry("500x300")

    frame = tk.Frame(root, width=400, height=200, bg="lightgray")
    frame.pack(pady=20)

    label = tk.Label(frame, text="Export this Frame to PDF", font=("Arial", 14))
    label.pack(pady=20)

    btn = tk.Button(root, text="Export to PDF", command=export_to_pdf())
    btn.pack()

    root.mainloop()

