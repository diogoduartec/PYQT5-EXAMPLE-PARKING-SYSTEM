from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem
from src.views.gui.ListAutos import ListAutos
from src.views.gui.NewAuto import NewAuto

import src._assets.Colors as COLORS
import src._assets.styles.ControllerView as STYLES


class ControllerView(QWidget):
    def __init__(self, vehicle_list):
        super().__init__()

        # LAYOUTS
        list_autos_container = QWidget()
        container = QHBoxLayout()

        # COMPONENTES DA TELA
        self.new_auto = NewAuto()
        self.list_autos = ListAutos(vehicle_list)

        # DEFININDO LAYOUTS
        container.addLayout(self.new_auto)
        container.addSpacing(3)
        container.addWidget(list_autos_container)

        list_autos_container.setLayout(self.list_autos)
        self.setLayout(container)

        # APLICANDO ESTILOS
        list_autos_container.setStyleSheet(STYLES.list_autos_container)
