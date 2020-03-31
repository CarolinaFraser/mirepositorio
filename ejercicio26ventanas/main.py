from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal, ventana_registrar_musica, ventana_listado_musica

    
def mostrar_registro_musica():
    ui_registrar_musica.setupUi(MainWindow)
    
def mostrar_listado_musica():
    ui_listar_musica.setupUi(MainWindow)
    
def mostrar_inicio():
    ui.setupUi(MainWindow)


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()
ui_registrar_musica = ventana_registrar_musica.Ui_MainWindow()
ui_listar_musica = ventana_listado_musica.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_registrar_2.triggered.connect(mostrar_registro_musica)
ui.submenu_listado_2.triggered.connect(mostrar_listado_musica)
ui.submenu_inicio_2.triggered.connect(mostrar_inicio)

MainWindow.show()

sys.exit(app.exec_())
