import sqlite3
from sqlite3 import Error
from src._db.db_path import db_path

class VehicleCrud:

    def sqlite_connection(self):
        try:
            connection = sqlite3.connect(db_path)
            return connection
        except Error as error:
            print(error)

    def db_create_vehicle(self, vehicle):
        connection = self.sqlite_connection()
        cursor = connection.cursor()
        sql_command = '''INSERT INTO tbl_vehicle(vehicle_plate, vehicle_model, vehicle_color, vehicle_arrival_time) VALUES(?, ?, ?, ?) '''
        entities = (vehicle.get_plate(), vehicle.get_model(), vehicle.get_color(), vehicle.get_arrival_time())
        try:
            cursor.execute(sql_command, entities)
            connection.commit()
        except Error as error:
            print(error)

    def db_register_departure(self, vehicle_id, departure_time, bill):
        connection = self.sqlite_connection()
        cursor = connection.cursor()
        sql_command = '''UPDATE tbl_vehicle SET vehicle_departure_time = ?, vehicle_bill = ? WHERE vehicle_id = ?'''
        entities = (departure_time, bill, vehicle_id)
        try:
            cursor.execute(sql_command, entities)
            connection.commit()
        except Error as error:
            print(error)

    def db_delete_vehicle(self, vehicle_id):
        connection = self.sqlite_connection()
        cursor = connection.cursor()
        sql_command = '''DELETE FROM tbl_vehicle WHERE vehicle_id = ?'''
        entities = (vehicle_id)
        try:
            cursor.execute(sql_command, entities)
            connection.commit()
        except Error as error:
            print(error)

    def get_last_id(self):
        connection = self.sqlite_connection()
        cursor = connection.cursor()
        sql_command = 'SELECT * FROM tbl_vehicle ORDER BY vehicle_id DESC LIMIT 1'
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        return rows[0][0]