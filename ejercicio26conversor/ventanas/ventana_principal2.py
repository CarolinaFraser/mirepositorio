# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 281)
        MainWindow.setStyleSheet("color: rgb(247, 255, 255);\n"
"background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(20, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(26)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(330, 60, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        self.entrada_euros.setFont(font)
        self.entrada_euros.setText("")
        self.entrada_euros.setObjectName("entrada_euros")
        self.moneda_dolares = QtWidgets.QPushButton(self.centralwidget)
        self.moneda_dolares.setGeometry(QtCore.QRect(40, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.moneda_dolares.setFont(font)
        self.moneda_dolares.setObjectName("moneda_dolares")
        self.moneda_libras = QtWidgets.QPushButton(self.centralwidget)
        self.moneda_libras.setGeometry(QtCore.QRect(140, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.moneda_libras.setFont(font)
        self.moneda_libras.setObjectName("moneda_libras")
        self.moneda_yenes = QtWidgets.QPushButton(self.centralwidget)
        self.moneda_yenes.setGeometry(QtCore.QRect(230, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.moneda_yenes.setFont(font)
        self.moneda_yenes.setObjectName("moneda_yenes")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(170, 160, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(26)
        self.label_resultado.setFont(font)
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Conversor de monedas"))
        self.label.setText(_translate("MainWindow", "Introduce la cantidad en euros"))
        self.moneda_dolares.setText(_translate("MainWindow", "Dolares"))
        self.moneda_libras.setText(_translate("MainWindow", "Libras"))
        self.moneda_yenes.setText(_translate("MainWindow", "Yenes"))
        self.label_resultado.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
