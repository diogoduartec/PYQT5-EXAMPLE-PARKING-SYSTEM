from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QWidget
from PyQt5.QtCore import Qt

import src.assets.styles.NewAuto as STYLE

class NewAuto(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.title = QLabel('Entrada de Veículos')
        self.textinput_plate = QLineEdit()
        self.textinput_model = QLineEdit()
        self.textinput_color = QLineEdit()
        self.button_save = QPushButton('REGISTRAR ENTRADA DO VEÍCULO')

        self.init()

        self.addWidget(self.title)
        self.addWidget(self.textinput_color)
        self.addWidget(self.textinput_model)
        self.addWidget(self.textinput_plate)
        self.addWidget(self.button_save)
        self.setAlignment(Qt.AlignCenter)

    def init(self):
        self.title.setStyleSheet(STYLE.label)
        self.title.setAlignment(Qt.AlignCenter)

        self.textinput_plate.setPlaceholderText('Placa do veículo')
        self.textinput_model.setPlaceholderText('Modelo do veículo')
        self.textinput_color.setPlaceholderText('Cor do veículo')

        self.textinput_plate.setStyleSheet(STYLE.input)
        self.textinput_model.setStyleSheet(STYLE.input)
        self.textinput_color.setStyleSheet(STYLE.input)
        self.button_save.setStyleSheet(STYLE.button)
