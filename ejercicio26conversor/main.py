from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal2

def conversor_euros_a_dolares():
    print("boton pulsado")
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    dolares = introducido_float * 1.10
    ui.label_resultado.setText("$ " + "{:.2f}".format(dolares).replace(".",","))
    
def conversor_euros_a_libras():
    print("boton pulsado")
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    libras = introducido_float * 0.89
    ui.label_resultado.setText("£ " + "{:.2f}".format(libras).replace(".",","))
    
def conversor_euros_a_yenes():
    print("boton pulsado")
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    yenes = introducido_float * 119.07
    ui.label_resultado.setText("圓  " + "{:.2f}".format(yenes).replace(".",","))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal2.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.moneda_dolares.clicked.connect(conversor_euros_a_dolares)
ui.moneda_libras.clicked.connect(conversor_euros_a_libras)
ui.moneda_yenes.clicked.connect(conversor_euros_a_yenes)
ui.moneda_dolares.setIcon(QtGui.QIcon("dolar.png"))
ui.moneda_libras.setIcon(QtGui.QIcon("libra.png"))
ui.moneda_yenes.setIcon(QtGui.QIcon("yen.png"))

MainWindow.show()
sys.exit(app.exec_())