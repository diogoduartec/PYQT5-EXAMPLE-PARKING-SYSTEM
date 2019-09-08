import sqlite3
from sqlite3 import Error

from src._db.db_path import db_path

class DayPrice:
    def __init__(self):
        connection = self.sqlite_connection()
        self.__price_table = self.__get_day_prices(connection)

        self.hours = {
            0: 'day_price_8_oclock',
            1: 'day_price_9_oclock',
            2: 'day_price_10_oclock',
            3: 'day_price_11_oclock',
            4: 'day_price_12_oclock',
            5: 'day_price_13_oclock',
            6: 'day_price_14_oclock',
            7: 'day_price_15_oclock',
            8: 'day_price_16_oclock',
            9: 'day_price_17_oclock',
            10: 'day_price_18_oclock',
        }

        self.days = {
            0: 'Dom',
            1: 'Seg',
            2: 'Ter',
            3: 'Qua',
            4: 'Qui',
            5: 'Sex',
            6: 'Sab',
        }

    def sqlite_connection(self):
        try:
            connection = sqlite3.connect(db_path)
            return connection
        except Error as error:
            print(error)

    def __get_day_prices(self, connection):
        cursor = connection.cursor()
        sql_command = 'SELECT * FROM tbl_day_price'

        table = []
        try:
            cursor.execute(sql_command)
            rows = cursor.fetchall()
            for row in rows:
                line = []
                for cel in range(len(row)):
                    if cel > 0:
                        line.append(row[cel])
                table.append(line)
        except Error as error:
            print(error)

        return table

    def get_price_table(self):
        return self.__price_table

    def update_price_table(self, day, hour, price):
        connection = self.sqlite_connection()
        cursor = connection.cursor()

        sql_command = 'UPDATE tbl_day_price SET '+self.hours[hour]+' = ? WHERE day_price_id = ?'
        entities = (price, self.days[day])
        try:
            cursor.execute(sql_command, entities)
            connection.commit()
        except Error as error:
            print(error)

    # def get_price_day_by_hour(self, day, hour):
    #     connection = self.sqlite_connection()
    #     cursor = connection.cursor()
    #     sql_command = 'SELECT '+self.hours[hour-8]+' FROM tbl_day_price WHERE day_price_id = ' + self.days[day]
    #
    #     table = []
    #     try:
    #         cursor.execute(sql_command)
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             line = []
    #             for cel in range(len(row)):
    #                 if cel > 0:
    #                     line.append(row[cel])
    #             table.append(line)
    #     except Error as error:
    #         print(error)
    #
    #     return table