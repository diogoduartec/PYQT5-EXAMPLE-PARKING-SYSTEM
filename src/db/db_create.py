import sqlite3
from sqlite3 import Error

def sqlite_connection():
    try:
        connection = sqlite3.connect('itriad.db')
        return connection
    except Error as error:
        print(error)

def tbl_vehicle(connection):
    cursor = connection.cursor()
    sql_command = "CREATE TABLE tbl_vehicle(vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_plate VARCHAR(8), vehicle_model VARCHAR(25), vehicle_color VARCHAR(20), vehicle_arrival_time INTEGER, vehicle_departure_time INTEGER)"
    try:
        cursor.execute(sql_command)
        connection.commit()
    except Error as error:
        print(error)

def tbl_day_price(connection):
    cursor = connection.cursor()
    sql_command = "CREATE TABLE tbl_day_price(day_price_id VARCHAR(6) PRIMARY KEY, day_price_8_oclock DOUBLE, day_price_9_oclock DOUBLE, day_price_10_oclock DOUBLE, day_price_11_oclock DOUBLE, day_price_12_oclock DOUBLE, day_price_13_oclock DOUBLE, day_price_14_oclock DOUBLE, day_price_15_oclock DOUBLE, day_price_16_oclock DOUBLE, day_price_17_oclock DOUBLE, day_price_18_oclock DOUBLE)"
    try:
        cursor.execute(sql_command)
        connection.commit()
    except Error as error:
        print(error)

if __name__ == '__main__':
    connection = sqlite_connection()
    tbl_vehicle(connection)
    tbl_day_price(connection)
