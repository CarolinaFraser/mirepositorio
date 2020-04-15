import mysql.connector
from modelo import constantes_sql, clases

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
    valores_a_insertar = (musica.cancion, musica.cantante, musica.numero_pistas, musica.precio, musica.estilo, musica.version, musica.formato, musica.envio)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.disconnect()
    return id_generado

def obtener_musica():
    sql = constantes_sql.SQL_SELECT_MUSICA
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado

def borrar_musica(id_musica):
    sql = constantes_sql.SQL_BORRAR_MUSICA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_musica,)
    cursor.execute(sql, val)
    conexion.commit()
    conexion.disconnect()
    
def obtener_musica_por_id(id):
    sql = constantes_sql.SQL_OBTENER_MUSICA_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    musica_obtenida = cursor.fetchone()
    conexion.disconnect()
    objeto_musica = clases.Musica(id = musica_obtenida[0], cancion = musica_obtenida[1], cantante = musica_obtenida[2], num_pistas = musica_obtenida[3], precio = musica_obtenida[4], estilo = musica_obtenida[5])
    return objeto_musica

def guardar_cambios_musica(musica):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_MUSICA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (musica.cancion, musica.cantante, musica.num_pistas, musica.precio, musica.estilo, musica.formato, musica.version, musica.envio, musica.id)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
    
    
    