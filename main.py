import sys
from PyQt5.QtWidgets import QApplication

import src.controllers.MainWindow

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = src.controllers.MainWindow.MainWindow()
	window.show()

	sys.exit(app.exec())
