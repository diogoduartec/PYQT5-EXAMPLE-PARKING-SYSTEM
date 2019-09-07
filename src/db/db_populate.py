import sqlite3
from sqlite3 import Error
from data import vehicles, day_prices

def sqlite_connection():
    try:
        connection = sqlite3.connect('itriad.db')
        return connection
    except Error as error:
        print(error)

def tbl_vehicle_insert(connection, data):
    cursor = connection.cursor()
    sql_command = '''INSERT INTO tbl_vehicle(vehicle_plate, vehicle_model, vehicle_color, vehicle_arrival_time, 
    vehicle_departure_time) VALUES(?, ?, ?, ?, ?) '''
    entities = (data["plate"], data["model"], data["color"], data["arrival_time"], data["departure_time"])
    try:
        cursor.execute(sql_command, entities)
        connection.commit()
    except Error as error:
        print(error)

def tbl_day_price(connection, day, prices):
    cursor = connection.cursor()
    sql_command = '''INSERT INTO tbl_day_price(day_price_id, day_price_8_oclock, 
    day_price_9_oclock, day_price_10_oclock, day_price_11_oclock, day_price_12_oclock, day_price_13_oclock, 
    day_price_14_oclock, day_price_15_oclock, day_price_16_oclock, day_price_17_oclock, day_price_18_oclock) VALUES(
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    entities = (day, prices[0], prices[1], prices[2], prices[3], prices[4], prices[5], prices[6], prices[7], prices[8], prices[9], prices[10])
    try:
        cursor.execute(sql_command, entities)
        connection.commit()
    except Error as error:
        print(error)

if __name__ == '__main__':
    connection = sqlite_connection()

    for vehicle in vehicles:
        tbl_vehicle_insert(connection, vehicle)

    for day in day_prices:
        tbl_day_price(connection, day, day_prices[day])
