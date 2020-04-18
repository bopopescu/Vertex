from mysql.connector import MySQLConnection, Error
from src.conexion.python_mysql_dbconfig import  *
from src.clases import juego

def crearJuego(fabricante, duracion, version, idioma, nombre, internet, descripcion, jugadores, inicio, final):

    args = (fabricante, duracion, version, idioma, nombre, internet, descripcion, jugadores, inicio, final)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor1 = conn.cursor()
        cursor1.callproc('crearJuego', args)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor1.close()
        conn.close()

def verJuego(nombre):

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor2 = conn.cursor()
        cursor2.callproc('verJuego', nombre)

        jueguito = cursor2.fetchall()

        for jueguitos in jueguito:
            return jueguitos

    except Error as e:
        print(e)

    finally:
        cursor2.close()
        conn.close()

def verJuegos():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('verJuegos')

        jueguito = cursor.fetchall()

        for jueguitos in jueguito:
            return jueguitos

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def modificarJuego(nombre):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('modificarJuego', nombre)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def eliminarJuego(nombre):

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('eliminarJuego' , nombre)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

