import mysql.connector

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='atm@2023',
    database='amc_tracker')