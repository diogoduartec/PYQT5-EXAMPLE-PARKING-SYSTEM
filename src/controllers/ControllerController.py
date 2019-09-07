from src.views.ControllerView import ControllerView
from src.models.VehicleList import VehicleList

class ControllerController:
    def __init__(self):
        self.view = ControllerView(self.get_vehicles_resume())
        self.button_save = self.view.new_auto.button_save
        self.input_plate = self.view.new_auto.textinput_plate
        self.input_model = self.view.new_auto.textinput_model
        self.input_color = self.view.new_auto.textinput_color

        #self.view.price_table.set_content(self.get_prices())

    def render_view(self):
        return self.view

    def get_vehicles_resume(self):
        vehicle_list = VehicleList()
        list = vehicle_list.get_list()
        vehicle_list_resume = []
        for vehicle in list:
            vehicle_list_resume.append(vehicle.get_resume())

        return vehicle_list_resume