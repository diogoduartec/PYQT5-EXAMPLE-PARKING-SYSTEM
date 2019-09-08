from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QWidget
from PyQt5.QtCore import Qt

import src._assets.styles.NewAuto as STYLE


class NewAuto(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # COMPONENTES DE TELA
        self.title = QLabel('Entrada de Veículos')
        self.textinput_plate = QLineEdit()
        self.textinput_model = QLineEdit()
        self.textinput_color = QLineEdit()
        self.button_save = QPushButton('REGISTRAR ENTRADA DO VEÍCULO')

        self.addWidget(self.title)
        self.addWidget(self.textinput_plate)
        self.addWidget(self.textinput_model)
        self.addWidget(self.textinput_color)
        self.addWidget(self.button_save)
        self.setAlignment(Qt.AlignCenter)

        self.init()

    def init(self):
        # DEFININDO CONTEÚDO
        self.textinput_plate.setPlaceholderText('Placa do veículo')
        self.textinput_model.setPlaceholderText('Modelo do veículo')
        self.textinput_color.setPlaceholderText('Cor do veículo')

        # APLICANDO ESTILOS
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(STYLE.label)
        self.textinput_plate.setStyleSheet(STYLE.input)
        self.textinput_model.setStyleSheet(STYLE.input)
        self.textinput_color.setStyleSheet(STYLE.input)
        self.button_save.setStyleSheet(STYLE.button)

    def set_events(self, on_button_clicked):
        self.on_button_clicked = on_button_clicked
        self.button_save.clicked.connect(self.on_button_clicked)