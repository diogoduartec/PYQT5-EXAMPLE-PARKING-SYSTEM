from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QBrush

import src.assets.styles.ListAutos as STYLES

class ListAutos(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.list_autos = QListWidget()

        items = []
        for i in range(100):
            items.append(QListWidgetItem('PDH-2250, Fiat UNO, Branco'))
            self.list_autos.addItem(items[i])
            items[i].setForeground(QBrush(QColor('#FFFFFF')))

        self.addWidget(self.list_autos)

        button_delete = QPushButton('REGISTRAR SAÍDA DO VEÍCULO')
        button_delete.setStyleSheet(STYLES.button)

        self.addWidget(button_delete)

