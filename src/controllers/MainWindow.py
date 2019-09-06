from PyQt5.QtWidgets import QMainWindow, QToolBar, QToolButton, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from src.views.PriceTable import PriceTable
import assets.styles.MainWindow as STYLES



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

        self.load_prices()
        self.setFixedWidth(760)
        self.setFixedHeight(500)

    def setup_toobar(self):
        logo = QPixmap('assets/images/logo.png')
        label_logo = QLabel()
        label_logo.setPixmap(logo)

        btn_register = QToolButton()
        btn_register.setText("Preços")

        btn_controler = QToolButton()
        btn_controler.setText("Controle")

        btn_report = QToolButton()
        btn_report.setText("Relatório")

        toolbar = QToolBar()
        toolbar.addWidget(label_logo)
        toolbar.addWidget(btn_register)
        toolbar.addWidget(btn_controler)
        toolbar.addWidget(btn_report)
        btn_register.setStyleSheet(STYLES.active_tool_button)
        btn_report.setStyleSheet(STYLES.tool_button)
        btn_controler.setStyleSheet(STYLES.tool_button)

        toolbar.setAllowedAreas(Qt.TopToolBarArea)
        toolbar.setStyleSheet(STYLES.toolbar)

        self.addToolBar(toolbar)

    def load_prices(self):
        container = QWidget()
        price_table_container = QVBoxLayout()
        button_container = QHBoxLayout()

        price_table = PriceTable()
        button = QPushButton("SALVAR ALTERAÇÕES")
        button.setFixedWidth(200)

        button_container.addWidget(button)
        price_table_container.addWidget(price_table)
        price_table_container.addLayout(button_container)
        container.setLayout(price_table_container)

        button.setStyleSheet(STYLES.button)
        self.setCentralWidget(container)