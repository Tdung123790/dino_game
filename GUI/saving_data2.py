# Form implementation generated from reading ui file 'C:\Users\Dung\PycharmProjects\Dino_Game\dino_game\game\saving_data2.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(110, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputname = QtWidgets.QLineEdit(parent=Dialog)
        self.inputname.setGeometry(QtCore.QRect(60, 150, 261, 51))
        self.inputname.setObjectName("inputname")
        self.label_score = QtWidgets.QLabel(parent=Dialog)
        self.label_score.setGeometry(QtCore.QRect(110, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_score.setFont(font)
        self.label_score.setText("")
        self.label_score.setObjectName("label_score")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.label.setText(_translate("Dialog", "Enter your name:"))
