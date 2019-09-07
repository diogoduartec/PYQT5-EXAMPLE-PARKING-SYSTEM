from src.models.Vehicle import Vehicle

import sqlite3
from sqlite3 import Error
from datetime import date

class VehicleList:
    def __init__(self):
        connection = self.sqlite_connection()
        self.__list_vehicle = self.__get_vehicle_list(connection)

    def sqlite_connection(self):
        try:
            connection = sqlite3.connect('src/db/itriad.db')
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
            for row in rows:
                id = row[0]
                plate = row[1]
                model = row[2]
                color = row[3]
                arrival_time = row[4]
                v = Vehicle(id, plate, model, color, arrival_time)
                list.append(v)

        except Error as error:
            print(error)

        return list

    def get_list(self):
        return self.__list_vehicle

    def get_first_day(self):
        return date.fromtimestamp(self.__list_vehicle[0].get_arrival_time())
        #return date.fromtimestamp(1505534159.34238)

    def get_last_day(self):
        last_position = len(self.__list_vehicle) - 1
        return date.fromtimestamp(self.__list_vehicle[last_position].get_arrival_time())
        #return date.fromtimestamp(1505534159.34238)
