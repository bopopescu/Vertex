class Juego():

    __nomFab = None
    __duracion = None
    __version = None
    __idioma = None
    __nombre = None
    __internet = False
    __descripcion = None
    __numJugadores = 0
    __fechaComienzo = None
    __fechaFinal = None

    def __init__(self, nomFab, duracion, version, idioma, nombre, internet, descripcion, numJugadores, fechaComienzo, fechaFinal):
        self.__nomFab = nomFab
        self.__duracion = duracion
        self.__version = version
        self.__idioma = idioma
        self.__nombre = nombre
        self.__internet = internet
        self.__descripcion = descripcion
        self.__numJugadores = numJugadores
        self.__fechaComienzo = fechaComienzo
        self.__fechaFinal = fechaFinal

    @property
    def nombreFabricante(self):
        return self.__nomFab

    @nombreFabricante.setter
    def nombreFabricante(self, nomFab):
        self.__nomFab = nomFab

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, dura):
        self.__duracion = dura

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, ver):
        self.__version = ver

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, languaje):
        self.__idioma = languaje

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, name):
        self.__nombre = name

    @property
    def internet(self):
        return self.__internet

    @internet.setter
    def internet(self, inter):
        self.__internet = inter

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, desc):
        self.__descripcion = desc

    @property
    def numeroJugadores(self):
        return self.__numJugadores

    @numeroJugadores.setter
    def numeroJugadores(self, num):
        self.__numJugadores = num

    @property
    def fechaComienzo(self):
        return self.__fechaComienzo

    @fechaComienzo.setter
    def fechaComienzo(self, comienzo):
        self.__fechaComienzo = comienzo

    @property
    def fechaFinal(self):
        return self.__fechaFinal

    @fechaFinal.setter
    def fechaFinal(self, final):
        self.__fechaFinal = final
