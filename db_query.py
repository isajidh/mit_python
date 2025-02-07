import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
import json

class DatabaseConnection:
    def __init__(self):
        """Initialize the database connection with error handling."""
        self.db_connection = None
        self.db_cursor = None
        try:
            self.db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='atm@2023',
                database='amc_tracker'
            )
            if self.db_connection.is_connected():
                self.db_cursor = self.db_connection.cursor()
                #print("✅ Database connection established successfully.")
        except Error as e:
            messagebox.showerror("Error",f"Error while connecting to database: {e}")
            self.db_connection = None
            self.db_cursor = None

    def close_connection(self):
        """Close the database connection safely."""
        try:
            if self.db_cursor:
                self.db_cursor.close()
            if self.db_connection and self.db_connection.is_connected():
                self.db_connection.close()

                print("🔌 Database connection closed successfully.")
        except Error as e:
            #print(f"⚠️ Error while closing the connection: {e}")
            messagebox.showerror("Error",f"⚠️ Error while closing the connection: {e}")

# Database Query Class
class DBQuery:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db_cursor = self.db_connection.db_cursor

    def asset_type(self):
        query = "SELECT type, description FROM asset_type ORDER BY type"
        self.db_cursor.execute(query)
        return [f"{row[0]} {row[1]}" for row in self.db_cursor.fetchall()]

    def asset_sub_type(self, asset_type):
        query = "SELECT sub_type, description FROM asset_sub_type WHERE type = %s ORDER BY sub_type"
        self.db_cursor.execute(query, (asset_type,))
        return [f"{row[0]} {row[1]}" for row in self.db_cursor.fetchall()]

    def check_inventory_number(self, inventory_number):
        query = "SELECT inventory_number FROM asset WHERE inventory_number=%s and deleted=%s"
        self.db_cursor.execute(query, (inventory_number,0,))

        result = self.db_cursor.fetchone()  # Fetch the first row

        if result:
            return True
        else:
            return False

    def check_serial_number(self, asset_serial):
        query = "SELECT asset_serial FROM asset WHERE asset_serial=%s and deleted=%s"
        self.db_cursor.execute(query, (asset_serial,0,))

        result = self.db_cursor.fetchone()  # Fetch the first row

        if result:
            return True
        else:
            return False

    def get_new_serial(self,code):
        query = "SELECT serial FROM serial WHERE code=%s"
        self.db_cursor.execute(query, (code,))

        result = self.db_cursor.fetchone()  # Fetch the first row

        if result:
            serial = result[0]  # Extract the first column (type)
            serial += 1
            query = "UPDATE serial SET serial=%s WHERE code=%s"
            self.db_cursor.execute(query, (serial,code,))
        else:
            serial =1
            query = """INSERT INTO serial (code, serial) VALUES (%s, %s)"""
            self.db_cursor.execute(query, (code,serial,))
        return serial

    def add_asset(self, data):
        try:
            query = """
                INSERT INTO asset (
                    asset_serial, asset_type, asset_sub_type, inventory_number, description, date_purchase, 
                    purchase_price, vender_name, vender_address, vender_phone, asset_location, 
                    asset_owner, asset_custodian, depreciation_rate,entered_on,entered_by
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err

    def update_asset(self, data):
        try:
            asset_serial=data[0]
            deleted_by=data[14]
            deleted_on=data[15]

            query = """UPDATE asset SET deleted_by=%s, deleted_on=%s, deleted=%s WHERE asset_serial=%s and deleted=%s"""
            self.db_cursor.execute(query, (deleted_on, deleted_by, 1, asset_serial, 0, ))
            self.db_connection.db_connection.commit()

            query = """
                INSERT INTO asset (
                    asset_serial, asset_type, asset_sub_type, inventory_number, description, date_purchase, 
                    purchase_price, vender_name, vender_address, vender_phone, asset_location, 
                    asset_owner, asset_custodian, depreciation_rate,entered_on,entered_by
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err

    def add_amc(self, data):
        try:
            query = """UPDATE amc SET is_current=%s WHERE asset_serial=%s"""
            self.db_cursor.execute(query, (0, data[0],))
            self.db_connection.db_connection.commit()

            query = """
                INSERT INTO amc (
                    asset_serial,amc_signed_date,amc_start_date,amc_end_date,charge_amount,remarks,amc_signed_by,entered_on,entered_by,is_current
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err

    def asset_detail(self, asset_serial):
        query = """SELECT asset_type, asset_sub_type, inventory_number, description, date_purchase,
                    purchase_price, vender_name, vender_address, vender_phone, asset_location, asset_owner, asset_custodian, depreciation_rate, entered_on, entered_by,
                    (SELECT description from asset_type t where t.type=a.asset_type) asset_type_name,
                    (SELECT description from asset_sub_type s where s.type=a.asset_type and s.sub_type=a.asset_sub_type) asset_sub_type_name
                    FROM asset a WHERE asset_serial=%s and deleted=%s"""

        self.db_cursor.execute(query, (asset_serial,0,))
        result = self.db_cursor.fetchone()  # Fetch the first row
        return result
    def view_asset(self, asset_type, asset_sub_type, report_type):
        match report_type:
            case 1:
                query = """SELECT a.asset_serial, a.inventory_number, a.description, a.date_purchase,
                            a.purchase_price, a.vender_name, a.asset_location, 
                            (SELECT c.amc_end_date FROM amc c where c.asset_serial=a.asset_serial and c.is_current=1) amc_end_date,
                            a.vender_address, a.vender_phone, a.asset_owner, a.asset_custodian,                  
                            a.depreciation_rate, a.entered_on, a.entered_by,a.asset_type, a.asset_sub_type, 
                            (SELECT description from asset_type t where t.type=a.asset_type) asset_type_name,
                            (SELECT description from asset_sub_type s where s.type=a.asset_type and s.sub_type=a.asset_sub_type) asset_sub_type_name
                            FROM asset a WHERE a.asset_type=%s and a.asset_sub_type=%s and a.deleted=%s"""
                self.db_cursor.execute(query, (asset_type, asset_sub_type, 0,))
            case 2:
                query = """SELECT a.asset_serial, a.inventory_number, a.description, a.date_purchase,
                            a.purchase_price, a.vender_name, a.asset_location, 
                            (SELECT c.amc_end_date FROM amc c where c.asset_serial=a.asset_serial and c.is_current=1) amc_end_date,
                            a.vender_address, a.vender_phone, a.asset_owner, a.asset_custodian,                  
                            a.depreciation_rate, a.entered_on, a.entered_by,a.asset_type, a.asset_sub_type, 
                            (SELECT description from asset_type t where t.type=a.asset_type) asset_type_name,
                            (SELECT description from asset_sub_type s where s.type=a.asset_type and s.sub_type=a.asset_sub_type) asset_sub_type_name
                            FROM asset a WHERE a.deleted=%s"""
                self.db_cursor.execute(query, (0,))
            case 3:
                query = """SELECT a.asset_serial, a.inventory_number, a.description, a.date_purchase,
                            a.purchase_price, a.vender_name, a.asset_location, 
                            (SELECT c.amc_end_date FROM amc c where c.asset_serial=a.asset_serial and c.is_current=1) amc_end_date,
                            a.vender_address, a.vender_phone, a.asset_owner, a.asset_custodian,                  
                            a.depreciation_rate, a.entered_on, a.entered_by,a.asset_type, a.asset_sub_type, 
                            (SELECT description from asset_type t where t.type=a.asset_type) asset_type_name,
                            (SELECT description from asset_sub_type s where s.type=a.asset_type and s.sub_type=a.asset_sub_type) asset_sub_type_name
                            FROM asset a WHERE a.asset_type=%s and a.deleted=%s"""
                self.db_cursor.execute(query, (asset_type, 0,))
        result = self.db_cursor.fetchall()  # Fetch the first row
        return result

    def amc_expiring(self, date_1, date_2):
        query = """select a.asset_serial, a.inventory_number, a.description, a.date_purchase,
                a.purchase_price, a.vender_name, a.asset_location,c.amc_end_date
                from asset a, amc c
                where a.asset_serial = c.asset_serial and c.amc_end_date  between %s and %s and a.deleted = %s"""
        self.db_cursor.execute(query, (date_1, date_2, 0,))
        result = self.db_cursor.fetchall()  # Fetch the first row
        return result

    def amc_history(self, asset_serial):
        query = """SELECT amc_signed_date, amc_start_date, amc_end_date, charge_amount, remarks, is_current
         FROM amc WHERE asset_serial=%s order by entered_on desc"""
        self.db_cursor.execute(query, (asset_serial,))
        result = self.db_cursor.fetchall()  # Fetch the first row
        return result

    def add_login(self, data):
        try:
            query = """
                INSERT INTO user_login (
                    USER_ID, LOGIN_IP, LOGIN_TIME, LOGIN_STATUS, LOGIN_ERR, LOGOUT_TIME
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err
        
# functions for asset type configuration
    def check_type_code(self, type):
        query = "SELECT type FROM asset_type WHERE type=%s"
        self.db_cursor.execute(query, (type,))

        result = self.db_cursor.fetchone()
        return result is not None

    def check_sub_type_code(self, sub_type):
        query = "SELECT sub_type FROM asset_sub_type WHERE sub_type=%s"
        self.db_cursor.execute(query, (sub_type,))

        result = self.db_cursor.fetchone()
        return result is not None

    def add_asset_type(self, data):
        try:
            query = """
                INSERT INTO asset_type (
                   type, description) VALUES (%s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err

    def add_asset_sub_type(self, data):
        try:
            query = """
                INSERT INTO asset_sub_type (
                   type, sub_type, description) VALUES (%s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Database Error: {err}")
            return err

class SessionManager:
    def load_session_from_file(self):
        try:
            with open("session.json", "r") as file:
                self.session = json.load(file)
            return self.session
        except FileNotFoundError:
            return None  # Handle the case if the session file is not found