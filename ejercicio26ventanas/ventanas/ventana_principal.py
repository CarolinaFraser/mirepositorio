# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
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
        self.titulo_principal = QtWidgets.QLabel(self.centralwidget)
        self.titulo_principal.setGeometry(QtCore.QRect(30, 20, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.titulo_principal.setFont(font)
        self.titulo_principal.setObjectName("titulo_principal")
        self.informativo_principal = QtWidgets.QLabel(self.centralwidget)
        self.informativo_principal.setGeometry(QtCore.QRect(60, 150, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        self.informativo_principal.setFont(font)
        self.informativo_principal.setObjectName("informativo_principal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMusica = QtWidgets.QMenu(self.menuBar)
        self.menuMusica.setObjectName("menuMusica")
        MainWindow.setMenuBar(self.menuBar)
        self.actionRegistrar_musica = QtWidgets.QAction(MainWindow)
        self.actionRegistrar_musica.setObjectName("actionRegistrar_musica")
        self.actionListar_musica = QtWidgets.QAction(MainWindow)
        self.actionListar_musica.setObjectName("actionListar_musica")
        self.actionRegistrar_musica_2 = QtWidgets.QAction(MainWindow)
        self.actionRegistrar_musica_2.setObjectName("actionRegistrar_musica_2")
        self.actionListar_musica_2 = QtWidgets.QAction(MainWindow)
        self.actionListar_musica_2.setObjectName("actionListar_musica_2")
        self.actionInicio = QtWidgets.QAction(MainWindow)
        self.actionInicio.setObjectName("actionInicio")
        self.submenu_registrar = QtWidgets.QAction(MainWindow)
        self.submenu_registrar.setObjectName("submenu_registrar")
        self.submenu_listado = QtWidgets.QAction(MainWindow)
        self.submenu_listado.setObjectName("submenu_listado")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_registrar_2 = QtWidgets.QAction(MainWindow)
        self.submenu_registrar_2.setObjectName("submenu_registrar_2")
        self.submenu_listado_2 = QtWidgets.QAction(MainWindow)
        self.submenu_listado_2.setObjectName("submenu_listado_2")
        self.submenu_inicio_2 = QtWidgets.QAction(MainWindow)
        self.submenu_inicio_2.setObjectName("submenu_inicio_2")
        self.menuMusica.addAction(self.submenu_registrar_2)
        self.menuMusica.addAction(self.submenu_listado_2)
        self.menuMusica.addAction(self.submenu_inicio_2)
        self.menuBar.addAction(self.menuMusica.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo_principal.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; text-decoration: underline; color:#ff55ff;\">MUSICA CAROLINE FERNAN</span></p></body></html>"))
        self.informativo_principal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aa007f;\">Pulsa en el menú para utilizar la aplicación</span></p></body></html>"))
        self.menuMusica.setTitle(_translate("MainWindow", "Musica"))
        self.actionRegistrar_musica.setText(_translate("MainWindow", "Registrar musica"))
        self.actionListar_musica.setText(_translate("MainWindow", "Listar musica"))
        self.actionRegistrar_musica_2.setText(_translate("MainWindow", "Registrar musica"))
        self.actionListar_musica_2.setText(_translate("MainWindow", "Listar musica"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.submenu_registrar.setText(_translate("MainWindow", "Registrar Música"))
        self.submenu_listado.setText(_translate("MainWindow", "Listado Música"))
        self.submenu_inicio.setText(_translate("MainWindow", "Inicio"))
        self.submenu_registrar_2.setText(_translate("MainWindow", "Registrar musica"))
        self.submenu_listado_2.setText(_translate("MainWindow", "Listar musica"))
        self.submenu_inicio_2.setText(_translate("MainWindow", "Inicio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
