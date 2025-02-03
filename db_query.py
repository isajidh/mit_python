import mysql.connector
from tkinter import ttk, messagebox


# Database Connection
class DatabaseConnection:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='atm@2023',
            database='amc_tracker'
        )
        self.db_cursor = self.db_connection.cursor()

    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()


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

    def add_asset(self, data):
        try:
            query = """
                INSERT INTO asset (
                    asset_type, asset_sub_type, inventory_number, description, date_purchase, 
                    purchase_price, vender_name, vender_address, vender_phone, asset_location, 
                    asset_owner, asset_custodian, depreciation_rate
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.db_cursor.execute(query, data)
            self.db_connection.db_connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            return err


# Usage Example:
# db_conn = DatabaseConnection()
# db_query = DBQuery(db_conn)

# Remember to close the connection when done
# db_conn.close_connection()
