from src.views.PriceView import PriceView
from src.models.DayPrice import DayPrice

class PriceController:
    def __init__(self):
        self.view = PriceView(self.get_prices())
        self.table = self.view.price_table
        self.button_save = self.view.button_save
        #self.view.price_table.set_content(self.get_prices())

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