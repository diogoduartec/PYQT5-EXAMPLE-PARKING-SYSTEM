from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem
from src.views.gui.ListAutos import ListAutos
from src.views.gui.NewAuto import NewAuto

import src.assets.Colors as COLORS
import src.assets.styles.ControllerView as STYLES

class ControllerView(QWidget):
    def __init__(self):
        super().__init__()

        self.list_autos_container = QWidget()

        self.container = QHBoxLayout()
        self.new_auto = NewAuto()
        self.list_autos = ListAutos()

        self.list_autos_container.setLayout(self.list_autos)

        self.container.addLayout(self.new_auto)
        self.container.addSpacing(3)
        self.container.addWidget(self.list_autos_container)
        self.list_autos_container.setStyleSheet(STYLES.list_autos_container)

        self.setLayout(self.container)
