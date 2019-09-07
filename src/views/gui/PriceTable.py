from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush

import src.assets.Colors as COLORS
import src.assets.styles.PriceTable as STYLES

class PriceTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(11)
        self.setColumnCount(7)
        self.set_header()
        self.set_col()

        itens = []
        for i in range(11):
            row = []
            for j in range(7):
                row.append(QTableWidgetItem("5.00"))
                row[j].setTextAlignment(Qt.AlignCenter)
                row[j].setForeground(QBrush(QColor('#FFFFFF')))
                if j&1: #se a coluna for impar cor dark3
                    row[j].setBackground(QColor(COLORS.dark3))
                else: #se a coluna for par cor dark3
                    row[j].setBackground(QColor(COLORS.dark4))

                self.setItem(i,j, row[j])
            itens.append(row)
        self.setStyleSheet(STYLES.background)
        self.horizontalHeader().setStyleSheet(STYLES.header)
        self.verticalHeader().setStyleSheet(STYLES.header)

    def set_header(self):
        self.header_items = []
        days = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
        for i in range(7):
            self.header_items.append(QTableWidgetItem(days[i]))
            self.header_items[i].setBackground(QColor(COLORS.primary))
            self.header_items[i].setForeground(QBrush(QColor('#FFFFFF')))
            self.setHorizontalHeaderItem(i, self.header_items[i])

    def set_col(self):
        self.col_items = []
        times = ['8:00', '9:00', '10:00', '11:00','12:00','13:00','14:00','15:00','16:00','17:00', '18:00']
        for i in range(11):
            self.col_items.append(QTableWidgetItem(times[i]))
            self.col_items[i].setBackground(QColor(COLORS.primary))
            self.col_items[i].setForeground(QBrush(QColor('#FFFFFF')))
            self.setVerticalHeaderItem(i, self.col_items[i])
