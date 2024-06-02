from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.window()
        self.layout()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
