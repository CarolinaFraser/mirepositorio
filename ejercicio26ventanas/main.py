from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_registrar_musica, ventana_listado_musica,\
    ventana_list_widget, ventana_table_widget
import sys
from modelo.clases import Musica
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem

lista_resultado = None

def registrar_musica():
    musica = Musica()
    musica.cancion = ui_registrar_musica.registrar_cancion.text()
    musica.cantante = ui_registrar_musica.registrar_cantante.text()
    musica.numero_pistas = ui_registrar_musica.registrar_pistas.text()
    musica.precio = ui_registrar_musica.registrar_precio.text()
    musica.estilo = ui_registrar_musica.registrar_estilo.text()
    operaciones_bd.registro_musica(musica)
    QMessageBox.about(MainWindow, "Info", "Registro Musica, OK")
    
def mostrar_registro_musica():
    ui_registrar_musica.setupUi(MainWindow)
    ui_registrar_musica.btn_guardar_registro.clicked.connect(registrar_musica)
    
def mostrar_listado_musica():
    ui_listar_musica.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_musica()
    texto =""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " Canción: " + str(l[1]) + " Cantante: " + str(l[2]) + " Nº Pistas: " +  str(l[3]) + " Precio: " + str(l[4]) + " Estilo: "+ str(l[5]) + "\n"
    ui_listar_musica.label_2.setText(texto)
    

def mostrar_list_widget_musica():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_musica()
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_musica.addItem(l[1] + " Cantante: " + l[2])
    ui_ventana_list_widget.list_widget_musica.itemClicked.connect(mostrar_registro)   
     
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_musica.currentRow()
    texto = ""
    texto += "Canción: " + lista_resultado[indice_seleccionado][1] + "\n"
    texto += "Cantante: " + lista_resultado[indice_seleccionado][2] + "\n"
    texto += "Nº Pistas: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "Precio: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += "Estilo: " + lista_resultado[indice_seleccionado][5]
    QMessageBox.about(MainWindow,"Info",texto)
    
def mostrar_table_widget_musica():
    ui_ventana_table_widget.setupUi(MainWindow)
    musica = operaciones_bd.obtener_musica()
    fila = 0
    for m in musica:
        ui_ventana_table_widget.tabla_musica.insertRow(fila)
        
        celda = QTableWidgetItem(str(m[0]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 0, celda)
        
        celda = QTableWidgetItem(str(m[1]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 1, celda)
        
        celda = QTableWidgetItem(str(m[2]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 2, celda)
        
        celda = QTableWidgetItem(str(m[3]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 3, celda)
        
        celda = QTableWidgetItem(str(m[4]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 4, celda)
        
        celda = QTableWidgetItem(str(m[5]))
        ui_ventana_table_widget.tabla_musica.setItem(fila, 5, celda)
        
        fila += 1
 
def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_registrar_2.triggered.connect(mostrar_registro_musica)
    ui.submenu_listado_2.triggered.connect(mostrar_listado_musica)
    ui.submenu_inicio_2.triggered.connect(mostrar_inicio)
    ui.submenu_list_widget.triggered.connect(mostrar_list_widget_musica)
    ui.submenu_table_widget.triggered.connect(mostrar_table_widget_musica)

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()
ui_registrar_musica = ventana_registrar_musica.Ui_MainWindow()
ui_listar_musica = ventana_listado_musica.Ui_MainWindow()
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_registrar_2.triggered.connect(mostrar_registro_musica)
ui.submenu_listado_2.triggered.connect(mostrar_listado_musica)
ui.submenu_inicio_2.triggered.connect(mostrar_inicio)
ui.submenu_list_widget.triggered.connect(mostrar_list_widget_musica)
ui.submenu_table_widget.triggered.connect(mostrar_table_widget_musica)

MainWindow.show()

sys.exit(app.exec_())
