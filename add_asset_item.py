import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date
from db_query import DatabaseConnection, DBQuery

# Initialize Database Connection
db_conn = DatabaseConnection()
db_query = DBQuery(db_conn)

class AddAssetItem(tk.Frame):
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

    # def __del__(self):
    #     """Destructor to close the database connection when instance is deleted."""
    #     db_conn.close_connection()

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
        ttk.Label(self.entry_frame, background="white", text="Asset Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type = ttk.Combobox(self.entry_frame, values=asset_types, state="readonly", width=30)
        self.asset_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.asset_type.bind("<<ComboboxSelected>>", self.update_sub_type)

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Sub Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_sub_type = ttk.Combobox(self.entry_frame, state="readonly", width=60)
        self.asset_sub_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Inventory Number *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.inventory_number = ttk.Entry(self.entry_frame, width=30)
        self.inventory_number.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Description").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.description = ttk.Entry(self.entry_frame, width=60)
        self.description.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Date Purchase").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.date_purchase = DateEntry(self.entry_frame, width=28, date_pattern='dd-mm-yyyy')
        self.date_purchase.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Purchase Price").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.purchase_price = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdd)
        self.purchase_price.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Name").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_name = ttk.Entry(self.entry_frame, width=60)
        self.vender_name.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Address").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_address = ttk.Entry(self.entry_frame, width=60)
        self.vender_address.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Phone").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_phone = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdn)
        self.vender_phone.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        # Email field
        ttk.Label(self.entry_frame, background="white", text="Asset Location").grid(row=rpos, column=0, sticky="w",padx=5, pady=5)
        self.asset_location = ttk.Entry(self.entry_frame, width=60)
        self.asset_location.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        # Email field
        ttk.Label(self.entry_frame, background="white", text="Asset Owner").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_owner = ttk.Entry(self.entry_frame, width=60)
        self.asset_owner.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        # Email field
        ttk.Label(self.entry_frame, background="white", text="Asset Custodian").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_custodian = ttk.Entry(self.entry_frame, width=60)
        self.asset_custodian.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Depreciation Rate").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.depreciation_rate = ttk.Entry(self.entry_frame, width=30, validate="key", validatecommand=vcmdd)
        self.depreciation_rate.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="AMC Start Date *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_start_date = DateEntry(self.entry_frame, width=28, date_pattern='dd-mm-yyyy')
        self.amc_start_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="AMC End Date *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_end_date = DateEntry(self.entry_frame, width=28, date_pattern='dd-mm-yyyy')
        self.amc_end_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        self.submit_button = ttk.Button(self.entry_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=rpos, column=0, padx=20, pady=20, sticky="w")

        self.reset_button = ttk.Button(self.entry_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20, sticky="w")

    def update_sub_type(self, event):
        selected_category = self.asset_type.get()[:2]
        subcategories = db_query.asset_sub_type(selected_category)
        self.asset_sub_type["values"] = subcategories
        self.asset_sub_type.set('')
        #db_conn.close_connection()

    def submit_form(self):
        # Retrieve form data
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
        amc_start_date = self.amc_start_date.get()
        amc_end_date = self.amc_end_date.get()

        # Validate form data
        if not asset_type or not asset_sub_type or not inventory_number or not amc_start_date or not amc_end_date:
            messagebox.showerror("Error", "Fill all required fields!")
            return

        data = [asset_type,asset_sub_type,inventory_number,description,date_purchase,purchase_price,vender_name,vender_address,vender_phone,asset_location,asset_owner,asset_custodian,depreciation_rate]

        save_asset = db_query.add_asset(data)
        if save_asset:
            messagebox.showinfo("Success", "Asset added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add asset.")

        #db_conn.close_connection()

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
        self.depreciation_rate.delete(0, tk.END)
        self.amc_start_date.set_date(date.today())
        self.amc_end_date.set_date(date.today())

    def validate_integer_input(self, new_value):
        """Allow only numbers in the Purchase Price field."""
        return new_value.isdigit() or new_value == ""  # Allow digits and empty input
    def validate_decimal_input(self, new_value):
        """Allow only numeric input (integers & decimals) for Purchase Price."""
        if new_value == "":  # Allow empty input
            return True
        try:
            float(new_value)  # Check if the value can be converted to a float
            return True
        except ValueError:
            return False  # Reject non-numeric input

    # db_conn.close_connection()