import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class SecondaryUI(tk.Frame):
    def __init__(self, parent,text):
        super().__init__(parent,  background="white")  # Set background or other properties
        self.pack(expand=True, fill="both")  # Pack this frame to fill the parent
        self.text = text

        # frame = tk.Frame(self, bg="silver", borderwidth=0, relief="solid")
        # frame.pack(fill=tk.X, padx=0, pady=0)
        #
        # # Add a title to the frame using a Label widget
        # title_label = tk.Label(frame, bg="silver", text=self.text, font=("Arial", 12, "bold"), anchor="w")
        # title_label.grid(row=0, column=0, sticky="w", padx=10)
        #
        # # label = tk.Label(self, text=self.text, font=("Arial", 16), background="silver")
        # # label.pack(pady=0)
        #
        # button = ttk.Button(self, text="Back to Main", command=self.go_back)
        # button.pack(pady=10)

    # def go_back(self):
    #     # Example callback: destroy this frame to show the main UI again
    #     self.destroy()
