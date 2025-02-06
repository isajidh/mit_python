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

class EditAssetItem(tk.Frame):
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

        vcmdn = (self.register(self.validate_integer_input), "%P")  # Register validation function
        vcmdd = (self.register(self.validate_decimal_input), "%P")  # Register validation function

        rpos = 2
        rgap = 2

        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        # Fetch asset types from the database
        asset_types = db_query.asset_type()

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Serial Number", font=("Arial", 10, "bold")).grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_serial = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdn)
        self.asset_serial.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_serial.bind("<Return>", lambda event: self.show_asset())

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
        self.asset_sub_type.bind("<Return>", lambda event: self.focus_next(event, self.inventory_number))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Inventory Number").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.inventory_number = ttk.Entry(self.entry_frame, width=30)
        self.inventory_number.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.inventory_number.bind("<Return>", lambda event: self.focus_next(event, self.description))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Description *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.description = ttk.Entry(self.entry_frame, width=60)
        self.description.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.description.bind("<Return>", lambda event: self.focus_next(event, self.date_purchase))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Date Purchase").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.date_purchase = DateEntry(self.entry_frame, width=28, date_pattern='dd-mm-yyyy')
        self.date_purchase.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.date_purchase.bind("<Return>", lambda event: self.focus_next(event, self.purchase_price))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Purchase Price").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.purchase_price = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdd)
        self.purchase_price.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.purchase_price.bind("<Return>", lambda event: self.focus_next(event, self.vender_name))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Name").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_name = ttk.Entry(self.entry_frame, width=60)
        self.vender_name.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.vender_name.bind("<Return>", lambda event: self.focus_next(event, self.vender_address))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Address").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_address = ttk.Entry(self.entry_frame, width=60)
        self.vender_address.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.vender_address.bind("<Return>", lambda event: self.focus_next(event, self.vender_phone))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Phone").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_phone = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdn)
        self.vender_phone.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.vender_phone.bind("<Return>", lambda event: self.focus_next(event, self.asset_location))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Location").grid(row=rpos, column=0, sticky="w",padx=5, pady=5)
        self.asset_location = ttk.Entry(self.entry_frame, width=60)
        self.asset_location.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_location.bind("<Return>", lambda event: self.focus_next(event, self.asset_owner))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Owner").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_owner = ttk.Entry(self.entry_frame, width=60)
        self.asset_owner.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_owner.bind("<Return>", lambda event: self.focus_next(event, self.asset_custodian))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Custodian").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_custodian = ttk.Entry(self.entry_frame, width=60)
        self.asset_custodian.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_custodian.bind("<Return>", lambda event: self.focus_next(event, self.depreciation_rate))

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Depreciation Rate").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.depreciation_rate = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdd)
        self.depreciation_rate.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.depreciation_rate.bind("<Return>", lambda event: self.focus_next(event, self.submit_button))

        rpos += rgap
        self.submit_button = ttk.Button(self.entry_frame, text="Update", command=self.submit_form)
        self.submit_button.grid(row=rpos, column=0, padx=20, pady=20, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_form())

        self.reset_button = ttk.Button(self.entry_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20, sticky="w")

        self.asset_serial.focus_set()

    def update_sub_type(self, event):
        selected_category = self.asset_type.get()[:2]
        subcategories = db_query.asset_sub_type(selected_category)
        self.asset_sub_type["values"] = subcategories
        self.asset_sub_type.set('')

    def show_asset(self):
        self.reset_form()
        asset_serial = self.asset_serial.get()
        # selected_category = self.asset_type.get()[:2]
        asset_detail = db_query.asset_detail(asset_serial)
        if asset_detail:
            self.asset_type.set(f"{asset_detail[0]} {asset_detail[15]}")
            self.update_sub_type('')
            self.asset_sub_type.set(f"{asset_detail[1]} {asset_detail[16]}")

            self.inventory_number.insert(0,asset_detail[2])
            self.description.insert(0,asset_detail[3])
            self.date_purchase.set_date(asset_detail[4])
            self.purchase_price.insert(0,asset_detail[5])
            self.vender_name.insert(0,asset_detail[6])
            self.vender_address.insert(0,asset_detail[7])
            self.vender_phone.insert(0,asset_detail[8])
            self.asset_location.insert(0,asset_detail[9])
            self.asset_owner.insert(0,asset_detail[10])
            self.asset_custodian.insert(0,asset_detail[11])
            self.depreciation_rate.insert(0,asset_detail[12])
        else:
            messagebox.showerror("Information", f"Asset serial number ' {asset_serial} ' does  not exists!")


    def submit_form(self):
        # Retrieve form data
        asset_serial = self.asset_serial.get()
        asset_type = self.asset_type.get()[:2]
        asset_sub_type = self.asset_sub_type.get()[:6]
        inventory_number = self.inventory_number.get()
        description = self.description.get()
        date_purchase = self.date_purchase.get()
        purchase_price = self.purchase_price.get()
        vender_name = self.vender_name.get()
        vender_address = self.vender_address.get()
        vender_phone = self.vender_phone.get()
        asset_location = self.asset_location.get()
        asset_owner = self.asset_owner.get()
        asset_custodian = self.asset_custodian.get()
        depreciation_rate = self.depreciation_rate.get()

        # Validate form data
        if not asset_type or not asset_sub_type or not self.description:
            messagebox.showerror("Error", "Fill all required fields!")
            return

        if not Validation.is_valid_date(date_purchase,"%d-%m-%Y"):
            messagebox.showerror("Error", f"Date Purchase is invalid!")
            return

        if float(depreciation_rate) > 100:
            messagebox.showerror("Error", f"Depreciation rate should be less than or equal 100!")
            return

        date_purchase = datetime.strptime(date_purchase, "%d-%m-%Y").strftime("%Y-%m-%d")
        entered_on = datetime.now()
        session = load_session_from_file()
        entered_by = session['userID']

        data = [asset_serial,asset_type,asset_sub_type,inventory_number,description,date_purchase,purchase_price,vender_name,vender_address
            ,vender_phone,asset_location,asset_owner,asset_custodian,depreciation_rate,entered_on,entered_by]

        save_asset = db_query.update_asset(data)
        if save_asset:
            messagebox.showinfo("Success", f"Asset serial {asset_serial} updated successfully!")
            self.reset_form()
        else:
            messagebox.showerror("Error", "Failed to update asset.")

    def reset_form(self):
        self.asset_type.set('')
        self.asset_sub_type.set('')
        self.inventory_number.delete(0, tk.END)
        self.description.delete(0, tk.END)
        self.date_purchase.set_date(date.today())
        self.purchase_price.delete(0, tk.END)
        self.vender_name.delete(0, tk.END)
        self.vender_address.delete(0, tk.END)
        self.vender_phone.delete(0, tk.END)
        self.asset_location.delete(0, tk.END)
        self.asset_owner.delete(0, tk.END)
        self.asset_custodian.delete(0, tk.END)
        self.depreciation_rate.delete(0, tk.END)
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