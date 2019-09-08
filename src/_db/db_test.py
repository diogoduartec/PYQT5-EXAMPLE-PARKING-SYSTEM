import sqlite3
from sqlite3 import Error
from data import vehicles


def sqlite_connection():
    try:
        connection = sqlite3.connect('itriad.db')
        return connection
    except Error:
        print(Error)


def tbl_vehicle_select(connection):
    cursor = connection.cursor()
    sql_command = "SELECT * FROM tbl_vehicle"
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    for r in rows:
        print(r)


def tbl_day_price_select(connection):
    cursor = connection.cursor()
    sql_command = "SELECT * FROM tbl_day_price"
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    print(len(rows[0]))
    for r in rows:
        print(r)

def tbl_vehicle_update(connection):
    cursor = connection.cursor()
    sql_command = "UPDATE tbl_vehicle SET vehicle_color = 'Laranja' WHERE vehicle_id = 1"
    try:
        cursor.execute(sql_command)
        connection.commit()
    except Error as error:
        print(error)


def get_profit_amount(connection, initial_date, final_date):

    cursor = connection.cursor()
    sql_command = '''SELECT vehicle_departure_time, SUM(vehicle_bill) FROM tbl_vehicle WHERE vehicle_arrival_time >= ? AND 
    vehicle_arrival_time <= ? AND vehicle_departure_time != "None"'''
    entities = (initial_date, final_date)
    try:
        cursor.execute(sql_command,entities)
        result = cursor.fetchall()
        for r in result:
            print(r)
    except Error as error:
        print(error)

if __name__ == '__main__':
    connection = sqlite_connection()
    get_profit_amount(connection,1567946132,1567946132)
