
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Cargo_Screen import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.calculateCargo)

    def calculateCargo(self):
        cost = 0.00
        if self.ui.radioTrain.isChecked():
            cost = 5
        if self.ui.radioBus.isChecked():
            cost = 10
        if self.ui.radioPlane.isChecked():
            cost = 15
        if self.ui.radioShip.isChecked():
            cost = 20

        # CalculateContent
        if self.ui.checkFresh.isChecked():
            cost = cost + 100
        if self.ui.checkFrozen.isChecked():
            cost = cost + 200
        if self.ui.checkNonPerish.isChecked():
            cost = cost + 300

        print(cost)
        self.ui.label_2.setText(str(cost))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())