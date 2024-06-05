from PyQt5 import QtWidgets, QtGui, QtCore

import backend
import plots
from mywindow import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_currencies.clicked.connect(self.onButtonCurrenciesClick)
        self.ui.button_key_rate_and_inflation.clicked.connect(self.onButtonKeyRateClick)
        self.ui.button_gdp.clicked.connect(self.onButtonGDPClick)
        self.ui.button_back_currencies.clicked.connect(self.onButtonBackClick)
        self.ui.button_back_key_rate.clicked.connect(self.onButtonBackClick)
        self.ui.button_back_gdp.clicked.connect(self.onButtonBackClick)
        self.ui.menu.triggered.connect(self.onMenuUpdateDB)

    def onButtonCurrenciesClick(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def onButtonKeyRateClick(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        plots.plot_key_rate_all_time()

    def onButtonGDPClick(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def onButtonBackClick(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onMenuUpdateDB(self):
        backend.update_data()
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Сообщение")
        layout = QtWidgets.QVBoxLayout()

        message = QtWidgets.QLabel("База данных обновлена")
        layout.addWidget(message)

        buttonBox = QtWidgets.QDialogButtonBox()
        buttonBox.addButton("Ok", QtWidgets.QDialogButtonBox.AcceptRole)

        buttonBox.accepted.connect(lambda: dialog.close())
        layout.addWidget(buttonBox)
        dialog.setLayout(layout)
        dialog.exec_()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
