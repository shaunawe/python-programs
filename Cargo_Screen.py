# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cargo_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 220, 51, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 101, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(31, 51, 90, 112))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioTrain = QtWidgets.QRadioButton(self.widget)
        self.radioTrain.setObjectName("radioTrain")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioTrain)
        self.radioBus = QtWidgets.QRadioButton(self.widget)
        self.radioBus.setObjectName("radioBus")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioBus)
        self.radioPlane = QtWidgets.QRadioButton(self.widget)
        self.radioPlane.setObjectName("radioPlane")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.radioPlane)
        self.radioShip = QtWidgets.QRadioButton(self.widget)
        self.radioShip.setObjectName("radioShip")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.radioShip)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 220, 53, 15))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(240, 60, 127, 83))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkFresh = QtWidgets.QCheckBox(self.widget2)
        self.checkFresh.setObjectName("checkFresh")
        self.verticalLayout.addWidget(self.checkFresh)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.checkFrozen = QtWidgets.QCheckBox(self.widget2)
        self.checkFrozen.setObjectName("checkFrozen")
        self.verticalLayout.addWidget(self.checkFrozen)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.checkNonPerish = QtWidgets.QCheckBox(self.widget2)
        self.checkNonPerish.setObjectName("checkNonPerish")
        self.verticalLayout.addWidget(self.checkNonPerish)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondf = QtWidgets.QAction(MainWindow)
        self.actiondf.setObjectName("actiondf")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Cargo Transport"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Cargo"))
        self.label_4.setText(_translate("MainWindow", "Content of Cargo"))
        self.radioTrain.setText(_translate("MainWindow", "The Train"))
        self.radioBus.setText(_translate("MainWindow", "The Bus"))
        self.radioPlane.setText(_translate("MainWindow", "The Plane"))
        self.radioShip.setText(_translate("MainWindow", "The Ship"))
        self.label_3.setText(_translate("MainWindow", "The cost:"))
        self.checkFresh.setText(_translate("MainWindow", "Fresh Cargo"))
        self.checkFrozen.setText(_translate("MainWindow", "Frozen Cargo"))
        self.checkNonPerish.setText(_translate("MainWindow", "Non-Perishable cargo"))
        self.actiondf.setText(_translate("MainWindow", "df"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
