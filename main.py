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

        # self.ui.button_show_plot_currency.clicked.connect()
        # self.ui.button_show_diagram_currencies.clicked.connect()

        self.ui.button_show_plot_all_time_key_rate.clicked.connect(plots.plot_key_rate_all_time)
        self.ui.button_show_plot_for_period_key_rate.clicked.connect(self.onButtonShowPlotKeyRateForPeriodClick)

        self.ui.button_show_plot_pie_gdp.clicked.connect(self.onButtonShowPlotPieGDP)
        self.ui.button_show_plot_gdp.clicked.connect(self.onButtonShowPlotGDPAllTime)
        # self.ui.button_show_plot_gdp_growth.clicked.connect()

        self.ui.menu.triggered.connect(self.onMenuUpdateDB)

        years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

        self.ui.combo_year_key_rate1.addItems(years)
        self.ui.combo_month_key_rate1.addItems(months)
        self.ui.combo_year_key_rate2.addItems(years)
        self.ui.combo_month_key_rate2.addItems(months)

        self.ui.combo_year_currencies1.addItems(years)
        self.ui.combo_month_currencies1.addItems(months)
        self.ui.combo_year_currencies2.addItems(years)
        self.ui.combo_month_currencies2.addItems(months)

        self.ui.combo_year_gdp1.addItems(years)
        self.ui.combo_month_gdp1.addItems(months)
        self.ui.combo_year_gdp2.addItems(years)
        self.ui.combo_month_gdp2.addItems(months)

    def onButtonCurrenciesClick(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def onButtonKeyRateClick(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def onButtonGDPClick(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def onButtonBackClick(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onButtonShowPlotKeyRateForPeriodClick(self):
        start_year = self.ui.combo_year_key_rate1.currentText()
        start_month = self.ui.combo_month_key_rate1.currentText()
        end_year = self.ui.combo_year_key_rate2.currentText()
        end_month = self.ui.combo_month_key_rate2.currentText()
        if start_year == '2013' and (int(start_month) < 9 or int(end_month) < 9):
            pass
        else:
            plots.plot_key_rate_for_period(start_year, start_month, end_year, end_month)

    @staticmethod
    def onButtonShowPlotPieGDP():
        plots.pie_diagram_gdp_in_monetary_current()

    @staticmethod
    def onButtonShowPlotGDPAllTime():
        plots.plot_gdp_all_time()

    @staticmethod
    def onMenuUpdateDB():
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
