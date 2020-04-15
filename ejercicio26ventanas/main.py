from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_registrar_musica, ventana_listado_musica,\
    ventana_list_widget, ventana_table_widget, ventana_guardar_cambios_musica
import sys
from modelo.clases import Musica
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton, QFileDialog,\
    QPixmap, QLabel
from _functools import partial
import shutil
from pathlib import Path

lista_resultado = None

def registrar_musica():
    musica = Musica()
    musica.cancion = ui_registrar_musica.registrar_cancion.text()
    musica.cantante = ui_registrar_musica.registrar_cantante.text()
    musica.numero_pistas = ui_registrar_musica.registrar_pistas.text()
    musica.precio = ui_registrar_musica.registrar_precio.text()
    musica.estilo = ui_registrar_musica.registrar_estilo.text()
    
    if ui_registrar_musica.check_digital.isChecked():
        musica.version = True
        
    indice_seleccionado = ui_registrar_musica.combo_formato.currentIndex()
    musica.formato = ui_registrar_musica.combo_formato.itemText(indice_seleccionado)
    
    if ui_registrar_musica.radio_email.isChecked():
        musica.envio = "Email"
    if ui_registrar_musica.radio_sms.isChecked():
        musica.envio = "SMS"
    if ui_registrar_musica.radio_whatsapp.isChecked():
        musica.envio = "WhatsApp"
        
    id_generado = operaciones_bd.registro_musica(musica)
    
    
    ruta_imagen_destino = "imagenes/" + str(id_generado) + ".jpg"
    shutil.move("temporal/imagen.jpg", ruta_imagen_destino)

    QMessageBox.about(MainWindow, "Info", "Registro Musica, OK")
    
def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo, "temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ui_registrar_musica.label_imagen.setPixmap(pixmap)
    alto_label_imagen = ui_registrar_musica.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_registrar_musica.label_imagen.setPixmap(pixmap_redim)
    
def mostrar_registro_musica():
    ui_registrar_musica.setupUi(MainWindow)
    ui_registrar_musica.btn_guardar_registro.clicked.connect(registrar_musica)
    ui_registrar_musica.boton_imagen.clicked.connect(seleccionar_imagen)
    
def mostrar_listado_musica():
    ui_listar_musica.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_musica()
    texto =""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " Canción: " + str(l[1]) + " Cantante: " + str(l[2]) + " Nº Pistas: " +  str(l[3]) + " Precio: " + str(l[4]) + " Estilo: "+ str(l[5]) + " Formato: " + str(l[6])  + " Versión: " + str(l[7]) + " Envío: " + str(l[8]) + "\n"
    ui_listar_musica.label_2.setText(texto)
    

def mostrar_list_widget_musica():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_musica()
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_musica.addItem("Canción: " + l[1] + " - Cantante: " + l[2])
    ui_ventana_list_widget.list_widget_musica.itemClicked.connect(mostrar_registro)   
     
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_musica.currentRow()
    texto = ""
    texto += "Canción: " + lista_resultado[indice_seleccionado][1] + "\n"
    texto += "Cantante: " + lista_resultado[indice_seleccionado][2] + "\n"
    texto += "Nº Pistas: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "Precio: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += "Estilo: " + lista_resultado[indice_seleccionado][5] + "\n"
    texto += "Formato: " + str(lista_resultado[indice_seleccionado][6]) + "\n"
    texto += "Versión: " + str(lista_resultado[indice_seleccionado][7]) + "\n"
    texto += "Envío: " + str(lista_resultado[indice_seleccionado][8])
    QMessageBox.about(MainWindow,"Info",texto)
    
def mostrar_table_widget_musica():
    ui_ventana_table_widget.setupUi(MainWindow)
    musica = operaciones_bd.obtener_musica()
    fila = 0
    for m in musica:
        ui_ventana_table_widget.tabla_musica.insertRow(fila)
        columna_indice = 0
        for valor in m:
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_musica.setItem(fila,columna_indice,celda)
            columna_indice +=1
        boton_borrar = QPushButton("Borrar")
        boton_borrar.clicked.connect(partial(borrar_musica,m[0]))
        ui_ventana_table_widget.tabla_musica.setCellWidget(fila,10,boton_borrar)
        boton_editar = QPushButton("Editar")
        boton_editar.clicked.connect(partial(editar_musica,m[0]))
        ui_ventana_table_widget.tabla_musica.setCellWidget(fila,11,boton_editar)
        
        label_miniatura = QLabel()
        ruta_imagen = "imagenes/" + str(m[0]) + ".jpg"
        objeto_path = Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe ==True:
            pixmap = QPixmap(ruta_imagen)
            pixmap_redim = pixmap.scaledToHeight(40)
            label_miniatura.setPixmap(pixmap_redim)
            ui_ventana_table_widget.tabla_musica.setCellWidget(fila,9,label_miniatura)
        
        fila += 1
        
def borrar_musica(id):
    res = QMessageBox.question(MainWindow, "Info", "Vas a borrar el registro id: " + str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_musica(id)
        mostrar_table_widget_musica()
        
        
def editar_musica(id_a_editar):
    QMessageBox.about(MainWindow, "Info", "Vas a editar el id: " + str(id_a_editar))
    ui_ventana_editar_musica.setupUi(MainWindow)
    musica_a_editar = operaciones_bd.obtener_musica_por_id(id_a_editar)
    ui_ventana_editar_musica.registrar_cancion.setText(musica_a_editar.cancion)
    ui_ventana_editar_musica.registrar_cantante.setText(musica_a_editar.cantante)
    ui_ventana_editar_musica.registrar_pistas.setText(str(musica_a_editar.num_pistas))
    ui_ventana_editar_musica.registrar_precio.setText(str(musica_a_editar.precio))
    ui_ventana_editar_musica.registrar_estilo.setText(musica_a_editar.estilo)
    ui_ventana_editar_musica.combo_formato.setCurrentText(musica_a_editar.formato)
    ui_ventana_editar_musica.check_digital.setChecked(musica_a_editar.version)
    
    ui_ventana_editar_musica.boton_guardar_cambios.clicked.connect(partial(guardar_cambios_musica,musica_a_editar.id))
    
def guardar_cambios_musica(id_guardarCambios):
    QMessageBox.about(MainWindow, "Info", "guardando cambios en el id: " + str(id_guardarCambios))
    musica_a_guardar_cambios = Musica()
    musica_a_guardar_cambios.id = id_guardarCambios
    musica_a_guardar_cambios.cancion = ui_ventana_editar_musica.registrar_cancion.text()
    musica_a_guardar_cambios.cantante = ui_ventana_editar_musica.registrar_cantante.text()
    musica_a_guardar_cambios.num_pistas = ui_ventana_editar_musica.registrar_pistas.text()
    musica_a_guardar_cambios.precio = ui_ventana_editar_musica.registrar_precio.text()
    musica_a_guardar_cambios.estilo = ui_ventana_editar_musica.registrar_estilo.text()
    if ui_ventana_editar_musica.check_digital.isChecked():
        musica_a_guardar_cambios.version = True
        
    indice_seleccionado = ui_ventana_editar_musica.combo_formato.currentIndex()
    musica_a_guardar_cambios.formato = ui_ventana_editar_musica.combo_formato.itemText(indice_seleccionado)
    
    if ui_ventana_editar_musica.radio_email.isChecked():
        musica_a_guardar_cambios.envio = "Email"
    if ui_ventana_editar_musica.radio_sms.isChecked():
        musica_a_guardar_cambios.envio = "SMS"
    if ui_ventana_editar_musica.radio_whatsapp.isChecked():
        musica_a_guardar_cambios.envio = "WhatsApp"
        
    operaciones_bd.guardar_cambios_musica(musica_a_guardar_cambios)
    mostrar_table_widget_musica()
    
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
ui_ventana_editar_musica = ventana_guardar_cambios_musica.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.submenu_registrar_2.triggered.connect(mostrar_registro_musica)
ui.submenu_listado_2.triggered.connect(mostrar_listado_musica)
ui.submenu_inicio_2.triggered.connect(mostrar_inicio)
ui.submenu_list_widget.triggered.connect(mostrar_list_widget_musica)
ui.submenu_table_widget.triggered.connect(mostrar_table_widget_musica)

MainWindow.show()

sys.exit(app.exec_())
