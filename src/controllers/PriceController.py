from src.views.PriceView import PriceView
from src.models.DayPrice import DayPrice
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QPushButton

class PriceController:
    def __init__(self):

        # ESPELHO PARA OTIMIZAR ATUALIZAÇÃO DA TABELA
        self.price_table_mirror = self.get_prices()

        # CHAMANDO VIEW E INICIALIZANDO TABELA DE PREÇOS
        self.view = PriceView(self.price_table_mirror)

        # CAPTURANDO REFERÊNCIAS DE COMPONENTES
        self.table = self.view.price_table
        self.button_save = self.view.button_save

        # DEFININDO COMPORTAMENTOS
        self.view.set_events(self.update_table)

    def render_view(self):
        return self.view

    def get_prices(self):
        day_prices = DayPrice().get_price_table()
        table = []
        for i in range(11):

            line = []
            for j in range(7):
                line.append(day_prices[j][i])
            table.append(line)
        return table

    def update_table(self):
        updates_position = []
        for i in range(11):
            for j in range(7):
                new_value = self.table.item(i, j).text()
                new_value = new_value.replace(',', '.')
                new_value = new_value.replace('R$ ', '')

                if str(self.price_table_mirror[i][j]) != new_value:
                    if self.check_update(new_value):
                        updates_position.append((j,i,float(new_value)))
                        self.price_table_mirror[i][j] = float(new_value)
                        self.table.item(i,j).setText('R$ '+str(float(new_value)))

                    else:
                        self.table.item(i,j).setText('R$ '+str(self.price_table_mirror[i][j]))

        self.update_prices_db(updates_position)


    def check_update(self, new_item):
        try:
            f = float(new_item)
            return True
        except ValueError:
            return False

    def update_prices_db(self, new_prices):
        day_prices = DayPrice()

        for p in new_prices:
            day = p[0]
            hour = p[1]
            price = p[2]
            day_prices.update_price_table(day, hour, price)