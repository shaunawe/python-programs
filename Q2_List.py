# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q2_List.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 311)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 160, 221, 141))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 90, 300, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.sortButton = QtWidgets.QPushButton(self.widget)
        self.sortButton.setObjectName("sortButton")        
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.sortButton)
        self.msgBox = QMessageBox(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.shaun)
        self.sortButton.clicked.connect(self.sorted)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Province"))
        self.label_2.setText(_translate("Dialog", "Provinces"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.sortButton.setText(_translate("Dialog", "Sort"))

    def shaun(self):
        provinces = self.lineEdit.text().title()    
        if self.listWidget.findItems(provinces,QtCore.Qt.MatchRegExp):
            self.msgBox.setText("Province has already been entered!");
            self.msgBox.exec();
            return
        else:
            self.listWidget.addItem(provinces) 

        self.lineEdit.clear()
    def sorted(self):
        self.listWidget.sortItems(QtCore.Qt.AscendingOrder)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
