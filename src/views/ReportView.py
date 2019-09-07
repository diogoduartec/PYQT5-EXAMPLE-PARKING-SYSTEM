from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPalette

from src.views.gui.PriceTable import PriceTable
import src.assets.styles.ReportView as STYLES
import src.assets.Colors as COLORS

class ReportView(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.inputs_layout = QHBoxLayout()
        self.labels_layout = QVBoxLayout()
        self.labels_layout.setAlignment(Qt.AlignCenter)
        self.labels_container = QWidget()


        self.title = QLabel('Arrecadação total no período')
        self.title.setAlignment(Qt.AlignCenter)
        self.money = QLabel('R$ 1800')
        self.money.setAlignment(Qt.AlignCenter)

        self.date_initial = QComboBox()
        self.date_final = QComboBox()

        self.date_initial.addItem('Início do período')
        self.date_final.addItem('Início do período')

        for i in range(100):
            self.date_initial.addItem('10/10/2018')
            self.date_final.addItem('12/11/2019')
        self.button_ok = QPushButton('CALCULAR')

        #DEFININDO LAYOUT DOS LABELS
        self.labels_layout.addWidget(self.title)
        self.labels_layout.addWidget(self.money)
        self.labels_container.setLayout(self.labels_layout)

        # DEFININDO LAYOUT DOS INPUTS
        self.inputs_layout.addWidget(self.date_initial)
        self.inputs_layout.addWidget(self.date_final)
        self.inputs_layout.addWidget(self.button_ok)

        # DEFININDO LAYOUT GERAL
        self.layout.addWidget(self.labels_container)
        self.layout.addLayout(self.inputs_layout)

        self.setLayout(self.layout)

        #APLICANDO ESTILO
        self.labels_container.setStyleSheet(STYLES.panel)
        self.title.setStyleSheet(STYLES.title)
        self.money.setStyleSheet(STYLES.money)
        self.button_ok.setStyleSheet(STYLES.button)