from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def crearJuego(nomFab, duracion, version, idioma, nombre, internet, descripcion, numJugadores, fechaComienzo, fechaFinal):

    args = (nomFab, duracion, version, idioma, nombre, internet, descripcion, numJugadores, fechaComienzo, fechaFinal)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('crearJuego', args)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def verJuego(nombre):

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('verJuego', nombre)

        jueguito = cursor.fetchall()

        for jueguitos in jueguito:
            return jueguitos

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def VerJuegos():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.callproc('verJuego')

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
        cursor.callproc('eliminarJuego', nombre)

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