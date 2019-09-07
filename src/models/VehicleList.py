from src.models.Vehicle import Vehicle

class VehicleList:
    def __init__(self):
        self.__list_vehicle = []

    def init(self):
        v1 = Vehicle('BP1-2245', 'Fiat UNO', 'Amarelo', 19201012)
        v2 = Vehicle('XXP-2341', 'Chevrolet Onix', 'Azul', 19201012)
        v3 = Vehicle('GA3-0938', 'Volkswagen Gol', 'Prata', 19201012)
        v4 = Vehicle('ESA-4531', 'Nissa March', 'Vermelho', 19201012)
        v5 = Vehicle('KLS-8349', 'Citroen C3', 'Preto', 19201012)
        v6 = Vehicle('QWE-8549', 'Ford Ka', 'Azul', 19201012)
        v7 = Vehicle('AFG-9341', 'Honda Civic', 'Branco', 19201012)
        v8 = Vehicle('FDS-0934', 'Hyundai HB20', 'Prata', 19201012)
        v9 = Vehicle('DCV-1562', 'Toyota Corola', 'Vermelho', 19201012)
        v10 = Vehicle('SAD-3756', 'Jeep Renegade', 'Preto', 19201012)
        v11 = Vehicle('JSS-4525', 'Land Rover Discovery', 'Branco', 19201012)

        self.__list_vehicle.append(v1)
        self.__list_vehicle.append(v2)
        self.__list_vehicle.append(v3)
        self.__list_vehicle.append(v4)
        self.__list_vehicle.append(v5)
        self.__list_vehicle.append(v6)
        self.__list_vehicle.append(v7)
        self.__list_vehicle.append(v8)
        self.__list_vehicle.append(v9)
        self.__list_vehicle.append(v10)
        self.__list_vehicle.append(v11)

    def get_list(self):
        return self.__list_vehicle