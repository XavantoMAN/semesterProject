import datetime

from PyQt5 import QtWidgets, QtGui, QtCore

import backend
import plots
from mywindow import Ui_MainWindow
import sys
import pandas as pd


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

        self.ui.button_show_plot_currency.clicked.connect(self.onButtonShowPlotCurrencyClick)
        self.ui.button_show_diagram_currencies.clicked.connect(self.onButtonShowDiagramCurrenciesClick)

        self.ui.button_show_plot_all_time_key_rate.clicked.connect(plots.plot_key_rate_all_time)
        self.ui.button_show_plot_for_period_key_rate.clicked.connect(self.onButtonShowPlotKeyRateForPeriodClick)

        self.ui.button_show_plot_pie_gdp.clicked.connect(self.onButtonShowPlotPieGDP)
        self.ui.button_show_plot_gdp.clicked.connect(self.onButtonShowPlotGDPForPeriod)
        self.ui.button_show_plot_gdp_growth.clicked.connect(self.onButtonShowPlotGDPGrowthForPeriod)

        self.ui.menu.triggered.connect(self.onMenuUpdateDB)

        years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

        years_gdp = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
                     '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                     '2019', '2020', '2021', '2022', '2023']
        with open('currency_names.csv', 'r') as f:
            currency_names = f.read().split(',')
        with open('currency_codes.csv', 'r') as f:
            currency_codes = f.read().split(',')

        currency_names.pop(0)
        currency_codes.pop(0)
        self.currency_dict = pd.DataFrame({'currency_code': currency_codes,
                                           'currency_name': currency_names})
        self.currency_dict['currency_code'] = self.currency_dict['currency_code'].astype('string')
        self.currency_dict['currency_name'] = self.currency_dict['currency_name'].astype('string')

        self.model = QtGui.QStandardItemModel()
        currencies = backend.get_today_currencies()
        for i in currencies.Валюта:
            item = QtGui.QStandardItem(i)
            item.setCheckable(True)
            check = QtCore.Qt.CheckState.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)
        self.ui.list_view_currencies.setModel(self.model)

        self.ui.combo_currency.addItems(currency_names)

        self.ui.combo_year_key_rate1.addItems(years)
        self.ui.combo_month_key_rate1.addItems(months)
        self.ui.combo_month_key_rate1.setCurrentIndex(8)
        self.ui.combo_year_key_rate2.addItems(years)
        self.ui.combo_year_key_rate2.setCurrentIndex(1)
        self.ui.combo_month_key_rate2.addItems(months)

        self.ui.combo_year_gdp1.addItems(years_gdp)
        self.ui.combo_year_gdp2.addItems(years_gdp)
        self.ui.combo_year_gdp2.setCurrentIndex(len(years_gdp)-1)

    def onButtonCurrenciesClick(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def onButtonKeyRateClick(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def onButtonGDPClick(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def onButtonBackClick(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def onButtonShowPlotCurrencyClick(self):
        currency_name = self.ui.combo_currency.currentText()
        currency_code = self.currency_dict.currency_code[self.currency_dict['currency_name'] == currency_name].values[0]
        from_date = self.ui.date_edit_currencies1.date().toString('dd.MM.yyyy')
        to_date = self.ui.date_edit_currencies2.date().toString('dd.MM.yyyy')
        plots.plot_currency_for_period(currency_code, from_date, to_date)

    def onButtonShowDiagramCurrenciesClick(self):
        choices = [self.model.item(i).text()
                   for i in range(self.model.rowCount())
                   if self.model.item(i).checkState() == QtCore.Qt.CheckState.Checked]
        plots.diagram_selected_currencies(choices)

    def onButtonShowPlotKeyRateForPeriodClick(self):
        start_year = self.ui.combo_year_key_rate1.currentText()
        start_month = self.ui.combo_month_key_rate1.currentText()
        end_year = self.ui.combo_year_key_rate2.currentText()
        end_month = self.ui.combo_month_key_rate2.currentText()
        if (start_year == '2013' and int(start_month) < 9) or (end_year == '2024' and int(end_month) > 4):
            pass
        else:
            plots.plot_key_rate_for_period(start_year, start_month, end_year, end_month)

    def onButtonShowPlotGDPForPeriod(self):
        start_year = self.ui.combo_year_gdp1.currentText()
        end_year = self.ui.combo_year_gdp2.currentText()
        plots.plot_gdp_for_period(start_year, end_year)

    def onButtonShowPlotGDPGrowthForPeriod(self):
        start_year = self.ui.combo_year_gdp1.currentText()
        end_year = self.ui.combo_year_gdp2.currentText()
        plots.plot_gdp_growth_for_period(start_year, end_year)

    @staticmethod
    def onButtonShowPlotPieGDP():
        plots.pie_diagram_gdp_in_monetary_current()

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
