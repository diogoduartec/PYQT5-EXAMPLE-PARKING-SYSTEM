from src.views.ControllerView import ControllerView
from src.models.VehicleList import VehicleList
from src.models.Vehicle import Vehicle
from src.models.VehicleCrud import VehicleCrud
from src.models.DayPrice import DayPrice

from datetime import date
import datetime
from math import ceil

class ControllerController:
    def __init__(self):

        # LISTA DE PREÇEÕS PARA CALCULAR PRECO CONTA DO VEÍCULO
        self.day_price = DayPrice().get_price_table()

        # ESPELHO DA LISTA DE VEICULOS
        self.vehicle_list_mirror = VehicleList().get_list()

        # CHAMANDO VIEW E INICIALIZANDO LISTA DE VEÍCULOS
        self.view = ControllerView(self.get_vehicles_resume())
        self.view.new_auto.set_events(self.add_new_vehicle)

        # CAPTURANDO REFERÊNCIAS DE COMPONENTES
        self.button_save = self.view.new_auto.button_save
        self.input_plate = self.view.new_auto.textinput_plate
        self.input_model = self.view.new_auto.textinput_model
        self.input_color = self.view.new_auto.textinput_color
        self.vehicle_list = self.view.list_autos

        # DEFININDO COMPORTAMENTOS
        self.vehicle_list.set_events(self.remove_vehicle)

    def render_view(self):
        return self.view

    def get_vehicles_resume(self):
        list = self.vehicle_list_mirror
        vehicle_list_resume = []
        for vehicle in list:
            vehicle_list_resume.append(vehicle.get_resume())

        return vehicle_list_resume

    def add_new_vehicle(self):
        plate = self.input_plate.text()
        model = self.input_model.text()
        color = self.input_color.text()
        arrival_time = int(datetime.datetime.now().timestamp())

        vehicle = Vehicle(plate, model, color, arrival_time)
        vehicle_crud = VehicleCrud()

        # PERSITE O VEÍCULO
        vehicle_crud.db_create_vehicle(vehicle)
        vehicle.set_id(vehicle_crud.get_last_id())

        # ADICIONA O VEÍCULO NA LISTA
        self.vehicle_list_mirror.append(vehicle)
        self.vehicle_list.add_item(vehicle.get_resume())

    def remove_vehicle(self):
        vehicle_crud = VehicleCrud()
        row = self.vehicle_list.list_autos.currentRow()
        item = self.vehicle_list.list_autos.takeItem(row)
        mirror_item = self.vehicle_list_mirror[row]
        departure_time = int(datetime.datetime.now().timestamp())
        mirror_item.set_departure_time(departure_time)

        # CALCULANDO CONTA
        bill = self.calculate_vehicle_bill(mirror_item)

        vehicle_crud.db_register_departure(mirror_item.get_id(), departure_time, bill)
        del item
        del self.vehicle_list_mirror[row]

    def calculate_vehicle_bill(self, vehicle):
        # DEFININDO DATA E HORÁRIOS
        arrival_time = vehicle.get_arrival_time()
        departure_time = vehicle.get_departure_time()
        total_time = int(ceil((departure_time - arrival_time)/3600))
        day = date.fromtimestamp(arrival_time).weekday()
        day = (day+1)%7 # corrigindo dia para semana começar no domingo
        initial_hour = datetime.datetime.fromtimestamp(arrival_time).hour

        sum = 0.0
        for i in range(total_time):
            hour = initial_hour+i-8
            sum += self.day_price[day][hour]

        return sum