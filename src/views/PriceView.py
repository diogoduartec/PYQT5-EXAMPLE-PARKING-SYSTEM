from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QObject

from src.views.gui.PriceTable import PriceTable
import src._assets.styles.PriceView as STYLES


class PriceView(QWidget):
    def __init__(self, table):
        super().__init__()

        # LAYOUTS
        price_table_container = QVBoxLayout()
        button_container = QHBoxLayout()

        # COMPONENTES DA TELA
        self.price_table = PriceTable(table)
        self.button_save = QPushButton("SALVAR ALTERAÇÕES")
        self.button_save.setFixedWidth(200)

        # DEFININDO LAYOUTS
        button_container.addWidget(self.button_save)
        price_table_container.addWidget(self.price_table)
        price_table_container.addLayout(button_container)
        self.setLayout(price_table_container)

        # APLICANDO ESTILOS
        self.button_save.setStyleSheet(STYLES.button)

    # COMPORTAMENTO DEFINIDO PELO CONTROLLER
    def set_events(self, on_button_clicked):
        self.on_button_clicked = on_button_clicked
        self.button_save.clicked.connect(self.on_button_clicked)