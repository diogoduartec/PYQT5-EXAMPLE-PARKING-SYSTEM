from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout

from src.views.gui.PriceTable import PriceTable
import src.assets.styles.PriceView as STYLES

class PriceView(QWidget):
    def __init__(self):
        super().__init__()
        price_table_container = QVBoxLayout()
        button_container = QHBoxLayout()

        price_table = PriceTable()
        button = QPushButton("SALVAR ALTERAÇÕES")
        button.setFixedWidth(200)

        button_container.addWidget(button)
        price_table_container.addWidget(price_table)
        price_table_container.addLayout(button_container)
        self.setLayout(price_table_container)

        button.setStyleSheet(STYLES.button)