from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout

from src.views.gui.PriceTable import PriceTable
import src.assets.styles.PriceView as STYLES

class PriceView(QWidget):
    def __init__(self, table):
        super().__init__()
        price_table_container = QVBoxLayout()
        button_container = QHBoxLayout()

        self.price_table = PriceTable(table)
        self.button_save = QPushButton("SALVAR ALTERAÇÕES")
        self.button_save.setFixedWidth(200)

        button_container.addWidget(self.button_save)
        price_table_container.addWidget(self.price_table)
        price_table_container.addLayout(button_container)
        self.setLayout(price_table_container)

        self.button_save.setStyleSheet(STYLES.button)