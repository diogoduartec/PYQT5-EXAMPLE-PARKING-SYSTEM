from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPalette

from src.views.gui.PriceTable import PriceTable
import src.assets.styles.ReportView as STYLES
import src.assets.Colors as COLORS

class ReportView(QWidget):
    def __init__(self, days):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        inputs_layout = QHBoxLayout()
        labels_layout = QVBoxLayout()
        labels_layout.setAlignment(Qt.AlignCenter)
        labels_container = QWidget()


        self.title = QLabel('Arrecadação total no período')
        self.title.setAlignment(Qt.AlignCenter)
        self.money = QLabel('R$ 1800')
        self.money.setAlignment(Qt.AlignCenter)

        self.date_initial = QComboBox()
        self.date_final = QComboBox()

        self.date_initial.addItem('Início do período')
        self.date_final.addItem('Fim do período')
        self.date_final.addItem('Fim do período')

        for day in days:
            self.date_initial.addItem(str(day))
            self.date_final.addItem(str(day))
        self.button_ok = QPushButton('CALCULAR')

        #DEFININDO LAYOUT DOS LABELS
        labels_layout.addWidget(self.title)
        labels_layout.addWidget(self.money)
        labels_container.setLayout(labels_layout)

        # DEFININDO LAYOUT DOS INPUTS
        inputs_layout.addWidget(self.date_initial)
        inputs_layout.addWidget(self.date_final)
        inputs_layout.addWidget(self.button_ok)

        # DEFININDO LAYOUT GERAL
        layout.addWidget(labels_container)
        layout.addLayout(inputs_layout)

        self.setLayout(layout)

        #APLICANDO ESTILO
        labels_container.setStyleSheet(STYLES.panel)
        self.title.setStyleSheet(STYLES.title)
        self.money.setStyleSheet(STYLES.money)
        self.button_ok.setStyleSheet(STYLES.button)