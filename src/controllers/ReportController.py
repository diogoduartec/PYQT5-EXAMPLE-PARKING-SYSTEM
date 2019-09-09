from src.views.ReportView import ReportView
from src.models.VehicleList import VehicleList

from datetime import timedelta, date


class ReportController:
    def __init__(self):
        # ESPELHO DA LISTA DE DIAS DISPONÍVEL PARA CONSULTA
        self.days_list_mirror = []

        # CHAMANDO VIEW E INICALIZANDO SETANDO OS DIAS QUE ESTACIONAMENTO FUNCIONOU
        self.view = ReportView(self.get_days())
        self.money_info = self.view.money
        self.money_info.setText('R$ 0.0')
        self.view.set_events(self.set_money_panel)

    def render_view(self):
        return self.view

    def get_days(self):

        # CAPTURANDO PRIMEIRO E ÚLTIMO DIA
        vehicle_list = VehicleList()
        first_day = vehicle_list.get_first_vehicle_date()
        last_day = vehicle_list.get_last_vehicle_date()

        # GERANDO LISTA DE DIAS
        registers_list = []
        delta = timedelta(days=1)
        iterator = first_day

        while iterator <= last_day:
            registers_list.append(iterator.date())
            self.days_list_mirror.append(iterator)
            iterator += delta

        return registers_list

    def calculate_profit(self):
        initial_index = self.view.date_initial.currentIndex() - 1
        final_index = self.view.date_final.currentIndex() - 1
        initial_date = int(self.days_list_mirror[initial_index].timestamp())
        final_date = int(self.days_list_mirror[final_index].timestamp())

        if final_index >= initial_index >= 0 and final_date >= 0 and initial_date >= 0:
            return VehicleList().get_profit_amount(initial_date, final_date)
        else:
            return 0.0

    def set_money_panel(self):
        self.view.money.setText('R$ ' + str(self.calculate_profit()))
