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


if __name__ == '__main__':
    connection = sqlite_connection()

    tbl_vehicle_select(connection)
    tbl_day_price_select(connection)
