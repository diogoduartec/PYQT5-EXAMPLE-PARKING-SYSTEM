from PyQt5.QtWidgets import QMainWindow, QToolBar, QToolButton, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from src.views.gui.PriceTable import PriceTable
import src.assets.styles.MainWindow as STYLES
import src.controllers.PriceController as PriceController

#IMPORTANTO VIEWS
from src.views.PriceView import PriceView
from src.views.ControllerView import ControllerView
from src.views.ReportView import ReportView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "ITRIAD"
        top = 100
        left = 100
        width = 760
        height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(top, left, width, height)
        self.setup_toobar()
        self.setStyleSheet(STYLES.container)

        self.setFixedWidth(760)
        self.setFixedHeight(500)

        price_view = PriceController.render_view()
        self.setCentralWidget(price_view)

    def setup_toobar(self):
        logo = QPixmap('src/assets/images/logo.png')
        label_logo = QLabel()
        label_logo.setPixmap(logo)

        self.btn_price = QToolButton()
        self.btn_price.setText("Preços")

        self.btn_controler = QToolButton()
        self.btn_controler.setText("Controle")

        self.btn_report = QToolButton()
        self.btn_report.setText("Relatório")

        toolbar = QToolBar()
        toolbar.addWidget(label_logo)
        toolbar.addWidget(self.btn_price)
        toolbar.addWidget(self.btn_controler)
        toolbar.addWidget(self.btn_report)

        self.btn_price.setStyleSheet(STYLES.active_tool_button)
        self.btn_report.setStyleSheet(STYLES.tool_button)
        self.btn_controler.setStyleSheet(STYLES.tool_button)

        self.btn_controler.clicked.connect(self.controller_handle_click)
        self.btn_report.clicked.connect(self.report_handle_click)
        self.btn_price.clicked.connect(self.price_handle_click)


        toolbar.setAllowedAreas(Qt.TopToolBarArea)
        toolbar.setStyleSheet(STYLES.toolbar)

        self.addToolBar(toolbar)

    def price_handle_click(self):
        self.btn_report.setStyleSheet(STYLES.tool_button)
        self.btn_controler.setStyleSheet(STYLES.tool_button)
        self.btn_price.setStyleSheet(STYLES.active_tool_button)
        price_view = PriceView()
        self.setCentralWidget(price_view)

    def report_handle_click(self):
        self.btn_price.setStyleSheet(STYLES.tool_button)
        self.btn_controler.setStyleSheet(STYLES.tool_button)
        self.btn_report.setStyleSheet(STYLES.active_tool_button)
        report_view = ReportView()
        self.setCentralWidget(report_view)

    def controller_handle_click(self):
        self.btn_price.setStyleSheet(STYLES.tool_button)
        self.btn_report.setStyleSheet(STYLES.tool_button)
        self.btn_controler.setStyleSheet(STYLES.active_tool_button)
        controller_view = ControllerView()
        self.setCentralWidget(controller_view)