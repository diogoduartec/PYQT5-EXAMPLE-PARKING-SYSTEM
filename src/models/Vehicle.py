class Vehicle:
    def __init__(self, plate, model, color, arrival_time):
        self.__id = -1
        self.__plate = plate
        self.__model = model
        self.__color = color
        self.__arrival_time = arrival_time
        self.__departure_time = 0
        self.__bill = 0.0

    def get_resume(self):
        return self.__plate + ', ' + self.__model + ', ' + self.__color

    def get_plate(self):
        return self.__plate
    def get_model(self):
        return self.__model
    def get_color(self):
        return self.__color
    def get_arrival_time(self):
        return self.__arrival_time
    def get_departure_time(self):
        return self.__departure_time
    def get_id(self):
        return self.__id
    def get_bill(self):
        return self.__bill

    def set_departure_time(self, time):
        self.__departure_time = time
    def set_id(self, id):
        self.__id = id
    def set_bill(self, bill):
        self.__bill = bill