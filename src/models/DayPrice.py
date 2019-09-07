import sqlite3
from sqlite3 import Error
class DayPrice:
    def __init__(self):
        self.__price_table = self.__get_day_prices(self.sqlite_connection())

    def sqlite_connection(self):
        try:
            connection = sqlite3.connect('src/db/itriad.db')
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