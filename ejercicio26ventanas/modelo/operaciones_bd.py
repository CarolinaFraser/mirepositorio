import mysql.connector
from modelo import constantes_sql

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_musica"
         )
    return conexion

def registro_musica(musica):
    sql = constantes_sql.SQL_INSERCION_MUSICA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (musica.cancion, musica.cantante, musica.numero_pistas, musica.precio, musica.estilo)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()

def obtener_musica():
    sql = constantes_sql.SQL_SELECT_MUSICA
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado