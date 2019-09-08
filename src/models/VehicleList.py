from src.models.Vehicle import Vehicle

import sqlite3
from sqlite3 import Error
from datetime import date, datetime

from src._db.db_path import db_path


class VehicleList:
    def __init__(self):
        connection = self.sqlite_connection()
        self.__list_vehicle = self.__get_vehicle_list(connection)

    def sqlite_connection(self):
        try:
            connection = sqlite3.connect(db_path)
            return connection
        except Error as error:
            print(error)

    def __get_vehicle_list(self, connection):
        cursor = connection.cursor()
        sql_command = 'SELECT * FROM tbl_vehicle'

        list = []
        try:
            cursor.execute(sql_command)
            rows = cursor.fetchall()
            rows = filter(lambda row: row[5] == None, rows)

            for row in rows:
                id = row[0]
                plate = row[1]
                model = row[2]
                color = row[3]
                arrival_time = row[4]
                v = Vehicle(plate, model, color, arrival_time)
                v.set_id(id)
                list.append(v)

        except Error as error:
            print(error)

        return list

    def get_list(self):
        return self.__list_vehicle

    def get_first_vehicle_date(self):
        return datetime.fromtimestamp(self.__list_vehicle[0].get_arrival_time())

    def get_last_vehicle_date(self):
        last_position = len(self.__list_vehicle) - 1
        return datetime.fromtimestamp(self.__list_vehicle[last_position].get_arrival_time())

    def get_profit_amount(self, initial_date, final_date):
        connection = self.sqlite_connection()
        cursor = connection.cursor()
        sql_command = '''SELECT SUM(vehicle_bill) FROM tbl_vehicle WHERE vehicle_arrival_time >= ? AND 
        vehicle_arrival_time <= ? AND vehicle_departure_time != "None"'''
        entities = (initial_date, final_date)
        result = 0.0
        try:
            cursor.execute(sql_command, entities)
            result = cursor.fetchone()[0]
        except Error as error:
            print(error)

        return result

