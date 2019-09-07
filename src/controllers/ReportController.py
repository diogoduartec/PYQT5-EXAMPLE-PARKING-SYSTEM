from src.views.ReportView import ReportView
from src.models.VehicleList import VehicleList

from datetime import timedelta, date

class ReportController:
    def __init__(self):
        self.view = ReportView(self.get_days())
        self.money_info = self.view.money
        self.money_info.setText('R$ 00,00')
        #self.view.price_table.set_content(self.get_prices())

    def render_view(self):
        return self.view


    def get_days(self):
        vehicle_list = VehicleList()
        registers_list = []
        first_day = vehicle_list.get_first_day()
        last_day = vehicle_list.get_last_day()

        delta = timedelta(days=1)
        iterator = first_day

        while iterator <= last_day:
            registers_list.append(iterator)
            iterator += delta

        return registers_list