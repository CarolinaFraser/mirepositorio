# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_registrar_musica.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 305)
        MainWindow.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.registrar_cancion = QtWidgets.QLineEdit(self.centralwidget)
        self.registrar_cancion.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.registrar_cancion.setObjectName("registrar_cancion")
        self.registrar_cantante = QtWidgets.QLineEdit(self.centralwidget)
        self.registrar_cantante.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.registrar_cantante.setObjectName("registrar_cantante")
        self.registrar_pistas = QtWidgets.QLineEdit(self.centralwidget)
        self.registrar_pistas.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.registrar_pistas.setObjectName("registrar_pistas")
        self.registrar_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.registrar_precio.setGeometry(QtCore.QRect(140, 200, 113, 20))
        self.registrar_precio.setObjectName("registrar_precio")
        self.registrar_estilo = QtWidgets.QLineEdit(self.centralwidget)
        self.registrar_estilo.setGeometry(QtCore.QRect(140, 240, 113, 20))
        self.registrar_estilo.setObjectName("registrar_estilo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; text-decoration: underline; color:#ff55ff;\">REGISTRA TU MUSICA</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Canción:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Cantante:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Nº pistas:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Precio:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Estilo:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
