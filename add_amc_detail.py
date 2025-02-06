import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date, datetime
from db_query import DatabaseConnection, DBQuery
from validation import Validation
import json

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

class AddAMCDetail(tk.Frame):
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

        self.frame3 = tk.Frame(self, bg="white", borderwidth=0, relief="solid")
        self.frame3.pack(fill=tk.X, padx=0, pady=10)

        # Add form fields
        self.create_form()

    def go_back(self):
        self.destroy()

    def create_form(self):
        style = ttk.Style()
        style.configure("Custom.TLabelframe", background="white")  # Set background for frame
        style.configure("Custom.TLabelframe.Label", background="white", font=("Arial", 10, "bold"))

        self.entry_frame = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="Asset Detail", relief="solid")
        self.entry_frame.grid(row=0, column=0, padx=20, pady=0, sticky="nsew")

        self.entry_frame1 = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="AMC Detail", relief="solid")
        self.entry_frame1.grid(row=0, column=1, padx=20, pady=0, sticky="nsew")

        self.entry_frame2 = ttk.LabelFrame(self.frame2, style="Custom.TLabelframe", borderwidth=0, text="AMC History", relief="solid")
        self.entry_frame2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

        vcmdn = (self.register(self.validate_integer_input), "%P")  # Register validation function
        vcmdd = (self.register(self.validate_decimal_input), "%P")  # Register validation function

        rpos = 2
        rgap = 2

        #Blank line
        ttk.Label(self.entry_frame, background="white", text="").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)

        # Fetch asset types from the database
        asset_types = db_query.asset_type()

        rpos += rgap
        ttk.Label(self.frame1, background="white", text="Asset Serial Number", font=("Arial", 10, "bold")).grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_serial = ttk.Entry(self.frame1, width=30, validate="key", validatecommand=vcmdn)
        self.asset_serial.grid(row=rpos, column=1, padx=20, pady=5, sticky="w")
        self.asset_serial.bind("<Return>", lambda event: self.show_asset())

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Type").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_type = ttk.Label(self.entry_frame, width=30)
        self.asset_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Sub Type *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_sub_type = ttk.Label(self.entry_frame, width=60)
        self.asset_sub_type.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Inventory Number").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.inventory_number = ttk.Label(self.entry_frame, width=30)
        self.inventory_number.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Description *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.description = ttk.Label(self.entry_frame, width=60)
        self.description.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Date Purchase").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.date_purchase = ttk.Label(self.entry_frame, width=28)
        self.date_purchase.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Purchase Price").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.purchase_price = ttk.Label(self.entry_frame, width=30)
        self.purchase_price.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Name").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_name = ttk.Label(self.entry_frame, width=60)
        self.vender_name.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Address").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_address = ttk.Label(self.entry_frame, width=60)
        self.vender_address.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Vendor Phone").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.vender_phone = ttk.Label(self.entry_frame, width=30)
        self.vender_phone.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Location").grid(row=rpos, column=0, sticky="w",padx=5, pady=5)
        self.asset_location = ttk.Label(self.entry_frame, width=60)
        self.asset_location.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Owner").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_owner = ttk.Label(self.entry_frame, width=60)
        self.asset_owner.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Asset Custodian").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.asset_custodian = ttk.Label(self.entry_frame, width=60)
        self.asset_custodian.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        rpos += rgap
        ttk.Label(self.entry_frame, background="white", text="Depreciation Rate").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.depreciation_rate = ttk.Label(self.entry_frame, width=30)
        self.depreciation_rate.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")

        #Reading AMC data ----------------------------------------------------------------------------------------------------------------
        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="AMC Signed Date *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_singed_date = DateEntry(self.entry_frame1, width=28, date_pattern='dd-mm-yyyy')
        self.amc_singed_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.amc_singed_date.bind("<Return>", lambda event: self.focus_next(event, self.amc_start_date))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="AMC Start Date *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_start_date = DateEntry(self.entry_frame1, width=28, date_pattern='dd-mm-yyyy')
        self.amc_start_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.amc_start_date.bind("<Return>", lambda event: self.focus_next(event, self.amc_end_date))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="AMC End Date *").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_end_date = DateEntry(self.entry_frame1, width=28, date_pattern='dd-mm-yyyy')
        self.amc_end_date.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.amc_end_date.bind("<Return>", lambda event: self.focus_next(event, self.charge_amount))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="AMC Charge Amount").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.charge_amount = ttk.Entry(self.entry_frame1, width=30, validate="key", validatecommand=vcmdd)
        self.charge_amount.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.charge_amount.bind("<Return>", lambda event: self.focus_next(event, self.remarks))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="Remarks").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.remarks = ttk.Entry(self.entry_frame1, width=60)
        self.remarks.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.remarks.bind("<Return>", lambda event: self.focus_next(event, self.amc_signed_by))

        rpos += rgap
        ttk.Label(self.entry_frame1, background="white", text="AMC signed by").grid(row=rpos, column=0, sticky="w", padx=5, pady=5)
        self.amc_signed_by = ttk.Entry(self.entry_frame1, width=60)
        self.amc_signed_by.grid(row=rpos, column=1, padx=5, pady=5, sticky="w")
        self.amc_signed_by.bind("<Return>", lambda event: self.focus_next(event, self.submit_button))

        rpos += rgap
        self.submit_button = ttk.Button(self.entry_frame1, text="Save", command=self.submit_form)
        self.submit_button.grid(row=rpos, column=0, padx=20, pady=20, sticky="w")
        self.submit_button.bind("<Return>", lambda event: self.submit_form())

        self.reset_button = ttk.Button(self.entry_frame1, text="Reset", command=self.reset_asset)
        self.reset_button.grid(row=rpos, column=1, padx=20, pady=20, sticky="w")

        self.asset_serial.focus_set()
        self.amc_history()

    def amc_history(self):
        # Add borders using a style
        style = ttk.Style()
        style.configure("Treeview", borderwidth=3, relief="solid")  # Apply borders
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Style headings

        # Create a frame to hold the table
        self.frame4 = ttk.Frame(self.entry_frame2, padding=10, borderwidth=2, width=200)
        self.frame4.grid(row=0, column=0, sticky="nsew")

        # Define columns
        columns = [
            [0, 'AMC Signed Date', 150,'center'],
            [1, 'AMC Start Date', 150,'center'],
            [2, 'AMC End Date', 150,'center'],
            [3, 'AMC Charge', 150,'e'],
            [4, 'Remarks', 150,'w'],
            [5, 'Is Curreny', 150,'center']
        ]
        # Create Treeview widget
        self.tree = ttk.Treeview(self.frame4, columns=columns, show="headings", height=5)

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

    def show_asset(self):
        self.reset_asset()
        asset_serial = self.asset_serial.get()
        # selected_category = self.asset_type.get()[:2]
        asset_detail = db_query.asset_detail(asset_serial)
        if asset_detail:
            self.asset_type.config(text=asset_detail[15])
            self.asset_sub_type.config(text=asset_detail[16])
            self.inventory_number.config(text=asset_detail[2])
            self.description.config(text=asset_detail[3])
            date_purchase = asset_detail[4]
            date_purchase.strftime("%d-%m-%Y")
            self.date_purchase.config(text=date_purchase)
            self.purchase_price.config(text=asset_detail[5])
            self.vender_name.config(text=asset_detail[6])
            self.vender_address.config(text=asset_detail[7])
            self.vender_phone.config(text=asset_detail[8])
            self.asset_location.config(text=asset_detail[9])
            self.asset_owner.config(text=asset_detail[10])
            self.asset_custodian.config(text=asset_detail[11])
            self.depreciation_rate.config(text=asset_detail[12])
            self.amc_singed_date.focus_set()

            self.show_amc(asset_serial)
        else:
            messagebox.showerror("Information", f"Asset serial number ' {asset_serial} ' does  not exists!")

    def show_amc(self,asset_serial):
        for row in self.tree.get_children():
            self.tree.delete(row)

        amc_history = db_query.amc_history(asset_serial)
        for row in amc_history:
            self.tree.insert("", "end", values=row)

    def submit_form(self):
        # Retrieve form data
        asset_serial = self.asset_serial.get()
        amc_signed_date = self.amc_singed_date.get()
        amc_start_date = self.amc_start_date.get()
        amc_end_date = self.amc_end_date.get()
        charge_amount = self.charge_amount.get()
        remarks = self.remarks.get()
        amc_signed_by = self.amc_signed_by.get()

        # Validate form data
        if not asset_serial or not amc_signed_date or not self.amc_start_date or not self.amc_end_date or not self.charge_amount:
            messagebox.showerror("Error", "Fill all required fields!")
            return

        if not db_query.check_serial_number(asset_serial):
            messagebox.showerror("Error", f"Serial number {asset_serial} does not exists")
            return

        if not Validation.is_valid_date(amc_signed_date,"%d-%m-%Y"):
            messagebox.showerror("Error", f"AMC signed date is invalid!")
            return

        if not Validation.is_valid_date(amc_start_date,"%d-%m-%Y"):
            messagebox.showerror("Error", f"AMC start date is invalid!")
            return

        if not Validation.is_valid_date(amc_end_date,"%d-%m-%Y"):
            messagebox.showerror("Error", f"AMC start date is invalid!")
            return

        amc_signed_date = datetime.strptime(amc_signed_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        amc_start_date = datetime.strptime(amc_start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        amc_end_date = datetime.strptime(amc_end_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        entered_on = datetime.now()
        session = load_session_from_file()
        entered_by = session['userID']
        is_current = 1

        data = [asset_serial,amc_signed_date,amc_start_date,amc_end_date,charge_amount,remarks,amc_signed_by,entered_on,entered_by,is_current]

        save_amc = db_query.add_amc(data)
        if save_amc:
            messagebox.showinfo("Success", "Asset added successfully!")
            self.show_amc(asset_serial)
        else:
            messagebox.showerror("Error", "Failed to add asset.")

    def reset_asset(self):
        self.asset_type.config(text="")
        self.asset_sub_type.config(text="")
        self.inventory_number.config(text="")
        self.description.config(text="")
        self.date_purchase.config(text="")
        self.purchase_price.config(text="")
        self.vender_name.config(text="")
        self.vender_address.config(text="")
        self.vender_phone.config(text="")
        self.asset_location.config(text="")
        self.asset_owner.config(text="")
        self.asset_custodian.config(text="")
        self.depreciation_rate.config(text="")

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