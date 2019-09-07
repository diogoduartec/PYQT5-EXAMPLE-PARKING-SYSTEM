from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem
from src.views.gui.ListAutos import ListAutos
from src.views.gui.NewAuto import NewAuto

import src.assets.Colors as COLORS
import src.assets.styles.ControllerView as STYLES

class ControllerView(QWidget):
    def __init__(self, vehicle_list):
        super().__init__()

        list_autos_container = QWidget()
        container = QHBoxLayout()

        self.new_auto = NewAuto()
        self.list_autos = ListAutos(vehicle_list)

        list_autos_container.setLayout(self.list_autos)

        container.addLayout(self.new_auto)
        container.addSpacing(3)
        container.addWidget(list_autos_container)
        list_autos_container.setStyleSheet(STYLES.list_autos_container)

        self.setLayout(container)
